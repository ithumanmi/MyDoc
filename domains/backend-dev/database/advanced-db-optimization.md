---
title: "Database Optimization Deep Dive"
description: "Checklist thao tác hóa để tối ưu query, replication, sharding và xử lý sự cố database ở quy mô triệu user."
tags:
  - backend
  - database
  - performance
updated: 2026-03-11
---

# 🗄️ Database Optimization: Indexing & Sharding Deep Dive

> [← Back to Backend Roadmap](../README.md)

Khi ứng dụng đạt 1 triệu users, **database** thường là bottleneck đầu tiên. Hướng dẫn này là phiên bản “thao tác hóa” của module Advanced Database: tập trung vào kỹ thuật đo đạc, tối ưu và vận hành production.

---

## 1. Indexing Deep Dive (Tối ưu truy vấn) 🔍

Index giống như "mục lục" của cuốn sách. Thay vì lật từng trang (full table scan), bạn nhảy thẳng đến trang cần thiết.

### 1.1 B-Tree Index (Default) 🌳
- **Hoạt động:** Dữ liệu được sắp xếp để binary search, leaf node chain để scan range nhanh.
- **Chi phí:** Update/insert phải chỉnh lại cấu trúc, gây thêm IO.
- **Thực hành:** Dùng `EXPLAIN` để đảm bảo query range đang dùng index thay vì seq scan.

### 1.2 Composite Index 🔗
- Query multi-condition (`WHERE last_name='Smith' AND first_name='John'`).
- Tạo index `(last_name, first_name)`.
- **Leftmost Prefix Rule:** `(A,B,C)` chỉ hỗ trợ query chứa A; bỏ A thì index vô dụng.

### 1.3 Covering Index ⚡
- Nếu index bao gồm toàn bộ cột trong `SELECT`, database không phải truy cập bảng chính (index only scan).
- MySQL InnoDB: tránh `SELECT *`, chỉ lấy cột cần.

### 1.4 Giám sát index bloat
- PostgreSQL `pg_stat_all_indexes`, `pg_stat_user_indexes` giúp tìm index ít được dùng.
- Chạy `REINDEX` khi index bloat > 20% (đặc biệt với update/delete nhiều).

---

## 2. Replication (Mở rộng read & HA) 📖

### Master–Slave / Primary–Replica
- Replica chịu tải read, primary lo write.
- **Replication lag** = thời gian giữa WAL apply trên replica so với primary.
- **Giải pháp:**
  - Route request cần dữ liệu mới nhất về primary (“read your writes”).
  - Bật semi-sync replication (MySQL) hoặc quorum commit.

### Monitoring checklist
- PostgreSQL: `pg_stat_replication` (lag, state, sync_priority).
- MySQL: `SHOW SLAVE STATUS\\G` (Seconds_Behind_Master).
- Alert khi lag > SLA (ví dụ 3 giây).

### Multi-region replication
- Dùng **logical replication** hoặc CDC để stream sang region khác.
- Hợp nhất với queue (Kafka) để xây analytics pipeline mà không ảnh hưởng OLTP.

---

## 3. Sharding (Mở rộng write & dung lượng) 🔪

### 3.1 Chiến lược shard
- **Hash-based:** phân phối đều nhưng reshard khó → dùng consistent hashing ring.
- **Range-based:** dễ hiểu, dễ thêm shard, nhưng dễ hotspot → cần auto-rebalance.
- **Directory-based:** lookup table map user → shard. Phải replicate + cache để tránh SPOF.

### 3.2 Tooling & migration
- Thiết kế **ID scheme** chứa shard id (Snowflake ID, ksuid) để biết data đang nằm đâu.
- Resharding: double-write vào shard mới, dùng CDC copy data lịch sử, sau đó flip traffic.
- Automation: Vitess, Citus, YugabyteDB giải quyết routing và failover.

### 3.3 Cross-shard transaction
- 2PC tốn chi phí, cần coordinator và timeout.
- Saga pattern: chia thành bước local transaction + step compensation.

---

## 4. Observability & Incident Handling 🛠️

### 4.1 Query diagnostics
- `EXPLAIN (ANALYZE, BUFFERS)` để thấy actual row vs estimate.
- Check `Rows Removed by Filter`, `Loop` count để biết mis-estimate.
- Lưu plan snapshot trước/ sau khi thêm index.

### 4.2 Lock & contention
- PostgreSQL: `pg_locks`, `pg_stat_activity` để phát hiện lock chồng chéo.
- MySQL: `INNODB_LOCKS`, `INNODB_LOCK_WAITS`.
- Giải pháp: chuẩn hóa thứ tự update bảng, giảm transaction scope, dùng optimistic lock.

### 4.3 Capacity planning
- Track storage growth, WAL size, checkpoint frequency.
- Đặt ngưỡng 70% disk usage → scale trước khi chạm 90%.
- Document RTO/RPO, diễn tập failover hàng quý.

---

## 5. Common Pitfalls 🕳️

### N+1 query
- Fix bằng JOIN hoặc batch `WHERE id IN (...)`.
- ORM: bật lazy/eager loading đúng chỗ, hoặc dùng data loader pattern.

### Deadlock
- Lock resource cùng thứ tự.
- Bật deadlock logging, capture query để phân tích.

### Hot partition
- Theo dõi top partition theo write/read.
- Reshard hoặc thêm caching layer trước partition hotspot.

---

## 6. Hands-on Checklist 📝
- [ ] Bật slow query log (Postgres: `log_min_duration_statement`, MySQL: `slow_query_log`).
- [ ] Lập bảng Top 10 query theo CPU/IO, attach plan.
- [ ] Review index usage mỗi sprint, drop index unused >90 ngày.
- [ ] Thiết lập dashboard replication lag, lock wait, deadlock count.
- [ ] Viết playbook failover + diễn tập 1 lần/quý.
- [ ] Mô phỏng reshard (dry-run) với tool/skript hiện có.
- [ ] Kết nối database metrics vào stack observability (Prometheus/Grafana/NewRelic).

## 7. Cross-links & Resources
- [Advanced Database Engineering](./advanced-db.md) – kiến thức nền & chiến lược tổng quan.
- [System Design Universe](../system-design/system-design-universe.md) – layer database architecture.
- [Backend Monitoring & Observability](../monitoring-observability.md)
- Tool: pgBadger, pt-query-digest, gh-ost, Vitess, Citus, Orchestrator.
