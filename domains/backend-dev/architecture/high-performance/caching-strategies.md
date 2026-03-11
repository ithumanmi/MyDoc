---
title: "Caching Strategies"
description: "Multi-layer caching, invalidation patterns, cache stampede prevention."
tags:
  - backend
  - performance
  - caching
updated: 2026-03-11
---

# 🧊 Caching Strategies (L2-L3)

## 1. Multi-layer caching
- **Client-side:** HTTP cache headers (`Cache-Control`, `ETag`).
- **CDN/Edge:** CloudFront, Cloudflare.
- **Reverse proxy:** Nginx, Varnish.
- **Application cache:** Redis, Memcached.
- **DB buffer pool:** InnoDB buffer pool, Postgres shared buffers.

## 2. Caching patterns
- **Cache Aside (Lazy):** App check cache → miss → query DB → set cache.
- **Write-through:** write cache + DB đồng thời.
- **Write-back (write-behind):** ghi cache trước, sync DB sau.
- **Read-through:** cache tự fetch từ DB (library hỗ trợ).

### TTL Strategy
- TTL động theo type dữ liệu (hot vs cold).
- Stagger invalidate để tránh thundering herd.

## 3. Invalidation challenges
- **Manual bust:** API invalidate by key/pattern.
- **Event-driven invalidation:** publish event khi record update.
- **Versioned key:** `user:123:v5` tránh stale.

## 4. Cache stampede prevention
- **Mutex/locking:** chỉ 1 request rebuild cache.
- **Early refresh:** refresh key trước khi hết hạn (refresh-ahead).
- **Randomized TTL:** tránh nhiều key hết hạn cùng lúc.
- **Request coalescing:** share result giữa các request.

## 5. Monitoring cache
- Hit ratio, eviction rate, latency.
- Keyspace size, memory usage.
- Alerts khi hit ratio < target.

## ✅ Apply it
- [ ] Map hiện trạng cache layers (client → CDN → app → DB).
- [ ] Chọn strategy (cache aside vs write-through) cho endpoint chủ lực.
- [ ] Implement mutex cache rebuild để tránh stampede.
- [ ] Thiết lập dashboard hit/miss, eviction.
- [ ] Viết playbook invalidation (manual + automated).

## 🔗 Cross-reference
- [connection-pooling.md](./connection-pooling.md) – caching phối hợp pooling.
- [scaling-strategy.md](../scaling-strategy.md) – khi nào scale vs cache.
- [profiling-optimization.md](./profiling-optimization.md) – đo trước/sau cache.