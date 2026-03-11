---
title: "Dungeon Generation"
description: "BSP, cellular automata, graph-based mission layouts."
tags:
  - pcg
  - dungeon
  - unity
updated: 2026-03-11
---

# 🏰 Dungeon Generation

## 1) BSP (Binary Space Partitioning)
- Chia vùng hình chữ nhật thành subtree (left/right hoặc top/bottom).
- Cho mỗi leaf tạo room ngẫu nhiên, nối bằng corridor giữa center.
- Parameters: min room size, depth/cut ratio, corridor width.
- Ưu: đảm bảo kết nối, dễ kiểm soát layout rectangular.

### Enhancements
- Add random “skip leaf” để tạo dead-end (loot room).
- Carve additional corridors (cross-link) để giảm linear.
- Decorate walls/floors theo depth level (biome).

## 2) Cellular Automata (CA)
- Grid binary (wall/floor). Seed noise random.
- Rule phổ biến: `if (neighborsWall >= 5) wall else floor`. Iterates 4–6 lần.
- Dùng flood fill để giữ region lớn nhất (remove isolated caves).
- Kết hợp smoothing (closing small holes), and door placement.

## 3) Graph-based / Mission Graph
- Tạo graph (nodes = rooms, edges = connection). Graph obeys mission design (key-lock, boss, puzzles).
- Sau khi graph có, embed lên grid (room templates) theo constraint.
- Use algorithms: random spanning tree + additional edges; layered graph (start → mid → boss).
- Weighted edges = distance difficulty.

## 4) Hybrid Approaches
- BSP cho macro layout + WFC/room templates cho chi tiết.
- CA cho caverns + connect via graph edges (ensures progression).
- Poisson disk để spawn rooms, sau đó Delaunay triangulation + MST cho corridor.

## 5) Unity Implementation Tips
- Represent room prefab + socket (north/east/south/west). Snap theo grid size.
- Use ScriptableObject room definitions: tags (combat, puzzle), size, connectors.
- Use navmesh prefab baking hoặc runtime navmesh build per room.
- Debug overlay: color-coded graph edges, show disconnected components.

## ✅ Apply it
- [ ] Chọn thuật toán chính (BSP, CA, graph) theo thể loại.
- [ ] Tune parameters (room size, neighbor threshold, graph depth) và expose cho designer.
- [ ] Đảm bảo connectivity: flood fill/check graph connected.
- [ ] Mix room prefab theo tag (combat/puzzle), spawn loot/boss theo mission graph.
- [ ] Build navmesh hoặc pathing sau khi generate; log seed để replay.