# 🧪 Backend Core Architecture Labs

> [← Quay lại Backend Roadmap](../README.md)

Bộ lab thực hành kiến trúc backend, mỗi lab tập trung một kỹ thuật cốt lõi kèm bài tập tự xây và kiểm thử.

---

## 🛡️ Lab 1: Go Reverse Proxy & Load Balancer L7

API Gateway đơn giản bằng Go, phân tải round-robin tới nhiều backend.

*   [Load balancer HTTP bằng Go](./lab-go-api-gateway.md): Proxy round-robin 3 service Node.js, gắn `X-Request-ID` để trace.

---

## ⚡ Lab 2: Rust WebSockets Chat Server hiệu năng cao

Chat server WebSockets, tối ưu concurrency, tiết kiệm RAM.

*   [Rust + Tokio + Tungstenite](./lab-rust-websockets-chat.md): Xử lý nhiều kết nối đồng thời, RAM thấp.

---

## 🧱 Lab 3: TypeScript/NestJS CQRS & Event Sourcing

Tách read/write, dùng event bus đẩy dữ liệu đọc sang store riêng, giảm contention DB ghi.

*   [CQRS + Event Sourcing với NestJS](./lab-nestjs-cqrs-event-sourcing.md): Command ghi MySQL/Postgres, event phát RabbitMQ/Kafka, service đọc cập nhật view MongoDB.

---
> Chạy thử từng lab, theo dõi log và số liệu để hiểu tác động của kiến trúc tới hiệu năng và độ tin cậy.
