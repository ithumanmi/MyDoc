---
title: "PCG Algorithms Deep Dive"
description: "Thuật toán cụ thể cho dungeon, map, spawn: BSP, drunkard walk, Poisson Disk, Marching Squares/Cubes, mission graph."
tags:
  - pcg
  - unity
updated: 2026-03-11
---

# 🧮 PCG Algorithms Deep Dive

> [← Back to Procedural Generation Module](./README.md)

Mục tiêu: cung cấp thuật toán cụ thể để thêm nội dung sinh ngẫu nhiên có kiểm soát, tránh cảm giác lặp.

## 1) BSP Dungeon (Binary Space Partitioning)
**Ý tưởng:** chia không gian thành các phòng rồi nối bằng corridor.

- Chia ngẫu nhiên theo chiều ngang/dọc đến kích thước tối thiểu.
- Đặt phòng (room) trong mỗi node lá, random offset để không quá đều.
- Nối các phòng theo cây BSP bằng corridor (L-shaped hoặc straight + offset).
- Thêm rule: minimum corridor width, cửa đặt ở vị trí an toàn (không sát góc phòng).

### Checklist BSP
- [ ] Kích thước phòng trong khoảng min/max hợp lý.
- [ ] Không có corridor width = 1 nếu game cần combat rộng.
- [ ] Seed cố định để debug layout.

## 2) Drunkard Walk (Random Walk Cave)
**Ý tưởng:** một “người say” đi ngẫu nhiên để khắc (carve) hang.

- Bắt đầu từ tâm map; mỗi bước chọn hướng ngẫu nhiên và mở ô.
- Giới hạn số bước hoặc tỉ lệ ô mở (fill ratio) để dừng.
- Có thể thêm bias (ưu tiên đi xuống hoặc về tâm) để giữ map kết nối.

### Checklist Drunkard Walk
- [ ] Kiểm tra connectivity (Flood Fill) sau khi sinh map.
- [ ] Giới hạn bước để không carve quá mỏng tường.
- [ ] Seed hóa để tái hiện bug.

## 3) Poisson Disk Sampling (Spawn/Scatter)
**Ý tưởng:** đặt vật thể với khoảng cách tối thiểu, phân bố “tự nhiên” nhưng không chồng.

- Đầu vào: bán kính tối thiểu r, vùng spawn (rect/mesh).
- Dùng **Bridson’s algorithm**: grid phụ trợ để kiểm tra lân cận O(1).
- Ứng dụng: cây/đá/loot spawn, vị trí enemy camp.

### Checklist Poisson
- [ ] Chọn r theo kích thước model + buffer tránh overlap animation.
- [ ] Dùng cùng seed cho client/server nếu cần đồng bộ.
- [ ] Clamp số điểm tối đa để tránh loop vô hạn khi r quá lớn.

## 4) Marching Squares / Marching Cubes (Terrain & Caves)
**Ý tưởng:** chuyển field giá trị (density/noise) thành mesh biên.

- **Marching Squares (2D):** 16 cấu hình ô; dùng cho biên dạng hang 2D, contour map.
- **Marching Cubes (3D):** 256 cấu hình; dùng cho voxel terrain (Minecraft-like), cave 3D.
- Kết hợp smooth normals + LOD để tối ưu.

### Checklist Marching
- [ ] Clamp field để tránh mesh bị hở (holes) do precision.
- [ ] Tạo LOD giảm polygon xa camera.
- [ ] Bật collision cook async nếu cập nhật runtime.

## 5) Mission Graph / Quest Graph
**Ý tưởng:** sinh chuỗi nhiệm vụ có ràng buộc.

- Dùng DAG với node nhiệm vụ, cạnh là điều kiện unlock.
- Thuật toán topological shuffle: trộn thứ tự nhưng vẫn tôn trọng phụ thuộc.
- Gán tag (combat/puzzle/travel) để đảm bảo nhịp pacing đa dạng.

### Checklist Mission Graph
- [ ] Không có chu trình (cycle) trong DAG.
- [ ] Phân bố loại nhiệm vụ xen kẽ (không dồn combat liên tục).
- [ ] Seed để tái lập progression khi cần debug.

## 6) Apply It
1) Chọn thể loại: dungeon? overworld? spawn?
2) Chọn thuật toán chính: BSP/Drunkard cho dungeon; Poisson cho spawn; Marching cho terrain.
3) Seed hóa toàn bộ pipeline để debug và tái hiện.
4) Thêm step validate (connectivity, overlap, min corridor width) trước khi build final map.
5) Đo FPS/CPU khi generate (Editor + device); tối ưu bằng job/burst nếu cần.

## 🔗 Cross-reference
- [procedural-generation.md](./procedural-generation.md): Noise, WFC, L-Systems.
- [../metrics/unity-impact-metrics.md](../metrics/unity-impact-metrics.md): Đo hiệu năng khi sinh runtime.