---
title: "Art Direction Techniques"
description: "Stylization, NPR (non-photorealistic), lighting & material trick."
tags:
  - graphics
  - art-direction
  - unity
updated: 2026-03-11
---

# 🎨 Art Direction Techniques

## 1) Stylization Pillars
- Định nghĩa visual pillars: shape language, color palette, material response.
- Moodboard → Style guide (value hierarchy, line weight, texture density).
- Blockout lighting + material early (graybox) để lock vibe.

## 2) Non-Photorealistic Rendering (NPR)
- **Toon shading**: ramp texture (Lighting → Sample ramp), outline pass (screen-space sobel hoặc inverted hull).
- **Posterization/Quantization**: hạn chế số level màu → painterly look.
- **Halftone/Sketch**: overlay pattern theo world/UV space.
- Kết hợp `Custom Render Passes` để inject outline, depth-step fog.

## 3) Material Tricks
- Triplanar hoặc gradient mapping để blend color theo height.
- Rim light highlight silhouette.
- Use matcaps để fake reflection (mobile-friendly).
- Dùng detail map tile nhỏ cho surface cohesion.

## 4) Lighting
- Key/Fill/Rim triad; color contrast warm key vs cool fill.
- Use baked GI + AO map để giữ style consistent.
- Volumetric fog tinted theo palette.
- LUT tonemapping align color script.

## 5) Tools & Process
- Style bible: Figma/Miro board + 3D swatch scene.
- Shader Graph templates: toon master, rim, gradient.
- Check-in: art review board, compare screenshot vs concept.
- Automation: screenshot bot capture daily build, auto-compare histogram.

## 6) Collaboration
- Tech Art + Concept + Lighting sync weekly.
- Document per-scene override (fog color, LUT, post-processing).
- Provide `ArtDirectionSettings` ScriptableObject: palette, ramp textures, outline thickness.

## ✅ Apply it
- [ ] Xác định pillars (shape, color, material) + style bible.
- [ ] Thiết lập shader/toon/outline pipeline consistent.
- [ ] Tạo ScriptableObject/scene template cho lighting + post-processing.
- [ ] Review screenshot vs concept theo cadence (daily/weekly).
- [ ] Iterate với tech art để đảm bảo performance/compatibility.