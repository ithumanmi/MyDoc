---
title: "Programming / Animation"
description: "Hub: Animator, blend tree, root-motion vs in-place, runtime rigging, facial."
tags: [animation, unity, game-dev]
updated: 2026-03-17
---

# 🎞️ Programming / Animation Hub

Tóm tắt: Thiết kế hệ animation có cấu trúc (layer/sub-state), blend mượt, quyết định root-motion vs in-place đúng theo gameplay/netcode, và dùng rigging/runtime IK hợp lý.

## Nội dung chính
- [Animator State Machine](./animator-state-machine.md)
- [Blend Trees](./blend-trees.md)
- [Root Motion vs In-Place](./root-motion-vs-in-place.md)
- [Animation Rigging](./animation-rigging.md)
- [Facial Animation](./facial-animation.md)
- [State Machine & Blend Tree Patterns](./state-machine-blend-tree.md)

## Khi nào dùng
- Gameplay cần locomotion/combat/hit-react rõ lớp, tránh spaghetti transition.
- Muốn tối ưu netcode: cân nhắc root-motion vs in-place và sync tốc độ.
- Cần rigging/IK runtime (aim, 2-bone) cho vũ khí/camera hoặc procedural adjustment.
- Nâng chất lượng nhân vật: facial, lip-sync, biểu cảm ổn định trên thiết bị đích.

## Checklist nhanh
- [ ] Layer & sub-state tách locomotion/combat/hit-react; transition có condition rõ.
- [ ] Blend Tree 1D/2D: tham số debounced/normalized; có fallbacks.
- [ ] Chọn root-motion hay in-place phù hợp gameplay/netcode; test drift/sync.
- [ ] Rigging/IK: order đúng, clamp góc quay, kiểm tra performance.
- [ ] Facial: blend shapes/lip-sync, emotion library; test trên target device.