---
title: "Backend Architecture Hub"
description: "Bản đồ điều hướng toàn bộ tài liệu kiến trúc backend: từ high performance, microservices, cloud-native đến distributed systems."
tags:
  - backend
  - architecture
  - roadmap
updated: 2026-03-10
---

# 🧱 Backend Architecture Hub

> Chọn đúng tài liệu, đúng thời điểm trong hành trình backend từ Level 2 đến Level 4. Mỗi mục dưới đây ghi rõ **Level gợi ý**, **đọc trước khi nào**, và **cách áp dụng thực tế**.

## 🗺️ Learning Paths & Level Tags

| Level | Mô tả | Tài liệu gợi ý |
| --- | --- | --- |
| **Level 2 – Professional API** | Chuẩn hoá service, tách layer, tối ưu performance ở mức đơn service | [high-performance.md](./high-performance.md) |
| **Level 3 – Scalable Systems** | Microservices, distributed data, cloud-native | [microservices-patterns.md](./microservices-patterns.md) · [microservices-patterns-deep-dive.md](./microservices-patterns-deep-dive.md) · [scaling-strategy.md](./scaling-strategy.md) |
| **Level 4 – Architect/SRE** | Hệ thống phân tán, thuật toán nâng cao, service mesh, design review | [distributed-systems.md](./distributed-systems.md) · [cloud-native.md](./cloud-native.md) · [advanced-algorithms.md](./advanced-algorithms.md) · [hexagonal-architecture.md](./hexagonal-architecture.md) |

**Cách sử dụng:**
1. Xác định mình đang ở level nào trong [backend-master-checklist.md](../backend-master-checklist.md).
2. Chọn bài tương ứng, đọc phần “Apply it” để thực hành ngay.
3. Link “Cross-reference” cuối mỗi file chỉ ra tài liệu hỗ trợ (DevOps, Testing, System Design…).

## 🔍 File Guide

| File | Level | Giàu nội dung gì? | Khi nào nên đọc |
| --- | --- | --- | --- |
| [high-performance.md](./high-performance.md) | L2-L3 | Concurrency, caching, load balancing, SLO | Sau khi ship API ổn định và muốn tối ưu độ trễ |
| [microservices-patterns.md](./microservices-patterns.md) | L3 | Decomposition, integration, data consistency, observability | Khi chuẩn bị tách monolith hoặc thiết kế multi-service |
| [microservices-patterns-deep-dive.md](./microservices-patterns-deep-dive.md) | L3-L4 | Circuit breaker, saga, sidecar, BFF | Khi đã hiểu microservices cơ bản và cần xử lý giao dịch phức tạp |
| [scaling-strategy.md](./scaling-strategy.md) | L2-L3 | Scale up vs scale out, cost trade-offs | Khi quyết định nâng cấu hình hay thêm node |
| [cloud-native.md](./cloud-native.md) | L3-L4 | 12-factor, serverless, service mesh, K8s patterns | Khi đưa workload lên cloud hoặc adopt GitOps/mesh |
| [distributed-systems.md](./distributed-systems.md) | L4 | CAP/PACELC, consistency, consensus, EDA | Khi thiết kế hệ thống đa region, yêu cầu HA cao |
| [hexagonal-architecture.md](./hexagonal-architecture.md) | L2-L3 | Ports & adapters, adapter layering, sample code | Khi refactor monolith để dễ test, dễ swap adapters |
| [advanced-algorithms.md](./advanced-algorithms.md) | L4 | Bloom filter, HyperLogLog, rate limiting, consistent hashing | Khi giải quyết bài toán data massive, cần tối ưu memory |

## 🧩 Recommended Progression

1. **Stabilize single service:** đọc `high-performance.md` + áp dụng caching, load balancing.
2. **Break apart systems:** đọc `microservices-patterns.md` → `microservices-patterns-deep-dive.md`.
3. **Think beyond servers:** lên cloud, nghiên cứu `cloud-native.md`, `distributed-systems.md`.
4. **Level up architecture DNA:** áp dụng `hexagonal-architecture.md`, `advanced-algorithms.md` cho solutions phức tạp.

> 📌 Tip: Sau mỗi file, thực hiện tối thiểu 1 bài tập trong phần “Apply it” để biến kiến thức thành kỹ năng thực tế.