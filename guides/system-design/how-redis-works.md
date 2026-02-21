# ⚡ How Redis Works: Giải Mã Kiến Trúc In-Memory Siêu Tốc

> **"Redis không chỉ là Key-Value Store, nó là một Swiss Army Knife (Dao đa năng) cho Backend Engineer."**

Redis (Remote Dictionary Server) là cơ sở dữ liệu In-Memory mã nguồn mở, nổi tiếng với tốc độ phản hồi cực nhanh (sub-millisecond). Nhưng điều gì khiến nó nhanh đến vậy?

Dưới đây là 8 nguyên lý cốt lõi trong kiến trúc của Redis.

---

## 1. In-Memory Storage (Lưu trữ trên RAM)
Khác với Database truyền thống (MySQL, Postgres) lưu dữ liệu trên ổ cứng (HDD/SSD), Redis lưu toàn bộ dữ liệu trên **RAM (Random Access Memory)**.

*   **Tốc độ:** Truy cập bộ nhớ nhanh hơn hàng nghìn lần so với truy cập ổ đĩa.
*   **Hiệu năng:** Độ trễ (Latency) thường nhỏ hơn 1ms.
*   **Ứng dụng:** Caching, Session Management, Real-time Analytics.

---

## 2. Single-Threaded (Đơn luồng)
Redis sử dụng kiến trúc **Single-Threaded** để xử lý các lệnh (Command).

*   **Cơ chế:** Một luồng (Thread) duy nhất xử lý tuần tự từng lệnh một.
*   **Lợi ích:**
    *   Loại bỏ chi phí chuyển đổi ngữ cảnh (Context Switching) của CPU.
    *   Không cần cơ chế khóa (Locking) phức tạp để tránh Race Condition.
    *   Đơn giản hóa kiến trúc phần mềm.
*   **Lưu ý:** Vì đơn luồng, các lệnh nặng (như `KEYS *` trên tập dữ liệu lớn) có thể chặn (block) toàn bộ server. Hãy cẩn thận!

---

## 3. I/O Multiplexing (Đa luồng nhập xuất)
Dù xử lý lệnh đơn luồng, Redis vẫn có thể xử lý hàng ngàn kết nối đồng thời nhờ **I/O Multiplexing**.

*   **Công nghệ:** Sử dụng `epoll` (Linux) hoặc `kqueue` (BSD/macOS) để theo dõi nhiều socket cùng lúc.
*   **Hoạt động:** Khi có dữ liệu đến từ client, kernel báo cho Redis biết. Redis chỉ việc xử lý dữ liệu đó mà không cần tạo thread mới cho mỗi kết nối.
*   **Hiệu quả:** Xử lý hàng chục ngàn kết nối với tài nguyên hệ thống tối thiểu.

---

## 4. Specialized Data Structures (Cấu trúc dữ liệu chuyên biệt)
Redis không chỉ lưu chuỗi (String). Nó hỗ trợ các cấu trúc dữ liệu tối ưu cho từng trường hợp sử dụng:

*   **String:** Caching cơ bản, Counter.
*   **Hash:** Lưu object (User profile).
*   **List:** Message Queue, Timeline.
*   **Set:** Lưu danh sách unique (Tags, Friends).
*   **Sorted Set (ZSet):** Leaderboard, Ranking (Game).
*   **Bitmap / HyperLogLog:** Đếm số lượng lớn với bộ nhớ cực thấp.

---

## 5. Pipelining (Đường ống)
Kỹ thuật giúp tăng thông lượng (Throughput) bằng cách giảm thời gian chờ mạng (RTT - Round Trip Time).

*   **Vấn đề:** Gửi 1 lệnh -> Chờ server trả lời -> Gửi lệnh tiếp theo (Tốn nhiều RTT).
*   **Giải pháp:** Client gửi một loạt lệnh cùng lúc mà không cần chờ phản hồi từng cái. Server xử lý và trả về một loạt kết quả.
*   **Ví dụ:** Thay vì `SET A 1`, chờ, `SET B 2`, chờ... -> Gửi gói tin chứa cả `SET A 1` và `SET B 2` đi một lần.

---

## 6. Persistence (Bền vững hóa dữ liệu)
Dù chạy trên RAM, Redis vẫn có thể lưu dữ liệu xuống ổ cứng để phục hồi khi restart.

1.  **RDB (Redis Database Snapshot):** Chụp ảnh (Snapshot) toàn bộ dữ liệu theo chu kỳ (ví dụ: mỗi 5 phút).
    *   *Ưu điểm:* Gọn nhẹ, restore nhanh.
    *   *Nhược điểm:* Mất dữ liệu giữa các lần chụp.
2.  **AOF (Append Only File):** Ghi log mọi lệnh thay đổi dữ liệu (Write operation) vào file.
    *   *Ưu điểm:* Bền vững hơn, ít mất dữ liệu (thường chỉ 1s).
    *   *Nhược điểm:* File log lớn, restore chậm hơn RDB.

---

## 7. Replication (Sao chép)
Mô hình **Master-Slave (Replica)** để tăng khả năng đọc và dự phòng.

*   **Master:** Nhận lệnh Ghi (Write) và Đọc (Read).
*   **Replica:** Sao chép dữ liệu từ Master (Async), chỉ phục vụ lệnh Đọc (Read Only).
*   **Lợi ích:**
    *   **Scale Read:** Tăng khả năng phục vụ đọc bằng cách thêm Replica.
    *   **High Availability:** Nếu Master chết, có thể thăng cấp Replica lên làm Master mới.

---

## 8. Clustering (Phân cụm)
Kỹ thuật **Sharding** để mở rộng khả năng lưu trữ và xử lý khi dữ liệu lớn hơn RAM của một máy.

*   **Cơ chế:** Chia dữ liệu thành 16384 **Hash Slots**.
*   **Phân tán:** Mỗi Node trong cụm giữ một phần các Slot này.
*   **Định tuyến:** Khi Client gửi key `user:42`, Redis tính toán hash `CRC16(user:42)` để biết key này thuộc Node nào và chuyển hướng request đến đúng nơi.
*   **Kết quả:** Cho phép Redis mở rộng ngang (Horizontal Scaling) lên tới hàng trăm Node.

---

> *Nguồn hình ảnh và concept: AlgoMaster.io*
