---
title: "Advanced Database Engineering"
description: "Nắm kiến trúc index, replication, sharding và playbook chẩn đoán bottleneck cho backend scale lớn."
tags:
  - backend
  - database
  - scaling
updated: 2026-03-11
---

# 🗄️ Advanced Database Engineering

> [← Back to Backend Development](../README.md)

Module này giúp bạn hiểu cách database hoạt động ở tầng máy, từ chiến lược index, partitioning, replication đến quan sát hiệu năng và công cụ chẩn đoán. Đây là lớp nền trước khi bước vào các bài system design nặng đô hơn.

## 1. Index Foundations (Data Structures)
Indexes tăng tốc đọc nhưng ảnh hưởng write và chiếm dung lượng. Hãy chọn đúng kiểu cho workload của bạn.

### B-Tree (Balanced Tree)
- **Dùng cho:** MySQL InnoDB, PostgreSQL, SQL Server.
- **Ưu tiên:** Query range (`BETWEEN`, `<`, `>`), ORDER BY.
- **Structure:** Leaf node link nhau để scan tuần tự nhanh.

### LSM Tree (Log-Structured Merge Tree)
- **Dùng cho:** Cassandra, RocksDB, ScyllaDB, LevelDB.
- **Luồng write:** MemTable trong RAM → flush thành SSTable bất biến.
- **Đánh đổi:** Write cực nhanh, read cần check nhiều SSTable → cần Bloom filter + compaction.

### Các Index đặc biệt
- **Hash Index:** O(1) lookup, không hỗ trợ range (Redis Hash, PostgreSQL Hash Index).
- **GIN/GiST:** Full-text, JSONB, spatial / nearest-neighbor (PostgreSQL).
- **BRIN:** Block Range Index – phù hợp bảng time-series khổng lồ.

## 2. Partitioning & Sharding Strategies

### Partitioning (Trong cùng instance)
- Range, List, Hash giúp chia bảng nội bộ → index nhỏ hơn, VACUUM nhanh.
- Dùng cho PostgreSQL declarative partitioning, MySQL partitioned tables.

### Sharding (Distributed)
- **Horizontal partitioning** sang nhiều node độc lập.
- Chọn shard key tránh hotspot (hash user_id, hoặc composite `tenant_id + hash(user_id)`).
- **Consistency trade-off:** cross-shard JOIN khó; transaction cần 2PC hoặc Saga.

### Directory & Consistent Hashing
- Directory service mapping (User → Shard) linh hoạt nhưng là SPOF → replicate + cache.
- Consistent hashing giảm data phải migrate khi thêm shard mới.

## 3. Replication & Consistency Models

### Primary-Replica
- Write vào Primary, replica phục vụ read. Cẩn thận replication lag.
- Tùy scenario: `read_your_own_writes` → route user-critical read về primary.

### Multi-Primary / Active-Active
- Dùng khi cần multi-region low latency.
- Cần conflict resolution (vector clock, CRDT) hoặc route theo region affinity.

### Consensus-based Replication
- **Raft/Paxos** dùng trong CockroachDB, TiDB, YugabyteDB để giữ ACID toàn cụm.
- Hiểu khái niệm **quorum** (ví dụ 5 node → cần 3 phiếu để commit).

## 4. SQL, NoSQL, NewSQL & Serverless

| Category | Khi nào dùng | Ví dụ |
| --- | --- | --- |
| SQL truyền thống | Transaction mạnh, schema rõ | PostgreSQL, MySQL |
| NoSQL (Key-value/Document) | Throughput cực lớn, schema linh hoạt | DynamoDB, MongoDB |
| NewSQL / Distributed SQL | Mở rộng ngang + ACID | CockroachDB, TiDB, YugabyteDB |
| Serverless DB | Traffic bursty, không muốn quản lý infra | Aurora Serverless v2, PlanetScale |

Vector/AI workloads đang yêu cầu **hybrid**: lưu metadata trong SQL, embedding trong vector store (Milvus/pgvector). Thiết kế sớm pipeline đồng bộ.

## 5. Query Diagnostics & Observability
- Bật **Slow Query Log** hoặc `pg_stat_statements`, `performance_schema` để thấy top query.
- Dùng `EXPLAIN (ANALYZE, BUFFERS)` (Postgres) / `EXPLAIN FORMAT=JSON` (MySQL) để hiểu plan.
- Theo dõi metric: buffer hit ratio, replication lag, checkpoint write, lock wait.
- Gắn alert khi p95 query latency > SLA hoặc deadlock tăng đột biến.

## 6. Caching & Application Patterns
- Luôn thử caching (Redis, Memcached) trước khi sharding.
- Pattern phổ biến: read-through cache, write-through, write-behind.
- Cân nhắc **materialized view + CDC** để giảm query phức.
- Kết hợp với [System Design Universe](../system-design/system-design-universe.md) layer 2 (Database Design) để định vị maturity.

## 7. Hands-on Playbook
1. **Bật observability**: slow query log, pg_stat_statements, cloud insights.
2. **Lập top offenders**: query chiếm >20% CPU/IO.
3. **EXPLAIN + Index review**: kiểm tra filter, join order, row estimate.
4. **Benchmark**: dùng `pgbench`, `sysbench` hoặc JMeter để mô phỏng workload.
5. **Test failover**: chạy chaos (kill primary) → đo thời gian promote replica.
6. **Plan sharding/caching**: mô tả routing layer, consistent hashing, migration plan.

## 8. ✅ Apply it
- [ ] Gắn front-matter & owner cho database tại công ty (version, RTO/RPO).
- [ ] Audit toàn bộ index: cột nào không còn xuất hiện trong query thì drop.
- [ ] Chạy `EXPLAIN ANALYZE` cho 5 query chậm nhất, ghi lại insight.
- [ ] Thiết kế chiến lược read replica + routing “read your writes”.
- [ ] Viết sơ đồ shard key + kế hoạch reshard (tooling, downtime, backfill).
- [ ] Lập dashboard replication lag, deadlock count, buffer hit ratio.

## 9. Further Reading & Cross-links
- [Database Optimization Deep Dive](./advanced-db-optimization.md)
- [System Design Case Studies](../system-design/case-studies.md)
- [Backend Monitoring & Observability](../monitoring-observability.md)
- Papers: *The Log-Structured Merge-Tree*, *Spanner*, *Calvin*.
