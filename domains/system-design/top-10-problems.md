# 🧧 Top 10 System Design Problems (Big Tech Interview Prep)

> **"Tết này Engineer Pro lì xì ngay kiến thức giúp tăng offer lên vài chục nghìn đô 💰. Nếu bạn đang nhắm tới Google, Meta, Amazon, Microsoft... đây là 10 bài toán kinh điển bạn chắc chắn sẽ gặp."**

Hệ thống hóa 10 bài toán System Design phổ biến nhất cùng các điểm mấu chốt (core discussion) giúp bạn vượt qua vòng phỏng vấn Senior/Staff level.

---

## 1. Design URL Shortener (TinyURL/Bitly)
*   **Hỏi về:** ID generation (Base62, counter, hash), Read-heavy architecture.
*   **Core Discussion:** 
    *   Chiến lược Cache (Redis).
    *   DB Sharding.
    *   Analytics click tracking.
*   *Ý nghĩa:* Kiểm tra tư duy scale cơ bản và khả năng xử lý truy vấn đọc lớn.

## 2. Design News Feed (Twitter/X)
*   **Hỏi về:** Fan-out on write (Push) vs Fan-out on read (Pull).
*   **Core Discussion:**
    *   Timeline ranking.
    *   High write throughput.
    *   Distributed cache.
    *   Partition theo userID.
*   *Ý nghĩa:* 90% phỏng vấn Senior Big Tech đều có dạng feed.

## 3. Design Chat System (WhatsApp/Messenger)
*   **Hỏi về:** WebSocket vs Polling.
*   **Core Discussion:**
    *   Message ordering.
    *   Delivery guarantee (At-least-once, Exactly-once).
    *   Online/offline handling & Push notification.
*   *Ý nghĩa:* Kiểm tra kiến thức về Real-time & Distributed systems.

## 4. Design Video Streaming Platform (YouTube/Netflix)
*   **Hỏi về:** CDN, Video encoding pipeline.
*   **Core Discussion:**
    *   Chunk streaming (HLS/DASH).
    *   Metadata vs Blob storage.
    *   Recommendation engine (high-level).
*   *Ý nghĩa:* Bài test về khả năng scale quy mô toàn cầu.

## 5. Design Distributed Cache (Redis concept)
*   **Hỏi về:** Consistent hashing, Replication.
*   **Core Discussion:**
    *   Eviction policies (LRU/LFU).
    *   Handling Hot keys.
    *   Failover mechanism.
*   *Ý nghĩa:* Thường xuất hiện trong phỏng vấn Staff level.

## 6. Design Ride Sharing System (Uber/Grab)
*   **Hỏi về:** Real-time location tracking.
*   **Core Discussion:**
    *   Geo-indexing (QuadTree/Google S2).
    *   Matching driver – rider.
    *   Surge pricing (giá tăng mạnh khi nhu cầu cao).
*   *Ý nghĩa:* Thiên về Geo + Real-time system.

## 7. Design File Storage System (Google Drive/Dropbox)
*   **Hỏi về:** Chunk upload, Metadata vs Object storage.
*   **Core Discussion:**
    *   Versioning & Conflict handling.
    *   Deduplication (loại bỏ dữ liệu trùng lặp).
    *   Access control list (ACL).
*   *Ý nghĩa:* Kiểm tra tư duy lưu trữ dữ liệu khối lượng lớn.

## 8. Design Rate Limiter
*   **Hỏi về:** Các thuật toán chặn (Token bucket vs Leaky bucket).
*   **Core Discussion:**
    *   Distributed limit handling.
    *   Atomic counter (dùng Redis).
    *   Per-user vs Global limit.
*   *Ý nghĩa:* Bài toán nhỏ nhưng cực kỳ nguy hiểm nếu không nắm chắc race condition.

## 9. Design Search Autocomplete (Google Search)
*   **Hỏi về:** Trie data structure.
*   **Core Discussion:**
    *   Prefix matching.
    *   Ranking based on frequency.
    *   Memory optimization & Near real-time update.
*   *Ý nghĩa:* Kiểm tra sự kết hợp giữa Data structure và Scale.

## 10. Design Logging / Monitoring System
*   **Hỏi về:** Log ingestion pipeline.
*   **Core Discussion:**
    *   Message queue (Kafka concept).
    *   Indexing (Elasticsearch concept).
    *   Alerting & High write throughput.
*   *Ý nghĩa:* Infra Engineer rất hay gặp bài này.

## 11. Design Notification System (Email/Push/In-app)
*   **Hỏi về:** User preference, idempotent delivery.
*   **Core Discussion:**
    *   Queue decouple, retry, DLQ.
    *   Provider abstraction layer.
    *   Scheduling, rate limit per user/campaign.
*   *Ý nghĩa:* Rất phổ biến trong e-commerce, fintech, SaaS.

## 12. Design API Gateway
*   **Hỏi về:** Routing, auth, observability.
*   **Core Discussion:**
    *   Path/header-based routing.
    *   JWT/API key validation, rate limiting.
    *   Logging, tracing, canary rollout.
*   *Ý nghĩa:* Mọi hệ thống microservices đều cần gateway chuẩn.

## 13. Design Distributed ID Generator (Snowflake)
*   **Hỏi về:** ID uniqueness, ordering.
*   **Core Discussion:**
    *   Snowflake bit layout, clock drift.
    *   Worker ID assignment, multi-region.
    *   Alternative: UUIDv7, KGS, Hi/Lo.
*   *Ý nghĩa:* Liên quan đến mọi hệ thống cần ID tăng dần (URL shortener, order, message).

---

## 🎯 Bonus: Interviewer thật sự chấm điểm gì?

Họ KHÔNG chấm bạn có nhớ kiến trúc giống production của họ hay không. Họ chấm:
1.  **Clarify Requirement:** Bạn có đặt câu hỏi để làm rõ yêu cầu không?
2.  **Estimation:** Bạn có ước lượng được QPS (Query Per Second) và Storage không?
3.  **Trade-offs:** Bạn chọn cái gì (Consistency vs Availability)? Vì sao?
4.  **Bottleneck:** Bạn có tìm ra điểm nghẽn và cách khắc phục không?
5.  **Scale:** Bạn mở rộng hệ thống như thế nào khi lượng user tăng 100 lần?

---

## 📚 Tài liệu liên quan
*   [How Redis Works](./how-redis-works.md)
*   [System Design Readme](./README.md)
*   [Interview Flow & Checklist (45’)](./interview-flow-and-checklist.md)
*   [Data Strategy](../data-strategy/README.md)
