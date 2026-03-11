# 🌌 The System Design Universe: Bản Đồ Toàn Cảnh

---
title: "System Design Universe"
description: "Bản đồ layer từ scalability đến observability cho backend architect."
tags:
  - backend
  - system-design
  - roadmap
updated: 2026-03-11
---

> [← Back to Backend Roadmap](../README.md)

Chào mừng bạn đến với "Vũ Trụ System Design". Đây là bản đồ khái niệm giúp bạn định vị mình đang ở đâu và cần học gì tiếp theo để trở thành một Architect thực thụ.
Kiến thức được chia thành các lớp (Layers) từ lõi ra ngoài.

---

## 🔴 Layer 1: Scalability & Performance (Lõi Hiệu Năng)
*Nền tảng để hệ thống chạy nhanh và chịu tải cao.*

1.  **Scalability:**
    *   **Vertical Scaling (Scale Up):** Nâng cấp phần cứng (CPU/RAM).
    *   **Horizontal Scaling (Scale Out):** Thêm nhiều máy chủ.
    *   **Auto-scaling:** Tự động tăng/giảm số lượng server theo traffic.
2.  **Performance Optimization:**
    *   **Caching:** Lưu dữ liệu vào RAM (Redis, Memcached). Strategies: LRU, LFU, Write-Through.
    *   **CDN (Content Delivery Network):** Phân phối nội dung tĩnh (ảnh/video) ở edge server.
    *   **Load Balancing:** Chia tải (Round Robin, Least Connections).
    *   **Throttling & Rate Limiting:** Giới hạn tốc độ request để bảo vệ server.

---

## 🟢 Layer 2: Database Design (Thiết Kế Dữ Liệu)
*Trái tim lưu trữ thông tin.*

1.  **Database Types:**
    *   **SQL vs NoSQL:** Cấu trúc chặt chẽ (Postgres) vs Linh hoạt (Mongo).
    *   **OLAP vs OLTP:** Phân tích (Analytics) vs Giao dịch (Transactions).
    *   **Time-series DB:** Dữ liệu theo thời gian (InfluxDB).
2.  **Scaling Data:**
    *   **Replication:** Master-Slave, Multi-Master.
    *   **Sharding (Partitioning):** Horizontal (Hash/Range) vs Vertical.
    *   **Indexing:** B-Tree, Hash Index, Inverted Index.
3.  **Consistency Models:**
    *   **ACID:** Atomicity, Consistency, Isolation, Durability.
    *   **BASE:** Basically Available, Soft state, Eventual consistency.
    *   **CAP Theorem:** Consistency, Availability, Partition Tolerance.

---

## 🟢 Layer 3: Microservices & Architecture (Kiến Trúc)
*Cách tổ chức code và service.*

1.  **Communication:**
    *   **REST vs gRPC:** JSON qua HTTP vs Protobuf qua HTTP/2.
    *   **Event-Driven:** Pub/Sub (Kafka, RabbitMQ).
2.  **Patterns:**
    *   **API Gateway:** Cổng vào duy nhất (Routing, Auth).
    *   **Circuit Breaker:** Ngắt kết nối khi lỗi (Resilience4j).
    *   **Saga Pattern:** Giao dịch phân tán (Distributed Transactions).
    *   **Sidecar Pattern:** Tách biệt logic hạ tầng (Service Mesh).
    *   **CQRS:** Tách biệt Read và Write model.

---

## 🟠 Layer 4: High Availability & Fault Tolerance (Độ Tin Cậy)
*Đảm bảo hệ thống luôn sống sót.*

1.  **Consensus Algorithms:**
    *   **Raft / Paxos:** Đồng thuận trong hệ thống phân tán (Leader Election).
    *   **Gossip Protocol:** Lan truyền thông tin peer-to-peer.
2.  **Resilience:**
    *   **Retry Mechanisms:** Thử lại khi lỗi (Exponential Backoff).
    *   **Failover:** Tự động chuyển sang backup server (Active-Passive).
    *   **Disaster Recovery:** Sao lưu và khôi phục thảm họa.
3.  **Deployment:**
    *   **Blue-Green / Canary:** Deploy không downtime.
    *   **Multi-Region:** Chạy trên nhiều khu vực địa lý.

---

## 🔴 Layer 5: Distributed Systems (Hệ Thống Phân Tán)
*Các vấn đề nâng cao khi máy chủ nằm rải rác.*

1.  **Distributed Computing:**
    *   **MapReduce:** Xử lý dữ liệu lớn song song.
    *   **Distributed File Systems:** HDFS, Ceph.
2.  **Algorithms:**
    *   **Consistent Hashing:** Phân phối dữ liệu khi thêm/bớt node.
    *   **Bloom Filter:** Kiểm tra sự tồn tại nhanh chóng.
    *   **Merkle Tree:** Kiểm tra tính toàn vẹn dữ liệu (Blockchain).

---

## 🔵 Layer 6: Security & Compliance (Bảo Mật)
*Lớp vỏ bảo vệ.*

1.  **Authentication & Authorization:**
    *   **OAuth2 / OIDC:** Ủy quyền đăng nhập.
    *   **JWT:** Token xác thực stateless.
    *   **RBAC / ABAC:** Phân quyền theo vai trò/thuộc tính.
2.  **Data Protection:**
    *   **Encryption:** At rest (AES) & In transit (TLS/SSL).
    *   **Hashing:** SHA-256, Bcrypt (cho password).
3.  **Network Security:**
    *   **DDoS Mitigation:** Chống tấn công từ chối dịch vụ.
    *   **Zero Trust:** Không tin tưởng bất kỳ ai, kể cả trong mạng nội bộ.

---

## 🟢 Layer 7: Observability & Monitoring (Giám Sát)
*Đôi mắt của hệ thống.*

1.  **The Three Pillars:**
    *   **Logs:** Ghi lại sự kiện (ELK Stack, Fluentd).
    *   **Metrics:** Số liệu đo lường (Prometheus, Grafana).
    *   **Tracing:** Theo dõi request qua nhiều service (Jaeger, Zipkin).
2.  **Reliability Engineering (SRE):**
    *   **SLO / SLA / SLI:** Các chỉ số cam kết chất lượng dịch vụ.
    *   **Alerting:** Cảnh báo khi có sự cố (PagerDuty).
    *   **Chaos Engineering:** Chủ động gây lỗi để test sức chịu đựng (Chaos Monkey).

---

> **Lời khuyên:** Đừng cố học hết cùng lúc. Hãy bắt đầu từ **Layer 1 & 2** (Core), sau đó mở rộng ra các lớp ngoài khi hệ thống của bạn lớn lên.

## ✅ Apply it!
- [ ] Chọn 1 dự án cá nhân hoặc hệ thống hiện tại → map vào 7 layer, đánh dấu layer yếu nhất.
- [ ] Viết sơ đồ kiến trúc high-level (diagram) và highlight những pattern đang dùng (cache, load balancer, CQRS…).
- [ ] Đặt mục tiêu 2 tuần học cho layer yếu nhất (ví dụ Distributed Systems) và log lại tài liệu/POC đã thực hiện.
- [ ] Tạo bảng Glossary cá nhân: mỗi thuật ngữ phải có ví dụ thực tế trong dự án.
- [ ] Cài dashboard observability (Grafana, ELK) cho ít nhất 1 service quan trọng.
