---
title: "Layout Principles"
description: "Flow, pacing, landmarks, readability, metrics cho level design."
tags:
  - level-design
  - layout
updated: 2026-03-11
---

# 🧭 Layout Principles

## 1) Goals
- Flow rõ ràng: player dễ định hướng (main path) nhưng có nhánh phụ.
- Pacing mượt: xen kẽ căng thẳng/giãn nhịp; đặt checkpoint hợp lý.
- Đọc hiểu nhanh: landmarks, silhouette, lighting dẫn hướng; tránh lạc.

## 2) Landmarks & Readability
- Landmarks: kiến trúc/địa hình nổi bật thấy từ xa; duy trì sightline từ hub/corner key.
- Breadcrumbs: ánh sáng, màu, particle, âm thanh chỉ hướng; UI diegetic (biển báo, đèn).
- Visual language: cửa đỏ = khóa, xanh = đã mở; surface texture khác biệt cho traversal (climb/slide).

## 3) Flow & Navigation
- Main path vs side path: side path ngắn, thưởng rõ; vòng lại main path để không lạc.
- Loop & shortcut: mở khóa đường tắt sau khi hoàn thành đoạn; giảm backtracking mệt mỏi.
- Choke point & arena: định nghĩa không gian giao chiến; tránh nhiều lối ra gây AI/perf quá tải.

## 4) Pacing & Encounter Placement
- Nhịp: Combat → Rest → Puzzle/Exploration; xen kẽ để tránh fatigue.
- Checkpoint/save: đặt sau đoạn khó hoặc trước boss; giữ nhịp nhưng không quá dày.
- Enemy spawn/AI: tránh spawn sau lưng nếu không có telegraph; telegraph audio/visual.

## 5) Metrics & Scale
- Player metrics: tốc độ chạy/nhảy/leo; chiều cao step, độ rộng cửa; thiết lập từ đầu để blockout đúng.
- Jump/climb: margin an toàn (nhảy 5m → design 4.2-4.5m).
- Camera: FOV, near clip; tránh corridor quá hẹp gây clip.

### Ví dụ metric (tham khảo, điều chỉnh theo game của bạn)
- Chiều cao nhân vật: ~1.8m; mắt ~1.6m.
- Cửa tiêu chuẩn: rộng 1.2–1.6m; cao 2.2–2.5m (tránh clip camera/FOV hẹp).
- Hành lang: tối thiểu 2–3m cho camera vai; 3.5–4.5m cho camera xa/party.
- Bậc/step: ≤0.3m để leo mượt; ramp 15–30°.
- Nhảy (example action game): max 5m khoảng cách phẳng → design 4.2–4.5m an toàn; max độ cao 2m → design 1.6–1.8m.
- Ledge grab: bề rộng ledge ≥0.3m; khoảng trống đầu ≥0.5m.

## 6) Guidance & UX
- Signposting: ánh sáng khác màu hướng về mục tiêu; NPC hoặc VO hint; minimap/compass nếu game cần.
- Diegetic cues: smoke, âm thanh máy móc, radio chatter, pipeline ánh sáng.
- Accessibility: high contrast path, subtitles/hints, không ép phản xạ quá nhanh ở early game.

## ✅ Apply it
- [ ] Thiết lập metric (tốc độ, jump height, door width) và dùng nhất quán khi blockout.
- [ ] Đặt landmarks nhìn thấy từ xa và breadcrumbs rõ ràng.
- [ ] Pacing xen kẽ combat/rest/puzzle; checkpoint sau đoạn khó.
- [ ] Side path ngắn, có thưởng, quay lại main path; mở shortcut giảm backtracking.
- [ ] Kiểm tra camera clip/FOV, signposting bằng lighting/màu/âm thanh.