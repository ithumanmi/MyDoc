---
title: "Oracle Enterprise Operations"
description: "Cẩm nang vận hành Oracle Database: kiến trúc, RAC, Data Guard, partitioning, tuning, backup và checklist doanh nghiệp."
tags:
  - backend
  - database
  - oracle
updated: 2026-03-11
---

# 🏛️ Oracle Enterprise Operations

> Dành cho đội backend/DBA vận hành Oracle Database trong môi trường doanh nghiệp (core banking, telco, government). Bao quát kiến trúc, clustering, replica, tối ưu, backup và readiness checklist.

## 1. Kiến trúc Oracle Database
- **Instance vs Database**: Instance = bộ process + memory (SGA, PGA). Database = data files + redo logs + control files.
- **SGA (System Global Area)** gồm buffer cache, shared pool, redo log buffer, large pool. Tune theo workload.
- **Redo/Archive Log**: đảm bảo durability và phục vụ Data Guard.
- **Listener & Service**: kết nối thông qua `listener.ora`, `tnsnames.ora`, có thể gán service cho PDB/DB service khác nhau.

## 2. Multitenant & Pluggable Database (PDB)
- Oracle 12c+ hỗ trợ CDB (Container DB) chứa nhiều PDB → dễ tách/migrate.
- PDB clone để tạo môi trường test nhanh; snapshot clone giảm thời gian provision.
- Ghi tài liệu mapping ứng dụng ↔ PDB để quản lý lifecycle.

## 3. High Availability: RAC & Data Guard
### Oracle Real Application Clusters (RAC)
- Multiple instances truy cập chung shared storage → scalability + HA.
- Yêu cầu clusterware (Grid Infrastructure) và GI services (SCAN, VIP, GNS).
- Monitor Global Cache Service (GCS) wait, interconnect latency.

### Data Guard
- Primary & standby (physical/logical). Sử dụng redo apply để đồng bộ.
- **Synchronous (Maximum Availability/Protection)** vs **Asynchronous (Maximum Performance)**.
- Use Fast-Start Failover (FSFO) với Data Guard Broker để failover tự động.
- Bố trí `Observer` server riêng để giám sát.

## 4. Partitioning & Storage Features
- Table partitioning (range, list, hash, composite) để tối ưu query và maintenance.
- Interval partition cho dữ liệu time-series.
- `In-Memory Column Store` (option) để accelerate analytical query.
- Automatic Storage Management (ASM) quản lý disk groups, rebalance tự động.

## 5. Performance & Diagnostics
- **AWR (Automatic Workload Repository)** và **ASH (Active Session History)**: snapshot hiệu năng.
- Tools: ADDM, SQL Monitor, SQL Tuning Advisor, SQL Plan Baselines.
- Main wait classes: DB CPU, User I/O, System I/O, Concurrency, Cluster.
- Dùng `DBMS_XPLAN.DISPLAY_CURSOR` để xem execution plan + actual row.
- Resource Manager: phân bổ CPU/IO cho consumer group.

## 6. Security & Auditing
- Tận dụng Database Vault, Transparent Data Encryption (TDE), Data Redaction.
- Unified Auditing: cấu hình policy (FGA, Logon/Logoff).
- Tránh chạy DB với SYS/SYSTEM cho ứng dụng; tạo user + role riêng.

## 7. Backup & Recovery
- RMAN (Recovery Manager) là tiêu chuẩn: full/incremental, block change tracking.
- **Flashback Technology**: Flashback Query/Table/Database giúp khôi phục nhanh sai sót logic.
- Chuẩn hóa RPO/RTO: set lịch backup full + incremental + archive log shipping.
- Kiểm thử restore định kỳ: duplicate database, simulate data corruption.

## 8. Observability & Automation
- Enterprise Manager (OEM) hoặc Cloud Control theo dõi toàn bộ cluster.
- Metrics chính: wait time (AAS), redo log generation, RAC interconnect, PGA/SGA usage, tablespace usage, Data Guard lag.
- Automation: use Ansible/Shell/SQL*Plus script cho backup, patching, user provisioning.
- Patching strategy: PSU/BP, Apply RU (Release Update) theo quý.

