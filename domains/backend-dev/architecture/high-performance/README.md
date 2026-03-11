---
title: "High Performance Series"
description: "Overview Level 2-3 cho hiệu năng backend: concurrency, caching, pooling, profiling."
tags:
  - backend
  - performance
updated: 2026-03-11
---

# ⚡ High Performance Series (L2-L3)

> Tách module `high-performance.md` thành series gồm 4 chủ đề chuyên sâu. Dùng README này để định hướng học.

## 📚 Sub-modules
| File | Nội dung chính | Khi nào đọc |
| --- | --- | --- |
| [concurrency-models.md](./concurrency-models.md) | Thread pool, async IO, goroutine, virtual threads | Khi cần xử lý nhiều request đồng thời |
| [caching-strategies.md](./caching-strategies.md) | Multi-layer cache, invalidation, stampede prevention | Khi latency đọc cao, DB quá tải |
| [connection-pooling.md](./connection-pooling.md) | DB pool, HTTP keep-alive, gRPC multiplex | Khi gặp bottleneck connection |
| [profiling-optimization.md](./profiling-optimization.md) | CPU/memory profiling, flame graph, benchmark | Khi cần đo và tối ưu chính xác |

## 🚀 Lộ trình gợi ý
1. **Đo**: xác định bottleneck (CPU, IO, DB) bằng metric hiện tại.
2. **Học module phù hợp** (concurrency/caching/pooling).
3. **Thực hành Apply it** trong từng file.
4. **Profiling liên tục** để xác minh hiệu quả.

## 🔗 Link cũ
- [high-performance.md](../high-performance.md) *(giữ lại như index cũ hoặc redirect)*