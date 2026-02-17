# 🗄️ Database Optimization: Indexing & Sharding Deep Dive

> [← Back to Backend Roadmap](../README.md)

Khi ứng dụng đạt 1 triệu users, **Database** thường là điểm nghẽn (bottleneck) đầu tiên.
Hướng dẫn này sẽ giúp bạn tối ưu Database từ **Query** (Indexing) đến **Architecture** (Sharding).

---

## 1. Indexing Deep Dive (Tối ưu Truy vấn) 🔍

Index giống như "Mục lục" của cuốn sách. Thay vì lật từng trang (Full Table Scan), bạn tìm trong mục lục để nhảy ngay đến trang cần thiết.

### 1.1. B-Tree Index (Cấu trúc mặc định) 🌳
Hầu hết Relational DB (MySQL, PostgreSQL) dùng B-Tree.
*   **Hoạt động:** Sắp xếp dữ liệu theo thứ tự -> Tìm kiếm nhị phân (Binary Search).
*   **Độ phức tạp:** O(log N) thay vì O(N).
*   **Lưu ý:** Index làm chậm thao tác **WRITE** (INSERT/UPDATE/DELETE) vì phải cập nhật lại cây B-Tree.

### 1.2. Composite Index (Index đa cột) 🔗
Khi bạn query nhiều điều kiện: `WHERE last_name = 'Smith' AND first_name = 'John'`.
Bạn cần tạo Index trên cả 2 cột: `CREATE INDEX idx_name ON users(last_name, first_name)`.

**⚠️ Quy tắc quan trọng: Leftmost Prefix Rule**
Thứ tự cột trong Index RẤT QUAN TRỌNG.
Nếu Index là `(A, B, C)`:
*   ✅ Query `WHERE A=1 AND B=2` -> Dùng Index.
*   ✅ Query `WHERE A=1` -> Dùng Index.
*   ❌ Query `WHERE B=2` -> **KHÔNG** dùng Index (Vì bỏ qua A).

### 1.3. Covering Index (Siêu tối ưu) ⚡
Nếu Index chứa **TẤT CẢ** các cột cần thiết trong câu `SELECT`, Database sẽ không cần truy cập vào bảng chính (Table Heap) nữa.
*   Query: `SELECT first_name FROM users WHERE last_name = 'Smith'`
*   Index: `(last_name, first_name)`
*   Kết quả: Siêu nhanh (Index Only Scan).

---

## 2. Replication (Nhân bản & Mở rộng Read) 📖

Khi lượng **READ** quá lớn (VD: Báo điện tử, Mạng xã hội), một server không chịu nổi.

### Architecture: Master-Slave
*   **Master (Leader):** Nhận tất cả **WRITE** (INSERT/UPDATE).
*   **Slaves (Followers):** Copy dữ liệu từ Master, chỉ phục vụ **READ**.

### Vấn đề: Replication Lag ⏳
Dữ liệu copy từ Master sang Slave mất một khoảng thời gian (ms đến vài giây).
*   User vừa update profile xong (Write to Master).
*   User reload trang ngay lập tức (Read from Slave).
*   -> **Vẫn thấy profile cũ!** (Eventual Consistency).

**Giải pháp:**
*   **Read your own writes:** Với dữ liệu user vừa sửa, luôn đọc từ Master.
*   Các dữ liệu khác (Feed, Comments) chấp nhận trễ 1 chút.

---

## 3. Sharding (Phân mảnh & Mở rộng Write) 🔪

Khi lượng **WRITE** quá lớn hoặc dữ liệu quá nhiều (VD: 10TB data), một server Master không chứa nổi.
Giải pháp: Chia nhỏ Database thành nhiều phần (Shards), mỗi phần nằm trên 1 server riêng.

### Các chiến lược Sharding:

#### 1. Key-based Sharding (Hash) #️⃣
Dùng hàm Hash để chia đều: `Shard_ID = hash(user_id) % Total_Shards`.
*   **Ưu:** Phân phối đều data.
*   **Nhược:** Khó thêm server mới (Resharding) vì công thức Hash thay đổi -> Phải di chuyển data.

#### 2. Range-based Sharding 🔢
Chia theo dải giá trị:
*   Shard 1: User ID 1 - 1,000,000
*   Shard 2: User ID 1,000,001 - 2,000,000
*   **Ưu:** Dễ thêm Shard mới.
*   **Nhược:** **Hotspot** (Điểm nóng). Nếu Shard 2 chứa user mới đăng ký (active nhiều), Shard 2 sẽ bị quá tải, trong khi Shard 1 ngồi chơi.

#### 3. Directory-based Sharding lookup bookshelf 📚
Dùng một bảng "Lookup Table" để lưu vị trí:
*   User A -> Shard 1
*   User B -> Shard 2
*   **Ưu:** Linh hoạt nhất.
*   **Nhược:** Lookup Table trở thành điểm thắt cổ chai (SPOF).

### Vấn đề nan giải của Sharding: 🤯
1.  **Cross-shard Join:** Không thể JOIN bảng `Orders` (Shard 1) với bảng `Users` (Shard 2). -> Phải xử lý ở Application level.
2.  **Transaction:** Không còn ACID trên toàn hệ thống. Phải dùng **2-Phase Commit (2PC)** hoặc **Saga Pattern**.

---

## 4. Common Pitfalls (Lỗi thường gặp) 🕳️

### N+1 Query Problem
*   Lỗi: Lấy danh sách 10 Users (1 query), sau đó lặp qua từng User để lấy Address (10 queries). -> Tổng: 11 queries.
*   Fix: Dùng `JOIN` hoặc `IN` (`SELECT * FROM address WHERE user_id IN (...)`).

### Deadlock
*   Transaction A: Lock bảng 1, chờ bảng 2.
*   Transaction B: Lock bảng 2, chờ bảng 1.
*   -> Cả 2 chờ nhau mãi mãi.
*   Fix: Luôn lock các resource theo một thứ tự nhất định.

---

## 5. Checklist Tối Ưu 📝
1.  [ ] Đã đánh Index cho các cột trong `WHERE`, `JOIN`, `ORDER BY` chưa?
2.  [ ] Có query nào dùng `SELECT *` không cần thiết không?
3.  [ ] Slow Query Log có báo query nào chạy quá 1s không?
4.  [ ] Cân nhắc Caching (Redis) trước khi nghĩ đến Sharding.
