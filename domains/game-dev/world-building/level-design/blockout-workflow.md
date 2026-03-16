---
title: "Blockout Workflow"
description: "Graybox → review → art pass; metrics, lighting tạm, performance, collaboration."
tags:
  - level-design
  - blockout
  - game-dev
updated: 2026-03-11
---

# 🧱 Blockout Workflow

## 1) Goals
- Kiểm chứng flow, pacing, metrics sớm bằng greybox; sửa nhanh trước art.
- Giữ readability và performance trong suốt pipeline.

## 2) Metrics & Greybox
- Dùng metric kit: chiều cao nhân vật, độ rộng hành lang, bậc thang, jump/climb tiêu chuẩn.
- Greybox bằng primitive/kit modular; đánh dấu surface loại traversal (climb/slide/vault).
- Camera pass sớm: kiểm tra FOV, near clip, va chạm camera.

## 3) Lighting/Proxy
- Dùng lighting tạm để dẫn hướng (key/fill/rim tối giản); đừng để tối quá gây hiểu sai flow.
- Color-code khu vực (nhịp/nhánh) để review dễ; gỡ dần khi art pass.

## 4) Review & Iterate
- Internal playtest: kiểm tra flow, pacing, combat space (cover, sightline, spawn).
- Metrics check: jump gap, headroom, cửa; tránh “art fix” che vấn đề thiết kế.
- Telemetry sớm: path/heatmap, death, time-per-room nếu có tool.

## 5) Art Pass Handoff
- Giao package: layout final, metrics, landmark vị trí, lighting ý định, material intent.
- Lock phần đã duyệt; thay đổi lớn cần quay lại blockout review.
- Performance budget: tri/LOD plan, lightmap/lighting plan, reflection probe placement.

## 6) Collaboration
- Checklists: gì đã khóa (metrics, pathing), gì còn thử nghiệm.
- Naming: đặt tên room/chunk nhất quán (L1_Atrium, L1_ServiceHall_A).
- Source control: scene/chunk tách; tránh conflict bằng phân mảnh scene/room.

## ✅ Apply it
- [ ] Dùng metric kit + greybox với dấu traversal rõ ràng.
- [ ] Pass camera + lighting tạm để dẫn hướng.
- [ ] Playtest nội bộ, đo flow/pacing, sửa trước art.
- [ ] Handoff art: landmark, lighting intent, budget perf/LOD.
- [ ] Quản lý scene/chunk, naming, checklist lock/unlock để tránh conflict.