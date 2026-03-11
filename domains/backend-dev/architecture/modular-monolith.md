---
title: "Modular Monolith Architecture"
description: "Level 2-3: xây dựng monolith có module rõ ràng, chuẩn bị sẵn đường tách microservices."
tags:
  - backend
  - architecture
  - modular-monolith
updated: 2026-03-11
---

# 🧩 Modular Monolith (L2-L3)

> Giải pháp trung gian giữa monolith lộn xộn và microservices phức tạp. Tổ chức code thành module độc lập, deploy chung một binary nhưng giới hạn coupling.

## 1. Đặc điểm chính
- **Module boundary rõ:** mỗi module = bounded context (Users, Billing, Catalog).
- **Internal API:** module expose service interface, các module khác gọi thông qua contract.
- **Data ownership:** mỗi module sở hữu schema của riêng nó (schema per module) ngay cả khi chia sẻ DB.
- **Build pipeline:** tách folder, namespace, test riêng → dễ migrate thành service.
- **Enforcement:** dùng static analysis / module boundary check (ArchUnit, Deptrac) để chặn import trái phép.

## 2. Cấu trúc gợi ý
```
src/
  modules/
    users/
      application/
      domain/
      infrastructure/
    billing/
    catalog/
  shared/
    kernel (event bus, auth, logging)
```

## 3. Giao tiếp giữa modules
- **Synchronous:** call thông qua service interface (dependency injection).
- **Asynchronous:** publish domain event nội bộ (in-memory/event bus) → module khác subscribe.
- **Anti-corruption layer:** khi module cần convert DTO → domain object.
- **Versioned contract:** dùng contract test (Pact) hoặc interface version để tránh breaking change khi refactor module.

## 4. Roadmap tách service
1. **Identify hot modules** (traffic cao, deploy độc lập).
2. **Tách DB schema** hoặc sử dụng schema riêng.
3. **Expose API** cho module (REST/GraphQL).
4. **Tách deploy**: packaging module thành service riêng.
5. **Strangler**: route traffic dần sang service mới; giữ fallback trong monolith cho đến khi ổn định.

## ✅ Apply it
- [ ] Review monolith hiện tại, phân nhóm code thành module theo bounded context.
- [ ] Tạo module template (application/domain/infrastructure) và migrate module đầu tiên.
- [ ] Thiết lập rule lint/CI đảm bảo module không import trực tiếp code của module khác.
- [ ] Ghi lại internal API giữa các module (interface + contract test).
- [ ] Log event nội bộ khi module giao tiếp để chuẩn bị cho tách microservice.
- [ ] Thử tách 1 module nhỏ theo mô hình “strangler” và đo lỗi/latency so với monolith.

## 🔗 Cross-reference
- [Domain-Driven Design](./domain-driven-design.md) – định nghĩa bounded context để map vào module.
- [Microservices Patterns](./microservices-patterns.md) – bước tiếp theo sau modular monolith.
- [Clean Architecture](./clean-architecture.md) – cấu trúc layer trong từng module.