---
title: "Particle Systems"
description: "So sánh Shuriken vs VFX Graph, tối ưu và workflow."
tags:
  - graphics
  - particles
  - unity
updated: 2026-03-11
---

# 💥 Particle Systems

## 1) Shuriken vs VFX Graph
- **Shuriken**: legacy particle system, chạy CPU + simple vertex shader.
  - Ưu: nhẹ, dễ dùng cho UI, mobile, simple FX.
  - Hạn chế: khó xử lý lượng lớn (>100k particles), ít tùy biến compute.
- **VFX Graph**: GPU-based, node graph, support millions particles + Lit output.
  - Ưu: GPU simulation, event system, mesh output, attribute map.
  - Hạn chế: yêu cầu SRP (URP/HDRP) + compute shader support.

## 2) Workflow
- Shuriken: prefab particle system, reuse module (Emission, Shape, Noise, Collision).
- VFX Graph: tạo VFX asset, set Spawn → Initialize → Update → Output block.
- Expose parameters qua blackboard; link VFX Event (Play/Stop/Custom) từ script.
- Bake flipbook/texture atlas cho effect phức tạp; dùng ShaderGraph (VFX master) cho material.

## 3) Optimization
- Use GPU instancing (VFX Graph default). Với Shuriken: limit particle count, use `Mesh` vs `Billboard` tùy case.
- LOD: dùng `ParticleSystemRenderer.renderMode = ParticleSystemRenderMode.Mesh` cho close-up, bất sang billboard xa.
- Culling: VFX Graph hỗ trợ frustum/auto culling. Shuriken: disable emission khi off-screen.
- Pooling: Shuriken modules scale emission theo distance/time, reuse via `ParticleSystem` pooling.
- Texture: 8-bit/lit vs unlit; pack alpha, reduce overdraw.

## 4) Tooling & Debug
- `VFX Graph > Compile` check warnings; `Window > Analysis > GPU Profiler` xem GPU time.
- Use Visual Effect Controller (Preview) để iterate.
- Shuriken: `Particle Effect` window preview, stat overlay “Total Particles”.
- Capture reference effect (video) để match timing/color.

## 5) Scripting
- Shuriken: `ParticleSystem.Emit`, `ParticleSystem.Pause/Play`. Custom data via `GetParticles/SetParticles`.
- VFX Graph: `VisualEffect.SetFloat/Vector/Texture`, `SendEvent("OnHit")`.
- Events: camera shake, spawn decal sau khi effect end.

## ✅ Apply it
- [ ] Chọn pipeline (Shuriken vs VFX Graph) theo platform & effect complexity.
- [ ] Chuẩn hóa texture atlas, flipbook, shader (lit/unlit) cho team VFX.
- [ ] Tối ưu particle count, overdraw, culling, pooling.
- [ ] Scripting hook (events) để sync gameplay → effect.
- [ ] Benchmark GPU/CPU cost trước khi ship.