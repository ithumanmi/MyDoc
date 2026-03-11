---
title: "Redis Durability Playbook"
description: "Cách Redis bảo toàn dữ liệu khi server sập nguồn: snapshot RDB, append-only file, replication và cluster."
tags:
  - backend
  - database
  - redis
updated: 2026-03-11
---

# 🧠 Redis Durability Playbook

> Redis chạy trong RAM nhưng không đồng nghĩa mất điện là mất sạch dữ liệu. Hệ thống dùng snapshot, append log, replication và cluster để đảm bảo dữ liệu có thể phục hồi.

## 1. Tại sao phải quan tâm?
- Redis thường giữ state quan trọng (session, counter, queue).
- Mất điện hoặc crash có thể xoá toàn bộ RAM.
- Do đó phải cấu hình **persistence + replication** phù hợp workload.

## 2. Cơ chế Persistence
### 2.1. RDB (Snapshot)
- Redis định kỳ chụp snapshot (RDB file) và lưu xuống disk.
- Ưu: file gọn, restore nhanh.
- Nhược: mất dữ liệu giữa 2 lần snapshot (ví dụ 5 phút).

### 2.2. AOF (Append-Only File)
- Ghi mỗi lệnh ghi (write command) vào log trên disk.
- Tùy chọn `appendfsync always/everysec/no`:
  - `always`: an toàn nhất, chậm nhất.
  - `everysec` (default): trade-off hợp lý (mất tối đa 1s).
  - `no`: phụ thuộc OS flush.
- Redis có thể rewrite AOF để tránh file quá lớn.

### 2.3. Hybrid Mode
- Từ Redis 4: `aof-use-rdb-preamble yes` → file AOF bắt đầu bằng snapshot RDB + append log.
- Lợi ích: startup nhanh như RDB, vẫn ghi incremental như AOF.

## 3. Replication & Sentinel/Cluster
- Dù bật persistence, nên có **replica** ở máy khác.
- Replication async: master ghi xong mới gửi replicates → có thể mất vài ms dữ liệu nếu master chết.
- Dùng **Redis Sentinel** hoặc **Redis Cluster** để failover tự động.
- Multi-AZ deployment: master và replica đặt ở data center khác nhau để tránh mất nguồn cùng lúc.

## 4. Cấu hình khuyến nghị
```conf
save 60 1000        # RDB: mỗi 60s nếu >=1000 keys thay đổi
appendonly yes
appendfsync everysec
dir /data/redis
dbfilename dump.rdb
appendfilename appendonly.aof
```
- Monitor `aof_current_size`, `rdb_last_bgsave_time_sec` để kiểm soát.

## 5. Khôi phục sau sự cố
1. Khi Redis khởi động lại, nó đọc RDB/AOF để load dữ liệu vào RAM.
2. Nếu cả master lẫn replica cùng mất, dùng backup file từ storage bên ngoài (S3/NFS).
3. Test recovery định kỳ: spin up instance mới, copy file RDB/AOF và start Redis.

## 6. Anti-pattern
- Tắt hoàn toàn persistence vì “Redis chỉ để cache” nhưng lại lưu session quan trọng.
- Chỉ dựa vào RDB với khoảng thời gian dài → mất dữ liệu nhiều.
- Không replicate → mất điện = mất dữ liệu.
- Đặt master và replica cùng rack (cùng nguồn điện).

## 7. Checklist
- [ ] Bật persistence: RDB, AOF hoặc hybrid.
- [ ] Đặt `appendfsync everysec` hoặc `always` cho data quan trọng.
- [ ] Deploy replica + Sentinel/Cluster cho failover.
- [ ] Lưu trữ backup RDB/AOF ra object storage định kỳ.
- [ ] Thực hiện recovery drill mỗi quý.

## 8. Liên kết
- [Redis Persistence Docs](https://redis.io/docs/management/persistence/)
- [Redis Sentinel](https://redis.io/docs/management/sentinel/)
- [Redis Cluster](https://redis.io/docs/management/scaling/)