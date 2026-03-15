# 🐦 Deep Dive: Design News Feed (Twitter/X)

> **"Mục tiêu: Thiết kế một hệ thống hiển thị dòng thời gian (timeline) của các bài đăng từ những người mà một người dùng đang theo dõi."**

---

## 1. Clarify Requirements (Làm rõ yêu cầu)

### Functional Requirements
*   **Posting:** Người dùng có thể đăng tweet (text, image, video).
*   **News Feed:** Hiển thị danh sách tweet từ những người đang follow theo thứ tự thời gian hoặc thuật toán.
*   **Following:** Theo dõi người dùng khác.

### Non-Functional Requirements
*   **Fast Feed Generation:** Tốc độ tải feed phải cực nhanh (< 200ms).
*   **Consistency:** Chấp nhận "[Eventual Consistency](./fundamentals-scalability-consistency.md#cap-theorem--consistency-spectrum)" (bạn đăng tweet, người khác có thể thấy chậm vài giây).
*   **High Availability:** Hệ thống phải luôn sẵn sàng phục vụ hàng triệu user đồng thời.

---

## 2. Back-of-the-envelope Estimation (Ước lượng)
*   **Users:** 300 triệu DAU (Daily Active Users).
*   **Read rate:** Giả sử mỗi user check feed 5 lần/ngày -> 1.5 tỷ lượt xem feed/ngày.
*   **Write rate:** Giả sử 10% user đăng tweet mỗi ngày -> 30 triệu tweet/ngày.
*   **Thách thức:** Hệ thống cực kỳ **Read-heavy**. Tỷ lệ Read/Write xấp xỉ 50:1.

---

## 3. High-level Design

### API Design
1.  `POST /api/v1/tweets` (Input: text, media_ids, Output: tweet_id)
2.  `GET /api/v1/feed` (Input: user_id, pagination_id, Output: list of tweets)

### Components
*   **Web Servers:** Xử lý request, authentication.
*   **Fan-out Service:** Đẩy tweet mới vào feed của các người theo dõi.
*   **News Feed Cache:** Lưu trữ feed đã được tính toán sẵn cho từng user để truy cập nhanh.

---

## 4. Deep Dive: Fan-out Strategy (Trọng tâm)

Đây là phần quan trọng nhất trong bài phỏng vấn. Có 2 cách để tạo feed:

### Phương án A: Pull Model (Fan-out on load)
*   Khi user mở app, hệ thống mới đi tìm tất cả người họ follow, lấy các tweet mới nhất và sắp xếp.
*   **Ưu điểm:** Tiết kiệm tài nguyên ghi (Write). Tweet mới đăng chỉ cần lưu vào 1 chỗ.
*   **Nhược điểm:** Tải feed cực chậm nếu user follow hàng nghìn người.

### Phương án B: Push Model (Fan-out on write) - **Khuyên dùng**
*   Khi user đăng tweet, hệ thống tự động đẩy tweet đó vào "News Feed Cache" của tất cả người đang follow.
*   **Ưu điểm:** Tải feed cực nhanh (chỉ cần đọc từ cache).
*   **Nhược điểm:** Tốn tài nguyên ghi. Nếu một người có 50 triệu followers (như Taylor Swift), một tweet đăng lên sẽ kích hoạt 50 triệu lượt ghi vào cache -> **Hot key/Celebrity Problem**.

### Phương án C: Hybrid Model (Kết hợp)
*   **User bình thường:** Dùng Push model (Fan-out on write).
*   **KOL/Celebrities (Nhiều followers):** Dùng Pull model. Followers của họ sẽ chủ động "kéo" tweet về khi load feed.

---

## 5. Caching & Scaling

*   **News Feed Cache:** Chỉ lưu `tweet_id` và `user_id` trong một danh sách liên kết (Linked List) hoặc Sorted Set của Redis. Không lưu nội dung tweet hoàn chỉnh để tiết kiệm bộ nhớ.
*   **Social Graph Service:** Một DB chuyên biệt (Graph DB như Neo4j hoặc In-memory DB) để quản lý quan hệ follow/following.
*   **Media Storage:** Dùng S3 cho ảnh/video và CDN để phân phối đến các vùng địa lý khác nhau.

---

## 6. Interview Pro-tips (Trade-offs)

1.  **Ranking Algorithm:** Ở mức cơ bản dùng thời gian (Recency), ở mức Senior nên đề cập đến các trọng số tương tác (like, reply, share) và machine learning model.
2.  **Pagination:** Luôn sử dụng **Cursor-based pagination** thay vì Offset-based để tránh bỏ sót bài đăng hoặc trùng lặp khi có tweet mới chèn vào giữa.

---

## 📚 Bài tiếp theo
*   [Design Chat System (WhatsApp/Messenger)](./design-chat-system.md)
