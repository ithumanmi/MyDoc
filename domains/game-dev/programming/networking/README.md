---
title: "Programming / Networking"
description: "Hub: Game networking & server – kiến trúc, netcode, vận hành."
tags: [networking, game-server, netcode]
updated: 2026-03-17
---

# 🌐 Programming / Networking Hub

Tóm tắt: Tổ chức netcode client/server, chiến lược lag/cheat, và vận hành backend game.

## Nội dung chính
- [game-server-guide.md](./game-server-guide.md) — Kiến trúc server, session, auth, storage, scaling.
- [senior-game-server-roadmap.md](./senior-game-server-roadmap.md) — Lộ trình kỹ sư server: từ foundation đến vận hành quy mô lớn.

## Khi nào dùng
- Xây dựng hoặc refactor server-side cho game (authoritative, phòng/room, matchmaking).
- Thiết kế netcode: lag compensation, prediction/rollback, chống cheat cơ bản.
- Chuẩn bị roadmap/skill-map cho kỹ sư server hoặc tư vấn kiến trúc.

## Checklist nhanh
- [ ] Chọn mô hình authoritative/lockstep/rollback phù hợp thể loại.
- [ ] Thiết kế đồng bộ trạng thái: snapshot & delta, hoặc command stream.
- [ ] Lag/cheat: prediction + reconciliation, server validation, rate limiting.
- [ ] Observability: log/metrics/tracing; test packet loss/latency.