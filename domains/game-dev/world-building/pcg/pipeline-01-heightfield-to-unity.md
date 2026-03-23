---
title: "Procedural World Pipeline 01 - Heightfield to Unity Terrain"
description: "Quy trình dựng địa hình AAA mini từ World Machine/Gaea sang Unity Terrain + lighting + navmesh."
tags:
  - pcg
  - world-building
  - terrain
  - pipeline
updated: 2026-03-23
---

# 🌄 Pipeline 01: Heightfield → Unity Terrain (Offline Authoring)

> **Goal:** Biến concept terrain từ công cụ chuyên dụng thành scene Unity hoàn chỉnh có lighting, splatmap, navmesh và ready cho world-building tiếp theo.
> **Deliverables:** Heightmap 16-bit, mask/splatmaps, Unity Terrain asset, lighting preset, navmesh bake checklist.
> **Success Criteria:**
> - Terrain không bị seam/step, normal hợp lý.
> - Lighting (sun/skybox) giữ đúng mood reference, shadow ổn định.
> - NavMesh bake được, không overflow memory.
> - Asset pipeline versioned được (Git LFS/Plastic).

## 1. Pre-production Checklist

| Step | Tool | Notes |
|------|------|-------|
| Moodboard | PureRef / Figma | Reference ảnh thật + game tương tự |
| Blockout rough terrain | Unity ProBuilder / Grease Pencil | Đặt camera path, focal point, metrics |
| Define biome palette | Notion/Sheet | Chọn 3-4 layer material (rock, grass, sand, cliff) |
| Source DEM (optional) | USGS, Tangram | Nếu muốn realism -> import DEM raw |

## 2. Sculpt & Bake Heightfield

### 2.1 Tool selection
- **World Machine**: node-based, dễ mask.
- **Gaea**: modern UI, erosion presets.
- **Houdini**: procedural, phức tạp hơn.

### 2.2 Workflow
1. **Base Shapes**: tạo macro forms (mountain ridge, valley). Use noise (Perlin/Ridge) + shape node.
2. **Erosion**: talus, flow, thermal để có realism.
3. **Mask output**: slope-based mask (cliff vs meadow) + height mask (snowcaps).
4. **Export**: heightmap 16-bit RAW (4097x4097 typical), splatmap (RGBA), normal map.

**Naming convention**
```
/TerrainExports/
  - height_main_4k_20260323.r16
  - mask_rgba_cliff_grass_snow_sand.png
  - normal_tangent_4k.tif
```

## 3. Unity Terrain Import

### 3.1 Project setup
- Unity 2022 LTS, URP/HDRP.
- Create `Terrain` with matching size (e.g. 2km x 2km). Set height map resolution and terrain height (Y scale).
- Import heightmap via `Terrain > Terrain Settings > Import Raw`. Ensure format matches (Windows byte order, 16 bit).

### 3.2 Material & Splatmap
1. Create Terrain Layer assets: `TL_Grass`, `TL_Rock`, `TL_Snow`, `TL_Sand`.
2. Assign textures (albedo, normal, mask). Use tile settings (Offset/Size).
3. Use Splatmap as control: `Terrain Tools > Paint Texture > Edit Terrain Layers > Import Splatmap`.
4. Blend adjustments: use `Opacity` brush to tweak transition.

### 3.3 Detail Objects
- Grass detail meshes with GPU instancing.
- Trees via `Terrain Trees` (use SpeedTree assets). Enable billboard LOD.

## 4. Lighting & Atmosphere

### 4.1 HDRP/URP setup
- HDRP: use **Physically Based Sky**, volumetric fog.
- URP: use **Sky and Fog Volume**, baked directional light.

### 4.2 Lighting pass
1. Set **Directional Light** angle/time-of-day.
2. Add **Reflection Probes** along path.
3. Post-processing volume: color grading, bloom, depth-of-field to match concept.

### 4.3 Performance guardrails
- Use `Shadow Cascades` (4) for large terrains.
- Enable `Terrain Streaming` if world >4 km.
- Use GPU instancing + LOD group for props.

## 5. Navigation & Gameplay Prep

### 5.1 NavMesh
- Use **NavMesh Components** (com.unity.ai.navigation).
- Split terrain into tiles (e.g. 512m). Bake per tile to avoid memory spikes.
- Exclude steep slopes using area masks (from slope mask).

### 5.2 Physics & Colliders
- Terrain collider auto from Terrain.
- Add mesh colliders for cliffs/rocks inserted manually.

### 5.3 Spawn/Encounter markers
- Place empty GameObjects with naming `SPN_Wolf_01`, `POI_Tower_Entrance`. Use `Gizmos` for readability.
- Export to ScriptableObject for procedural system to reference.

## 6. Version Control & Automation

### 6.1 File governance
- Large binary (heightmaps, splatmaps) tracked via **Git LFS** or **Plastic SCM**.
- Keep `.tif/.r16` outside Unity `Assets/` (e.g. `Assets/_External/`).
- In repo, store only final Terrain asset + materials.

### 6.2 Automation idea
- Create custom editor window `TerrainPipelineImporter` to re-import heightmap & splatmap with one click.
- Store metadata (`.pipeline.json`) describing source file, scale, last import timestamp.

## 7. Handoff Checklist
- [ ] Heightmap & masks archived (versioned).
- [ ] Terrain with layers + detail objects committed.
- [ ] Lighting profiles saved (Volume profiles, skybox asset).
- [ ] NavMesh data baked (asset saved). Document bake settings.
- [ ] Metrics logged: triangle count, draw calls, navmesh size.
- [ ] Screenshots/video for art review.
- [ ] Retro using [Retro Template](../../production/metrics/retro-template.md) with learnings & next steps.

## 🔗 Next Pipelines
- [Pipeline 02 - Runtime Streaming & Biome Blending](./pipeline-02-runtime-streaming.md)
- [Pipeline 03 - Authoring Tools & Version Control](./pipeline-03-tools-pipeline.md)