---
title: "Unity Fundamentals"
description: "Checklist nền tảng Unity: editor workflow, component model, build pipeline."
tags:
  - unity
  - fundamentals
  - game-dev
updated: 2026-03-16
---

# 🎯 Unity Fundamentals Cheat Sheet

> **Purpose:** Tách phần kiến thức nền khỏi README chính để bạn có thể rà soát nhanh trước mỗi sprint hoặc onboarding thành viên mới.

## 🧭 1. Editor & Project Setup
- Install Unity Hub + LTS version (khuyến nghị: 2022 LTS hoặc 2023 LTS tùy requirement).
- Template: 2D/3D tùy dự án → bật URP nếu hướng mobile/console.
- Folder convention:
  - `Assets/_Project`: Scripts/Prefabs/Scenes.
  - `Assets/Art`, `Assets/Audio`, `Assets/Runtime`, `Assets/Editor`.
- Version control:
  - Bắt buộc `.gitignore` chuẩn (không commit `Library`, `Logs`, `Temp`).
  - Dùng `meta` files → bật *Force Text* + *Visible Meta Files*.

## 🧩 2. Component Model Essentials
- `MonoBehaviour` lifecycle: `Awake` (init), `OnEnable`, `Start`, `Update`, `FixedUpdate`, `LateUpdate`, `OnDisable`, `OnDestroy`.
- Input:
  - Legacy Input Manager (simple) vs **Input System 1.5+** (Action Map, Rebinding, device-agnostic).
- Physics:
  - `FixedUpdate` cho force/velocity.
  - `RigidBody` (3D) vs `RigidBody2D` (2D) – đừng mix 2 hệ.
- Scripting patterns:
  - `SerializeField` + `ScriptableObject` cho config.
  - Event Channel hoặc `UnityEvent` để tránh hard reference.
- Prefab workflow:
  - Prefab Variant cho skin/behavior khác.
  - Prefab Stage để edit an toàn.

## 🧰 3. Tooling & Productivity
- Shortcuts quan trọng: `Q/W/E/R` (Move/Rotate/Scale/Rect), `F` focus, `Ctrl/Cmd + D` duplicate, `Ctrl/Cmd + P` Play.
- Custom tooling:
  - `EditorWindow`, `PropertyDrawer`, `MenuItem` để build inspector tool.
  - `Gizmos` + `Handles` hỗ trợ debug scene.
- Profiling nhanh:
  - Stats overlay (FPS, batches).
  - Profiler module: CPU, GPU, Memory, Rendering.

## 📦 4. Build Pipeline Basics
- **Scenes:** add vào *Build Settings* đúng thứ tự.
- **Scripting Backend:** IL2CPP cho release (mobile/console), Mono cho iteration nhanh.
- **Architecture choices:** URP vs HDRP, Addressables cho asset streaming.
- **Platform quirks:**
  - Android: Keystore, texture compression (ASTC/ETC2), IL2CPP ARM64.
  - iOS: Xcode export + provisioning profile.
  - PC/Console: Input remapping, controller icons, compliance checklist.
- **CI/CD:**
  - Unity Cloud Build hoặc custom GitHub Actions (use `game-ci/unity-builder`).
  - Cache `Library` với hash theo Unity version để giảm thời gian build.

## 🧪 5. Quality Checklist (Before Commit)
- [ ] Console không có error/warning lặp lại.
- [ ] Lighting baked/rebaked nếu thay đổi scene.
- [ ] Profiler snapshot: FPS ≥ target, GC Alloc low (<1 KB/frame cho mobile).
- [ ] Addressables/AssetBundle build không fail.
- [ ] Scenes có `Bootstrap` + `Gameplay` + `UI` rõ ràng.
- [ ] `ProjectSettings` backup (Input, Layer, Tag) nếu thay đổi.

## 🔗 Cross-links
- **C# refresher:** [csharp-for-unity.md](./csharp-for-unity.md)
- **Deeper architecture:** [../production/unity-deep-dive/README.md](../production/unity-deep-dive/README.md)
- **Metrics & telemetry:** [../production/metrics/unity-impact-metrics.md](../production/metrics/unity-impact-metrics.md)

> *Tip:* Pin tài liệu này trong Notion/GitHub Wiki để mọi thành viên team đều rà checklist trước khi merge.