---
title: "Procedural vs Handcrafted"
description: "Khi nào dùng procgen, khi nào thủ công; hybrid, công cụ authoring, QA."
tags:
  - level-design
  - procedural
  - handcrafted
updated: 2026-03-11
---

# 🔀 Procedural vs Handcrafted

## 1) Khi nào chọn procgen
- Replayability cao, nội dung lớn (roguelike, dungeon, loot) khó author thủ công.
- Cần biến thiên để thử nghiệm build, meta-progression.
- Đội ngũ nhỏ, cần công cụ sinh nhanh + kiểm soát rule.

## 2) Khi nào chọn thủ công
- Nhịp kể chuyện, set-piece, puzzle cần kiểm soát chính xác.
- Độ khó và pacing cần kịch bản chặt; camera/cutscene phụ thuộc layout cố định.
- Multiplayer competitive cần cân bằng map rõ ràng.

## 3) Hybrid
- Macro thủ công (hub, nhịp chính), micro procgen (room nội thất, loot spawn, enemy group).
- Tile/room library được curate thủ công, procgen chỉ shuffle/combine.
- Hand-placed landmarks để định hướng, procgen cho nhánh phụ.

## 4) Công cụ & Rule
- Grammar/Rule-based: kết hợp tag (combat/rest/puzzle), difficulty band, connectors hợp lệ.
- Metrics: giữ kích thước phòng/hành lang trong giới hạn camera/movement.
- Validation: path length, key-lock consistency, softlock check, dead-end có thưởng.

## 5) QA & Telemetry
- Generator test: sinh hàng loạt, tự động kiểm tra path/connectivity, unreachable spawn.
- Playtest nhiều seed; khóa seed khi debug.
- Telemetry: death heatmap per tile, time-to-exit, pickup rate.

## 6) Content Pipeline
- Build library (tile/room/encounter) với tag; mỗi item có metadata (difficulty, biome, traversal).
- Versioning: thay đổi tile cần QA lại; giữ compatibility với seed cũ nếu có live ops.
- Authoring tool: preview seed, lock/unlock phòng, override loot.

## ✅ Apply it
- [ ] Quyết định phạm vi procgen vs thủ công; điểm neo thủ công (hub/landmark/set-piece).
- [ ] Định nghĩa rule/grammar + metrics; validation tự động softlock/connectivity.
- [ ] Xây thư viện tile/room/encounter có tag/metadata.
- [ ] Playtest nhiều seed + telemetry death/time-to-exit/pickup.
- [ ] Tooling: preview seed, lock tile, override loot cho trường hợp đặc biệt.