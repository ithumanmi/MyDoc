---
title: "Connection Pooling"
description: "DB pool, HTTP keep-alive, gRPC multiplexing cho backend hiệu năng cao."
tags:
  - backend
  - performance
  - networking
updated: 2026-03-11
---

# 🌊 Connection Pooling (L2-L3)

## 1. Database Connection Pools
- **Vấn đề:** mở connection DB rất tốn thời gian & resource.
- **Giải pháp:** tái sử dụng connection qua pool (HikariCP, PgBouncer, .NET Connection Pool).

### Config chính
- **Pool size min/max:** = (CPU core * 2) ± workload.
- **Idle timeout:** đóng connection nhàn rỗi lâu.
- **Max lifetime:** recycle connection tránh lỗi mạng.

### Monitoring
- Connection in use vs pool size.
- Wait time khi lấy connection.
- Error rate (timeout, saturation).

## 2. HTTP Keep-Alive & Connection Reuse
- **HTTP/1.1** keep-alive → reuse TCP connection.
- **HTTP/2** multiplex nhiều stream trên 1 connection.
- Client (OkHttp, HttpClient) nên reuse connection.

### Best practice
- Thiết lập max idle per host.
- Tune `MAX_CONCURRENT_STREAMS` cho HTTP/2.

## 3. gRPC Multiplexing
- gRPC dựa trên HTTP/2 → multiplex binary stream.
- Dùng `ConnectionPool`/channel reuse để tránh overhead TLS handshake.
- Limit concurrent stream để tránh head-of-line blocking.

## 4. Queue + Pool interplay
- Worker queue phải phù hợp với pool size (tránh queue dài block).
- Circuit breaker khi pool full.

## ✅ Apply it
- [ ] Audit số connection mở (DB, HTTP) hiện tại.
- [ ] Tune pool size theo throughput target, tránh saturate DB.
- [ ] Enable HTTP/2 + gRPC channel reuse.
- [ ] Setup dashboard pool metric (usage, wait time).
- [ ] Thử POC PgBouncer (transaction pooling) nếu Postgres quá tải.

## 🔗 Cross-reference
- [concurrency-models.md](./concurrency-models.md) – số thread liên quan pool size.
- [caching-strategies.md](./caching-strategies.md) – giảm load DB để pool khỏe.
- [profiling-optimization.md](./profiling-optimization.md) – đo thời gian chờ connection.