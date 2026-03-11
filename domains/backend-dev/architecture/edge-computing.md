---
title: "Edge Computing"
description: "Cloudflare Workers, edge caching, geo routing, edge DB."
tags:
  - backend
  - architecture
  - edge
updated: 2026-03-11
---

# 🌍 Edge Computing (2024-2026)

## 1. Edge Runtime
- **Cloudflare Workers / Deno Deploy / Vercel Edge Functions**: chạy JS/Wasm gần người dùng, cold start <5ms.
- **Use cases:** personalization, A/B testing, feature flag, token validation.
- **Limits:** CPU time (10-50ms), memory nhỏ, không có socket dài.

## 2. Edge Caching & Rules
- Multi-layer cache (browser → CDN edge → regional → origin).
- **Cache rules:** cache key by header/cookie, variant theo locale/device.
- **Bypass logic:** authenticated request → bypass hoặc cache fragment.
- **Stale-while-revalidate:** giữ response cũ trong khi fetch mới.

## 3. Geolocation Routing
- **Geo load balancing:** định tuyến user tới region gần (Route53 latency routing, Cloudflare Load Balancer).
- **Geo-based rules:** block country, legal compliance.
- **Edge KV config:** store feature flag theo khu vực.

## 4. Edge Databases
- **Distributed KV:** Cloudflare D1, Workers KV, Fauna, Neon.
- **Eventual consistency**; cân nhắc khi viết nhiều.
- **Pattern:** read local, write fan-out về primary.
- **Edge queue/cron:** Workers Cron Trigger, queue delay <1s.

## ✅ Apply it
- [ ] Audit endpoint nào có latency cao cho user xa → move logic ra edge worker.
- [ ] Thiết lập cache policy (cache key, TTL) + test stale-while-revalidate.
- [ ] Cấu hình geo routing + health check multi-region.
- [ ] PoC edge database (Workers KV + D1) cho metadata/read-heavy.
- [ ] Monitor edge errors, CPU time, subrequest limit.

## 🔗 Cross-reference
- [deployment-guide.md](../deployment-guide.md) – CI/CD đa region.
- [high-performance/caching-strategies.md](./high-performance/caching-strategies.md) – phối hợp cache tầng edge.
- [system-design/realtime-flash-sale-inventory.md](../system-design/realtime-flash-sale-inventory.md) – latency-critical workload.
- [security/zero-trust-architecture.md](./zero-trust-architecture.md) – kết hợp identity proxy ở edge.