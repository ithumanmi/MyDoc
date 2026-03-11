---
title: "VR/AR/XR"
description: "Interaction patterns, motion sickness mitigation, performance budgets for immersive platforms."
tags:
  - vr
  - ar
  - xr
  - unity
updated: 2026-03-11
---

# 🥽 VR/AR/XR

> Mục tiêu: thiết kế tương tác tự nhiên, giảm say VR, và giữ hiệu năng ổn định theo ngân sách platform (Quest/PSVR/PCVR/Mobile AR).

## 1) Interaction Patterns
- **Locomotion:** teleport, dash, arm-swinger; tránh smooth locomotion nếu chưa có comfort mode.
- **Hands/Controllers:** raycast UI + direct grab; affordance rõ ràng; haptic nhẹ khi hover/grab.
- **AR Anchors:** plane detection, anchor persistence; occlusion với depth API.

## 2) Motion Sickness Mitigation
- FOV vignetting khi tăng tốc/quay; snap turn 30-45°.
- Giữ horizon ổn định; tránh camera animation cưỡng bức.
- Low latency tracking (<20ms motion-to-photon); 6DoF ổn định.

## 3) Performance Budgets
- **FPS targets:** 90/120 Hz (VR), 60 Hz (AR mobile). Frame drop gây say.
- **GPU/CPU budgets:** cap draw calls, hạn chế overdraw; light/shadow đơn giản; bake khi có thể.
- **Foveated rendering / Fixed foveated** cho mobile VR; LOD agresive.

## 4) UX & Safety
- Guardian/boundary: cảnh báo khi gần giới hạn không gian.
- Height calibration & recenter; accessibility cho người ngồi/đứng.
- UI diegetic gần tầm với; text lớn, contrast cao.

## 5) Testing & QA
- Test trên thiết bị thật: tracking drift, passthrough, room lighting.
- Comfort rating (user survey); session length trước khi mệt.
- Heat/thermals cho mobile AR/VR; throttle scenario.

## ✅ Apply it
- [ ] Cung cấp 2 mode locomotion (teleport + dash) + snap turn.
- [ ] Thêm vignette khi tăng tốc/quay; giữ horizon ổn định.
- [ ] Kiểm soát draw call/overdraw, bật foveated rendering nếu hỗ trợ.
- [ ] UI diegetic với text lớn, trong tầm với 0.5-1m.
- [ ] Test thực tế: motion-to-photon, comfort survey, nhiệt độ thiết bị.

## 🔗 Cross-reference
- [Performance Optimization](../unity-deep-dive/optimization-techniques.md) – ngân sách CPU/GPU cho mobile/VR.
- [UX/UI for Games](../ux-ui/README.md) – UI diegetic và comfort.