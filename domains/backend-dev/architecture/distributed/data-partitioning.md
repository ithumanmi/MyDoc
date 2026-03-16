---
title: "Data Partitioning & Sharding"
description: "Level 3-4: chiến lược partition dữ liệu (range/hash/directory/geo) và best practices vận hành."
tags:
  - backend
  - architecture
  - database
updated: 2026-03-11
---

# 🗂️ Data Partitioning (L3-L4)

> Khi dữ liệu vượt khả năng 1 node, cần partition để scale. Lựa chọn shard key và chiến lược balancing quyết định hiệu năng và độ phức tạp.

## 1. Partition strategies
- **Horizontal Partitioning (Sharding):** chia bảng theo range/hash/list.
- **Vertical Partitioning:** tách cột hoặc module sang DB khác.
- **Functional Partitioning:** mỗi bounded context → DB riêng.

### Sharding techniques
| Technique | Mô tả | Use case |
| --- | --- | --- |
| Range shard | Dựa trên timestamp/id sequence | Time-series, log, analytics |
| Hash shard | Hash key → shard | Tránh hotspot, user id |
| Directory-based | Metadata map key → shard | Dễ thay đổi shard nhưng thêm hop |
| Geo shard | Chia theo region | Multi-region compliance |

## 2. Shard key selection checklist
- Số lượng dữ liệu dự kiến per shard.
- Tốc độ tăng trưởng (avoid rebalancing quá thường xuyên).
- Query pattern (JOIN cross-shard?).
- Hotspot risk (user VIP, tenant lớn).

## 3. Rebalancing & migrations
- **Consistent hashing** giúp thêm shard không phải move tất cả data.
- **Dual write / cutover**: sync data sang shard mới trước khi chuyển traffic.
- **Automation**: tooling (Vitess, Citus, Cockroach) hỗ trợ reshard.
- **Online migration:** dùng change data capture (CDC) để đồng bộ trong khi migrate; validate bằng checksum per chunk.
- **Hot shard relief:** tạm thời thêm **captive shard** cho tenant/user lớn, hoặc dùng **hierarchical sharding**.

## 4. Indexing & routing
- Application cần `ShardResolver` để xác định shard trước khi query.
- Kết hợp cache layer (Redis cluster) để giảm cross-shard query.
- Query fan-out + merge: cẩn trọng latency.
- **Global secondary index:** nếu cần tra cứu theo khóa khác, cân nhắc index toàn cục hoặc duplicate dữ liệu; lưu ý chi phí fan-out.
- **Multi-region routing:** geo shard kết hợp latency-based routing; read local, write theo master hoặc per-region leader.

## 5. Observability
- Metric per shard: storage size, QPS, latency.
- Alert khi shard đầy hoặc lệch traffic.
- Log routing decision để debug.
- **Heatmap keys:** log top key/hash range gây hotspot.
- **SLO per shard:** error/latency budget riêng cho shard quan trọng.

## ✅ Apply it
- [ ] Đánh giá dữ liệu hiện tại: size mỗi bảng, tốc độ tăng trưởng, xác định ngưỡng shard.
- [ ] Chọn shard key cho bảng quan trọng (Users/Orders) và mô phỏng phân bố.
- [ ] Viết module ShardResolver + config mapping (range/hash).
- [ ] Thiết kế playbook resharding (dual write, backfill, cutover plan).
- [ ] Thiết lập dashboard monitor mỗi shard (disk, QPS, replication lag).

## 🔗 Cross-reference
- [Scaling Strategy](./scaling-strategy.md) – ra quyết định scale up vs shard.
- [Advanced Algorithms](./advanced-algorithms.md) – consistent hashing chi tiết.
- [Event Sourcing & CQRS](./event-sourcing-cqrs.md) – partition event store/read model.
- [Multi-Tenancy Patterns](./multi-tenancy-patterns.md) – shard theo tenant.