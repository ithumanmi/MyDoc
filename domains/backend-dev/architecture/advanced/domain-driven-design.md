---
title: "Domain-Driven Design Playbook"
description: "Hướng dẫn Level 3-4 về DDD: bounded context, aggregate, ubiquitous language, strategic/tactical patterns."
tags:
  - backend
  - architecture
  - ddd
updated: 2026-03-11
---

# 🧭 Domain-Driven Design (L3-L4)

> Dành cho đội ngũ đang chuyển từ “code theo function” sang “code theo domain”. DDD giúp ăn khớp giữa business và kỹ thuật, đặc biệt trước khi tách microservices.

## 1. Strategic Design
- **Ubiquitous Language:** từ điển chung giữa dev/product. Tạo wiki cho terms (Order, Invoice, Shipment).
- **Bounded Context:** phạm vi logic có schema & API riêng. Tránh domain model “God object”. Luôn kèm **owner team** và **deployment boundary**.
- **Context Map:** mô tả quan hệ giữa context: Partnership, Customer-Supplier, Anti-corruption Layer, Open Host Service, Published Language.
- **Event Storming:** workshop dán note event/command để tìm aggregate và flow nhanh chóng.

### Context Map ví dụ
```
[Sales Context] --Customer-Supplier--> [Billing Context]
       ^                                |
       | Partnership                     | Conformist
       +---------------------------------+

[Catalog] --Published Language--> [Search]
[Legacy ERP] --ACL--> [Billing]
```

## 2. Tactical Patterns
- **Entity/Aggregate:** Aggregate root kiểm soát invariants, expose behavior thay vì setters.
- **Value Object:** immutable, equality by values (Money, Address).
- **Domain Service:** logic không thuộc entity nào.
- **Repository:** contract truy xuất aggregate, hạ tầng implement.
- **Domain Event:** publish khi aggregate thay đổi trạng thái quan trọng.

### Sample (TypeScript)
```typescript
class Order extends AggregateRoot {
  private items: OrderItem[] = [];

  addItem(productId: string, quantity: number) {
    if (quantity <= 0) throw new Error("invalid");
    this.items.push(new OrderItem(productId, quantity));
    this.raise(new OrderItemAdded(this.id, productId, quantity));
  }
}
```

### Aggregate design checklist
- [ ] Mọi bất biến (invariant) nằm trong aggregate root; không phụ thuộc transaction bên ngoài.
- [ ] Aggregate đủ nhỏ để load + validate trong 1 request; tránh “mega aggregate”.
- [ ] Mọi command đi qua method của aggregate; không bypass bằng repository trực tiếp.
- [ ] Event phát ra từ aggregate có đầy đủ metadata (tenant, correlation).

## 3. Anti-Corruption Layer (ACL)
- Khi context A gọi B nhưng không muốn “đảo lộn” domain A.
- ACL translates DTO ↔ domain terms, mapping enum/value object.
- Giúp microservices dùng chung service nhưng không phụ thuộc schema của nhau.

## 4. Cách tiến hành DDD
1. **Domain discovery:** workshop với business → event storming.
2. **Context mapping:** xác định boundary, contract giữa team.
3. **Model refinement:** code aggregate, value object, service.
4. **Align deployment:** mỗi bounded context có repo/service riêng (monolith module hoặc microservice).

## ❗ Pitfalls
- Over-engineering cho domain đơn giản → keep it simple.
- Bounded context không đúng team structure → tạo bottleneck.
- Không cập nhật ubiquitous language → domain drift.

## ✅ Apply it
- [ ] Tổ chức 1 buổi event storming cho domain cốt lõi, ghi lại context map.
- [ ] Refactor module quan trọng thành bounded context rõ (namespace + folder structure).
- [ ] Xác định aggregate root & bất biến, viết test đảm bảo invariants.
- [ ] Tạo Anti-corruption Layer khi tích hợp legacy/3rd party để tránh rò rỉ schema.
- [ ] Review ubiquitous language mỗi quý với team product.

## 🔗 Cross-reference
- [Modular Monolith](./modular-monolith.md) – cách map bounded context vào monolith.
- [Hexagonal Architecture](./hexagonal-architecture.md) – tách core domain khỏi adapters.
- [Microservices Patterns](./microservices-patterns.md) – decomposition dựa trên context map.
- [Event Sourcing](./event-sourcing.md) – khi aggregate cần emit domain event.