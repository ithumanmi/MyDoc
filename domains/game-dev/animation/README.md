---
title: "Animation (Game Dev)"
description: "Animator state machine, blend trees, root motion vs in-place, runtime rigging, facial animation."
tags:
  - animation
  - unity
  - game-dev
updated: 2026-03-11
---

# 🎞️ Animation (Unity-focused)

## Modules
- [Animator State Machine](./animator-state-machine.md)
- [Blend Trees](./blend-trees.md)
- [Root Motion vs In-Place](./root-motion-vs-in-place.md)
- [Animation Rigging](./animation-rigging.md)
- [Facial Animation](./facial-animation.md)

## Checklist nhanh
- [ ] Rõ ràng layer/sub-state machine; tách locomotion/combat/hit-react.
- [ ] Blend tree 1D/2D cho locomotion; param debounced, normalized.
- [ ] Chọn root motion hay in-place theo gameplay/netcode; sync tốc độ.
- [ ] Runtime rigging: aim/IK/2-bone cho vũ khí/camera; order đúng.
- [ ] Facial: blend shapes/lip sync; emotion library; test trên device mục tiêu.