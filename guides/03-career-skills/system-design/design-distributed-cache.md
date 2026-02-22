# ⚡ Deep Dive: Design Distributed Cache (Redis Concept)

> **"Mục tiêu: Thiết kế một hệ thống lưu trữ dữ liệu tạm thời (in-memory) có khả năng mở rộng quy mô lớn, hỗ trợ đọc/ghi tốc độ cao và đảm bảo tính sẵn sàng."**

---

## 1. Clarify Requirements (Làm rõ yêu cầu)

### Functional Requirements
*   **Put(key, value):** Lưu giá trị vào cache.
*   **Get(key):** Lấy giá trị từ cache.
*   **Expiry:** Hỗ trợ TTL (Time To Live) cho từng key.

### Non-Functional Requirements
*   **Low Latency:** Tốc độ truy xuất tính bằng micro-seconds.
*   **Scalability:** Có thể mở rộng lên hàng nghìn máy chủ.
*   **High Availability:** Cache không được là điểm nghẽn gây sập hệ thống (Single point of failure).

---

## 2. High-level Design

### Components
*   **Cache Client:** Thư viện cài đặt ở phía App, chịu trách nhiệm băm (hashing) và tìm đúng node cache để đọc/ghi.
*   **Cache Nodes:** Các máy chủ lưu trữ dữ liệu trong RAM.
*   **Configuration Service (Zookeeper/Etcd):** Quản lý danh sách các node hiện có trong cluster.

---

## 3. Deep Dive: Sharding & Consistent Hashing (Trọng tâm)

Khi có 100 node cache, làm sao để biết `key "user_1"` nằm ở node nào?

### Vấn đề của Modulo Hashing (`hash(key) % n`)
*   Nếu thêm hoặc bớt 1 node (n thay đổi), hầu hết các key sẽ bị ánh xạ sai node -> **Cache Storm** (toàn bộ app phải truy cập DB gốc cùng lúc vì cache miss).

### Giải pháp: Consistent Hashing - **Bắt buộc phải trả lời**
*   Tất cả các node và các key được đặt trên một "Vòng tròn băm" (Hash Ring).
*   Mỗi key sẽ được lưu tại node gần nhất theo chiều kim đồng hồ.
*   **Virtual Nodes:** Mỗi node vật lý được ánh xạ thành nhiều node ảo trên vòng tròn để phân bổ dữ liệu đều hơn, tránh tình trạng một node bị quá tải (Hotspot).

---

## 4. Deep Dive: Eviction Policies & Expiry

RAM có hạn, khi cache đầy, ta phải xóa bớt dữ liệu cũ.

### Eviction Policies (Chính sách loại bỏ)
1.  **LRU (Least Recently Used) - Phổ biến nhất:** Xóa key đã lâu không được truy cập.
2.  **LFU (Least Frequently Used):** Xóa key có tần suất truy cập thấp nhất.
3.  **FIFO:** Xóa key vào đầu tiên.

### Expiry (Cơ chế hết hạn)
*   **Passive Expiry:** Chỉ xóa khi có request truy cập vào key đã hết hạn.
*   **Active Expiry:** Một luồng chạy ngầm (background thread) định kỳ quét và xóa các key đã hết hạn.

---

## 5. Caching Strategy & Failure Handling

### Caching Strategy
*   **Write-through:** Ghi vào cache và DB đồng thời (Đảm bảo nhất quán cao).
*   **Write-back:** Chỉ ghi vào cache, sau đó mới đồng bộ vào DB (Tốc độ ghi cực nhanh).
*   **Cache-aside:** App kiểm tra cache trước, nếu miss mới đọc DB rồi ghi vào cache.

### Replication & Failover
*   Mỗi node chính (Master) nên có các node phụ (Slaves).
*   Nếu Master chết, một Slave sẽ được bầu làm Master mới để đảm bảo hệ thống không bị gián đoạn.

---

## 6. Interview Pro-tips (Trade-offs)

1.  **Hot Key Problem:** Nếu một key quá "hot" (ví dụ: thông tin Taylor Swift), một node sẽ bị quá tải.
    *   *Giải pháp:* Tạo bản sao của key đó sang nhiều node khác nhau.
2.  **Consistency:** Cache không bao giờ đảm bảo nhất quán 100% với DB. Hãy thảo luận về **Eventual Consistency**.

---

## 📚 Bài tiếp theo
*   [Design Ride Sharing System (Uber/Grab)](./design-ride-sharing.md)
