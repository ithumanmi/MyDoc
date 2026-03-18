---
title: "Domain-Driven Design Playbook (Deep Dive L3-L4)"
description: "Hướng dẫn tối thượng về DDD: Giải phẫu Bounded Contexts, Tactical Patterns (Aggregates, Value Objects) để đập tan Distributed Monolith."
tags:
  - backend
  - ddd
  - microservices
  - architecture
updated: 2026-03-18
---

# 🧠 Domain-Driven Design (DDD) - Vũ Khí Của Kiến Trúc Cấp Thần

> [← Back to Advanced Architecture](./README.md)

Lập trình theo mô hình MVC (Model-View-Controller) là bài học vỡ lòng. Nhưng khi Business Logic (Nghiệp vụ doanh nghiệp) phình to: Hàm `xuatKho()` chứa cả tính thuế, gửi mail, và gọi API Logistic... lúc này MVC hiện nguyên hình là "Một bãi rác khổng lồ", và Database-Driven Development (Code phụ thuộc SQL) đã giết chết linh hồn của Bộ Mã Lõi.

Eric Evans giới thiệu **Domain-Driven Design (DDD)** để đập tan điều đó. Code phải là tấm gương phản chiếu chính xác tiếng nói Kinh Doanh (Business).

---

## 🗺️ 1. Thiết Kế Chiến Lược (Strategic Design)
Bài toán lớn nhất của cái chết Microservice không phải mạng chậm, mà là: Chia Cắt Sai!

### A. Ubiquitous Language (Ngôn Ngữ Đồng Nhất)
Từ chức danh CEO, Nhân viên Sale, BA, đến Anh Coder đều phải gọi tên Object như nhau.
*   *Sai:* Sale gọi là `Customer`. BA gọi là `Client`. Coder lại khai báo DB là `tbl_user`. 
*   *Đúng (DDD):* Thống nhất dùng duy nhất một chữ: **`Buyer`** (VD trong sàn E-commerce). Việc đổi tên sai có thể làm sai hoàn toàn logic nghiệp vụ.

### B. Bounded Contexts (Khoanh Lãnh Thổ)
Chữ "Sản Phẩm" (`Product`) mang hai ý nghĩa Hoàn Toàn Trái Ngược:
1.  **Ở Kho (Inventory Context):** Product là cái Thùng Nặng 5kg, Size XXL, Nằm Ở Kệ Số 3.
2.  **Ở Quầy Bán (Sales Context):** Product là Giá Bán 100K VND, Khuyến mãi mua 2 tặng 1.

**Lập Trình Viên Thường:** Ráng nhét Chung Cái `Product` Mập Ú Nụ bằng 50 Cột Columns vào 1 bảng DB duy nhất cho Toàn Hệ Thống! Cập nhật gây Lock Bảng.
**Coder DDD:** Chia Nhánh Giới Tuyến! Kho Context quản lý Database Product riêng. Sales Context quản lý Database Product riêng. 2 khối này giao tiếp đồng bộ qua Message Broker (Kafka/RabbitMQ). Hệ thống Monolith bị cắt rời mạch lạc!

---

## ⚔️ 2. Thiết Kế Chiến Thuật (Tactical Design)
Đừng dán mắt vào Table SQL nữa. Hãy dán mắt vào OOP Thuần Tuý.

### 🛡️ 1. Value Object (Vật Thể Lưu Trữ Giá Trị)
Object không cần khóa ID theo dõi. Bất Biến (Immutable). Sức mạnh nằm ở sự tự Validate.
**Ví dụ Tiền (Money):**
Không định nghĩa biến `gia_san_pham = -100` (Gây Bug Nghiệp Vụ Sinh Lãi Ảo).
Ép tạo Class `MoneyValueObject`. Khởi tạo sai (Âm tiền) -> Văng Exception ngay tại Khởi Tạo Lập Trình. Giết lỗi Tức Khắc. Không để dính vào Controller hay SQL.

