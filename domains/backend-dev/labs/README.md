# 🧪 Backend Core Architecture Labs 

> [← Back to Backend Roadmap](../README.md)

Lý Thuyết Khó Không Đóng Cũi Nổi Lập Trình Viên Đích Thực Khi Chưa Nhúng Tay Vào "Máu Tanh". Gấp Rút Giải Thoát Cơ Bản Mảnh Nhấn App CRUD Tầm Thường Ngôn Ngữ Bậc Cao Bập Bẹ!
Chào Mừng Xuống Hầm Nóng! Viết Bằng Ngôn Ngữ Core Nhấp Máy. 

---

## 🛡️ Lab 1: Golang Tự Code Reverse Proxy & Cửa Phân Tải Layer 7 (Load Balancer API Gateway)

Viết API Chạy Rỗng Trên Cổng 3000 Đợi Chặn Nhận File Của Rớt Nước.
Thay Vào Đó Go Chỉnh Bóp Request Trực Mạng Rẽ Nhánh Lừa Chấp Client Gọi. 

*   [Bài Thiết Lập Load Balancer Bằng Go Viết Tay Cưa Request HTTP](./lab-go-api-gateway.md): Phân Tải Round-Robin Chạy Vào 3 Docker Trạm NodeJs. Áp `X-Request-ID` Tracing Độc Vào Hệ Đội Nhận.

---

## ⚡ Lab 2: Rust Hệ Tốc Độ Mở Nghẽn Đồng Thời Concurrency Khắc C10K (WebSockets Chat Server Đỉnh RAM)

Máy Chạy `Socket.io` NodeJS Lên 5000 Đứa Client Cùng Connect Lên Chat Ngốn Gốc RAM 1GB Sụp Đoạn Chờ Hơi Thở Cạn. Thử Lột Xác Chuyển Trạm Dùng Khung Máy Sóc Kẽ Rớt Đứt Giấc Với Tốc Độ Vượt Máy Ảo Rừng C Tôn Lên WebSockets!

*   [Bài Trượng Rust Mỏ Chat Khỏng Tokio + Tungstenite Concurrent Scale](./lab-rust-websockets-chat.md): Xây Chuyển Giao Trạm Rớt Async Siêu Tốc Điểm Giao Cấp Chết Giữ Ngàn Mối Liên WebSockets. Bất Tận Giao Khung RAM Chưa Tới 30MB!

---

## 🧱 Lab 3: TypeScript/NestJS Phá Gỡ Kiến Trúc Lộn Xộn Event-Driven CQRS (Đọc Đi Đằng Đọc, Viết Chạy Server Viết)

Nếu Backend Đọc Viết Nhồi Chung Ném Cột Trong 1 Bảng SQL Ngắn. User Truy Viết Mua Hàng Khóa Bảng Kế Nát Rớt Request Đứa Khách Đang Tải Về Trình Quản Đơn Rỗng Read Châm.

*   [Bài Tác Nghẽn CQRS Split Tách Database Write SQL & Read MongoDB NodeJs Bằng Mảnh Hệ Event](./lab-nestjs-cqrs-event-sourcing.md): Khi Người User Lập `Command Mua Đồ Tăng` Viết Vào DB MySQL Cứng Chuẩn ACID. Hệ Thống Dắn Sự Kiện Bay Lỗ RabbitMQ Gào Chú Microservice Nhánh Giả (Luôn Chực Read) Gom Mực Đẩy View Sang Mảng MongoDB Nhanh Kinh Thần Tốc Rẻ Mạt RAM Bọt Cho Request Trình GET. System Cưa 2! Bất Sập!

---
> Gắn Máy Chạy Dev Server Và Theo Từng Lớp Lệnh Để Thở Hơi Máy Core Engineer Bộc Lộ Xây Tool Khung! Mồ Hôi Sẽ Khắc Hệ Nhớ Kỹ Arch Nhất Backend!
