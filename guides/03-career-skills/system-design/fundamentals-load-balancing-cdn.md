# 🌐 Load Balancing, CDN & High Scalability Basics

> [← Back to System Design](./README.md) | [Glossary](../../GLOSSARY.md)

Tài liệu ngắn gọn này giúp bạn nắm các khái niệm cơ bản thường gặp khi nói về khả năng mở rộng (High Scalability), bao gồm load balancer, health check, sticky session và CDN edge cache.

---

## 1. Load Balancer 101

### Layer 4 vs Layer 7
| Loại | Đặc điểm | Khi dùng |
| --- | --- | --- |
| **Layer 4 (TCP/UDP)** | Không hiểu HTTP; chỉ chuyển packet dựa trên IP/port. Overhead thấp, rất nhanh. | Game server, dịch vụ không cần thao tác header. |
| **Layer 7 (HTTP/HTTPS)** | Hiểu header, cookie, path. Có thể làm routing theo URL, A/B testing. | Web/API gateway, microservices HTTP. |

### Algorithms phổ biến
- **Round Robin / Weighted RR:** đơn giản, hiệu quả khi server cấu hình tương đương.
- **Least Connection / Fastest Response:** phù hợp khi load không đồng đều.
- **Consistent Hashing:** dùng cho sticky session hoặc cache (ví dụ CDN).

### Health Check & Auto-scaling
- LB ping endpoint `/healthz` hoặc kiểm tra TCP handshake. Nếu fail → đưa server ra khỏi pool.
- Kết hợp **Auto Scaling Group** để thêm server mới khi CPU/QPS vượt ngưỡng.
- **Drain connection** trước khi shutdown để tránh rớt request.

### Sticky Session
- **Cookie-based hash** (Layer 7) hoặc **Source IP hash** (Layer 4).
- Nên kết hợp với **Session Store chung** (Redis/Memcached) để không phụ thuộc duy nhất vào LB.
- Khi nào cần? Khi ứng dụng chưa stateless hoàn toàn (ví dụ user cart, chat socket).

---

## 2. CDN & Edge Cache

### Kiến trúc cơ bản
```
Client → Edge POP (cache) → Origin Shield → Origin Server
```
- **Edge POP:** đặt gần người dùng cuối, giảm latency.
- **Origin Shield:** lớp cache trung gian bảo vệ origin khỏi burst.

### Cache Key & TTL
- Cache key thường gồm URL + query params + headers quan trọng (Accept-Language, Device).
- TTL ngắn cho nội dung thay đổi thường xuyên, TTL dài cho asset tĩnh.
- **Cache invalidation:** Purge theo URL/prefix hoặc dùng versioning (`app.v123.js`).

### Streaming & Large Object
- **Chunked transfer / HLS/DASH:** CDN cache từng segment video.
- **Range request:** hỗ trợ resume download.
- **Zero-downtime deploy:** đẩy asset mới lên CDN trước rồi flip switchover.

---

## 3. High Scalability Patterns (gộp nhanh)
- **Stateless services + Horizontal scaling:** dễ auto-scale, kết hợp LB phía trước.
- **Cache-aside:** Redis/Memcached phía trước DB để giảm read load.
- **Backpressure & Queue:** Khi downstream quá tải, đặt queue để san phẳng lưu lượng.
- **Circuit Breaker & Retry policy:** tránh cascade failure khi một service chết.

---

## 4. Checklist phỏng vấn
| Chủ đề | Bạn cần nhắc tới |
| --- | --- |
| Load Balancer | Layer 4/7, algorithm, health check, sticky session, autoscaling |
| CDN | Edge cache, invalidation, TTL, origin shielding |
| Scalability | Cache, queue, stateless design, circuit breaker |

---

## 5. Tài liệu liên quan
- [System Design Fundamentals](./system-design-fundamentals.md)
- [Design Logging / Monitoring](./design-logging-monitoring.md) để hiểu health check + observability.
- [Design Video Streaming](./design-video-streaming.md) và [Design Distributed Cache](./design-distributed-cache.md) cho ví dụ thực tế.