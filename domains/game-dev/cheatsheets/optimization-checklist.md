---
title: "Game Optimization Checklist"
description: "One-pager kiểm tra performance cho build Unity/Unreal."
tags:
  - optimization
  - cheatsheet
updated: 2026-03-11
---

# 🚀 Game Optimization Checklist

## CPU
- [ ] Profile `CPU Usage` (Unity) / Unreal Insights.
- [ ] Batch similar systems (Job System/DOTS, multithread).
- [ ] Object Pool thay vì Instantiate/Destroy.
- [ ] Giảm `Update()` rỗng; dùng event hoặc co-routine.

## GPU
- [ ] Check draw calls, use SRP Batcher/Instancing.
- [ ] LOD + Occlusion Culling bật trên mesh lớn.
- [ ] Texture compression đúng platform (ASTC/ETC2/BC7).
- [ ] Post-processing tối ưu: tắt effect không cần.

## Memory
- [ ] Addressables/AssetBundle cho asset lớn.
- [ ] Check GC Alloc mỗi frame < ~1KB (mobile).
- [ ] Pool string builder/logging.
- [ ] Unload unused assets khi chuyển scene.

## I/O & Build Size
- [ ] Streaming audio/video, giảm seek time.
- [ ] Crunch/ASTC texture, remove unused locale.
- [ ] Stripping engine code (IL2CPP, Managed Stripping Level).

## Platform Specific
- Mobile: limit overdraw, heat budget, battery profiling.
- Console: TRC perf metrics, async compute.
- PC: scalable quality preset.

## Workflow
- [ ] Thiết lập perf budget (CPU/GPU ms) theo target platform.
- [ ] Thêm automated perf test vào CI.
- [ ] Telemetry in-game (FPS, memory, spikes) gửi về backend.