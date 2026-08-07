# 📝 Checklist ôn tập System Design trước ngày phỏng vấn

> Mục tiêu: Trong 15–30 phút cuối trước phỏng vấn, rà soát nhanh framework tư duy và các điểm hay bị hỏi. Không nhồi thêm kiến thức mới.

Checklist ôn tập trước ngày phỏng vấn System Design

1. Ôn lại nền tảng cốt lõi
Trước khi nói về scale, hãy đảm bảo bạn hiểu rõ từng “mảnh ghép nhỏ” trong hệ thống:
- Cách hoạt động của Load Balancer, Cache, Database, Queue, CDN, Shard, Replication.
- Nắm được ưu - nhược điểm của từng giải pháp: SQL vs NoSQL, Vertical vs Horizontal Scaling, Monolith vs Microservices.
- Đừng chỉ đọc định nghĩa, hãy tự hỏi: “Trong tình huống nào mình sẽ dùng cái này?”

2. Rèn luyện tư duy phân tích bài toán
Một buổi phỏng vấn System Design không bao giờ có câu trả lời duy nhất. Cái họ muốn thấy là cách bạn tư duy:
- Bạn có đặt câu hỏi làm rõ yêu cầu không?
- Bạn có biết xác định bottleneck chính trong hệ thống không?
- Bạn có đưa ra được trade-off hợp lý giữa hiệu năng, chi phí, độ tin cậy và khả năng mở rộng không?
-> Luyện tập tư duy phản biện và diễn đạt mạch lạc chính là chìa khóa để ghi điểm trong mắt interviewer.

3. Làm quen với format phỏng vấn thực tế
Phần lớn các buổi System Design Interview kéo dài từ 45–60 phút. Hãy dành thời gian luyện theo cấu trúc chuẩn:
- Hiểu yêu cầu.
- Phác thảo kiến trúc tổng quan.
- Thiết kế các thành phần chính.
- Tính toán khả năng scale.
- Bàn về trade-off và cải tiến.
Bạn có thể thực hành bằng cách record lại buổi mock interview để xem mình có nói quá lan man, thiếu logic hoặc bỏ sót phần tính toán quan trọng nào không.

4. Chuẩn bị mindset và thời gian
Trước ngày phỏng vấn, đừng cố nhồi thêm kiến thức mới. Hãy tập trung ôn lại framework tư duy, ngủ đủ giấc, và giữ đầu óc tỉnh táo.
Một buổi System Design Interview thành công không đến từ việc bạn nhớ được bao nhiêu pattern, mà từ việc bạn biết cách đặt câu hỏi và dẫn dắt người phỏng vấn đi cùng mình qua dòng suy nghĩ.

## 1) Ôn nền tảng cốt lõi
- [ ] Load Balancer: L4 vs L7, health check, sticky session, failover multi-AZ/region.
- [ ] Cache/CDN: Cache aside vs write-through, TTL/eviction, cache stampede/thundering herd, CDN cho static/media.
- [ ] Database: SQL vs NoSQL (schema, transaction, secondary index, scale pattern), replication vs sharding, read replica vs leader election.
- [ ] Queue/Stream: At-least-once vs at-most-once, ordering per key, DLQ, backpressure.
- [ ] ID/Shard: Chọn shard key, hot shard, resharding, distributed ID (Snowflake).
- [ ] Consistency/HA: CAP, quorum, multi-region (active-active vs active-passive), disaster recovery RPO/RTO.

## 2) Rèn tư duy phân tích bài toán
- [ ] Hỏi rõ yêu cầu: Functional / Non-functional / Out-of-scope.
- [ ] Xác định bottleneck sớm: read-heavy, write-heavy, latency budget, storage growth.
- [ ] Nêu trade-off khi chọn: SQL vs NoSQL, cache vs chi phí, eventual vs strong, monolith vs microservices, vertical vs horizontal.
- [ ] Luôn gắn con số: QPS peak, read/write ratio, storage × retention, bandwidth upload/download.

## 3) Format phỏng vấn 45–60 phút (gợi ý khung 45’)
- Clarify (5’): Yêu cầu, constraint, SLA/latency, compliance, geo.
- Estimate (5’): QPS, storage, throughput, giả định công khai.
- High-level (10’): Client → API/LB → Service → Cache/DB/Queue/CDN; call out SPOF & redundancy.
- Deep dive (15–20’): Chọn 1–2 trọng tâm (data model/consistency, caching, indexing, replication, geo, realtime) → vấn đề → giải pháp → trade-off.
- Wrap/Q&A (5’): Nhắc quyết định chính, trade-off, monitoring/alerting, “nếu traffic tăng 10x…”.

## 4) Mindset & chuẩn bị cuối
- [ ] Không học thêm pattern mới; củng cố framework Clarify → Estimate → High-level → Deep dive → Wrap.
- [ ] Ngủ đủ, chuẩn bị giấy/bút hoặc tool vẽ; xin phép note/whiteboard đầu buổi.
- [ ] Giữ lời giải gọn: nói bằng con số và trade-off; mời interviewer chọn phần muốn đào sâu.

## 5) Cách tự luyện nhanh
- [ ] Tự mock 1 bài (vd: rate limiter, feed, chat) trong 15’ và tự ghi âm: xem có lan man/bỏ qua estimation không.
- [ ] Với mỗi kiến trúc, tự hỏi: shard key gì? cache ở đâu? anti-SPOF? chiến lược retry/DLQ?
- [ ] Nối lại với fundamentals nếu bí: CAP, replication, sharding, cache strategy.

---

Tham khảo thêm:
- [Interview Flow & Checklist (45’)](./interview-flow-and-checklist.md)
- [System Design Interview Flow (chi tiết)](./system-design-interview-flow.md)
- [Top 10 System Design Problems](./top-10-problems.md)