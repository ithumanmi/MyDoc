---
title: "Large-Scale System Architecture"
description: "Khung kiến trúc tổng thể cho hệ thống lớn: từ yêu cầu, macro design, decomposition tới vận hành."
tags:
  - backend
  - system-design
  - architecture
updated: 2026-03-11
---

# 🏗️ Large-Scale System Architecture

> Bài viết dạng “archetype” để mô tả cách tiếp cận thiết kế kiến trúc cho một hệ thống lớn: từ xác định mục tiêu, decomposing domain, chọn nền tảng core cho đến vận hành và cải tiến liên tục.

## 1. Yêu cầu & Ràng buộc
- **Business Goal**: OKR, SLA trải nghiệm, khu vực triển khai.
- **Traffic Profile**: DAU/MAU, TPS, pattern theo giờ.
- **Data & Compliance**: loại dữ liệu (PII, tài chính), quy định (PCI, GDPR).
- **Constraints**: thời gian build, đội ngũ, budget, legacy cần tích hợp.

## 2. Macro Architecture Steps
1. **Context Diagram**: hệ thống tương tác với ai? (client, partner, data lake).
2. **Domain Decomposition**: phân thành bounded context: (Accounts, Inventory, Billing...).
3. **Communication Style**: sync API vs async event, final consistency.
4. **Data Strategy**: OLTP, OLAP, cache layer, storage tiering.
5. **Operational Pillars**: observability, security, deployment pipeline.

## 3. Layered Architecture (Example)
```
Clients (Web/Mobile) → Edge (CDN, WAF) → API Gateway → Domain Services → Data Stores → Analytics/ML
                                                ↓                 ↓
                                         Event Bus        Data Lake / Warehouse
```
- **Edge**: CDN, rate limiting, auth.
- **Gateway**: routing, policy, versioning.
- **Domain Services**: microservices hoặc modular monolith theo bounded context.
- **Data Stores**: polyglot persistence (SQL, NoSQL, search, cache).
- **Event Bus**: Kafka/Pulsar cho async processing, CQRS.
- **Analytics/ML**: streaming + batch pipeline.

## 4. Bounded Context & Team Topology
- Mỗi context map với 1 squad, kèm API contract rõ ràng.
- Sử dụng **API catalogue** + schema registry để quản lý interface.
- DDD pattern: Entity, Aggregate, Domain Event.

## 5. Cross-Cutting Concerns
- **Security**: IAM, secrets, zero-trust, data encryption.
- **Resilience**: circuit breaker, retry, bulkhead, graceful degradation.
- **Scalability**: auto-scaling, partitioning, caching.
- **Observability**: tracing, metrics, structured log.
- **Release**: CI/CD, canary, feature flag.

## 6. Data Strategy (Polyglot)
- **Transactional DB**: PostgreSQL/MySQL hoặc CockroachDB.
- **Cache**: Redis/Memcached cho hot path.
- **Analytical**: Data Lakehouse (S3 + Iceberg/Delta) + Warehouse (BigQuery/Snowflake).
- **Search**: Elasticsearch/OpenSearch cho text/aggregations.
- **Object Storage**: S3/GCS cho file/media.

## 7. Observability & Operations
- SLO/SLA matrix (availability, latency, error budget).
- Alerting tiêu chuẩn: latency p95, error rate, queue lag.
- Runbook & on-call rotation.
- Chaos engineering & game day.

## 8. Evolution roadmap
- Phase 0: Monolith + modular boundaries.
- Phase 1: Service decomposition theo domain sinh tải nặng.
- Phase 2: Multi-region active-active, data replication, edge compute.
- Phase 3: Autonomous teams + platform engineering.

## 9. Checklist dự án kiến trúc lớn
- [ ] Thu thập yêu cầu business + SLA rõ ràng.
- [ ] Vẽ context/bounded context diagram.
- [ ] Chọn communication style + data strategy.
- [ ] Định nghĩa cross-cutting policies (security, observability, release).
- [ ] Lập roadmap tiến hóa kiến trúc theo phase.
- [ ] Chuẩn hóa tài liệu: ADR, playbook, runbook.

## 10. Liên kết hữu ích
- [System Design Universe](./system-design-universe.md)
- [Backend System Design Playbook](./README.md)
- [Monitoring & Observability](../monitoring-observability.md)