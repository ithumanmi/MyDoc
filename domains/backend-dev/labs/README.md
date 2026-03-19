# 🧪 Backend Core Architecture Labs

> [← Quay lại Backend Roadmap](../README.md)

Bộ lab thực hành các chủ đề nền tảng về kiến trúc backend. Mỗi lab tập trung vào một kỹ thuật cốt lõi, kèm bài tập nhỏ để tự tay xây dựng và kiểm thử.

---

## 🛡️ Lab 1: Golang tự viết Reverse Proxy & Load Balancer Layer 7

Xây một API Gateway đơn giản bằng Go, phân tải round-robin tới nhiều service backend.

*   [Tự code load balancer HTTP bằng Go](./lab-go-api-gateway.md): Proxy round-robin tới 3 service Node.js, gắn `X-Request-ID` để trace request.

---

## ⚡ Lab 2: Rust WebSockets Chat Server hiệu năng cao

Xây chat server dùng WebSockets, tối ưu concurrency để vượt giới hạn C10K và tiết kiệm RAM.

*   [Chat server Rust với Tokio + Tungstenite](./lab-rust-websockets-chat.md): Xử lý hàng ngàn kết nối đồng thời, giữ mức RAM thấp.

---

## 🧱 Lab 3: TypeScript/NestJS với CQRS & Event Sourcing

Tách read/write, dùng event bus để đẩy dữ liệu đọc sang store riêng, tránh contention trên DB ghi.

*   [CQRS + Event Sourcing với NestJS](./lab-nestjs-cqrs-event-sourcing.md): Command ghi vào MySQL/Postgres, event phát qua RabbitMQ/Kafka, service đọc cập nhật view MongoDB.

---
> Chạy thử từng lab, theo dõi log và số liệu để hiểu tác động của kiến trúc tới hiệu năng và độ tin cậy.
