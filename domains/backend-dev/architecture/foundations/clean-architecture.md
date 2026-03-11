---
title: "Clean Architecture vs Hexagonal vs Layered"
description: "Level 2-3: so sánh clean architecture, hexagonal và layered pattern, cách chọn cấu trúc code phù hợp."
tags:
  - backend
  - architecture
  - clean-architecture
updated: 2026-03-11
---

# 🧼 Clean Architecture (L2-L3)

> Robert C. Martin (Uncle Bob) đề xuất “Onion/Clean Architecture” để giữ business logic độc lập với framework. Bài này so sánh Clean với Hexagonal & Layered để bạn chọn phù hợp.

## 1. Clean Architecture core
```
Entities → Use Cases → Interface Adapters → Frameworks & Drivers
```
- **Entities:** business rules cốt lõi (Aggregate, domain object).
- **Use Cases:** orchestration, ứng dụng logic (service layer).
- **Interface Adapters:** chuyển đổi dữ liệu giữa use case và framework.
- **Frameworks/Drivers:** web, database, UI, external systems.

### Nguyên tắc
- Dependency rule: code chỉ phụ thuộc vào vòng trong.
- Use case biết interface repository, nhưng repository implementation phụ thuộc use case.
- Dependency inversion + DI container giúp wiring.

### Checklist layered vs hexagonal vs clean
- [ ] Domain layer không import infrastructure/framework.
- [ ] Adapter chỉ phụ thuộc vào port (interface) từ trong ra.
- [ ] Use case không bị rò rỉ DTO/ORM entity ra ngoài; mapping nằm ở adapter.
- [ ] Controller/transport không chứa business rule.
- [ ] Test use case không cần khởi động framework.

## 2. So sánh với các pattern khác

| Pattern | Điểm mạnh | Khi dùng |
| --- | --- | --- |
| **Layered (MVC, 3-tier)** | Dễ hiểu, phù hợp CRUD app | L2 trở xuống, team nhỏ |
| **Clean Architecture** | Tách rõ domain/use case, dễ test | L2-L3, hệ thống cần sống lâu |
| **Hexagonal (Ports & Adapters)** | Mở rộng integration đa kênh, swap adapter dễ | Khi phải tích hợp nhiều adapter/tech |

**Clean vs Hexagonal**
- Clean nhấn mạnh Use Case layer (Application) làm trung tâm orchestration.
- Hexagonal nhấn mạnh Port/Adapter: mọi IO đi qua port; phù hợp khi có nhiều giao thức (REST, gRPC, queue).
- Có thể kết hợp: dùng port/adapters + application service (use case) ở lõi.

Clean ~ Hexagonal: đều bảo vệ core domain. Hexagonal nhấn mạnh ports/adapters, Clean nhấn mạnh use case layer.

## 3. Cấu trúc thư mục gợi ý
```
src/
  domain/ (Entities, Value Objects)
  application/ (Use Cases, Ports)
  infrastructure/
    repositories/
    controllers/
    gateways/
```

## 4. Checklist áp dụng
- Define boundary giữa **domain** và **application** rõ ràng.
- Repository interface ở domain/application, implementation ở infrastructure.
- Controller chỉ gọi use case, không chứa business logic.
- Use case trả DTO đơn giản, controller mapping sang HTTP response.

## ✅ Apply it
- [ ] Refactor service hiện có thành lớp Use Case (Application) + Domain Entities.
- [ ] Di chuyển repository interface vào layer trong, generate adapter ở layer ngoài.
- [ ] Viết unit test cho use case không cần touch database/framework.
- [ ] So sánh Clean vs Hexagonal cho dự án, chọn pattern phù hợp.

## 🔗 Cross-reference
- [Hexagonal Architecture](./hexagonal-architecture.md) – xem sự khác biệt chi tiết ports/adapters.
- [Backend Testing Guide](../testing-guide.md) – chiến lược test cho từng layer.
- [Modular Monolith](./modular-monolith.md) – cấu trúc clean cho hệ monolith lớn.