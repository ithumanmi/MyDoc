---
title: "Backend System Design Playbook"
description: "Trạm trung chuyển cho các bài phân tích system design: universe map, glossary, case studies, realtime chat, storage, search."
tags:
  - backend
  - system-design
updated: 2026-03-11
---

# 🧠 Backend System Design Playbook

> Tổng hợp kiến thức “khung xương” cho backend architect: bản đồ chủ đề, glossary, case study, realtime, storage, search và các hướng dẫn đang xây dựng (streaming platform, analytics pipeline).

## 📚 Nội dung chính
| Tài liệu | Nội dung | Khi nào dùng |
| --- | --- | --- |
| [System Design Universe](./system-design-universe.md) | Bản đồ 7 layer từ scalability đến observability | Định hướng học, phỏng vấn tổng quát |
| [System Design Glossary](./system-design-glossary.md) | 20 thuật ngữ “must-know” | Ôn trước vòng phỏng vấn, mentoring |
| [Case Studies](./case-studies.md) | URL shortener, chat, rate limiter, streaming, Uber, news feed | Luyện bài phỏng vấn/đề án nội bộ |
| [Real-time Chat System](./realtime-chat-system.md) | WebSocket, Redis Pub/Sub, Cassandra | Xây hoặc audit hệ thống chat/messaging |
| [Amazon S3 Architecture](./amazon-s3-architecture.md) | Metadata/data separation, erasure coding | Thiết kế object store, đánh giá durability |
| [Design Instagram](./design-instagram.md) | Hybrid fan-out feed, S3, CDN | Social feed, content platform |
| [Search Engine Architecture](./search-engine-architecture.md) | Crawl → index → vector retrieval | Site/vertical search, RAG search |
| [Large Video Upload Architecture](./large-video-upload-architecture.md) | Chunked upload 50GB, pipeline transcode, CDN | Nền tảng video & UGC dung lượng lớn |
| [Large-Scale System Architecture](./large-scale-system-architecture.md) | Khung thiết kế hệ thống lớn (bounded context, data, ops) | Architecture blueprint tổng thể |
| [Real-time Flash Sale Inventory](./realtime-flash-sale-inventory.md) | Redis counter, reservation window, anti-oversell | Flash sale, inventory realtime |
| [Circuit Breaker vs Retry](./circuit-breaker-vs-retry.md) | Lý do cần circuit breaker, pattern triển khai | Reliability, dependency protection |
| [Redis Durability Playbook](./redis-durability.md) | RDB/AOF persistence, replication, failover | Redis dùng làm state store an toàn |
| [Realtime Payment Microservice](./realtime-payment-microservice.md) | 100k RPS, exactly-once, active-active multi-region, ledger/outbox | Hệ thống payment realtime cần đúng/sống sót đa vùng |
| [Designing Data-Intensive Apps (cheatsheet)](./designing-data-intensive-applications.md) | Tóm tắt DDIA: mô hình dữ liệu, replication, partition, idempotency, streaming/batch, di trú | Khi cần ra quyết định kiến trúc dữ liệu
| [Distributed Messaging & Coordination](./distributed-messaging-and-coordination.md) | Kafka/Pulsar/RabbitMQ, Paxos/Raft/ZooKeeper, EOS patterns, saga, 2PC, idempotent producer/consumer dedup | Thiết kế messaging + exactly-once + coordination

## 🗺️ Roadmap sắp tới
- [ ] **Event Streaming Platform** – Kafka/Pulsar, schema registry, consumer scaling.
- [ ] **Analytics Pipeline** – Batch + realtime metrics, lakehouse kiến trúc.
- [ ] **Apply-it Templates** – Google Sheet/Notion checklist đi kèm từng bài.

## ✅ Cách sử dụng
1. **Định vị level** bằng `System Design Universe` → chọn module cần thiết.
2. **Ôn thuật ngữ** với Glossary rồi dive sâu các case study.
3. **Chốt deliverable** với checklist/Apply-it trong từng bài để biến lý thuyết thành artifact (diagram, script, metric dashboard).

> Góp ý thêm topic? Mở issue hoặc PR trong repo Docs. Luôn giữ nội dung “bias for action”: sau mỗi bài, nên có diagram, PoC hoặc checklist audit đi kèm.