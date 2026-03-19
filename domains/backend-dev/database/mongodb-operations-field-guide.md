---
title: "MongoDB Operations Field Guide"
description: "Chiến lược thiết kế schema, tối ưu hiệu năng, replica set, sharding và playbook vận hành MongoDB ở production."
tags:
  - backend
  - database
  - mongodb
updated: 2026-03-11
---

# 🍃 MongoDB Operations Field Guide

Hướng dẫn cho backend/infra vận hành MongoDB từ startup đến enterprise: thiết kế schema tối ưu đọc/ghi, index, replica set, sharding, backup và checklist giám sát.

## 1. Kiến trúc MongoDB
- **Document store**: dữ liệu JSON/BSON linh hoạt, hỗ trợ nested document.
- **WiredTiger storage engine**: copy-on-write, sử dụng compression (snappy/zstd) và cache riêng (`wiredTigerCacheSizeGB`).
- **Replica set**: 1 primary + nhiều secondary, dùng RAFT-like election.
- **OpLog**: log vòng (cửa sổ thời gian) để secondary tailing, cũng dùng cho change stream.

## 2. Schema Design Principles
- **Model theo query**, không theo normalization truyền thống. Ưu tiên embed dữ liệu hay truy cập cùng lúc.
- **Embed vs Reference**:
  - Embed: quan hệ 1-n nhỏ (profile + settings).
  - Reference: n-n, hoặc document lớn vượt 16MB.
- Dùng **Bucket pattern** cho time-series/logs (group 1 giờ/1 ngày).
- Tránh document phình to liên tục (update `$push` không giới hạn) → dùng capped array hoặc bucket.
- Tận dụng **schema validation** (JSON Schema) để giữ chất lượng dữ liệu.

## 3. Index Strategy
- Index là B-Tree; hỗ trợ compound, multikey (array), wildcard, partial index.
- **Compound index**: tuân thủ rule `prefix` (giống SQL). Example: `{ userId:1, createdAt:-1 }`.
- **TTL index** cho dữ liệu hết hạn (cache, session), tự động xóa.
- **Text/Atlas Search**: dùng text index hoặc tích hợp Atlas Search (Lucene) để query full-text nâng cao.
- Monitor `db.collection.stats().indexSizes`, `system.profile` để phát hiện query không dùng index.

## 4. Performance & Diagnostics
- Bật **Profiling** (`db.setProfilingLevel(1)`) cho query > N ms; log vào `system.profile`.
- Sử dụng `explain("executionStats")` để xem plan, số document scan.
- Theo dõi `wiredTiger.cache`, `opcounters`, `locks`, `page faults`.
- Tinh chỉnh **connection pooling** ở driver (maxPoolSize, minPoolSize) và dùng **retryable writes** để tránh lỗi transient.

## 5. Replica Set & High Availability
- Thiết lập 3 node tối thiểu (Primary, Secondary, Arbiter hoặc thứ hai Secondary) để đảm bảo quorum.
- `priority` điều chỉnh node nào được ưu tiên làm primary.
- `hidden` secondary phục vụ analytics để tránh ảnh hưởng traffic.
- `readPreference`: `primary`, `primaryPreferred`, `secondary`, `nearest` tùy use case.
- Change Streams/OpLog: dùng để sync sang cache, search, hoặc trigger event.

## 6. Sharding
- Thành phần: **Config Server**, **Mongos router**, **Shard (replica set)**.
- **Shard key** quyết định phân phối dữ liệu:
  - Hash key → phân bố đều, tránh hotspot (phù hợp write nhiều).
  - Range key → thuận lợi range scan nhưng dễ hotspot → cần **zone sharding**.
- Bật **balancer** để tự động di chuyển chunk, nhưng nên tắt khi chạy bulk migration.
- Monitor chunk size, chunk imbalance, `balancerStatus` để tránh shard bias.

## 7. Backup & Recovery
- **Mongodump/mongorestore**: phù hợp DB nhỏ, backup logic.
- **Filesystem snapshot**: dùng LVM/EBS snapshot, nhớ `fsyncLock` để đảm bảo nhất quán.
- **Oplog based backup**: sử dụng MongoDB Cloud Backup hoặc `mongobackup` (Percona Backup for MongoDB).
- Test restore định kỳ: downtime, consistency, và script automation.

