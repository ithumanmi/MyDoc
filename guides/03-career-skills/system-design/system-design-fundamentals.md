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

## 2. Bản đồ kiến thức tiếp theo
- **[⚖️ Scalability & Consistency](./fundamentals-scalability-consistency.md):** CAP sâu hơn, replication, quorum, sharding.
- **[🌐 Load Balancing & CDN](./fundamentals-load-balancing-cdn.md):** Layer 4 vs 7, sticky session, edge cache, invalidation.

👉 Nếu các mục này đã nắm vững, tiếp tục xuống phần dưới để xem microservices, cheat sheet…

---

## 5. Microservices vs Monoliths

- **Monolith:** nhanh triển khai, ít complexity. Khó scale riêng lẻ, release ảnh hưởng toàn hệ thống.
- **Microservices:** chia theo domain bounded context, giao tiếp qua API/gRPC/Event bus.
- **Trade-offs:** thêm complexity (service discovery, observability, data consistency). Nên chỉ tách khi team/traffic đạt ngưỡng.

---

## 3. Tóm tắt nhanh (Cheatsheet)

| Chủ đề | Hỏi gì trong phỏng vấn? | Trả lời nhanh |
| --- | --- | --- |
| CAP | Nếu partition xảy ra bạn chọn gì? | Tùy domain: ngân hàng chọn CP; mạng xã hội chọn AP. |
| Consistency | Làm sao để eventual consistency không gây UX xấu? | Dùng read-your-writes hoặc cache per-user. |
| Sharding | Làm sao tìm đúng shard? | Consistent hashing hoặc metadata service + caching. |
| Replication | Nếu primary chết? | Chạy failover (manual/semi-auto) + đảm bảo replica up-to-date. |
| Load Balancer | Xử lý session stickiness? | Dùng cookie-based hash hoặc session store ngoài. |
| CDN | Làm sao cập nhật nội dung mới? | Purge API + short TTL cho tài nguyên động. |

---

## 4. Next Steps
- Đọc tiếp các bài toán cụ thể (URL shortener, News Feed…).
- Ôn lại thuật ngữ trong [Glossary](../../GLOSSARY.md) và [domains/backend-dev](../../domains/backend-dev/README.md).
- Thực hành estimation & trade-offs với [challenges/backend](../../challenges/backend/README.md).