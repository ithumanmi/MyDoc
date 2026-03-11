---
title: "Shader Math Cheatsheet"
description: "One-pager công thức toán phổ biến cho shader/VFX."
tags:
  - shaders
  - math
  - cheatsheet
updated: 2026-03-11
---

# ✨ Shader Math Cheatsheet

## Trig Basics
- `sin(x)` / `cos(x)` dùng cho wave, offset UV.
- Phase shift: `sin(x + φ)`.
- Amplitude: `A * sin(x)`.
- Frequency: `sin(2πfx)` (f = cycles).

## UV Distortion
- Scrolling UV: `float2 uv2 = uv + float2(speedX, speedY) * _Time.y;`
- Polar coords: `float angle = atan2(uv.y, uv.x); float radius = length(uv);`
- Tiling/offset: `frac(uv * tiling + offset);`

## Noise & Masks
- Use `dot(uv, float2(12.9898,78.233))` + frac to seed.
- `smoothstep(edge0, edge1, x)` để tạo mask mềm.

## Fresnel & Rim Light
- `float fresnel = pow(1 - saturate(dot(N, V)), power);`
- Multiply với color để tạo highlight.

## Normal Tricks
- Reconstruct binormal: `float3 B = cross(N, T) * T.w;`
- Blend normals: use `BlendNormal` function hoặc renormalize.

## Color Ops
- HDR bloom boost: `pow(color, float3(1/2.2)) * intensity` (gamma correction).
- Desaturate: `dot(color, float3(0.299, 0.587, 0.114));`

## Optimization Notes
- Precompute constant (2π).
- Avoid branching → dùng `lerp`.
- Pack data vào half precision khi có thể.