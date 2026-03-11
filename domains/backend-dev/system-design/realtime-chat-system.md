# 💬 Real-time Chat System Design: Facebook Messenger / WhatsApp

---
title: "Real-time Chat System"
description: "Thiết kế chat app chịu tải cao với WebSocket, Redis Pub/Sub, Cassandra."
tags:
  - backend
  - realtime
  - system-design
updated: 2026-03-11
---

> [← Back to Backend Roadmap](../README.md)

Thiết kế một ứng dụng Chat là bài toán kinh điển để kiểm tra kiến thức về **Stateful Architecture**.
Khác với API thông thường (Stateless), Chat đòi hỏi kết nối liên tục và khả năng scale phức tạp hơn nhiều.

---

## 1. Thách Thức Cốt Lõi (Core Challenges) 🧩

### 1.1. HTTP vs WebSocket
*   **HTTP:** Client hỏi -> Server trả lời. Muốn nhận tin nhắn mới? Client phải hỏi liên tục (Polling) -> Tốn tài nguyên, độ trễ cao.
*   **WebSocket:** Kết nối 2 chiều bền vững (Persistent Connection). Server chủ động đẩy tin nhắn xuống Client ngay khi có. -> **Lựa chọn bắt buộc cho Chat.**

### 1.2. Stateful Scaling (Vấn đề khó nhất) 🔥
Tưởng tượng bạn có 2 server chat: Server 1 và Server 2.
*   **User A** kết nối tới **Server 1**.
*   **User B** kết nối tới **Server 2**.
*   User A gửi tin nhắn cho User B.
*   Server 1 nhận tin nhắn, nhưng nó **không biết User B đang ở đâu** (vì B đang kết nối với Server 2).

👉 **Giải pháp:** Cần một cơ chế để các Server "nói chuyện" với nhau -> **Redis Pub/Sub**.

---

## 2. Architecture Overview 🏛️

```mermaid
graph TD
    UserA[User A] <-->|WebSocket| WS1[Chat Server 1]
    UserB[User B] <-->|WebSocket| WS2[Chat Server 2]
    
    WS1 <--> Redis[(Redis Pub/Sub)]
    WS2 <--> Redis
    
    WS1 -->|Lưu tin nhắn| Queue[Message Queue (Kafka)]
    Queue --> Worker[Chat History Worker]
    Worker --> Cassandra[(Cassandra DB)]
    
    WS1 -->|Update Online| Presence[Presence Service]
    Presence --> RedisCache[(Redis Cache)]
```

### Các thành phần chính:
1.  **Chat Service (WebSocket Server):** Giữ kết nối với User. Stateful.
2.  **Redis Pub/Sub:** "Bưu điện" trung chuyển. Khi Server 1 nhận tin nhắn cho User B, nó "hét" lên kênh Pub/Sub. Server 2 nghe thấy và đẩy tin xuống cho User B.
3.  **Presence Service:** Quản lý trạng thái Online/Offline (Heartbeat).
4.  **Cassandra/ScyllaDB:** Lưu trữ lịch sử chat. (Tại sao không dùng MySQL? Xem phần Database Design).

---

## 3. Database Design: Tại sao chọn Cassandra? 🗄️

Chat Apps có đặc thù:
*   **Write-heavy:** Hàng tỷ tin nhắn mỗi ngày.
*   **Read access pattern:** Luôn đọc tin nhắn mới nhất trước (Time-series). Ít khi sửa/xóa tin nhắn cũ.
*   **MySQL/PostgreSQL:** B-Tree index không tối ưu cho write-heavy khủng khiếp như vậy. Sharding rất đau đầu.
*   **Cassandra/ScyllaDB (Wide-column NoSQL):**
    *   Write cực nhanh (Append-only).
    *   Scale ngang dễ dàng.
    *   Query theo `partition_key` (Conversation ID) và sort theo `clustering_key` (Timestamp) siêu tốc.

**Schema:**
```sql
CREATE TABLE messages (
    conversation_id UUID,
    created_at TIMESTAMP,
    message_id UUID,
    sender_id UUID,
    content TEXT,
    PRIMARY KEY (conversation_id, created_at DESC)
);
```

---

## 4. Message Flow (Luồng đi của tin nhắn) 📨

### Kịch bản: User A gửi tin cho User B

1.  **A gửi:** User A gửi msg qua WebSocket tới **Chat Server 1**.
2.  **Xử lý:** Server 1 gán `message_id`, `timestamp`.
3.  **Lưu trữ (Async):** Server 1 đẩy msg vào **Kafka**. Worker sẽ đọc từ Kafka và lưu vào **Cassandra** (để đảm bảo msg không bị mất nếu DB chậm).
4.  **Định tuyến (Routing):**
    *   Server 1 check **Redis**: "User B đang kết nối tới Server nào?"
    *   Nếu B đang ở **Server 2** -> Server 1 Publish msg vào channel của Server 2 trên Redis Pub/Sub.
5.  **Giao hàng:** **Chat Server 2** nhận được msg từ Redis -> Đẩy xuống WebSocket của User B.
6.  **Ack:** User B gửi lại tín hiệu "Đã nhận" (Delivery Receipt).

---

## 5. Tối ưu hóa nâng cao 🚀

### 5.1. Group Chat Optimization
Nếu nhóm có 1000 người:
*   **Cách ngây thơ:** Loop 1000 lần gửi 1000 tin nhắn -> Chết Server.
*   **Cách tối ưu:** Chỉ gửi 1 message vào Channel của Group. Các Server giữ kết nối với thành viên trong Group đó sẽ nhận msg và fan-out cho các thành viên local của nó.

### 5.2. Media Handling
Ảnh/Video không bao giờ đi qua WebSocket (tốn băng thông server).
1.  Client upload ảnh lên **Object Storage (S3)** qua HTTP API.
2.  Lấy được URL ảnh.
3.  Gửi tin nhắn WebSocket chứa URL đó (Text message).

### 5.3. Online/Offline Status (Heartbeat)
*   Client gửi ping mỗi 10s tới Presence Service.
*   Service lưu `last_active_time` vào Redis (TTL = 30s).
*   Nếu không nhận được ping sau 30s -> Redis key hết hạn -> Coi là Offline.

---

## 6. Bài tập thực hành (Homework) 🏠
Hãy thử dùng **Node.js (Socket.io) + Redis** để viết một ứng dụng chat đơn giản:
1.  Chạy 2 instance Node.js (cổng 3001, 3002).
2.  Dùng **Redis Adapter** của Socket.io.
3.  Mở 2 tab trình duyệt: Tab 1 kết nối cổng 3001, Tab 2 kết nối cổng 3002.
4.  Chat thử xem 2 tab có nhận được tin nhắn không? (Nếu dùng Redis đúng, nó sẽ hoạt động!).

## ✅ Checklist Audit
- [ ] Mỗi WebSocket server publish/subscribe chuẩn trên Redis channel.
- [ ] Luồng ghi lịch sử chat tách khỏi path realtime (queue → worker → DB).
- [ ] Presence service có timeout rõ ràng và metric cảnh báo khi heartbeat rớt.
- [ ] Media đi qua object storage, chỉ gửi URL qua WebSocket để giảm băng thông.
- [ ] Benchmark p95/p99 send-receive latency và log khi vượt ngưỡng.
- [ ] Script chaos gây rớt 1 Redis node để kiểm chứng failover.
