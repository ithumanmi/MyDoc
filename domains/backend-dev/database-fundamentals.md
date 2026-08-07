# 🗄️ Database Deep Dive: The Core of Backend Engineering

> [← Back to Backend Roadmap](./README.md) | [Home](../../README.md)

<!-- agent-summary -->
**Agent SUMMARY** (read this first; jump to `##` needed):
- Senior DB fundamentals: right tool SQL vs NoSQL, query optimization, transactions/isolation, normalization, pooling, schema examples, action plan.
- Prefer this for “how databases work for backend”; glossary ACID terms may also appear in `GLOSSARY.md`.
<!-- /agent-summary -->

Hướng dẫn chuyên sâu về Database - kỹ năng quan trọng nhất (chiếm 50% công việc) của một Senior Backend Engineer. Không chỉ là viết SQL, mà là thiết kế schema, tối ưu queries, và đảm bảo data consistency ở scale lớn.

---

## 📋 Mục lục

1. [Relational vs NoSQL](#1-relational-vs-nosql-cuộc-chiến-không-hồi-kết)
2. [Query Optimization](#2-query-optimization-nghệ-thuật-tối-ưu)
3. [Transactions & Isolation Levels](#3-transactions--isolation-levels-đảm-bảo-tính-toàn-vẹn)
4. [Database Normalization](#4-database-normalization-thiết-kế-schema-chuẩn)
5. [Connection Pooling](#5-connection-pooling-quản-lý-tài-nguyên)
6. [Practical Examples](#6-practical-examples-schema-design-thực-chiến)
7. [Action Plan](#7-action-plan-lộ-trình-luyện-tập)

---

## 1. Relational vs NoSQL: Cuộc chiến không hồi kết

Sai lầm phổ biến: "NoSQL nhanh hơn SQL" hoặc "SQL đã lỗi thời". Thực tế: **Right tool for the right job**.

### 1.1. So sánh PostgreSQL (RDBMS) vs MongoDB (NoSQL)

| Tiêu chí | PostgreSQL (Relational) | MongoDB (Document Store) |
| :--- | :--- | :--- |
| **Data Structure** | Structured (Tables, Rows, Columns) | Semi-structured (JSON/BSON documents) |
| **Schema** | Rigid (Phải define trước) | Flexible (Schema-less) |
| **Relations** | JOINs (Mạnh mẽ, chuẩn hóa) | Embedded hoặc Manual Reference (Yếu) |
| **Transactions** | ACID (Atomicity, Consistency, Isolation, Durability) | ACID (Từ v4.0, nhưng performance hit) |
| **Consistency** | Strong Consistency | Eventual Consistency (thường gặp trong distributed setup) |
| **Scaling** | Vertical (Tăng RAM/CPU) dễ hơn, Horizontal khó | Horizontal (Sharding) dễ dàng |
| **Best Use Case** | Financial, ERP, E-commerce (cần data integrity) | Logs, Analytics, User Profiles, Content Management |

### 1.2. ACID vs BASE

**ACID (RDBMS - Ưu tiên an toàn dữ liệu):**
- **Atomicity:** Giao dịch thành công trọn vẹn hoặc thất bại hoàn toàn.
- **Consistency:** Dữ liệu luôn hợp lệ theo constraints.
- **Isolation:** Các giao dịch song song không ảnh hưởng lẫn nhau.
- **Durability:** Commit xong là lưu vĩnh viễn (kể cả mất điện).

**BASE (NoSQL - Ưu tiên tốc độ & scale):**
- **Basically Available:** Hệ thống luôn phản hồi (có thể lỗi data).
- **Soft state:** State có thể thay đổi theo thời gian (dù không có input mới).
- **Eventual consistency:** Data sẽ đồng bộ sau một khoảng thời gian.

### 1.3. Decision Tree: Khi nào dùng gì?

1.  **Dữ liệu có cấu trúc phức tạp, quan hệ chặt chẽ?** (VD: Orders có OrderItems, User, Payment) → **PostgreSQL**.
2.  **Cần transaction tuyệt đối an toàn?** (VD: Chuyển tiền ngân hàng) → **PostgreSQL**.
3.  **Dữ liệu dạng document, thay đổi schema liên tục?** (VD: Product catalog với attributes khác nhau) → **MongoDB**.
4.  **Cần write speed cực cao, chấp nhận mất mát nhỏ?** (VD: Sensor data, Logs) → **MongoDB/Cassandra**.
5.  **Cần graph relationships?** (VD: Social network friends recommendation) → **Neo4j** (Graph DB).

---

## 2. Query Optimization: Nghệ thuật tối ưu

Sự khác biệt giữa Junior và Senior là query chạy trong 10ms hay 10s.

### 2.1. EXPLAIN ANALYZE

Câu lệnh quan trọng nhất để debug performance. Nó cho biết Database *thực sự* làm gì.

```sql
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'test@example.com';
```

**Key terms cần chú ý:**
- **Seq Scan (Sequential Scan):** Quét toàn bộ bảng. 🚨 *Báo động đỏ nếu bảng lớn.*
- **Index Scan:** Dùng index để tìm. ✅ *Tốt.*
- **Index Only Scan:** Chỉ đọc index, không cần đọc bảng chính. 🚀 *Rất nhanh.*
- **Bitmap Heap Scan:** Kết hợp nhiều index.

### 2.2. Index Types (PostgreSQL)

Không phải cứ đánh Index là nhanh. Phải chọn đúng loại.

1.  **B-Tree (Default):**
    - Tốt cho: `=`, `>`, `<`, `>=`, `<=`, `BETWEEN`, `IN`.
    - Use case: ID, Email, CreatedAt, Status.
2.  **Hash:**
    - Chỉ tốt cho: `=` (Equality). Nhanh hơn B-Tree chút xíu nhưng hạn chế.
    - Use case: Session ID lookup.
3.  **GIN (Generalized Inverted Index):**
    - Tốt cho: Full-text search, Array, JSONB.
    - Use case: Tìm kiếm trong JSON document hoặc tags array.
4.  **GiST (Generalized Search Tree):**
    - Tốt cho: Geometric data (Location), Range types.
    - Use case: Tìm quán ăn gần đây (PostGIS).

### 2.3. N+1 Query Problem

Vấn đề hiệu năng phổ biến nhất khi dùng ORM (Prisma, Entity Framework, TypeORM).

**Kịch bản:** Lấy danh sách 10 Users và Posts mới nhất của họ.

**Bad Code (N+1 Queries):**
```javascript
// 1 Query lấy users
const users = await prisma.user.findMany({ take: 10 });

// 10 Queries lấy posts cho từng user (Loop)
for (const user of users) {
  user.posts = await prisma.post.findMany({ where: { userId: user.id } });
}
// Tổng: 1 + 10 = 11 queries. Nếu 1000 users → 1001 queries (Chết DB).
```

**Solution 1: Eager Loading (SQL JOIN / ORM Include):**
```javascript
// Prisma
const users = await prisma.user.findMany({
  take: 10,
  include: { posts: true } // 1 Query duy nhất dùng JOIN
});
```

**Solution 2: Data Loader (Cho GraphQL/Complex logic):**
- Gom ID của 10 users lại (`[1, 2, ..., 10]`).
- Query 1 lần: `SELECT * FROM posts WHERE user_id IN (1, 2, ..., 10)`.
- Map posts về lại user tương ứng.

### 2.4. Query Rewriting Techniques

-   **Tránh `SELECT *`:** Chỉ lấy cột cần thiết. Giảm network bandwidth và memory.
-   **Thay thế Subquery bằng JOIN:** Subquery thường (nhưng không phải luôn luôn) chậm hơn JOIN.
-   **Dùng `EXISTS` thay vì `IN`:** Với tập dữ liệu lớn, `EXISTS` thường nhanh hơn.
-   **Pagination:** Tránh `OFFSET` lớn (`OFFSET 1000000` rất chậm). Dùng Cursor-based pagination (`WHERE id > last_seen_id LIMIT 10`).

---

## 3. Transactions & Isolation Levels: Đảm bảo tính toàn vẹn

Khi nhiều users cùng truy cập/sửa đổi dữ liệu, làm sao để không bị loạn?

### 3.1. 4 Isolation Levels (PostgreSQL)

Mức độ cô lập càng cao → An toàn càng cao → Performance càng thấp.

1.  **Read Uncommitted (Thấp nhất):**
    - Transaction A chưa commit, nhưng Transaction B đã đọc được (Dirty Read).
    - *PostgreSQL mặc định coi như Read Committed.*
2.  **Read Committed (Default):**
    - Chỉ đọc được data đã commit. Tránh Dirty Read.
    - Vấn đề: **Non-repeatable Read**. (A đọc row X = 10. B update X = 20 & commit. A đọc lại row X thấy = 20).
3.  **Repeatable Read:**
    - Đảm bảo trong 1 transaction, đọc 1 row bao nhiêu lần cũng giống nhau.
    - Vấn đề: **Phantom Read**. (A đếm users = 100. B insert 1 user. A đếm lại vẫn 100, nhưng thực tế DB đã có 101).
4.  **Serializable (Cao nhất):**
    - Thực thi song song nhưng kết quả giống như thực thi tuần tự.
    - An toàn tuyệt đối nhưng **rất chậm** và dễ gây lỗi `Serialization Failure` (cần retry logic).

### 3.2. Locking Strategies

-   **Optimistic Locking (Lạc quan):**
    - Giả sử ít khi xung đột.
    - Dùng cột `version`. Khi update check `WHERE id=1 AND version=1`. Nếu row đã bị ai update (version=2) → Fail → Retry.
    - Tốt cho Web Apps đọc nhiều ghi ít.
-   **Pessimistic Locking (Bi quan):**
    - Giả sử xung đột chắc chắn xảy ra. Lock luôn row khi đọc.
    - `SELECT * FROM products WHERE id=1 FOR UPDATE`. Transaction khác muốn đọc phải chờ.
    - Tốt cho hệ thống tài chính nhạy cảm.

---

## 4. Database Normalization: Thiết kế Schema chuẩn

Chuẩn hóa (Normalization) giúp giảm dư thừa dữ liệu (redundancy) và dị thường (anomalies).

### 4.1. Các dạng chuẩn (Normal Forms)

-   **1NF:** Mỗi ô chỉ chứa 1 giá trị đơn (Atomic). Không lưu JSON array, CSV trong 1 column.
-   **2NF:** Đạt 1NF + Mọi non-key attribute phụ thuộc hoàn toàn vào Primary Key (loại bỏ partial dependency).
-   **3NF:** Đạt 2NF + Không có phụ thuộc bắc cầu (Transitive dependency). (VD: Table `Order` có `CustomerName`. `CustomerName` phụ thuộc `CustomerId`, không phụ thuộc `OrderId` → Tách bảng `Customer`).

### 4.2. Denormalization (Phi chuẩn hóa)

Đôi khi ta cố tình vi phạm 3NF để **tăng tốc độ đọc**.

**Ví dụ:** E-commerce Order History.
-   **Normalized:** Khi hiển thị lịch sử đơn hàng, phải JOIN `Orders` -> `OrderItems` -> `Products`. Nếu Product đổi tên/giá, lịch sử bị sai.
-   **Denormalized:** Lưu snapshot `ProductName` và `Price` vào bảng `OrderItems` lúc mua.
    -   Ưu điểm: Query cực nhanh (không cần JOIN Product), giữ đúng lịch sử giá.
    -   Nhược điểm: Data bị lặp lại. Tốn dung lượng.

**Rule of Thumb:** Normalize first. Denormalize only for performance bottlenecks or history tracking.

---

## 5. Connection Pooling: Quản lý tài nguyên

Mở 1 connection tốn kém (TCP handshake, SSL, Auth). Nếu 1 request mở 1 connection → Server sập.

### 5.1. Cơ chế hoạt động
Pool duy trì sẵn một số lượng connections (VD: 20).
- Request đến → Mượn connection từ Pool.
- Xử lý xong → Trả connection về Pool (không đóng).
- Nếu Pool hết → Request phải chờ (Queue).

### 5.2. Tools
-   **pgBouncer:** Lightweight connection pooler cho PostgreSQL. Giúp handle hàng nghìn concurrent connections nhưng chỉ giữ vài chục kết nối thật tới DB.
-   **Application Side:** HikariCP (Java), Generic Pool (Node.js), Prisma (Built-in).

### 5.3. Công thức tính Pool Size
Sai lầm: Pool càng to càng tốt. Thực tế: Pool quá to làm CPU context switch nhiều → Chậm hơn.

Công thức tham khảo (PostgreSQL):
```
Pool Size = ((Core Count * 2) + Effective Spindle Count)
```
*VD: Server 4 Core → Pool Size khoảng 10-15 là tối ưu.*

---

## 6. Practical Examples: Schema Design thực chiến

### 6.1. E-commerce Schema (Relational)

**Yêu cầu:** Users, Products, Categories, Orders, Inventory.

-   **Users**: `id, email, password_hash, created_at`
-   **Categories**: `id, name, parent_id` (Self-referencing cho danh mục con)
-   **Products**: `id, name, price, category_id`
-   **Inventory**: `product_id, quantity` (Tách riêng để lock khi order dễ hơn)
-   **Orders**: `id, user_id, status, total_price`
-   **OrderItems**: `id, order_id, product_id, price_at_purchase, quantity` (Denormalize price)

**Key Decisions:**
-   Dùng `DECIMAL` cho Price (Không dùng `FLOAT` vì sai số làm tròn).
-   `Index` vào `user_id` trong Orders để lấy lịch sử nhanh.
-   Transaction khi đặt hàng:
    1. `BEGIN`
    2. `SELECT quantity FROM Inventory FOR UPDATE` (Pessimistic lock)
    3. Check đủ hàng? Nếu không → `ROLLBACK`
    4. `INSERT INTO Orders`
    5. `UPDATE Inventory SET quantity = quantity - sold`
    6. `COMMIT`

### 6.2. Social Network Feed (Hybrid)

**Yêu cầu:** Users post status, Friends view feed.

-   **Users (PostgreSQL):** Quản lý login, profile an toàn.
-   **Relationships (Graph DB / Redis):** Friend list.
-   **Posts (MongoDB/Cassandra):**
    -   Document chứa: `content`, `images` (array), `comments_preview` (3 comments đầu - Denormalization), `likes_count`.
    -   Sharding theo `user_id` hoặc `time`.

**Chiến lược Feed (Fan-out):**
-   Với User thường (ít followers): Khi post, đẩy ID bài viết vào list "Feed" của tất cả bạn bè (Write heavy).
-   Với Celeb (triệu followers): Không đẩy. Khi user view feed, query lấy bài của Celeb trộn vào (Read heavy).

---

## 7. Action Plan: Lộ trình luyện tập

### Tuần 1: Nắm vững SQL & Indexing
- [ ] Cài PostgreSQL & pgAdmin. Import sample database (DVD Rental).
- [ ] Viết query dùng JOIN, GROUP BY, HAVING, Window Functions (`RANK`, `ROW_NUMBER`).
- [ ] Dùng `EXPLAIN ANALYZE` để so sánh query có Index và không có Index. Thử tạo 1 triệu rows giả để thấy sự khác biệt.

### Tuần 2: Design & ORM
- [ ] Thiết kế schema cho Clone Shopee (bản đơn giản). Vẽ ER Diagram.
- [ ] Viết API dùng Node.js/Prisma hoặc C#/EF Core kết nối schema đó.
- [ ] Implement Pagination (Cursor-based).
- [ ] Xử lý N+1 Problem (Cố tình viết sai rồi sửa lại).

### Tuần 3: Advanced
- [ ] Thử nghiệm Transaction: Mở 2 terminal psql, thử `BEGIN; UPDATE...` ở bên này và xem bên kia bị block như thế nào.
- [ ] Cài Redis làm caching layer cho query chậm.

### 📚 Tài liệu tham khảo
-   **Book:** "Designing Data-Intensive Applications" (Martin Kleppmann) - *Must read*.
-   **Web:** "Use The Index, Luke" (Giải thích indexing cực hay).
-   **Tool:** dbdiagram.io (Vẽ ERD).

> **Lời khuyên:** Đừng học thuộc lòng syntax. Hãy hiểu **cách Database hoạt động bên dưới**. Đó là chìa khóa để trở thành Senior.