## 8. Observability Stack
- Atlas đã tích hợp metric/alert; tự host nên dùng `prometheus-mongodb-exporter`.
- Metric quan trọng:
  - Opcounters (insert/query/update/delete).
  - Replication lag (`rs.printSlaveReplicationInfo()`).
  - Cache usage (`wiredTiger cache used %`).
  - Connections, locks, document/idx scan ratio.
- Log audit: bật `auditLog` nếu có yêu cầu compliance.

## 9. Sự cố phổ biến & Playbook
| Sự cố | Triệu chứng | Hướng xử lý |
| --- | --- | --- |
| Write concern timeout | Driver báo `WriteConcernFailed` | Tăng replication capacity, kiểm tra secondary lag, điều chỉnh `w` phù hợp |
| Chunk hotspot | Shard cụ thể đầy CPU/disk | Đánh giá shard key, bật hashed key hoặc zone sharding, rebalance chunk |
| Cache full (WiredTiger) | `cache dirty bytes` cao, latency tăng | Giảm `wiredTigerCacheSizeGB`, optimize query/index, thêm RAM |
| Oplog overflow | Secondary out of sync | Tăng kích thước oplog, đảm bảo backup không giữ lâu, khôi phục từ snapshot |

## 10. ✅ Checklist hành động
- [ ] Thiết kế schema (embed/reference) dựa trên top 5 query thực tế.
- [ ] Index review mỗi sprint: drop index không dùng, thêm compound/TTL đúng nhu cầu.
- [ ] Thiết lập replica set 3 node + hidden node cho analytics.
- [ ] Script backup (mongodump/snapshot) + test restore hàng tháng.
- [ ] Dashboard replication lag, opcounters, cache usage, chunk distribution.
- [ ] Ghi tài liệu playbook sharding (thêm shard, reshard, chunk migration).
- [ ] Bật alert khi profiling phát hiện query > 500ms.

## 11. 🧪 Hands-on Labs
1. **Replica Set Lab (3 node)**
   - Spin up 3 mongod instance: `mongod --replSet rs0 --port 27017/27018/27019`.
   - `mongosh` → `rs.initiate({ _id: 'rs0', members:[{_id:0,host:'localhost:27017'},{_id:1,host:'localhost:27018'},{_id:2,host:'localhost:27019',arbiterOnly:true}] })`.
   - Test failover: stop primary, kiểm tra election time, readPreference.

2. **Profiling & Query Tuning Lab**
   - `db.setProfilingLevel(1, { slowms: 50 })`.
   - Chạy workload sample, đọc `db.system.profile.find().sort({ millis:-1 }).limit(5)`.
   - Với query chậm, `db.collection.find(...).explain('executionStats')`, thêm index/điều chỉnh schema.

3. **Sharding PoC với Hashed Key**
   - Khởi tạo config server + mongos (dùng docker compose).
   - `sh.enableSharding('appdb')`, `sh.shardCollection('appdb.events', { userId: 'hashed' })`.
   - Bulk insert, kiểm tra `sh.status()` xem distribution.
   - Chạy balancer và theo dõi chunk move trong `config.changelog`.

4. **Backup/Restore Pipeline**
   - `mongodump --uri='mongodb://primary' --archive | gzip > backup.archive.gz`.
   - Simulate data loss, restore bằng `gunzip -c backup.archive.gz | mongorestore --archive --drop`.
   - Với cluster lớn, thử Percona Backup for MongoDB: `pbm backup --type=physical`.

## 11. Liên kết & tài nguyên
- [Advanced Database Engineering](./advanced-db.md)
- [Database Optimization Deep Dive](./advanced-db-optimization.md)
- Official docs: docs.mongodb.com – mục Schema Design, Production Notes.
- Công cụ: MongoDB Atlas, Compass, `mongosh`, Percona Backup for MongoDB, MMS/Cloud Manager.