---
title: "Hades Procedural Encounter"
description: "Room generation, pacing và encounter design trong Hades."
tags:
  - procedural
  - roguelike
  - case-study
updated: 2026-03-11
---

# 🔥 Hades Procedural Case Study

## Room Generation Flow
1. **Biome Graph**: mỗi biome (Tartarus, Asphodel...) có weighted graph định nghĩa loại phòng.
2. **Template Room**: layout được hand-crafted, procedural chỉ chọn biến thể + modifiers.
3. **Encounter Seed**: RNG seed dựa trên run progression → đảm bảo fairness.

## Encounter Design
- **Pacing tiers**: mix 3 loại encounter (Swarm, Elite, Trap) theo pattern `easy → spike → reward`.
- **Boons & Rewards**: drop table phụ thuộc vào lựa chọn player (god favor system).
- **Heat modifiers** (Pact of Punishment) inject rule variation nhưng reuse cùng room template.

## Systems Notes
- Content được định nghĩa bằng **data-driven JSON** + editor tool internal.
- AI spawn script sử dụng **scheduler** để delay wave, giữ readability.
- Telemetry theo dõi death cause → điều chỉnh spawn pattern/buff enemy.

## Lessons
1. **Hybrid hand-crafted + procedural** tạo cảm giác bespoke nhưng vẫn replayable.
2. **Data-driven graph** giúp designer chỉnh pacing mà không cần coder.
3. **Telemetry loop** cực quan trọng để tune roguelike fairness.