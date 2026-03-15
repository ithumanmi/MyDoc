# 📘 System Design Fundamentals (Nền tảng bắt buộc)

> [← Back to System Design](./README.md) | [domains/backend-dev](../../domains/backend-dev/README.md) | [Glossary](../../GLOSSARY.md)

Tài liệu này cung cấp từ vựng và khái niệm cơ bản trước khi bạn bước vào các bài toán System Design. Nếu bạn chưa quen với các thuật ngữ như CAP, sharding, replication… hãy dành 30 phút đọc hết phần này trước.

---

## 1. Prerequisites nên có

| Nền tảng | Bạn cần nắm | Gợi ý ôn tập |
| --- | --- | --- |
| **Networking cơ bản** | TCP vs UDP, HTTP, DNS, CDN | [domains/backend-dev/networking](../../domains/backend-dev/architecture/networking.md) |
| **Cơ sở dữ liệu** | ACID, Index, Query plan, Normalization | [domains/backend-dev/database](../../domains/backend-dev/architecture/database.md) |
| **Data Structures** | Hash table, Heap, Trie, Graph | [challenges/dsa](../../challenges/dsa/README.md) |

---

## 2. CAP Theorem & Consistency Models

### CAP
- **Consistency:** Tất cả node thấy cùng dữ liệu tại cùng thời điểm.
- **Availability:** Hệ thống trả lời mọi yêu cầu (thành công hoặc lỗi) ngay cả khi mất node.
- **Partition Tolerance:** Hệ thống vẫn hoạt động khi mạng phân mảnh.

> Không thể tối đa cả 3. Trong thực tế: CP (ví dụ HBase) vs AP (ví dụ Cassandra). Rất ít hệ thống chọn CA vì mạng phân mảnh luôn có thể xảy ra.

### Consistency Models
- **Strong consistency:** Đọc luôn thấy dữ liệu mới nhất. Trade-off: latency cao.
- **Eventual consistency:** Chấp nhận dữ liệu lỗi thời trong thời gian ngắn, đổi lại độ trễ thấp và sẵn sàng cao.
- **Read-your-writes / Monotonic reads:** Các biến thể đảm bảo trải nghiệm cụ thể cho user.

👉 Tham khảo thêm trong [Glossary: CAP, Consistency](../../GLOSSARY.md#distributed-systems).

---

## 3. Sharding vs Replication

### Replication (Nhân bản dữ liệu)
- **Master-Slave / Primary-Replica:** Write vào Primary, replicate sang Replica để Read.
- **Sync vs Async:** Sync đảm bảo mạnh nhưng chậm; Async nhanh nhưng có khả năng mất dữ liệu khi Primary chết.
- **Use case:** Tăng khả năng chịu đọc, HA.

### Sharding (Phân mảnh dữ liệu)
- Chia dữ liệu thành nhiều shard theo **Key Range**, **Hash**, hoặc **Geo**.
- Cần **Shard Map** (ví dụ: Consistent Hash Ring, Metadata service).
- Thử thách: Resharding khi shard đầy, Hot shard, Giao dịch multi-shard.

> Rule of thumb: Replication = tăng độ sẵn sàng; Sharding = vượt giới hạn dung lượng/throughput.

---

## 4. Load Balancing & CDN

### Load Balancer
- **Layer 4 vs Layer 7:** TCP vs HTTP-aware.
- **Algorithm:** Round Robin, Least Connection, Consistent Hashing.
- **Health check & Auto-scaling:** Kết hợp với Auto Scaling Group để thay server hỏng.

### CDN
- **Edge cache** nội dung tĩnh (image, video segment, JS bundle) ở POP gần người dùng.
- **Invalidation & TTL:** Kiểm soát khi nào nội dung mới được refresh.
- **Video streaming:** CDN + origin shielding để bảo vệ server gốc.

---

## 5. Microservices vs Monoliths

- **Monolith:** nhanh triển khai, ít complexity. Khó scale riêng lẻ, release ảnh hưởng toàn hệ thống.
- **Microservices:** chia theo domain bounded context, giao tiếp qua API/gRPC/Event bus.
- **Trade-offs:** thêm complexity (service discovery, observability, data consistency). Nên chỉ tách khi team/traffic đạt ngưỡng.

---

## 6. Tóm tắt nhanh (Cheatsheet)

| Chủ đề | Hỏi gì trong phỏng vấn? | Trả lời nhanh |
| --- | --- | --- |
| CAP | Nếu partition xảy ra bạn chọn gì? | Tùy domain: ngân hàng chọn CP; mạng xã hội chọn AP. |
| Consistency | Làm sao để eventual consistency không gây UX xấu? | Dùng read-your-writes hoặc cache per-user. |
| Sharding | Làm sao tìm đúng shard? | Consistent hashing hoặc metadata service + caching. |
| Replication | Nếu primary chết? | Chạy failover (manual/semi-auto) + đảm bảo replica up-to-date. |
| Load Balancer | Xử lý session stickiness? | Dùng cookie-based hash hoặc session store ngoài. |
| CDN | Làm sao cập nhật nội dung mới? | Purge API + short TTL cho tài nguyên động. |

---

## 7. Next Steps
- Đọc tiếp các bài toán cụ thể (URL shortener, News Feed…).
- Ôn lại thuật ngữ trong [Glossary](../../GLOSSARY.md) và [domains/backend-dev](../../domains/backend-dev/README.md).
- Thực hành estimation & trade-offs với [challenges/backend](../../challenges/backend/README.md).