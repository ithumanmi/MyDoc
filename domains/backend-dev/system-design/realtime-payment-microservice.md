# Real-time Payment Microservice (100k RPS, Exactly-Once, Multi-Region)

## 1) Requirements & Constraints
- **Functional:**
  - Process card/account-to-account payments in real-time.
  - Exactly-once debit/credit per transaction; idempotent public API.
  - Support auth/capture, void/refund; async webhooks to merchants.
  - Multi-region active-active; cross-region failover < 60s.
- **Non-functional:** 100k req/s peak (p99<150ms in-region), durability (RPO≈0), availability ≥99.99%, PCI-DSS scope minimised, observability (traces/metrics/logs), backpressure.
- **Data correctness:** Atomic persistence of payment state + ledger entries; no double-debit; de-dup across regions.

## 2) High-Level Architecture
- **ASCII sơ đồ (rút gọn):**

```
Client
  |
  v
+--------------+     +--------------------+     +-----------------+
| Anycast DNS  | --> | CDN/WAF + API GW   | --> | Payment API     |
+--------------+     | (rate-limit/auth)  |     | (Idempotency    |
                    +--------------------+     |  Cache + produce |
                                                |  Kafka)          |
                                                +--------+--------+
                                                         |
                                                         v
                                                +-----------------+
                                                | Kafka (payments)|
                                                +--------+--------+
                                                         |
                                                         v
            +--------------------+    +----------------------+   +-------------------+
            | Orchestrator/Saga  |--->| Payment DB (OLTP)    |-->| Outbox (in DB)    |
            | (fraud, auth,      |    | + Idempotency table  |   +---------+---------+
            |  reservation)      |    +----------+-----------+             |
            +---------+----------+               |                         v
                      |                          |                +-----------------+
                      v                          |                | CDC / Debezium  |
            +--------------------+               |                +--------+--------+
            | Ledger Service     |<--------------+                         |
            | (double-entry)     |                                         v
            +--------------------+                               +-------------------+
                                                                     | Kafka events      |
                                                                     +---------+---------+
                                                                               |
                                                                               v
                                                                     +-------------------+
                                                                     | Webhook Service   |
                                                                     | (retry, DLQ)      |
                                                                     +-------------------+

Cross-region: Global Idempotency Registry (Redis/DynamoDB global) + async DB/Kafka replication + GSLB for failover.
```

- **Edge:** Global Anycast DNS + CDN/WAF → API Gateway (rate limit, auth, JWT, HMAC).
- **Ingestion:** Idempotent Payment API (REST/gRPC) writes request to **Kafka** (regional) with a **write-token** (idempotency key + merchant + region) and stores **Idempotency Cache** (Redis/Memcached + persistence) for quick replay.
- **Processing pipeline:**
  - **Orchestrator** service consumes from Kafka, executes **Saga** steps (fraud → balance/reservation → authorization → ledger commit → notification).
  - **Outbox + CDC:** Payment service writes state changes + outbox row to **Payment DB** (regional Postgres/Spanner/Cloud SQL HA). Debezium/CDC streams outbox to Kafka to notify downstream (ledger, webhooks, settlements).
  - **Ledger Service:** Appends double-entry postings to **Ledger DB** (append-only, partitioned). Idempotent by transaction_id + sequence.
  - **Notification/Webhook Service:** Consumes outbox events, delivers with exponential backoff + DLQ.
- **State stores:**
  - **Payment DB:** OLTP for payment state (auth/capture/refund), optimistic locking (version column).
  - **Ledger DB:** Immutable postings, partitioned by account/tenant; compression + tiered storage.
  - **Idempotency Store:** Redis with TTL + persistent backing (e.g., Redis AOF/Backup) to survive restart; cross-region replicate for active-active.
- **Coordination:** **Dedup Filter** on Kafka consumer side (transaction_id, idempotency_key). **Exactly-once** via idempotency keys + outbox + idempotent ledger writes + transactional Kafka (if available) or idempotent producer + consumer offsets stored in DB.
- **Multi-region:**
  - Active-active per region with **regional Kafka + DB primary**, **asynchronous cross-region replication** (logical/Spanner multi-region). Route traffic via **latency-based routing**.
  - **Global Idempotency Registry** (Redis Enterprise / DynamoDB global table) to dedup cross-region retries; key = merchant_id + idem_key → final status + response payload.

## 3) Data Model (simplified)
- `payments`: id (UUID), merchant_id, idem_key, amount, currency, state (initiated|authorized|captured|voided|refunded|failed), version, created_at, updated_at.
- `payment_events` (outbox): id, payment_id, event_type, payload, state(pending|sent), created_at.
- `ledger_postings`: id, transaction_id, account_id, direction(debit|credit), amount, currency, batch_id, created_at.
- `idempotency_keys`: merchant_id, idem_key, status, http_status, response_body, expires_at.

## 4) Exactly-Once & Ordering Strategy
- **Inbound idempotency:** Client sends `Idempotency-Key`; API checks `idempotency_keys`. If exists, return stored response; else reserve and proceed.
- **Producer semantics:** Kafka producer idempotent + acks=all; partition by `transaction_id` to keep ordering per payment.
- **Consumer processing:**
  - Consume message → execute business logic → within DB transaction: update `payments`, insert `ledger_postings`, insert `payment_events` (outbox) → commit.
  - Commit Kafka offset **after** DB commit (or use Kafka transactions linking offset commit with outbox write if supported).
- **Dedup ledger:** Unique constraint on (`transaction_id`,`sequence`) prevents double post.
- **Cross-region dedup:** Check `Global Idempotency Registry` before processing when traffic may spill to another region.

