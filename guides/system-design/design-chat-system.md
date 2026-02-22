# 💬 Deep Dive: Design Chat System (WhatsApp/Messenger)

> **"Mục tiêu: Thiết kế một hệ thống tin nhắn tức thời (Instant Messaging) hỗ trợ trò chuyện 1-1, trò chuyện nhóm và trạng thái online/offline."**

---

## 1. Clarify Requirements (Làm rõ yêu cầu)

### Functional Requirements
*   **1-on-1 Chat:** Gửi và nhận tin nhắn giữa hai người dùng.
*   **Group Chat:** Trò chuyện nhóm (tối đa ví dụ 500 người).
*   **Presence:** Trạng thái online/offline và "last seen".
*   **Delivery Status:** Đã gửi (sent), đã nhận (delivered), đã đọc (read).
*   **Media Support:** Hỗ trợ ảnh, video, tệp tin (ngoài phạm vi cơ bản nhưng cần lưu ý).

### Non-Functional Requirements
*   **Low Latency:** Tin nhắn phải được chuyển đi gần như tức thì.
*   **Reliability:** Không được mất tin nhắn.
*   **Message Ordering:** Tin nhắn phải hiển thị đúng thứ tự thời gian.
*   **Scalability:** Hỗ trợ hàng tỷ user và hàng tỷ tin nhắn mỗi ngày.

---

## 2. High-level Design

### Giao thức kết nối (Protocols)
Đây là câu hỏi phỏng vấn cực kỳ phổ biến: **HTTP vs WebSocket.**
*   **HTTP:** Phù hợp cho việc gửi tin nhắn (Client -> Server), nhưng không tốt cho việc nhận tin nhắn (Server -> Client) vì Server không thể chủ động đẩy dữ liệu. Polling hoặc Long-polling đều tốn tài nguyên.
*   **WebSocket:** Kết nối 2 chiều (Bidirectional) và duy trì (Persistent). Phù hợp nhất cho Chat vì giảm thiểu overhead của HTTP header và cho phép Real-time.

### Components
*   **Chat Service:** Quản lý việc gửi/nhận tin nhắn qua WebSocket.
*   **Presence Service:** Quản lý trạng thái online/offline.
*   **KV Store (NoSQL):** Lưu trữ lịch sử tin nhắn (Message History).
*   **Push Notification:** Gửi thông báo khi người dùng offline.

---

## 3. Deep Dive: Message Storage (Trọng tâm)

Chọn Database nào cho Chat? 
Hệ thống chat có đặc thù là **Write-heavy** và truy vấn theo thời gian.

### Tại sao NoSQL (LSM Tree) là lựa chọn tối ưu?
*   **RDBMS (SQL):** Chậm khi số lượng bản ghi lên tới hàng tỷ. Index theo `timestamp` sẽ bị quá tải khi Write rate cao.
*   **Cassandra / HBase:** Sử dụng cấu trúc LSM Tree, cho phép tốc độ ghi cực nhanh. Dữ liệu được sắp xếp sẵn theo thời gian trên đĩa cứng, giúp truy vấn các tin nhắn gần nhất rất hiệu quả.

**Data Schema:**
*   `Table: messages`
    *   `message_id` (Primary Key)
    *   `chat_id` (Partition Key - nhóm các tin nhắn trong cùng 1 hội thoại vào 1 node)
    *   `timestamp` (Clustering Key - sắp xếp tin nhắn theo thời gian)
    *   `content`, `sender_id`

---

## 4. Deep Dive: Group Chat & Presence

### Group Chat (Fan-out)
*   Khi A gửi tin nhắn vào nhóm có 100 người, hệ thống phải copy tin nhắn đó vào "Message Sync Queue" của 100 người đó.
*   Với nhóm quá lớn (ví dụ Telegram 200k người), ta không thể dùng Push model cho tất cả. Ta chỉ lưu 1 bản duy nhất của tin nhắn và mỗi user sẽ Pull về khi mở app.

### Presence Service (Trạng thái Online)
*   Làm sao biết user online? Duy trì một kết nối WebSocket là dấu hiệu tốt nhất.
*   **Heartbeat mechanism:** Client gửi một tín hiệu nhỏ (heartbeat) sau mỗi 5-10 giây. Nếu Server không nhận được sau 30 giây -> Đánh dấu offline.
*   *Optimization:* Chỉ cập nhật trạng thái online cho bạn bè khi người dùng thực sự mở app (để tiết kiệm tài nguyên).

---

## 5. Message ID Generation
Trong hệ thống phân tán, không thể dùng `AUTO_INCREMENT` của SQL.
*   **Snowflake (Twitter):** Tạo ID 64-bit dựa trên timestamp + worker_id + sequence.
*   ID phải duy nhất và có tính sắp xếp theo thời gian (Sortable).

---

## 6. Interview Pro-tips (Trade-offs)

1.  **Consistency vs Availability:** Trong Chat, tính khả dụng quan trọng hơn. Nếu DB chính chết, ta có thể ghi tạm vào một DB khác rồi sync sau. Người dùng thà nhận tin nhắn chậm vài giây còn hơn là không gửi được.
2.  **End-to-End Encryption (E2EE):** Nếu được hỏi về bảo mật (như WhatsApp), hãy giải thích rằng Server chỉ đóng vai trò trung chuyển các gói tin đã mã hóa. Chỉ người nhận mới có Key để giải mã.

---

## 📚 Bài tiếp theo
*   [Design Video Streaming Platform (YouTube)](./design-video-streaming.md)
