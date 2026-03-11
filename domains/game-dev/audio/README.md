---
title: "Game Audio (Unity)"
description: "Sound design fundamentals, adaptive audio, middleware, spatial 3D, và tối ưu hóa cho Unity."
tags:
  - audio
  - sound-design
  - unity
  - game-dev
updated: 2026-03-11
---

# 🎧 Game Audio (Unity)

> Mục tiêu: xây soundscape rõ ràng, nhạc/FX thích ứng trạng thái game, spatial hợp lý, và tối ưu CPU/memory/bandwidth trên Unity.

## Modules
- [Sound Design Fundamentals](./sound-design-fundamentals.md)
- [Adaptive Audio](./adaptive-audio.md)
- [Audio Middleware](./audio-middleware.md)
- [Spatial Audio 3D](./spatial-audio-3d.md)
- [Audio Optimization](./audio-optimization.md)

## Checklist nhanh
- [ ] Thiết lập bus/mixer structure, loudness target, và stem export.
- [ ] Chọn pipeline: Unity Audio vs middleware (FMOD/Wwise) và tích hợp Input/Events.
- [ ] Triển khai adaptive music/SFX theo state/RTPC/parameters.
- [ ] Spatial: HRTF, occlusion/obstruction, reverb zone; kiểm tra downmix stereo.
- [ ] Tối ưu: streaming, compression per platform, voice limit, CPU budget profiling.

## 🔗 Cross-reference
- [Localization](../localization/README.md) — VO, per-locale bank.
- [Mobile Optimization](../mobile-optimization/README.md) — battery/thermal ảnh hưởng audio CPU.
- [Console Development](../console-dev/README.md) — TRC/TCR audio, party chat/presence.