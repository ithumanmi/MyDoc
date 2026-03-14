# Distributed Messaging & Coordination: Kafka, Pulsar, RabbitMQ, Consensus & Exactly-Once

## 1) Mental Models
- **Coordination vs Messaging**: Paxos/Raft/ZooKeeper solve agreement/metadata; Kafka/Pulsar/RabbitMQ move data/events. You often need both.
- **Ordering & Delivery**: per-partition ordering ≠ global ordering. Exactly-once = *idempotent effects + atomic offset/state updates*, not magic.
- **State Change as Events**: Event Sourcing (write facts, derive views); Saga for cross-service workflows; 2PC for tight atomicity (rarely needed across services due to blocking).

## 2) Consensus & Metadata
- **Paxos**: theoretical baseline; harder to implement/operate directly.
- **Raft**: simpler mental model (leader, log replication, commit index). Used by etcd/Consul.
- **ZooKeeper**: CP metadata store (ZAB protocol); used by older Kafka for controller/offsets (pre-KIP-500). Patterns: ephemeral znodes for liveness, watches for notifications.
- **etcd/Consul**: Raft-based, modern choice for service discovery, config, locks.

## 3) Messaging Systems Snapshot
- **Kafka**: append-only log, partitions, pull-based consumers, idempotent producer + transactions, strong ecosystem (Connect, Streams, ksqlDB). Exactly-once *processing* via idempotent producer + transactional writes + EOS sinks.
- **RabbitMQ**: AMQP broker, exchange→queue routing, push-based; great for work queues, routing keys, per-message acks; ordering per-queue not guaranteed under redelivery.
- **Apache Pulsar**: multi-tenant, segment + BookKeeper storage, geo-replication built-in; supports **exactly-once semantics natively** via transactions (producers/consumers), and topic-level subscriptions; good for multi-region and tenancy isolation.

## 4) Exactly-Once & Idempotency Patterns
- **Idempotent Producer (Kafka)**: enable `enable.idempotence=true`, `acks=all`, proper retries/backoff; prevents duplicate appends on retry.
- **Transactional Producer/Consumer (Kafka EOS)**: producers start TX, write to topic + consumer offsets in TX; commit → atomic visibility of data + offsets; requires transactional.id and proper isolation.level=read_committed.
- **Consumer-side Dedup**: maintain processed keys (idempotency keys) in fast store (Redis/DB) or by using primary-key/upsert in sink. Use windowed dedup to bound memory.
- **Outbox + CDC**: write DB row + outbox row in same DB TX; stream outbox to bus; ensures no dual-write gaps.
- **幂等 API**: Idempotency-Key header; store prior response keyed by (tenant, idem_key).

## 5) Event Sourcing vs 2PC vs Saga
- **Event Sourcing**: append events as source of truth; rebuild state via fold; projections for queries. Pros: auditability, temporal queries; Cons: schema evolution, replay time, projection lag.
- **Saga**: split long/跨 boundary workflow into steps with compensations; choreography (events) vs orchestration (controller). Prefer Saga over 2PC across services.
- **Two-Phase Commit (2PC)**: atomic across resources; blocking, coordinator is SPOF; use within a single domain/store if absolutely required; avoid cross-service 2PC.

## 6) CRDT (Conflict-free Replicated Data Types)
- Data types that converge without coordination using merge functions (G-Counter, PN-Counter, OR-Set, LWW-Register).
- Great for **offline/edge**, multi-leader replication, collaborative apps. Trade-off: tombstone growth, semantic fit required.

## 7) Pulsar vs Kafka vs RabbitMQ (TL;DR)
- **Throughput/log semantics:** Kafka & Pulsar excel at high throughput log streaming; RabbitMQ shines for work queues and flexible routing.
- **Geo-replication:** Pulsar has built-in; Kafka uses MirrorMaker2/MSK Replicator; RabbitMQ has federations/shovels.
- **Exactly-once:**
  - Kafka: idempotent producer + transactions + read_committed; EOS sinks in Flink/Kafka Streams.
  - Pulsar: **native transactions** across topics/subscriptions for exactly-once; per-message ack with cumulative ack; BookKeeper ledgers.
  - RabbitMQ: at-least-once by default; exactly-once requires idempotent consumer/sink logic.
- **Multi-tenancy:** Pulsar built-in namespaces; Kafka needs conventions/ACLs; RabbitMQ via virtual hosts.
- **Storage layer:** Kafka log per partition; Pulsar segments to BookKeeper (separates serving vs storage).

## 8) How to Implement Exactly-Once (Practical)
- **Ingest:** Idempotent producer; partition by key for ordering.
- **Process:**
  - Kafka Streams/Flink with EOS: state store + changelog + transactional commits to sink.
  - Custom consumer: do work → in a DB TX upsert results + store last processed offset → commit offset after DB commit.
- **Dedup keys:** transaction_id or event_id as primary key in sink (upsert) + TTL if appropriate.
- **Webhooks/side effects:** enqueue outbox with status; worker reads outbox, delivers with retry/backoff/DLQ; idempotent receiver (signature + idem key).

## 9) ZooKeeper-less Kafka (KIP-500)
- Newer Kafka uses the internal **KRaft** controller (Raft-based) to remove ZooKeeper dependency. Reduces split-brain risk and simplifies ops.

## 10) Operational Gotchas
- Hot partitions (bad key); unbounded consumer lag; misaligned retention vs replay needs; compaction misconfig; DLQ visibility.
- For Pulsar: ledger retention/compaction, BookKeeper disk/IO; subscription type (exclusive/shared/failover/key_shared) affects ordering guarantees.
- For RabbitMQ: unacked message buildup, queue length limits, per-queue ordering broken by redelivery, head-of-line blocking.

## 11) Reference Patterns
- **Audit/ledger:** Event sourcing + append-only log + materialized views.
- **Work queue:** RabbitMQ / Kafka with compaction-off, consumer group per worker pool.
- **Multi-region active-active:** Pulsar geo-replication or Kafka + MM2; global idempotency registry to avoid duplicates across regions.

## 12) When to Choose What?
- **Kafka**: high-throughput streaming, strong ecosystem, EOS with Streams/Flink, large ops community.
- **Pulsar**: multi-tenant, geo-replication baked in, topic-level transactions for exactly-once, storage/compute separation.
- **RabbitMQ**: simple work queues, routing patterns (fanout/topic/headers), fast to adopt, smaller operational footprint.

## 13) Interview / Design Checklist
- Delivery needs (at-least/at-most/exactly-once)? Ordering scope? Idempotency keys?
- Throughput/latency SLO? Hot-key risk? Partitioning strategy?
- Replay story (retention, compaction, DLQ)?
- Schema evolution plan? (registry, compatibility mode)
- Ops: monitoring Kafka/Pulsar metrics (lag, ISR/URP, ledger health), RabbitMQ (unacked, ready, rate), alerting.