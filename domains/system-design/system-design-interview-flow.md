# 🧭 45’ System Design Interview Flow

> [← Back to System Design](./README.md) | [Top 10 Problems](./top-10-problems.md)

Phỏng vấn system design thường kéo dài ~45 phút. Checklist dưới đây giúp bạn điều hướng cuộc trò chuyện mạch lạc, thể hiện tư duy có cấu trúc.

---

## 0. Mindset & Setup (2 phút)
- Xin phép ghi chú/whiteboard.
- Confirm domain: mobile/web/backend, số user, traffic.
- Nhớ “đàm phán” scope: cái gì ngoài phạm vi thì nói rõ để tránh lan man.

---

## 1. Clarify Requirements (5 phút)
| Checklist | Ghi chú |
| --- | --- |
| Functional chính? | Ví dụ: shorten URL, feed realtime, upload video |
| Non-functional | Latency target, availability, scale |
| Constraints | Compliance, multi-tenant, multi-region |
| Success metric | QPS, DAU, retention |

**Tip:** Dùng template “Functional / Non-functional / Out-of-scope”.

---

## 2. Back-of-the-envelope Estimation (5 phút)
| Hạng mục | Ví dụ câu hỏi | Ghi chú |
| --- | --- | --- |
| Traffic | Bao nhiêu DAU? Peak QPS? | Ước lượng order-of-magnitude |
| Storage | Data mỗi entity, retention | Tính TB/GB |
| Throughput | Write/read ratio, bandwidth | Giúp chọn DB/cache |

**Tip:** Nếu không chắc, nêu giả định công khai (“Giả sử 100M DAU…”).

---

## 3. High-level Architecture (10 phút)
1. Vẽ diagram: client → API Gateway → Service → DB/Cache. Thêm message queue nếu cần.
2. Nói to các component chính, lý do chọn: load balancer, CDN, microservices.
3. Chỉ ra điểm single point of failure & cách xử lý (replication, multi-AZ).

**Checklist:**
- [ ] Có Layer 7 LB?
- [ ] Có Cache/CDN nếu read-heavy?
- [ ] DB đã xác định loại (SQL vs NoSQL)?

---

## 4. Deep Dive by Bottleneck (15 phút)
Chọn 2-3 trọng tâm tùy bài:

| Chủ đề | Khi nào chọn |
| --- | --- |
| **Data model + Consistency** | URL shortener, Transaction-heavy |
| **Caching strategy** | Rate limiter, Feed |
| **Storage/Replication** | File storage, Video streaming |
| **Geo/Realtime** | Ride sharing, Chat |

**Template trình bày:**
1. Nêu vấn đề (vd: hạn chế read latency).
2. Đề xuất giải pháp (cache, sharding…)
3. Trade-offs (stale data, write amplification).
4. Kết luận vì sao chọn.

---

## 5. Q&A / Extension (5 phút)
- Đề xuất thêm monitoring, alerting, rate limiter.
- Nêu thử failure scenario: “Nếu Region A chết thì…”.
- Hỏi interviewer xem muốn đào sâu phần nào nữa.

---

## Mini Cheat Sheet
- **Thứ tự cố định:** Clarify → Estimate → High-level → Deep dive → Q&A.
- **Nói bằng con số:** mọi quyết định nên đi kèm order-of-magnitude.
- **Ưu tiên trade-off:** “Chọn eventual consistency để giảm P99 latency xuống <200ms”.
- **Đề cập cross-domain:** liên hệ với [System Design Fundamentals](./system-design-fundamentals.md) khi giải thích CAP/sharding.

---

## Tài liệu liên quan
- [Top 10 System Design Problems](./top-10-problems.md)
- [domains/backend-dev](../../domains/backend-dev/README.md)
- [challenges/backend](../../challenges/backend/README.md)