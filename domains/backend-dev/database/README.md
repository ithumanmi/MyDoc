---
title: "Backend Database Hub"
description: "Tổng quan database cho backend engineer: kiến trúc, tối ưu, PostgreSQL, MongoDB, Redis, Elasticsearch."
tags:
  - backend
  - database
updated: 2026-03-11
---

# 🗄️ Backend Database Hub

Module database cho backend roadmap: chiến lược tổng quát (index, replication, sharding) và sổ tay vận hành cho từng hệ quản trị.

## 📚 Tài liệu chính
| File | Nội dung chính | Khi nào đọc |
| --- | --- | --- |
| [Advanced Database Engineering](./advanced-db.md) | Kiến trúc index, replication, sharding, caching, observability | Làm quen database ở quy mô lớn |
| [Database Optimization Deep Dive](./advanced-db-optimization.md) | Checklist thao tác: profiling, replication, sharding, xử lý sự cố | Khi cần tối ưu hoặc xử lý bottleneck cụ thể |
| [PostgreSQL Operations Handbook](./postgres-operations-handbook.md) | Vận hành Postgres: tuning, backup/PITR, extensions, playbook sự cố | Đội vận hành PostgreSQL production |
| [MongoDB Operations Field Guide](./mongodb-operations-field-guide.md) | Schema, index, replica set, sharding, backup MongoDB | Đội dùng MongoDB/Document DB |
| [Next-Gen Storage & Databases](./next-gen-databases.md) ✨ | (⭐ **NEW**) Vector DBs (AI), Graph DBs, Distributed SQL, Time-Series DBs | Nâng cấp Senior Engineer cho dữ liệu hiện đại |

## 🧪 Database Practical Labs
Dựng node và giả lập lỗi để thực hành:
* [Replication master-slave PostgreSQL & failover](./labs/lab-postgres-replication-failover.md) 🔥 (dựng cụm Docker, thử failover)
* [Redis cluster & chống cache stampede](./labs/lab-redis-cluster-anti-stampede.md) 🔥 (viết mutex lock, bảo vệ DB khi traffic spike)


## 🚀 Lộ trình học gợi ý
1. **Hiểu nền tảng**: đọc *Advanced Database Engineering* để nắm khái niệm.
2. **Thao tác hóa**: chuyển sang *Database Optimization Deep Dive* để biết các bước đo/khắc phục.
3. **Chuyên sâu hệ quản trị**: chọn Postgres hoặc MongoDB handbook tùy hệ thống hiện có.
4. **Áp dụng & log kết quả**: dùng checklist Apply-it trong từng tài liệu để audit sản phẩm của bạn.

## 🔗 Liên kết tham khảo
- [Backend Roadmap](../README.md)
- [System Design Universe](../system-design/system-design-universe.md)
- [Backend Monitoring & Observability](../monitoring-observability.md)

> Tip: mỗi lần thực hiện thay đổi database lớn (reshard, failover, migrate), cập nhật vào tài liệu tương ứng để giữ knowledge base sống.