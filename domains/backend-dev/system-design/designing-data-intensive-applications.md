# Designing Data-Intensive Applications (DDIA-inspired Cheatsheet)

## 1) Objectives
- Build systems that are **correct, resilient, and evolvable** under high data volume/velocity/variety.
- Make trade-offs explicit: **consistency vs availability**, **latency vs durability**, **read/write amplification vs flexibility**.

## 2) Workload Profiling
- **Access pattern:** read-heavy vs write-heavy, point lookup vs range scan vs full-text/vector.
- **Latency targets:** p99 SLA per operation; tail tolerance (p99.9?).
- **Consistency needs:** monotonic reads? read-your-writes? bounded-staleness? linearizability?
- **Growth:** data size, request RPS, QPS per shard, hot partitions risk.

## 3) Storage & Data Models
- **Relational (normalized)**: integrity, joins; good for OLTP with strict constraints.
- **Wide-column (Cassandra/Bigtable)**: high write throughput, predictable queries; denormalize by query pattern.
- **Document (Mongo/ES)**: flexible schema; beware unbounded doc growth & secondary index cost.
- **Key-Value**: fastest point reads/writes; design keys for distribution.
- **Time-series**: ingestion-optimized, TTL/retention, compression; downsampling pipelines.
- **Graph**: traversals, relationship-heavy workloads.

## 4) Encoding & Schema
- Backward/forward compatibility: use **schema registry** (Protobuf/Avro), avoid field reuse.
- Avoid breaking changes: additive fields; keep defaults; version topics/events.
- Migrate with **dual-write/dual-read** during transitions.

## 5) Replication Models
- **Synchronous**: strong consistency, higher latency; quorum writes.
- **Asynchronous**: lower latency, possible data loss on primary fail; eventual consistency.
- **Leader-Follower**: simple, write funnel; failover complexity.
- **Leaderless/Quorum (Dynamo)**: high write availability; conflict resolution (LWW/CRDT/Merge).

## 6) Partitioning (Sharding)
- **Hash-based**: uniform distribution; harder range queries.
- **Range-based**: good for ordered scans; risk hot partitions; needs split/merge.
- **Directory-based**: lookup indirection; easier rebalancing; metadata hotspot risk.
- Key design: include **tenant_id** + **entropy** to avoid hotspots; support **composite keys** for access paths.

## 7) Transactions & Consistency
- **ACID** (single partition) vs **distributed transactions** (2PC/Sagas).
- **Isolation levels:**
  - Read Uncommitted < Read Committed < Repeatable Read < Snapshot < Serializable.
  - Use **Serializable** for money/ledger; **Read Committed/Snapshot** for most OLTP; **Read Your Writes/Monotonic Reads** for UX correctness.
- **Sagas** for long-running, cross-boundary workflows; define compensations.

## 8) Indexing & Query Patterns
- **B-tree**: range scans, equality.
- **LSM** (RocksDB/Cassandra): write-optimized; compaction overhead; tune Bloom filters.
- **Secondary indexes**: beware write amplification; consider **materialized views** per access pattern.
- **Search/Vector**: inverted index (BM25) vs ANN (HNSW/IVF); filter-first then vector search for cost.

## 9) Caching Strategy
- Layers: client/browser, CDN, edge KV, service cache, DB cache.
- Patterns: **Read-through**, **Write-through**, **Write-back** (rare), **Cache-aside**.
- Invalidation: TTL + explicit bust; versioned keys; idempotent recompute.
- Prevent stampede: request coalescing (single-flight), jittered TTL, semaphore.

## 10) Durability & Backup
- **WAL + snapshots**; multi-AZ replicas.
- **Backups**: point-in-time restore (PITR); test restores regularly.
- **RPO/RTO** targets; simulate region failover.