## 5) Multi-Region Deployment
- **Pattern:** Active-active; each region handles local traffic; async replicate state.
- **Split-brain guard:**
  - Idempotency registry is globally replicated.
  - Payments are **region-sticky** unless region is degraded; failover uses deterministic tie-break (e.g., lowest-latency healthy region), but idempotency lookup prevents duplicates.
- **Failover:** DNS/GSLB health-check → reroute; consumers in surviving region can consume from paired Kafka via MirrorMaker 2 / MSK Replicator; reconcile outbox gaps via CDC.

## 6) Capacity & Performance Notes
- **Target:** 100k req/s; assume p99 150ms.
- **Sizing sketch:**
  - API tier: ~1k pods x 100 rps each (autoscale on CPU/RPS); keep-alive + H2 for gRPC.
  - Kafka: 30–50 partitions for payments topic per region; retention short (e.g., 24–48h); use SSD, 3 AZ.
  - DB: sharded/partitioned by merchant/tenant; connection pooling; async writes for webhook queue.
- **Hot paths:**
  - Cache merchant config & FX rates (Redis, TTL 5–15m).
  - Fraud model served via feature store + in-memory model server; hard timeout 20–30ms budget.

## 7) Reliability & Fault Tolerance
- Timeouts + retries with jitter; circuit-breaker to issuers/fraud; bulkhead pools.
- DLQ for Kafka consumers; replay tools with idempotency protections.
- Graceful degradation: if fraud service down, fallback to ruleset; if webhook down, queue to retry.
- Chaos drills + regional failover game days.

## 8) Security & Compliance
- PCI-DSS scope minimised: tokenize PAN; vault secrets (HSM/KMS); P2PE if applicable.
- mTLS between services; JWT for merchants; HMAC signatures for webhooks.
- PII encryption at rest; row-level access by tenant; audit log immutable (WORM storage).

## 9) Observability & SLOs
- SLO: Availability 99.99%, p99 latency <150ms (in-region), webhook delivery success >99.5% within 1 minute.
- Telemetry: OpenTelemetry traces with payment_id baggage; metrics (RPS, p99, error rate, ledger lag, idempotency hits/misses, Kafka lag, CDC lag); structured logs with correlation ids.
- Alerts: Latency/error budget burn, idempotency miss spikes, ledger append failures, cross-region replication lag.

## 10) Testing & Validation
- Property-based tests for idempotency/dedup.
- Fault-injection (kill Kafka broker, drop DB primary, fraud timeout) to validate exactly-once and recovery.
- Load test to 120% peak with mixed auth/capture/refund traffic model.

## 11) Sequence (Happy Path: Auth+Capture)
1) Client → API with Idempotency-Key.
2) API checks registry; produce to Kafka `payments.in` with idem_key.
3) Orchestrator consumes, calls fraud, reserves funds/authorization with issuer, updates payment + ledger + outbox in one DB tx.
4) CDC streams outbox → Kafka `payments.events`.
5) Webhook service delivers status; retries with backoff; DLQ on exhaust.
6) Response served from cached idempotency record for retries.

## 12) Trade-offs
- Active-active + global idempotency increases complexity but reduces RTO/RPO.
- Kafka transactional producers simplify exactly-once offsets; if unavailable, rely on idempotent writes + offset-after-commit pattern.
- Spanner/multi-region SQL eases consistency at higher cost; Postgres + logical replica is cheaper but needs more ops.

## 14) Tech Decision Matrix

| Choice | Option A | Option B | Why pick A | Why pick B | Recommendation |
| --- | --- | --- | --- | --- | --- |
| Event Bus | **Kafka** (idempotent producer, mature ecosystem, MirrorMaker2) | **Pulsar** (built-in geo-replication, multi-tenancy) | Proven exactly-once patterns with outbox; large ops community | Simpler geo-replication; good for multi-tenant isolation | Kafka, unless multi-tenant isolation/geo-sync simplicity is top priority → Pulsar |
| DB (payments) | **Spanner/Citus multi-region** | **Postgres regional + logical replica** | Strong consistency, built-in multi-region, fewer failover playbooks | Lower cost, flexible, but more ops (failover, split-brain handling) | Spanner if budget; Postgres+Citus/shards if cost-sensitive with solid ops |
| Idempotency Store | **Redis Enterprise / DynamoDB Global Table** | **Plain Redis + cross-region backup** | Built-in global replication, low-latency reads | Cheaper, but higher RPO in failover | Redis Enterprise/DynamoDB for active-active; plain Redis if accept longer RTO/RPO |
| Outbox transport | **CDC (Debezium → Kafka)** | **Direct Kafka TX producer** | Works with standard SQL, decouples app | Lower latency, but tighter coupling to Kafka TX support | CDC for portability; TX producer if infra fully Kafka-native |
| Ledger storage | **Append-only SQL (partitioned)** | **Event-store (Kafka compacted topic + OLAP sink)** | Familiar SQL semantics, strong constraints | Cheaper long-term storage, streaming-friendly | SQL append-only for control; add OLAP sink for analytics |


## 13) Ops Runbook (essentials)
- **Duplicate detected:** Check idempotency registry; return stored response; ensure dedup metrics steady.
- **Kafka lag spike:** Scale consumers; check broker health; consider pausing low-priority topics.
- **Regional outage:** Trigger failover; enable cross-region consumption; reconcile outbox gaps.
- **Ledger mismatch alert:** Halt captures for affected tenant; replay from outbox with dry-run; compare posting hashes.