### 👑 2. Entity (Chủ Thể Xương Lõi Mềm)
Lớp Phân Tách Có Cột ID Định Danh. Bản sắc tồn tại qua thời gian bất kể các trường râu ria (Tên, Địa Chỉ) đổi form. Xử lý thao tác dựa vào ID. (Ví dụ: `Customer`, `Order`).

### 🏰 3. Aggregate Root (Rễ Mẹ Ôm Bầu Con)
Hành Cục Lõi Nhất của DDD: Nhóm Các Entity & Value Object Liên Quan Lại Thành 1 Giao Dịch Đáng Tin Toàn Vẹn (Transaction/Invariants).
Hoá Đơn `Order` Là Mẹ -> Item Cái Bánh Mua Có 3 Loại Là Khách Gọi `OrderItems`. 
-> **Thao Tác DDD Bắt Buộc:** Hệ thống ngoài (Controller) **KHÔNG BAO GIỜ** được móc thẳng Code đập vào Repo `OrderItems` mà sửa giá chiếc Bánh! Phải gọi thông qua Mẹ: `Order.UpdateItemPrice(Bánh, 50K)`. Rễ Mẹ sẽ kiểm tra luật lệ của Toàn Hóa Đơn (Phải Chưa Thanh Toán Mới Được Đổi Giá) rồi mới cho Xuống DB!

### 📣 4. Domain Events (Sự Kiện Vùng Miền)
Hoạt động kết thúc Trơn Tru, Aggreate Root Hét Lên "OrderThanhToanXongEvent". Ở Bounded Context Của Kho Hàng (Inventory), Một Listener Chộp Lấy Dãy Sự Kiện Đó Và Tự Rút Kho. Giảm Tính Dính Mắc (Decoupling) Xa Khỏi Vòng Ôm Viết Microservices Cứng!

---

## 💻 Sample (TypeScript) Minh Họa Lõi Vùng 

```typescript
// Lệnh Root Cấm Bypass Mọi Hành Động.
export class Order extends AggregateRoot {
  private items: OrderItem[] = [];
  private orderStatus: OrderStatus;

  // Lõi Value Object Chặn Tiền Âm 
  addItem(productId: ProductId, price: MoneyValueObject, quantity: number) {
    if (this.orderStatus === OrderStatus.SHIPPED) {
       throw new Error("Tuyệt Đối Cấm Đổi Hàng Khi Đã Lên Tàu Giao Khách!");
    }
    this.items.push(new OrderItem(productId, price, quantity));
    
    // Gầm Hét Đánh Dấu Event Vào Cuống Não Framework Gửi Đi Khắp Các Service
    this.apply(new OrderItemAddedEvent(this.id, productId, quantity));
  }
}
```

---

## 🎯 Tổng KẾT (Dành Cho Architecture):
Quy tắc Bất Môn của Kiến Trúc DDD Lớp Architecture (Software Design):
> **"Domain Model Của Tôi Phải Trắng Tinh Hoàn Hảo. Không Import Expressjs Hay Entity Framework Của DB Trong Class Lõi Này. Framework Truyền Tải (REST/gRPC) Hay Database SQL/NoSQL Là Cục Viền Hạ Tầng (Infrastructure) Khi Tôi Thích Mới Xài. Business Mới Là Vị Vua Duy Nhất Của Code Mạng Tôi Gõ Ra!"**

## ✅ Apply Checklist
- [ ] Tổ chức 1 buổi Event Storming cho domain cốt lõi, ghi lại context map trên tường cty.
- [ ] Refactor module Controller/Services Bùi Nhùi thành Bounded Context rõ.
- [ ] Xác định Aggregate Root & Test bảo vệ dòng chảy thay vì Mock DB điên cuồng.
- [ ] Tạo Anti-corruption Layer (ACL) khi tích hợp Third Party cũ để tránh Vấy Bẩn Kiến Trúc Sạch (Clean Architecture) Nhà Mình.