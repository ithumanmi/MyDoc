---
title: "Backend Database Hub"
description: "Tổng quan module database cho backend engineer: từ kiến trúc, tối ưu, PostgreSQL đến MongoDB."
tags:
  - backend
  - database
updated: 2026-03-11
---

# 🗄️ Backend Database Hub

> Module phụ trách kiến thức database cho backend roadmap. Bạn sẽ tìm thấy chiến lược tổng quát (index, replication, sharding) và sổ tay vận hành cho từng hệ quản trị cụ thể.

## 📚 Tài liệu chính
| File | Nội dung chính | Khi nào đọc |
| --- | --- | --- |
| [Advanced Database Engineering](./advanced-db.md) | Kiến trúc index, replication, sharding, caching, observability | Bước đầu làm quen database ở quy mô lớn |
| [Database Optimization Deep Dive](./advanced-db-optimization.md) | Checklist thao tác hóa: profiling, replication, sharding, incident handling | Lúc cần tối ưu hoặc xử lý bottleneck cụ thể |
| [PostgreSQL Operations Handbook](./postgres-operations-handbook.md) | Vận hành Postgres: tuning, backup/PITR, extensions, playbook sự cố | Đội đang chạy PostgreSQL production |
| [MongoDB Operations Field Guide](./mongodb-operations-field-guide.md) | Schema design, index, replica set, sharding, backup của MongoDB | Đội sử dụng MongoDB/Document DB |

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