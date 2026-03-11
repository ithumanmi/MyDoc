---
title: "Multi-Tenancy Architecture Patterns"
description: "Level 3-4: chiến lược multi-tenant cho SaaS (shared db, schema per tenant, isolation, billing)."
tags:
  - backend
  - architecture
  - saas
updated: 2026-03-11
---

# 🏢 Multi-Tenancy Patterns (L3-L4)

> Xây SaaS phục vụ nhiều khách hàng (tenant) nhưng vẫn đảm bảo isolation, cost efficiency và compliance. Lựa chọn phụ thuộc vào security, quy mô, và khả năng tùy biến.

## 1. Kiến trúc multi-tenant phổ biến

| Pattern | Mô tả | Khi dùng |
| --- | --- | --- |
| **Shared Everything** | Cùng database/table, phân biệt bằng `tenant_id` | Tier thấp, nhiều tenant nhỏ |
| **Shared DB, Schema per Tenant** | Chung instance DB nhưng schema riêng | Cân bằng giữa isolation và cost |
| **Database per Tenant** | Mỗi tenant DB riêng, có thể multi-VM | Tenant enterprise, yêu cầu compliance |

### Routing & provisioning
- **Tenant resolver:** từ domain/header/token → tenant context; lưu tại middleware.
- **Routing DB/cache:** dựa trên tenant context, chọn pool/connection đúng.
- **Provisioning workflow:** idempotent; tạo schema/DB + user + seed data + quota.
- **On-call safety:** flag đóng tenant tạm thời nếu vượt quota hoặc bị xâm nhập.

## 2. Tenant Isolation Checklist
- **Auth**: JWT chứa tenant context, middleware kiểm tra quyền.
- **Row-level security**: enforce `tenant_id` ở DB layer.
- **Rate limiting per tenant**: tránh tenant xấu ảnh hưởng toàn hệ thống.
- **Resource quota**: CPU/memory/queue limit tùy mức gói dịch vụ.
- **Secret isolation:** mỗi tenant có key riêng nếu cần mã hóa dữ liệu at-rest.
- **Noise isolation:** cách ly queue/topic hoặc prefix theo tenant để giảm noisy neighbor.

## 3. Data lifecycle per tenant
- **Provisioning**: automation tạo schema/DB/video bucket.
- **Backup & Restore**: backup theo tenant, hỗ trợ export hợp đồng.
- **Deletion (GDPR)**: xóa dữ liệu tenant, audit log.
- **Migration/plan change**: nâng/downgrade gói, có bước migrate schema/quota an toàn.

## 4. Customization model
- **Configurable feature flags**: enable/disable module theo tenant.
- **Extension point**: webhooks, workflow engine cho khách hàng lớn.
- **Branding**: custom domain, theme.
- **Data overrides:** cho phép một số field override theo tenant (pricing rules) nhưng giới hạn phạm vi để tránh fork code.

## 5. Monitoring/Billing
- Metrics theo tenant: request count, storage usage.
- Cost allocation: gắn tag tenant vào resource cloud.
- Billing pipeline: thu phí theo usage hoặc seat.
- Alert per tenant: error rate, latency, quota breach.
- Audit log: hành động quản trị và truy cập dữ liệu theo tenant.

## ✅ Apply it
- [ ] Chọn mô hình storage phù hợp (shared schema vs schema per tenant) dựa trên số tenant & compliance.
- [ ] Thêm middleware enforce tenant context ở mọi layer (API, DB, cache).
- [ ] Thiết kế job provisioning tự động tạo tenant mới (schema + config).
- [ ] Thiết lập dashboard usage/billing per tenant.
- [ ] Viết runbook backup/restore cho từng tenant quan trọng.

## 🔗 Cross-reference
- [Scaling Strategy](./scaling-strategy.md) – cân nhắc cost vs isolation khi scale multi-tenant.
- [Security Guide](../security/backend-security.md) – bảo vệ dữ liệu tenant, row-level security.
- [Data Partitioning](./data-partitioning.md) – chiến thuật shard theo tenant.
- [Monitoring & Observability](../monitoring-observability.md) – metric breakdown per tenant.