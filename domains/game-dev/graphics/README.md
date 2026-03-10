---
title: "Graphics & Tech Art Module"
description: "Shader, render pipeline và workflow Technical Artist cho Unity."
tags:
  - graphics
  - shaders
  - unity
updated: 2026-03-11
---

# 🌈 Graphics & Tech Art Module

| File | Nội dung | Khi nào dùng |
| --- | --- | --- |
| [shader-programming.md](./shader-programming.md) | Nền tảng HLSL/Shader Graph + tips VFX | Bước vào con đường Technical Artist |
| [trig-shaders.md](./trig-shaders.md) | Water/Fire effect dùng lượng giác | Làm effect tùy biến high-fidelity |
| [render-pipelines.md](./render-pipelines.md) | So sánh URP vs HDRP, cấu hình pipeline | Quyết định pipeline cho dự án mobile/console |

**Playbook:**
1. Chọn pipeline (URP/HDRP) → khóa spec.
2. Dùng `shader-programming.md` để chuẩn hóa naming + LUT.
3. Lặp effect theo checklist trong `trig-shaders.md`, log FPS trong [metrics](../metrics/unity-impact-metrics.md).

> Phối hợp với [Unity Deep Dive / VFX & Lighting](../unity-deep-dive/vfx-lighting-mastery.md) để đồng bộ lighting + shader.