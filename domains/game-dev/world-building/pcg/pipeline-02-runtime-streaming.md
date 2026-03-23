---
title: "Procedural World Pipeline 02 - Runtime Streaming & Biome Blending"
description: "Thiết kế hệ thống load/unload địa hình, biome blending runtime bằng DOTS/Jobs và Addressables."
tags:
  - pcg
  - world-building
  - streaming
  - dots
updated: 2026-03-23
---

# 🌍 Pipeline 02: Runtime Streaming & Biome Blending

> **Goal:** Đưa địa hình khổng lồ chạy mượt runtime thông qua chunk streaming, biome blending động và hệ thống job-friendly.
> **Deliverables:** Chunking spec, streaming controller, biome data schema, performance budget.
> **Success Criteria:**
> - Streaming không gây hitch >16ms.
> - Biome rules modular, designer chỉnh được qua config.
> - Memory footprint giữ < target (ví dụ 2GB trên PC, 500MB mobile).
> - Profiling capture (Player & Editor) trước/ sau tối ưu.

## 1. Architecture Overview

```
Player Position -> Streaming Controller
Streaming Controller -> Chunk Loader (Addressables / Asset Bundle)
Chunk Data -> Terrain Mesh + Props + AI spawn points
Biome Controller -> Material/FX swap + weather state
DOTS/Jobs -> Async prepare data (height, vegetation)
```

## 2. Chunking Strategy

### 2.1 Grid vs Hex
- **Grid (square):** đơn giản, dễ align navmesh.
- **Hex:** mượt cho world spherical, phức tạp hơn.

### 2.2 Chunk size guidelines
- PC/Console: 256m - 512m.
- Mobile: 128m.
- `Preload radius = active chunk + 1 ring`.

### 2.3 Data layout
- Each chunk folder:
```
Chunks/
  chunk_x0_y0/
    terrain.asset
    navmesh.asset
    props.json
    biome.meta
```
- Use ScriptableObject `ChunkDescriptor` referencing Addressables labels.

## 3. Streaming Controller

### 3.1 Player tracking
- Use Cinemachine camera or player transform as origin.
- Compute chunk index via `floor(position / chunkSize)`.

### 3.2 Load/unload flow
```
OnPositionChanged -> Determine NeededChunks
Compare with LoadedChunks -> call LoadChunk / UnloadChunk
LoadChunk => Addressables.LoadAssetAsync -> instantiate pool
```
- Use coroutine/Task with `AwaitLoad` to avoid blocking.
- Prefetch next ring when player speed cao.

### 3.3 DOTS/Jobs integration
- Convert chunk data to Entities via Baker.
- Use Subscenes per chunk (Entities Graphics + Baking settings).
- For Hybrid approach: use `SceneSection` streaming API.

## 4. Biome System

### 4.1 Data schema
```json
{
  "biome_id": "tundra",
  "height_range": [600, 2000],
  "temperature": [0, 10],
  "materials": {
    "terrain_layer": "TL_Snow",
    "foliage_prefab": "Pine_LowPoly"
  },
  "fx": {
    "weather_profile": "SnowStorm",
    "ambient_audio": "Wind_Howl"
  }
}
```
- Store as ScriptableObject or JSON to allow designers editing.

### 4.2 Blend logic
- Evaluate rule per chunk or per vertex.
- Use compute shader to blend splatmaps runtime (height/slope mask).
- Weather manager transitions (Timeline/Playable) based on active biome.

### 4.3 Wildlife/AI ties
- Each biome maps to spawn tables.
- Example: `biome.tundra → spawn (wolf 0.3, deer 0.7)`.
- Use Weighted Random + density cap per chunk.

## 5. Performance Budget & Telemetry

### 5.1 Budget table (example PC target)
| System | Budget |
|--------|--------|
| Streaming CPU | < 4 ms/frame |
| GPU terrain draw | < 5 ms |
| Memory per chunk | < 150 MB |
| Loading hitch | < 16 ms |

### 5.2 Instrumentation
- Use Unity Profiler `Timeline` capture per travel scenario.
- Log custom metric `chunk_load_time`, `biome_swap_ms` into [Unity Impact Metrics](../production/metrics/unity-impact-metrics.md).
- Setup runtime HUD showing loaded chunks count, memory, active biome.

## 6. Testing Checklist
- [ ] Test moving at max speed (vehicle, teleport) → ensure prefetch adequate.
- [ ] Simulate low bandwidth (Console devkit network throttling) → verify fallback.
- [ ] Stress test spawn density per biome.
- [ ] Verify detach/cleanup when player logout (no orphan GameObjects).
- [ ] Automated PlayMode test to warp player across grid -> check no crash/leak.

## 7. Next Steps
- Hook up Pipeline 03 tooling to allow artists reimport chunk data.
- Integrate streaming metrics into build validation pipeline.
- Extend to multiplayer (server authoritative streaming hints).