---
title: "PostgreSQL Operations Handbook"
description: "Hướng dẫn vận hành PostgreSQL: kiến trúc, tuning, observability, backup/restore và best practice production."
tags:
  - backend
  - database
  - postgres
updated: 2026-03-11
---

# 🐘 PostgreSQL Operations Handbook

> Tài liệu dành cho backend engineer muốn vận hành PostgreSQL ở quy mô production (từ single node tới cluster). Che phủ kiến trúc lõi, tối ưu hiệu năng, quan sát, replication và kịch bản sự cố.

## 1. Kiến trúc lõi Postgres
- **Process-based**: mỗi connection = 1 process (`postgres` backend). Cần connection pooling (PgBouncer) để tránh fork quá nhiều.
- **MVCC**: Multi-Version Concurrency Control giữ snapshot per transaction → cần VACUUM để dọn tuple chết.
- **WAL (Write-Ahead Log)**: mọi thay đổi ghi vào WAL trước khi flush data file → nền tảng cho crash recovery & replication.
- **Buffer cache**: `shared_buffers` lưu page nóng; OS page cache vẫn quan trọng.

## 2. Tuning cốt lõi
| Tham số | Gợi ý | Ghi chú |
| --- | --- | --- |
| `shared_buffers` | 25% RAM (max 8GB recommend) | Quá lớn sẽ giảm hiệu quả OS cache |
| `work_mem` | 4–64 MB per connection | Dùng cho sort/hash; đừng set quá cao tránh OOM |
| `maintenance_work_mem` | 512MB–2GB | VACUUM/CREATE INDEX |
| `effective_cache_size` | 50–75% RAM | Giúp planner ước lượng khả năng hit cache |
| `max_wal_size` | 1–4 lần write peak trong 5 phút | Tránh checkpoint quá dày |

- Bật `autovacuum` và monitor `pg_stat_user_tables.vacuum_count` để tránh bloat.
- Sử dụng `pg_stat_statements` để thấy query “top talkers”.

## 3. Index & Query Plan
- Dùng `EXPLAIN (ANALYZE, BUFFERS)` để đo thực tế (row estimate vs actual).
- `btree` là mặc định, nhưng đừng quên `GIN` (full-text/JSONB), `BRIN` (time series), `GiST` (spatial).
- `partial index` giảm kích thước (ví dụ chỉ index status='active').
- Theo dõi `idx_scan`, `idx_tup_read` vs `idx_tup_fetch` để biết index hiệu quả.

## 4. Replication & High Availability
- **Streaming replication**: standby đọc WAL từ primary qua `walreceiver`.
- Cấu hình `synchronous_commit = remote_apply` khi cần consistency mạnh.
- Tooling failover: Patroni, repmgr, Stolon, pg_auto_failover.
- Đối với multi-region: logical replication hoặc CDC (Debezium) để stream sang region/phân tích.

## 5. Backup & Restore
- **Physical backup**: `pg_basebackup`, hoặc dùng `wal-g`, `pgBackRest` để lưu lên object storage.
- **Point-in-time recovery (PITR)**: lưu WAL archive (`archive_mode=on`, `archive_command`).
- **Logical backup**: `pg_dump`/`pg_restore` – tiện di chuyển schema, nhưng chậm với DB lớn.
- Lập script test restore (spin up instance mới, apply backup + WAL) mỗi quý.

## 6. Observability Stack
- Metric cốt lõi: `xact_commit`, `blks_hit/read`, `deadlocks`, `temp_files`, replication lag, autovacuum lag.
- Dùng exporter: `postgres_exporter`, `pganalyze`, `pgwatch2`.
- Log: set `log_line_prefix` chuẩn hóa, bật `log_duration`, `log_lock_waits`, `log_statement = 'ddl'`.
- Tạo dashboard: TPS, cache hit ratio, slow query count, autovacuum hoạt động.

## 7. Extensions nên biết
- `pg_stat_statements`: profiling query.
- `pg_partman`: quản lý partition.
- `pg_cron`: scheduling job SQL.
- `pg_repack`: rebuild bảng/index online.
- `pgvector`: lưu trữ embedding.
- `timescaledb`: time-series extension.

## 8. Kịch bản sự cố & Playbook
| Sự cố | Triệu chứng | Hướng xử lý nhanh |
| --- | --- | --- |
| Autovacuum không theo kịp | Table bloat, query chậm | Tăng `autovacuum_work_mem`, chạy `VACUUM (FULL)` off-peak, chia partition |
| Replication lag tăng | `pg_stat_replication` lag > SLA | Kiểm tra network/WAL bandwidth, tune `wal_sender_timeout`, thêm replica slot dedicated |
| Connection saturation | QPS giảm, connection full | Deploy PgBouncer (transaction pooling), giới hạn `max_connections` hợp lý |
| Checkpoint quá dày | đĩa IO spike | Tăng `max_wal_size`, tune `checkpoint_timeout`, giám sát `checkpoint_warning` |

## 9. ✅ Apply Checklist
- [ ] Cấu hình PgBouncer/Pgpool để pool connection.
- [ ] Bật `pg_stat_statements` và set job thu thập top query hàng tuần.
- [ ] Thiết lập `wal-g` hoặc `pgBackRest` + kiểm thử restore định kỳ.
- [ ] Dashboard replication lag + alert khi > 5s.
- [ ] Run `VACUUM (FULL)` hoặc `pg_repack` cho bảng bloat > 30%.
- [ ] Kiểm tra extension inventory, cập nhật version/tính tương thích.
- [ ] Tài liệu hóa playbook failover và diễn tập với Patroni/repmgr.

## 10. 🧪 Hands-on Labs
1. **Thiết lập Streaming Replication**
   - Backup base bằng `pg_basebackup -h primary -D /var/lib/postgresql/standby -R -X stream`.
   - Sửa `postgresql.conf`: bật `wal_level = replica`, `max_wal_senders`, `archive_mode`.
   - Cấu hình `pg_hba.conf` để secondary kết nối.
   - Start standby, kiểm tra `pg_stat_replication`.

2. **PITR với wal-g/pgBackRest**
   - Cài `wal-g` (hoặc pgBackRest), cấu hình storage backend (S3/MinIO).
   - Chạy full backup: `wal-g backup-push /var/lib/postgresql/data`.
   - Tạo điểm restore `SELECT pg_create_restore_point('before_migration');`.
   - Xóa dữ liệu thử nghiệm, dùng `wal-g backup-fetch` + replay WAL đến restore point.

3. **Profiling Query bằng pg_stat_statements + EXPLAIN**
   - Bật extension: `CREATE EXTENSION pg_stat_statements;` và update `shared_preload_libraries`.
   - Gửi workload thực tế.
   - `SELECT query, calls, total_exec_time FROM pg_stat_statements ORDER BY total_exec_time DESC LIMIT 5;`.
   - Với query chậm, chạy `EXPLAIN (ANALYZE, BUFFERS)` để tối ưu index/plan.

4. **VACUUM/REINDEX cho bảng bloat**
   - Dùng `pgstattuple` hoặc `pg_class` để đo bloat.
   - Chạy `VACUUM (FULL)` hoặc `pg_repack --table=public.orders` ở off-peak.
   - So sánh size trước/sau, cập nhật maintenance window.

## 10. Liên kết & tài nguyên
- [Advanced Database Engineering](./advanced-db.md)
- [Database Optimization Deep Dive](./advanced-db-optimization.md)
- Sách: *PostgreSQL Up & Running*, *High Performance PostgreSQL*.
- Blog/tool: CYBERTEC, pganalyze, CrunchyData, `pgMustard`.