## 11) Streaming vs Batch
- **Batch (ETL/ELT)**: large window, cheap per byte, higher latency.
- **Streaming**: near-real-time, complex event processing; exactly-once via idempotency + transactional sinks + outbox.
- **Lambda vs Kappa**: single pipeline (Kappa) reduces dual-logic; use CDC + stream processor (Flink/Kafka Streams/Spark).

## 12) Idempotency & Exactly-Once Effectively
- **Idempotency keys** at API; dedup at consumer.
- **Outbox + CDC** to keep DB/source of truth in sync with event bus.
- **Transactional sinks**: use upsert keys in warehouses/lakes; EOS sinks in Flink.

## 13) Observability for Data Systems
- Traces with baggage (traceparent) across producers/consumers.
- Metrics: lag (consumer/kafka), throughput, p99, error rate, dead-letter volume, compaction %, spill %, checkpoint duration.
- Data quality: freshness, completeness, schema drift, null-rate, anomaly detection.

## 14) Reliability Patterns
- **Backpressure**: bounded queues, rate limit per tenant, shed load.
- **Retries with jitter**; avoid infinite retries; circuit breakers around sinks.
- **Dead-letter + replay** tooling; idempotent reprocessing.
- **Graceful degradation**: serve stale cache; downgrade features when dependencies fail.

## 15) Evolution & Migration Playbook
- Strangler pattern for stores: dual-write → shadow read → cutover.
- Backfill with verifiable hashes; run parity checks.
- Feature-flag for new code paths; dark launch before full traffic.

## 16) Security & Compliance
- Encryption at rest + in transit; KMS/HSM for keys; rotate secrets.
- Row/column-level security for multi-tenant; tokenization for PII; audit trails.
- Access via service accounts + least privilege; break-glass flows.

## 17) Cost & Efficiency Levers
- Storage tiering (hot/warm/cold); compression; TTL for logs/events.
- Right-size partitions; avoid over-partitioning; compact topics where possible.
- Precompute views for high-QPS reads; push filters down to storage engines.

## 18) Quick Reference: When to Pick What?
- **OLTP, strong constraints:** Postgres/MySQL, possibly sharded/Citus.
- **Global consistency:** Spanner/YugabyteDB/CockroachDB (cost ↑, ops ↓ for multi-region correctness).
- **Write-heavy, predictable queries:** Cassandra/Scylla (LSM, wide-table by access path).
- **Search/vector heavy:** Elasticsearch/OpenSearch; add vector ANN; watch heap/GC.
- **Event backbone:** Kafka/Pulsar/Redpanda; choose based on ops stack & geo needs.
- **HTAP/analytics:** Snowflake/BigQuery/ClickHouse/Iceberg+Trino; choose by latency/cost/governance.

### 18.1 RDBMS vs Wide-Column vs Global SQL (Postgres vs Cassandra vs Spanner)

| Dimension | Postgres (sharded/Citus) | Cassandra/Scylla | Spanner (or Cockroach/Yugabyte) |
| --- | --- | --- | --- |
| Consistency | Strong (per shard); cross-shard needs app logic or 2PC | Tunable (QUORUM/R+W>N); eventual by default | Global strong (TrueTime/Hybrid logical clock) |
| Schema | Rigid, rich constraints | Denormalized by access pattern; sparse columns ok | Rigid SQL + DDL; strong constraints |
| Workload fit | OLTP, joins, transactions; moderate write | Write-heavy, time-series-like, predictable queries | Global OLTP with strong consistency; multi-region correctness |
| Query | Rich SQL, joins, indexes | Limited joins; query-by-partition-key; secondary index cost | Rich SQL, distributed queries |
| Ops | Well-known, simpler; need manual sharding/partitioning | Operationally sensitive (compaction, tombstones, RF/GC) | Managed (if Spanner) but costly; ops complexity hidden |
| Latency | Low single-region; cross-shard joins can cost | Low/consistent at scale; tail latency sensitive to GC/compaction | Cross-region latency bounded by TrueTime; predictable |
| Storage model | B-Tree/heap; optional LSM (some extensions) | LSM; log-structured, high write | Spanner’s Paxos/raft-replicated segments |
| When to pick | Strong constraints, transactional, smaller teams | Massive scale write/read with simple access paths, multi-AZ | Need global strong consistency, simpler dev story, higher budget |

