# 📨 Messaging Patterns & Distributed Queues

> [← Back to System Design](./README.md)

Messaging bảo đảm service tách rời, không nghẽn khi downstream chậm và giữ thứ tự xử lý theo nhu cầu. Tài liệu này tóm tắt các pattern cốt lõi, trade-off và checklist phỏng vấn.

---

## 1. Broker Options
| Loại | Khi nào dùng | Đặc điểm |
| --- | --- | --- |
| **Queue (RabbitMQ, SQS)** | Work queue, task async | FIFO, ack, routing key |
| **Log (Kafka, Pulsar)** | Stream event, analytics | Partitioned append log, consumer group |
| **Pub/Sub (SNS, GCP Pub/Sub)** | Fan-out thông báo | Push/pull, at-least-once |

---

## 2. Core Patterns

### a. Work Queue (Task Distribution)
- Producer push job (resize image, send email)
- Consumer pool pull job, ack khi xong
- **Checklist:** visibility timeout, retry/backoff, DLQ.

### b. Event Bus / Event Streaming
- Producer append event (UserSignedUp)
- Nhiều consumer group đọc song song → analytics, billing.
- **Checklist:** partition key, ordering guarantee per key, offset management.

### c. Pub/Sub fan-out
- Một message gửi đến nhiều subscriber.
- Dùng cho notification, invalidate cache, webhook.

### d. Request/Reply trên message
- Correlation ID + reply queue.
- Hạn chế: latency cao hơn HTTP, cần timeout logic.

---

## 3. Delivery Semantics
| Semantics | Ý nghĩa | Technique |
| --- | --- | --- |
| At-most-once | Không retry, có thể mất message | Fire-and-forget, UDP-like |
| At-least-once | Retry cho tới khi ack | Delivery ID + idempotent consumer |
| Exactly-once (logic) | Kết hợp idempotent + dedupe store | Kafka transactional write, outbox pattern |

> **Interview tip:** Nêu rõ hệ thống cần loại nào. Ví dụ: “Billing bắt buộc at-least-once + idempotent handler, log analytics có thể at-most-once.”

---

## 4. Ordering & Scaling
- **Partition key** quyết định event cùng key ở cùng partition → đảm bảo order per user.
- **Hot partition**: khi một key quá nhiều traffic → hash key + suffix, hoặc multi-tenant partitioning.
- **Consumer scale**: tăng consumer group instance nhưng <= số partition (Kafka).

---

## 5. Reliability Patterns
1. **Dead Letter Queue (DLQ):** message lỗi quá `n` lần → chuyển sang DLQ để điều tra.
2. **Retry + Backoff:** exponential backoff tránh đánh sập service downstream.
3. **Outbox Pattern:** ghi event vào outbox table trong transaction DB → background publisher push vào broker → đảm bảo consistency giữa DB & queue.
4. **Idempotent Consumer:** dùng `messageId` + store processed ID hoặc sử dụng upsert.

---

## 6. Monitoring Checklist
- [ ] Lag của consumer group (Kafka lag metric)
- [ ] DLQ size
- [ ] Throughput (msg/s)
- [ ] Processing latency (ingest → ack)
- [ ] Error rate per consumer

---

## 7. Phỏng vấn: câu hỏi gợi ý
- “Nếu consumer chết giữa chừng?” → visibility timeout/reset offset.
- “Có cần transaction giữa DB và queue?” → outbox pattern + CDC.
- “Webhook thất bại thì sao?” → retry + exponential backoff + DLQ.
- “Tại sao Kafka phù hợp cho log pipeline?” → append log, retention, replay.

---

## 8. Thực hành & tài liệu
- [Kafka Design](https://kafka.apache.org/documentation/) tài liệu chính thức.
- [AWS SQS vs SNS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html).
- Bài tập: áp dụng vào [Design Logging/Monitoring](./design-logging-monitoring.md) hoặc [Rate Limiter](./design-rate-limiter.md) để xử lý fan-out log & throttle.