## 9. Sự cố phổ biến & Playbook
| Sự cố | Dấu hiệu | Hướng xử lý |
| --- | --- | --- |
| RAC node eviction | Instance reboot, CRS log báo eviction | Kiểm tra heartbeat network, storage latency, cập nhật patch GI |
| Data Guard lag tăng | `v$dataguard_stats` báo apply lag lớn | Kiểm tra băng thông, CPU standby, redo shipping, tạm giảm workload hoặc chuyển log transport mode |
| Tablespace full | ORA-01653/54 | Thiết lập autoextend, monitor tablespace usage, di chuyển segment ít dùng |
| Redo log switch quá nhanh | Archive log queue backlog | Tăng size redo log, chỉnh checkpoint, xem xét batching transaction |
| Lock contention | Session chờ `enq: TX - row lock` | Review ứng dụng, thêm index, dùng `FOR UPDATE SKIP LOCKED`, tune transaction scope |

## 10. ✅ Checklist vận hành
- [ ] Bật AWR snapshot (15 phút) và lưu retention >= 30 ngày.
- [ ] Audit RAC interconnect latency và redundancy mạng.
- [ ] Thiết lập Data Guard Broker + Fast-Start Failover + observer.
- [ ] Lập lịch backup RMAN full + incremental, test restore mỗi quý.
- [ ] Theo dõi tablespace, ASM disk group, flash recovery area.
- [ ] Rà soát security: TDE, auditing, password policy, least privilege.
- [ ] Tạo runbook patching (GI + DB RU) và rehearsal trên environment dự phòng.
- [ ] Document mapping service ↔ ứng dụng, service level (OLTP, batch, reporting).

## 11. 🧪 Hands-on Labs
1. **RMAN Full Backup + Restore Test**
   - Chuẩn bị storage backup riêng, xác định channel (DISK/SBT_TAPE).
   - Chạy `rman target /` → `BACKUP DATABASE PLUS ARCHIVELOG`.
   - Tạo instance test → `DUPLICATE DATABASE TO testdb FROM ACTIVE DATABASE;`.
   - Kiểm tra mở database, so khớp SCN và datafile.

2. **Thiết lập Data Guard Physical Standby**
   - Bật `force logging`, `archive_lag_target`, tạo standby redo log.
   - Tạo password file, `tnsnames.ora`/`listener.ora` cho standby.
   - `RMAN BACKUP AS COMPRESSED BACKUPSET DATABASE` → ship sang standby → `RESTORE CONTROLFILE`, `RESTORE DATABASE`, `RECOVER MANAGED STANDBY DATABASE USING CURRENT LOGFILE DISCONNECT`.
   - Cấu hình Data Guard Broker (`dgmgrl`) và FSFO.

3. **RAC Node Failover Drill**
   - Trên cluster test, dừng 1 instance bằng `srvctl stop instance`.
   - Xác nhận service tự động relocate, session reconnect qua SCAN.
   - Quan sát AWR/ASH wait class, interconnect metric.
   - Ghi lại thời gian failover, cập nhật playbook.

4. **Partition Maintenance Window**
   - Tạo bảng partition range (theo ngày) với `interval partition`.
   - Viết script `ALTER TABLE ... SPLIT PARTITION` để chuẩn bị cho tháng mới.
   - Chạy `DBMS_STATS.GATHER_TABLE_STATS` cho partition mới.
   - Kiểm tra query dùng partition pruning qua `EXPLAIN PLAN`.

## 11. Liên kết & tài nguyên
- [Advanced Database Engineering](./advanced-db.md)
- [Database Optimization Deep Dive](./advanced-db-optimization.md)
- Oracle Docs: *Concepts*, *Administrator's Guide*, *Data Guard Concepts*, *RAC Administration*.
- Tool: Oracle Enterprise Manager, AWR Warehouse, SQLcl, Ansible modules for Oracle, Ora2pg (migration).