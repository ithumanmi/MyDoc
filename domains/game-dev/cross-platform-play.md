---
title: "Cross-Platform Play"
description: "Account linking, progression sync, platform parity considerations."
tags:
  - game-dev
  - multiplayer
updated: 2026-03-11
---

# 🔄 Cross-Platform Play & Progression

## 1) Account Linking
- Identity provider trung tâm (Epic Account, Ubisoft Connect, custom).
- Flow: console login -> link code -> backend maps platform ID ↔ master ID.
- Handle compliance: PSN/Xbox policy không chia sẻ dữ liệu bạn bè.

## 2) Progression Sync
- Cloud save service: authoritative profile (level, inventory).
- Conflict resolution: last-write-wins vs merge logic (currency, quest state).
- Offline mode: cache + sync queue khi có mạng.

## 3) Commerce & Platform Rules
- Cosmetic bán chéo platform? Cấu trúc SKU mapping.
- Revenue share tracking theo store.
- Sony cross-play tax (historical) → theo dõi ratio spend.

## 4) Platform Parity
- Input fairness: aim assist cho controller vs KBM, matchmaking pools.
- Feature parity: chat, DLC availability, seasonal content.
- Certification: mỗi platform release phải pass TRC/TCR/XR.

## 5) Tech Stack
- Backend: identity service, inventory, cloud save.
- Realtime: cross-platform party/matchmaking (PlayFab, Epic Online Services, custom).
- Social: friend list bridging hoặc in-game ID.

## ✅ Apply it
- [ ] Chọn identity strategy (own vs Epic/PlayFab).
- [ ] Thiết kế data model cho progression unified.
- [ ] Build cloud save conflict resolver + telemetry.
- [ ] Align với policy platform (Sony/Xbox/Nintendo/Steam/iOS/Android).