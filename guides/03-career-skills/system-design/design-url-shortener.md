# 🔗 Deep Dive: Design URL Shortener (TinyURL)

> **"Mục tiêu: Thiết kế một dịch vụ nhận vào một URL dài và trả về một URL ngắn (ví dụ: bit.ly/3Sabc). Khi truy cập URL ngắn, hệ thống phải chuyển hướng người dùng về URL gốc."**

---

## 1. Clarify Requirements (Làm rõ yêu cầu)

### Functional Requirements
*   **Shortening:** Nhập URL dài -> Trả về URL ngắn.
*   **Redirection:** Click URL ngắn -> Chuyển hướng (301/302) về URL dài.
*   **Custom alias:** Người dùng có thể chọn tên mong muốn cho link (tùy chọn).
*   **Expiration:** Link có thời hạn mặc định (ví dụ 10 năm).

### Non-Functional Requirements
*   **High Availability:** Hệ thống không bao giờ được "chết".
*   **Low Latency:** Thời gian chuyển hướng phải cực nhanh (< 100ms).
*   **Scalability:** Xử lý hàng triệu request mỗi giây.

---

## 2. Back-of-the-envelope Estimation (Ước lượng)
*   **Write rate:** 100 triệu link mới/tháng.
*   **Read rate:** Tỷ lệ Read/Write là 100:1 (Read-heavy) -> 10 tỷ lượt click/tháng.
*   **Storage:** Giả sử mỗi cặp link chiếm 500 bytes -> 100 triệu * 500 = 50GB/tháng. 
    *   10 năm = 6TB. Đây là lượng dữ liệu không quá lớn, có thể quản lý được.

---

## 3. High-level Design

### API Design
1.  `POST /api/v1/shorten` (Input: long_url, Output: short_url)
2.  `GET /{short_url}` (Output: 301/302 Redirect to long_url)

### Data Model
Sử dụng **NoSQL (Key-Value)** như Cassandra hoặc DynamoDB vì chúng scale theo chiều ngang tốt và chúng ta chỉ cần query đơn giản theo Key.
*   `Table: Mapping` (Key: short_url, Value: long_url)

---

## 4. Deep Dive: Key Generation (Mấu chốt)

Làm sao để tạo ra chuỗi ký tự (ví dụ 7 ký tự) duy nhất?

### Phương án A: Hashing (MD5/SHA)
*   Hash URL dài rồi lấy 7 ký tự đầu.
*   **Vấn đề:** Dễ bị trùng (Collision). Cần phải kiểm tra trong DB xem đã tồn tại chưa -> Chậm.

### Phương án B: Key Generation Service (KGS) - **Khuyên dùng**
*   Dùng một service chuyên tạo ra các Key ngẫu nhiên từ trước và lưu vào một bảng `KeyQueue`.
*   Khi có request `shorten`, KGS chỉ việc bốc 1 Key chưa dùng và gán cho URL đó.
*   *Ưu điểm:* Không lo trùng, tốc độ cực nhanh vì không cần tính toán lúc run-time.

---

## 5. Caching & Scaling

*   **Caching:** Vì tỷ lệ đọc rất cao (100:1), dùng **Redis** để lưu các URL ngắn "hot". Dùng thuật toán **LRU (Least Recently Used)** để đẩy các link cũ ra khỏi cache.
*   **DB [Sharding](./fundamentals-scalability-consistency.md#2-replication--sharding):** Mặc dù 6TB không quá lớn, nhưng để scale hàng tỷ request, ta nên sharding theo `short_url`.
*   **Redirection:** Sử dụng mã **301 (Permanent Redirect)** để trình duyệt lưu cache, giảm tải cho server trong những lần click sau của cùng một user.

---

## 6. Interview Pro-tips (Trade-offs)

1.  **301 vs 302:** 
    *   301: Tốt cho SEO, giảm tải server (vì trình duyệt cache).
    *   302: Tốt cho Analytics (vì request luôn phải đi qua server để đếm click).
2.  **Analytics:** Dùng một Message Queue (Kafka) để đẩy dữ liệu click ra và xử lý bất đồng bộ, tránh làm chậm quá trình redirect.

---

## 📚 Bài tiếp theo
*   [Design News Feed (Twitter/X)](./design-news-feed.md)
