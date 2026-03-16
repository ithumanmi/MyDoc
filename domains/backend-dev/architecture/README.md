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
| **Level 2 – Professional API** | Chuẩn hoá service, tách layer, tối ưu performance ở mức đơn service | [foundations/high-performance.md](./foundations/high-performance.md) · [foundations/clean-architecture.md](./foundations/clean-architecture.md) |
| **Level 2.5 – Modular Foundation** | Chuẩn bị cấu trúc module rõ ràng trước khi tách microservice | [foundations/scaling-strategy.md](./foundations/scaling-strategy.md) · [foundations/hexagonal-architecture.md](./foundations/hexagonal-architecture.md) |
| **Level 3 – Scalable Systems** | Microservices, distributed data, cloud-native | [distributed/microservices-patterns.md](./distributed/microservices-patterns.md) · [distributed/microservices-patterns-deep-dive.md](./distributed/microservices-patterns-deep-dive.md) |
| **Level 3.5 – Data & SaaS Specialization** | Tập trung vào consistency, multi-tenant, event log | [distributed/event-sourcing-cqrs.md](./distributed/event-sourcing-cqrs.md) · [distributed/data-partitioning.md](./distributed/data-partitioning.md) · [multi-tenancy-patterns.md](./multi-tenancy-patterns.md) |
| **Level 4 – Architect/SRE** | Hệ thống phân tán, cloud-native đa vùng, kiến trúc nâng cao | [distributed/distributed-systems.md](./distributed/distributed-systems.md) · [cloud/cloud-native.md](./cloud/cloud-native.md) · [advanced/advanced-algorithms.md](./advanced/advanced-algorithms.md) |

**Cách sử dụng:**
1. Xác định mình đang ở level nào trong [backend-master-checklist.md](../backend-master-checklist.md).
2. Chọn bài tương ứng, đọc phần “Apply it” để thực hành ngay.
3. Link “Cross-reference” cuối mỗi file chỉ ra tài liệu hỗ trợ (DevOps, Testing, System Design…).

## 🔍 File Guide

| File | Level | Giàu nội dung gì? | Khi nào nên đọc |
| --- | --- | --- | --- |
| [foundations/high-performance.md](./foundations/high-performance.md) | L2-L3 | Concurrency, caching, pooling, profiling | Sau khi ship API ổn định và muốn tối ưu độ trễ |
| [foundations/clean-architecture.md](./foundations/clean-architecture.md) | L2-L3 | Layered vs clean vs hexagonal, dependency rule | Khi cần tổ chức lại service cho dễ test |
| [foundations/hexagonal-architecture.md](./foundations/hexagonal-architecture.md) | L2-L3 | Ports & adapters, adapter layering, sample code | Khi refactor monolith để dễ swap adapters |
| [foundations/scaling-strategy.md](./foundations/scaling-strategy.md) | L2-L3 | Scale up vs scale out, cost trade-offs | Khi quyết định nâng cấu hình hay thêm node |
| [distributed/microservices-patterns.md](./distributed/microservices-patterns.md) | L3 | Decomposition, integration, data consistency, observability | Khi chuẩn bị tách monolith hoặc thiết kế multi-service |
| [distributed/microservices-patterns-deep-dive.md](./distributed/microservices-patterns-deep-dive.md) | L3-L4 | Circuit breaker, saga, sidecar, BFF | Khi đã hiểu microservices cơ bản và cần xử lý giao dịch phức tạp |
| [distributed/distributed-systems.md](./distributed/distributed-systems.md) | L4 | CAP/PACELC, consistency, consensus, EDA | Khi thiết kế hệ thống đa region, yêu cầu HA cao |
| [distributed/event-sourcing-cqrs.md](./distributed/event-sourcing-cqrs.md) | L3-L4 | CQRS, event store, projector, replay | Khi cần audit/time-travel và tích hợp downstream |
| [distributed/data-partitioning.md](./distributed/data-partitioning.md) | L3-L4 | Sharding strategy, resharding, observability | Khi data vượt 1 node |
| [cloud/cloud-native.md](./cloud/cloud-native.md) | L3-L4 | 12-factor, serverless, service mesh, K8s patterns | Khi đưa workload lên cloud |
| [cloud/serverless-patterns.md](./cloud/serverless-patterns.md) | L3 | Event-driven FaaS patterns tách từ cloud-native |
| [cloud/multi-region.md](./cloud/multi-region.md) | L4 | Active-active, failover, control plane | Khi phục vụ khách hàng đa châu lục |
| [cloud/edge-computing.md](./cloud/edge-computing.md) | L3 | Cloudflare Workers, edge caching, geo routing | Khi tối ưu latency toàn cầu |
| [advanced/domain-driven-design.md](./advanced/domain-driven-design.md) | L3-L4 | Context map, aggregate, ACL, event storming | Khi chuẩn bị tách domain phức tạp |
| [advanced/advanced-algorithms.md](./advanced/advanced-algorithms.md) | L4 | Bloom filter, HyperLogLog, rate limiting, consistent hashing | Khi giải quyết bài toán data massive |
| [advanced/ai-infrastructure.md](./advanced/ai-infrastructure.md) | L3-L4 | Vector DB, embedding pipeline, LLM serving, RAG | Khi tích hợp AI sâu vào sản phẩm |

## 🧩 Recommended Progression

1. **Stabilize single service:** đọc `high-performance.md` + áp dụng caching, load balancing.
2. **Break apart systems:** đọc `microservices-patterns.md` → `microservices-patterns-deep-dive.md`.
3. **Think beyond servers:** lên cloud, nghiên cứu `cloud-native.md`, `distributed-systems.md`.
4. **Level up architecture DNA:** áp dụng `hexagonal-architecture.md`, `advanced-algorithms.md` cho solutions phức tạp.

> 📌 Tip: Sau mỗi file, thực hiện tối thiểu 1 bài tập trong phần “Apply it” để biến kiến thức thành kỹ năng thực tế.

## ⚠️ Common Mistakes
1. **Over-engineering quá sớm:** Tách microservice trong khi monolith còn đáp ứng, dẫn tới chi phí vận hành đội hình lớn.
2. **Bỏ qua network latency:** Một request gọi đồng bộ 10 service khiến P95/P99 tăng vọt, khó debug.
3. **Không có fallback strategy:** Circuit breaker mở nhưng thiếu kế hoạch degrade (cache, queue, default response).

## 🏢 Real-world Examples
- **Netflix:** Circuit breaker + bulkhead với Hystrix/Resilience4j giúp dịch vụ stream ổn định khi dependency lỗi.
- **Uber:** Saga orchestration điều phối quy trình ride booking (matching → billing → notification) để đảm bảo consistency.
- **Shopify:** Duy trì modular monolith, hạn chế microservices để giảm chi phí vận hành và giữ tốc độ phát triển.