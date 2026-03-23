---
title: "Procedural World Pipeline 03 - Authoring Tools & Version Control"
description: "Thiết kế tool nội bộ & quy trình version để artist ↔ engineer đồng bộ khi build world procedurally."
tags:
  - pcg
  - tooling
  - pipeline
  - version-control
updated: 2026-03-23
---

# 🛠️ Pipeline 03: Authoring Tools & Version Control

> **Goal:** Tạo bộ tool editor + pipeline quản lý dữ liệu procedural (heightmap, biome, spawn rule) để artist/level designer có thể iterate nhanh mà không phá build.
> **Deliverables:** Editor tooling spec, data schema, CI validation script, branching policy.
> **Success Criteria:**
> - Import/export heightmap/splatmap chỉ 1 click.
> - Dữ liệu procedural có schema rõ, detect conflict.
> - CI báo lỗi khi chunk thiếu asset hoặc navmesh mismatch.
> - Team biết cách review & retro per change với template.

## 1. Tool Stack Overview

| Layer | Tool | Purpose |
|-------|------|---------|
| DCC | World Machine / Gaea / Houdini | Authoring heightmap & masks |
| Unity Editor Tools | Custom windows, Terrain Tools | Import/export, preview |
| Data Storage | ScriptableObject + JSON sidecar | Store meta, version |
| Version Control | Git + LFS / Plastic SCM | Manage large binaries |
| CI | GitHub Actions / Jenkins | Validate chunk integrity |

## 2. Editor Tooling

### 2.1 Terrain Importer Window
- Fields: source heightmap, scale, smoothing, auto material mapping.
- Buttons: `Import Heightmap`, `Reapply Splatmaps`, `Bake NavMesh`.
- Logs result to console + write metadata `.terrainmeta`.

### 2.2 Biome Painter
- Custom inspector for painting biome ID onto grid.
- Save as texture (biome map) or data array.
- Integration with PlayMode preview: show overlay for designers, toggle heatmap.

### 2.3 Spawn Rule Editor
- Node-based UI (GraphView) where designer defines spawn conditions (biome, slope, proximity).
- Export JSON consumed by runtime spawn system.

### 2.4 Pipeline Dashboard
- EditorWindow summarizing chunk status: `Chunk ID`, last edit, navmesh status, warnings.
- Buttons to open chunk scene/subscene quickly.

## 3. Data Schema & Storage

### 3.1 Chunk descriptor example
```yaml
chunk_id: x0_y1
heightmap: Assets/_External/TerrainExports/height_x0_y1.r16
biome_map: Assets/_External/TerrainExports/biome_x0_y1.png
navmesh_asset: Assets/World/NavMesh/x0_y1.asset
spawn_profile: Assets/World/Spawn/x0_y1.asset
version: 12
last_editor: linh.nguyen
notes: "Added cliff + wolf den"
```

### 3.2 Validation rules
- All referenced files exist.
- Heightmap resolution matches terrain settings.
- NavMesh asset updated after last height change.
- Spawn profile references valid prefab IDs.

## 4. Version Control Strategy

### 4.1 Git + LFS best practices
- Track `.r16/.tif/.png` heavy files with LFS.
- Keep `Assets/_External` for raw data (excluded from build but tracked).
- Use `.gitattributes` to enforce LFS.

### 4.2 Branch workflow
- `main`: stable world.
- `world/dev`: staging for world updates.
- Per feature: `world/chunk-x0y1-cliff-pass`.

### 4.3 Plastic SCM alternative
- Branch per chunk, merge tool handles binary.
- Use Plastic file locks when editing same chunk.

### 4.4 Change review
- Mandatory PR template capturing: objective, affected chunks, metrics (tri count, navmesh size), screenshot link.
- Reviewers: 1 engineer + 1 artist.

## 5. CI Validation

### 5.1 Sample pipeline
1. `Checkout` repo with LFS.
2. Run `validate_chunks.py` (custom script) to ensure schema & file existence.
3. Use Unity CLI to run automated PlayMode test `ChunkLoadsAllScenes` (headless) to ensure no missing asset.
4. Upload report (HTML) to artifact, fail build if errors.

### 5.2 Metrics logging
- Script extracts navmesh size, chunk memory estimate → push to telemetry sheet.
- Compare vs budget, flag > +15%.

## 6. Retro & Documentation
- Mỗi lần update world major: viết retro theo [Retro Template](../../production/metrics/retro-template.md).
- Checklist retro: performance delta, bug count, art direction feedback, pipeline issue.
- Maintain `/docs/world-building-log.md` ghi timeline thay đổi.

## 7. Collaboration Tips
- Weekly sync artist ↔ engineer: review pipeline issues.
- Provide example chunk as reference for new hires.
- Keep tool video walkthrough (Loom) để onboarding nhanh.

## 🔗 Links
- [Pipeline 01 - Heightfield to Unity](./pipeline-01-heightfield-to-unity.md)
- [Pipeline 02 - Runtime Streaming](./pipeline-02-runtime-streaming.md)