#### Benchmarks (mang tính tham khảo, phụ thuộc hạ tầng)
- **Postgres (single region, OLTP)**: p99 ~3–15ms read, ~5–20ms write ở mức vài nghìn TPS trên hardware phổ thông; scale-out sharded có thể thêm 10–30% tail latency do cross-shard.
- **Cassandra/Scylla (RF=3, QUORUM)**: p99 ~5–15ms đọc/ghi ở mức 50–200k ops/s khi key phân bổ đều; tail tăng mạnh nếu compaction/tombstone nhiều hoặc hot partition.
- **Spanner**: p99 single-row read/write ~5–15ms trong cùng khu vực; cross-region commit thêm 10–50ms tuỳ khoảng cách và TrueTime bound; throughput scale tuyến tính theo node nhưng chi phí cao.

#### Checklist chọn partition key (Cassandra/Scylla)
- Tránh hotspot: key phải có entropy (ví dụ thêm bucket/hash) nếu traffic tập trung vào 1 id.
- Query-first: mỗi truy vấn chính cần partition key đầy đủ (tránh full scan/allow filtering).
- TTL/time-series: cân nhắc bucketing theo thời gian (ngày/giờ) để tránh partition phình vô hạn.
- Kích thước partition: giữ <100MB; quá lớn gây GC/compaction chậm.
- Secondary index hạn chế; ưu tiên thiết kế bảng theo truy vấn hoặc materialized view có kiểm soát.

#### Checklist chọn key/partition (Spanner hoặc Cockroach/Yugabyte)
- Tránh sequential monotonic key (auto-increment) vì hotspot; dùng UUID v4 hoặc hash-prefix.
- Nếu cần ordering, dùng **composite key**: (hash_prefix, business_id, timestamp) để vừa phân tán vừa sắp xếp.
- Phân vùng theo tenant/shard id nếu multi-tenant; giữ mỗi range nhỏ để dễ rebalancing.
- Xem xét locality: đặt **interleaved tables** hoặc **zone configs** (nếu có) để giảm cross-region hops cho truy cập nội vùng.

### 18.2 ASCII: CDC → Kafka → Flink → Lakehouse (Iceberg/Delta/Hudi)

```
 [Source DB] --binlog/CDC--> [Debezium/Connector]
        |                              |
        |                              v
        |                    +----------------+
        |                    | Kafka (topics) |
        |                    +---+--------+---+
        |                        |        |
        |                        |        +--> [DLQ / Replay]
        |                        v
        |                  +-----------+
        |                  | Flink Job |
        |                  | (EOS on   |
        |                  |  Kafka +  |
        |                  |  sink)    |
        |                  +-----+-----+
        |                        |
        |                        v
        |              +-------------------+
        |              | Lakehouse Table   |
        |              | (Iceberg/Delta/   |
        |              |  Hudi)            |
        |              +-------------------+
        |                        |
        |                        v
        |               [Queries: Trino/Presto/Spark/BI]
```

Key points:
- Flink set `exactly-once` checkpointing; Kafka sink with transactional.id; lakehouse sink with upsert/merge semantics (Iceberg MERGE, Delta UPSERT, Hudi UPSERT/BULK INSERT).
- Schema registry for evolution; compaction strategy in lakehouse; partitioning by date/tenant to avoid small files.

## 19) Appendix: Anti-Patterns
- Single hot partition (user id as key without entropy).
- Join-heavy workloads on NoSQL without careful modeling.
- Dual-writes without outbox/CDC; lost updates under concurrent writes.
- Infinite retry without DLQ; cache without stampede protection; unbounded compaction backlog.

---
> Use this as a checklist: start with workload profile → choose model → plan partition & consistency → define durability/SLO → add observability & migration plan.