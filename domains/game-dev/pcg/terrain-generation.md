---
title: "Terrain Generation"
description: "Heightmap, erosion, biome layering cho thế giới mở."
tags:
  - pcg
  - terrain
  - unity
updated: 2026-03-11
---

# 🏞️ Terrain Generation

## 1) Heightmap Basics
- Heightmap = texture grayscale (0–1). Dùng noise (Perlin, Simplex) + ridge noise.
- Multi-octave + domain warp cho chi tiết.
- Mask biomes theo noise (heat + moisture) → blend height profile.
- Lưu heightmap raw (float array) để feed vào mesh/terrain system.

## 2) Erosion Models
- **Thermal erosion:** slope vượt angle → vật liệu chảy xuống. Thực hiện iteration update height.
- **Hydraulic erosion:** mô phỏng nước chảy mang sediment.
  - Raindrop: thả giọt nước, update velocity, sediment capacity, deposit khi chậm.
  - River: trace flow map theo gradient, accumulate water, carve channel.
- Erosion giúp terrain tự nhiên (river/valley). Tốn CPU → nên precompute hoặc GPU compute.

## 3) Biome Layering
- Input maps: height, temperature, moisture.
- Phân zone (snow, desert, forest) dựa threshold.
- Blend terrain splat/texture per biome (Unity Terrain: SplatMap). Sử dụng noise để soften border.
- Spawn vegetation/lake/props theo biome rules.

## 4) Chunking & Streaming
- Chia thế giới thành chunk (256x256) -> generate lazily khi camera gần.
- Sử dụng seed + chunk coordinate (x,z) để deterministic.
- Cache heightmap + mesh; unload khi xa.
- Burst/Jobs hoặc compute shader để generate chunk parallel.

## 5) Unity Implementation Tips
- Unity Terrain API: `TerrainData.SetHeights`, `SetAlphamaps` cho texture.
- Custom mesh: build grid mesh, sample heightmap array.
- GPU-based: compute shader cho noise + erosion, copy result vào RenderTexture → Texture2D.
- Editor tool: create ScriptableObject profile (seed, octave, erosion iterations) để share giữa designer.

## ✅ Apply it
- [ ] Generate heightmap base (noise + domain warp) theo seed.
- [ ] Áp erosion (thermal/hydraulic) nếu cần realism.
- [ ] Map biome (height/temp/moisture) và blend texture/props tương ứng.
- [ ] Chunk-based streaming; deterministic theo chunk coordinate.
- [ ] Tối ưu bằng Jobs/compute shader, expose profile cho designer.