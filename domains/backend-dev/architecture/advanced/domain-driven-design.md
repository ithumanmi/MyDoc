---
title: "Cẩm nang Domain-Driven Design (L3-L4)"
description: "DDD: Giải phẫu Bounded Context, Tactical Patterns (Aggregate, Value Object) để tránh Distributed Monolith."
tags:
  - backend
  - ddd
  - microservices
  - architecture
updated: 2026-03-18
---

# 🧠 Domain-Driven Design (DDD) - Vũ khí của kiến trúc sư

> [← Quay lại Advanced Architecture](./README.md)

Lập trình theo mô hình MVC (Model-View-Controller) là bài học vỡ lòng. Nhưng khi business logic phình to (ví dụ hàm `xuatKho()` vừa tính thuế, gửi mail, gọi API logistics), MVC dễ trở thành mô hình rối, và Database-Driven Development (code phụ thuộc SQL) làm suy yếu domain.

Eric Evans giới thiệu **Domain-Driven Design (DDD)** để giải quyết vấn đề này: code phải phản chiếu chính xác ngôn ngữ và quy tắc của business.

---

## 🗺️ 1. Thiết kế chiến lược (Strategic Design)
Vấn đề lớn nhất khiến microservice thất bại không chỉ là mạng chậm, mà là **chia tách sai**.

### A. Ubiquitous Language (Ngôn ngữ chung)
Mọi bên (CEO, Sales, BA, Dev) cần dùng cùng một thuật ngữ.
*   *Sai:* Sales gọi `Customer`, BA gọi `Client`, Dev đặt bảng `tbl_user`.
*   *Đúng (DDD):* Thống nhất một chữ: **`Buyer`** (ví dụ trong sàn thương mại điện tử). Sai tên có thể sai logic nghiệp vụ.

### B. Bounded Context (Ranh giới ngữ cảnh)
Từ "Product" có thể có nghĩa khác nhau:
1.  **Inventory Context:** Thùng nặng 5kg, size XXL, nằm ở kệ số 3.
2.  **Sales Context:** Giá 100K VND, khuyến mãi mua 2 tặng 1.

**Cách sai:** Nhồi một bảng `Product` chung cho toàn hệ thống, dễ lock và rối.
**Cách DDD:** Tách context. Inventory có database riêng, Sales có database riêng. Hai context giao tiếp qua message broker (Kafka/RabbitMQ). Monolith được tách rõ ràng.

---

## ⚔️ 2. Thiết kế chiến thuật (Tactical Design)
Tập trung vào mô hình domain, không gắn chặt vào bảng SQL.

### 🛡️ 1. Value Object (Giá trị bất biến)
Không cần ID, bất biến, tự bảo toàn tính hợp lệ.
**Ví dụ Money:**
Không cho phép `gia_san_pham = -100`. Dùng `MoneyValueObject`; nếu khởi tạo âm -> ném exception tại chỗ, trước khi chạm controller hay DB.

### 👑 2. Entity (Thực thể)
Có ID định danh, danh tính tồn tại qua thời gian dù thuộc tính thay đổi. Thao tác dựa trên ID (ví dụ: `Customer`, `Order`).

### 🏰 3. Aggregate Root (Gốc kết tập)
Nhóm các entity và value object liên quan thành một đơn vị giao dịch, bảo toàn invariants.
Ví dụ: `Order` là aggregate root, `OrderItems` thuộc `Order`.
> **Nguyên tắc:** Bên ngoài (controller) **không** thao tác trực tiếp `OrderItems` để đổi giá. Phải qua `Order.updateItemPrice(...)`. Aggregate root kiểm tra luật (chưa thanh toán mới đổi giá) rồi mới ghi DB.

### 📣 4. Domain Events (Sự kiện miền)
Sau khi nghiệp vụ hoàn tất, aggregate root phát sự kiện (vd: `OrderPaidEvent`). Ở Inventory context, listener tiêu thụ sự kiện và trừ kho. Giảm coupling giữa các service.

---

## 💻 Sample (TypeScript) minh họa domain 

```typescript
// Aggregate root kiểm soát mọi hành động.
export class Order extends AggregateRoot {
  private items: OrderItem[] = [];
  private orderStatus: OrderStatus;

  // Value Object chặn giá trị âm 
  addItem(productId: ProductId, price: MoneyValueObject, quantity: number) {
    if (this.orderStatus === OrderStatus.SHIPPED) {
       throw new Error("Không thể sửa đơn khi đã giao hàng");
    }
    this.items.push(new OrderItem(productId, price, quantity));

    // Phát domain event cho các service khác
    this.apply(new OrderItemAddedEvent(this.id, productId, quantity));
  }
}
```

---

## 🎯 Tổng kết (cho kiến trúc sư)
Quy tắc: Domain Model phải thuần, không phụ thuộc framework hay ORM. REST/gRPC, SQL/NoSQL là phần hạ tầng, không xâm nhập domain. Business là trung tâm của code.

## ✅ Checklist áp dụng
- [ ] Tổ chức Event Storming cho domain cốt lõi, vẽ context map.
- [ ] Refactor controller/service rối thành các bounded context rõ ràng.
- [ ] Xác định aggregate root và viết test bảo vệ invariants thay vì lạm dụng mock DB.
- [ ] Tạo Anti-Corruption Layer (ACL) khi tích hợp hệ thống/third party cũ để bảo vệ kiến trúc sạch.