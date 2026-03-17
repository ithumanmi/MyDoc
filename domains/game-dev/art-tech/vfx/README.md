---
title: "Art-Tech / VFX"
description: "Hub: VFX Graph, particle, shader recipe, performance."
tags: [vfx, shaders, unity]
updated: 2026-03-17
---

# 💥 Art-Tech / VFX Hub

Tóm tắt: Xây effect đẹp nhưng nhẹ, phối hợp chặt với graphics và audio để tạo cảm xúc và đảm bảo performance.

## Nội dung chính
| File | Nội dung | Khi nào dùng |
| --- | --- | --- |
| [particle-systems.md](./particle-systems.md) | Shuriken vs VFX Graph, batching, budgeting | Thiết kế particle effect & tối ưu draw call |
| [trig-shaders.md](./trig-shaders.md) | Công thức nước/lửa bằng sin/cos, distortion | Tạo effect stylized với shader tùy biến |

## Workflow đề xuất
1) Khóa spec look-dev cùng art direction → palette + motion language.  
2) Prototype trên Shuriken hoặc VFX Graph → log perf trong Profiler.  
3) Tái sử dụng shader function từ [graphics/shader-programming.md](../graphics/shader-programming.md).  
4) Kết hợp cue âm thanh (xem [audio/README.md](../audio/README.md)) để tạo feedback đầy đủ.

## Checklist
- [ ] Mỗi effect có budget rõ (particle count, overdraw, texture size).
- [ ] Test trên target platform (mobile/console) bằng RenderDoc capture.
- [ ] Dùng Addressables cho effect hiếm/đắt đỏ.
- [ ] Viết note handoff cho designer (trigger, timing, cooldown).

## Cross-links
- [Graphics](../graphics/README.md)
- [Unity Deep Dive – VFX & Lighting](../unity-deep-dive/vfx-lighting-mastery.md)
- [Metrics – Unity Impact Metrics](../metrics/unity-impact-metrics.md)