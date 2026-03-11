---
title: "Concurrency Models"
description: "Thread pool, async IO, goroutines, virtual threads cho backend hiệu năng cao."
tags:
  - backend
  - performance
  - concurrency
updated: 2026-03-11
---

# 🧵 Concurrency Models (L2-L3)

## 1. Thread-based + Thread Pool
- **Thread per request**: đơn giản nhưng tốn RAM (stack ~1MB/thread). C10K problem.
- **Thread pool**: giới hạn số thread, tái sử dụng. Config size theo CPU core + workload.
- **Blocking I/O**: thread chờ response → cần nhiều thread hơn.

### Best practice
- Luôn dùng pool (Executors, .NET ThreadPool).
- Monitor queue length để scale pool hợp lý.
- Dùng `CompletableFuture/Task` khi có nhiều I/O.

## 2. Event Loop / Async I/O
- **Single-threaded loop** xử lý I/O non-blocking (Node.js, Netty, Python asyncio).
- **Callback/Promise/Future** để xử lý khi I/O xong.
- **Backpressure**: khi event loop quá tải, cần queue limit.

### Pattern
- Split CPU-heavy work vào worker pool để tránh block loop.
- Kết hợp `await`/`async` để code readable.

## 3. Goroutines (Go) & Green Threads
- **Goroutine**: stack nhỏ (~2KB), runtime schedule M:N.
- **Channel**: giao tiếp lock-free.
- **Go scheduler** dùng worker thread (GOMAXPROCS).

### Apply it
- Tuned `GOMAXPROCS` theo CPU core.
- Dùng `context.Context` để cancel goroutine.

## 4. Virtual Threads (Java 21 / Project Loom)
- **Virtual Thread**: lightweight thread managed by JVM, mount/dismount trên OS thread.
- Cho phép viết code kiểu blocking nhưng vẫn scale hàng chục nghìn request.
- Tương thích với API blocking hiện tại → migrate ít vất vả.

### Ưu/nhược
- ✅ Giảm nhu cầu async phức tạp.
- ⚠️ Cần Java 21+, framework hỗ trợ (Spring Boot 3.2+, Helidon, Micronaut).

## 5. Chọn mô hình nào?
| Scenario | Gợi ý |
| --- | --- |
| API CRUD đơn giản, synchronous | Thread pool | 
| High I/O, nhiều external call | Event loop hoặc virtual thread |
| CPU-bound jobs, concurrency mass | Goroutines hoặc thread pool với work stealing |

## ✅ Apply it
- [ ] Đo thread count, context switch, event loop latency hiện tại.
- [ ] Thử implement endpoint bằng async framework (Netty/FastAPI async) và đo throughput.
- [ ] Với Java: enable virtual threads (`Executors.newVirtualThreadPerTaskExecutor`) cho một service, benchmark.
- [ ] Với Go: profile goroutine leak bằng `pprof goroutine`.

## 🔗 Cross-reference
- [connection-pooling.md](./connection-pooling.md) – pooling kết hợp concurrency.
- [monitoring-observability](../../monitoring-observability.md) – metric concurrency.
- [profiling-optimization.md](./profiling-optimization.md) – phát hiện bottleneck CPU vs IO.