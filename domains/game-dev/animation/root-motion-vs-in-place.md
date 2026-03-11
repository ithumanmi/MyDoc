---
title: "Root Motion vs In-Place"
description: "Trade-offs, khi nào dùng, sync tốc độ, netcode."
tags:
  - animation
  - unity
  - root-motion
updated: 2026-03-11
---

# 🏃 Root Motion vs In-Place

## 1) Khi dùng Root Motion
- Animation là nguồn chân thực (melee, cinematic, traversal phức tạp).
- Camera theo sát nhân vật; tránh foot slide; sync với clip chính xác.
- Singleplayer hoặc netcode client-auth/lag-comp phù hợp.

## 2) Khi dùng In-Place
- Gameplay điều khiển bởi code/physics (shooter, MMO); cần phản hồi tức thời.
- Netcode server-auth cần đồng bộ vị trí chính xác; root motion khó reconcile.
- Thay đổi tốc độ linh hoạt (buff/debuff) không cần re-author clip.

## 3) Hybrid
- Traversal đặc biệt (vault/climb) dùng root motion trong montage; locomotion thường in-place.
- Additive root motion cho đòn đặc biệt, còn di chuyển chính do code.

## 4) Sync Tốc Độ
- Root motion: scale clip speed hoặc param speed để match gameplay; tránh scale quá lớn gây méo anim.
- In-place: tính velocity từ input, set Animator param speedNormalized; đảm bảo blend tree khớp tốc độ.
- Foot IK: bật để giảm trượt ở in-place; tắt nếu làm hỏng pose đặc biệt.

## 5) Netcode
- Root motion multiplayer: cần snapshot/rewind hoặc server drive; tránh divergence.
- In-place: server điều khiển velocity; client chỉ là visual; dễ reconcile.
- Montage root motion ngắn: sync trigger từ server; clamp drift bằng warp nhẹ khi kết thúc.

## 6) Debug/Perf
- Check foot sliding: so sánh distance travelled vs intended speed.
- Camera/Collision: root motion có thể xuyên nếu không check; cần raycast/character controller sync.
- Authoring: giữ vận tốc clip tương đồng để tránh blend trượt.

## ✅ Apply it
- [ ] Chọn root motion cho hành vi cinematic/traversal; in-place cho di chuyển gameplay/netcode.
- [ ] Sync tốc độ: scale hợp lý hoặc normalize speed param; foot IK hỗ trợ.
- [ ] Hybrid: montage root motion cho moveset đặc biệt; locomotion in-place.
- [ ] Netcode: server-auth ưu tiên in-place; nếu root motion, cần rewind/warp nhẹ.
- [ ] Debug foot slide và collision xuyên; điều chỉnh clip speed hoặc IK.