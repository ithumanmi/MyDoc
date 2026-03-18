# 🏗️ System Design & Architecture (Thiết kế Hệ thống)

> [← Back to domains](../README.md) | [Home](../../README.md) | **Last reviewed:** March 2026

Chào mừng bạn đến với hướng dẫn về **System Design**.
Tại đây chúng ta sẽ đi sâu vào kiến trúc phần mềm, khả năng mở rộng (Scalability) và các công nghệ cốt lõi của backend hiện đại.

---

## 🆕 Cập nhật mới nhất (March 2026)
*   **Design Notification System:** Multi-channel pipeline, idempotency, preference service.
*   **Design API Gateway:** Routing, auth, rate limit, observability & canary.
*   **Design Distributed ID Generator:** Snowflake, UUIDv7, KGS/Hi-Lo.

---

## 📚 Mục lục

### 0. Foundations
*   **[System Design Fundamentals](./system-design-fundamentals.md):** Lộ trình đọc + microservices overview.
*   **[⚖️ Scalability & Consistency](./fundamentals-scalability-consistency.md):** CAP, eventual vs strong, replication, quorum, sharding.
*   **[🌐 Load Balancing & CDN](./fundamentals-load-balancing-cdn.md):** Layer 4/7, health check, sticky session, CDN edge cache.
*   **[🌀 Event Sourcing & CQRS Fundamentals](./fundamentals-event-sourcing.md):** Khi nào dùng event store, snapshot, saga.
*   **[📨 Messaging Patterns & Distributed Queues](./fundamentals-messaging-patterns.md):** Queue vs log, delivery semantics, reliability patterns.
*   **[🗳️ Consensus Algorithms ✨](./fundamentals-consensus-algorithms.md):** Cơ chế Raft, Paxos, Quorum, chống Split-brain. (⭐ **New**)
*   **[🎲 Probabilistic Data Structures ✨](./fundamentals-probabilistic-data-structures.md):** Bloom Filter, Count-Min Sketch, HyperLogLog với Big Data. (⭐ **New**)
*   **Prerequisites:**
    *   Hiểu HTTP/HTTPS, REST, load balancer cơ bản.
    *   Nắm chắc cấu trúc dữ liệu & thuật toán phổ biến (hash map, heap, trie…)
    *   Kiến thức database cơ bản (transaction, indexing, replication, CAP)
    *   Trải nghiệm backend (API, microservices, message queue) giúp hấp thụ nhanh hơn.

### 1. Databases & Caching (Cơ sở dữ liệu & Bộ nhớ đệm)
*   **[How Redis Works (Kiến trúc Redis)](./how-redis-works.md):** Giải mã sức mạnh của In-Memory Database phổ biến nhất thế giới.
*   *(Coming Soon)*: SQL vs NoSQL Deep Dive.

### 2. High Scalability (Khả năng mở rộng cao)
*   **[🌐 Load Balancing & CDN](./fundamentals-load-balancing-cdn.md)** *(đang bổ sung ví dụ thực chiến)*

### 3. Distributed Systems (Hệ thống phân tán)
*   **[⚖️ Scalability & Consistency](./fundamentals-scalability-consistency.md)** *(đang bổ sung: event sourcing, messaging)*

### 4. Interview Preparation (Luyện phỏng vấn)
*   **[45’ System Design Flow](./system-design-interview-flow.md):** Clarify → Estimate → High-level → Deep dive → Q&A checklist.
*   **[Interview Flow & Checklist (45’)](./interview-flow-and-checklist.md):** Breakdown thời gian + checklist chi tiết cho từng pha.
*   **[Top 10 System Design Problems](./top-10-problems.md):** 10 bài toán kinh điển tại các Big Tech.
*   **[1. Design URL Shortener](./design-url-shortener.md):** Deep dive bài toán TinyURL.
*   **[2. Design News Feed](./design-news-feed.md):** Deep dive bài toán Twitter/X.
*   **[3. Design Chat System](./design-chat-system.md):** Deep dive bài toán WhatsApp/Messenger.
*   **[4. Design Video Streaming Platform](./design-video-streaming.md):** Deep dive bài toán YouTube/Netflix.
*   **[5. Design Distributed Cache](./design-distributed-cache.md):** Deep dive bài toán Redis.
*   **[6. Design Ride Sharing System](./design-ride-sharing.md):** Deep dive bài toán Uber/Grab.
*   **[7. Design File Storage System](./design-file-storage.md):** Deep dive bài toán Google Drive.
*   **[8. Design Rate Limiter](./design-rate-limiter.md):** Deep dive hệ thống chặn truy cập.
*   **[9. Design Search Autocomplete](./design-search-autocomplete.md):** Deep dive bài toán Google Search.
*   **[10. Design Logging / Monitoring](./design-logging-monitoring.md):** Deep dive hệ thống giám sát.
*   **[11. Design Notification System](./design-notification-system.md):** Push/email/in-app với queue, idempotency, user preferences.
*   **[12. Design API Gateway](./design-api-gateway.md):** Routing, auth, rate limiting, observability.
*   **[13. Design Distributed ID Generator](./design-distributed-id-generator.md):** Snowflake, UUID, KGS cho mọi dịch vụ cần ID.
*   **[14. Design Ticketmaster/Booking ✨](./design-ticket-booking.md):** Chống nhồi nhét concurrent cao bằng Queue CDN, Distributed Locking qua Redis SETNX. (⭐ **New**)
*   **[15. Design Gaming Leaderboard ✨](./design-leaderboard.md):** Lọc Bảng xếp hạng Real-time 10 Triệu Game thủ với Redis ZSET/Skip List. (⭐ **New**)

### 5. Thực Hành Hiện Thực (System Coded Labs)
*   **[🧪 Code Lab: Xây Dựng Rate Limiter Redis ✨](./labs/lab-redis-rate-limiter.md):** Rời rãnh lý thuyết vẽ. Lập trình Token Bucket API Rate Limiter tuyệt đối Atomic bằng Redis Lua Script bọc Middleware. (⭐ **New**)

---

## 🔗 Cross-link & Prerequisites
- [domains/backend-dev](../../domains/backend-dev/README.md): kiến trúc backend, API, database, networking.
- [challenges/backend](../../challenges/backend/README.md): luyện tập system design thực chiến.
- [GLOSSARY](../../GLOSSARY.md): thuật ngữ CAP, eventual consistency, sharding, replication…
- [domains/data-analytics/logging](../../domains/data-analytics/README.md) & [challenges/devops-sre](../../challenges/devops-sre/README.md) cho các chủ đề monitoring/logging nâng cao.
