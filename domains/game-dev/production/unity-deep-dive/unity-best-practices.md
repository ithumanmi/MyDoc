---
title: "Unity Best Practices"
description: "Quy chuẩn coding, asset, scene và build để tránh technical debt trong dự án Unity."
tags:
  - unity
  - best-practices
updated: 2026-03-11
---

# ✅ Unity Best Practices Checklist

> Dùng checklist này ở đầu sprint để đảm bảo team bám quy chuẩn, tránh nợ kỹ thuật và rò rỉ hiệu năng.

## 1. Coding Standards
- **SOLID + ScriptableObject Architecture**: config data tách khỏi logic.
- **Event Channel thay vì `FindObjectOfType`**: dùng `ScriptableObject` event để broadcast.
- **Avoid Update Hell**: gom logic theo system (Input, Movement, Combat) và tick bằng manager.
- **Dependency Injection (Zenject/Extenject)**: tránh singleton cứng, dễ test.
- **Naming & Folder**: `Scripts/Systems`, `Scripts/Features`, `Scripts/Runtime`/`Editor` rõ ràng.

## 2. Asset & Scene Hygiene
- **No giant scene**: chia scene theo additive (Environment, Gameplay, UI) + Bootstrap.
- **Addressables**: mọi asset runtime phải đi qua Addressables profile, có group staging/prod.
- **Texture budget**: <2K cho mobile, dựng atlas; dùng Sprite Atlas cho UI.
- **Prefab Variant**: base prefab + variant cho skin khác, tránh duplication.
- **Lightmap & Reflection Probe** đặt tên rõ ràng, commit metadata đầy đủ.

## 3. Performance Safeguards
- **Profiler Marker bắt buộc** cho hệ thống quan trọng.
- **GC Alloc target < 1KB/frame**: review script nào allocate trong Update/LateUpdate.
- **Object Pooling** cho VFX/Projectile/UI popups.
- **Quality Settings**: document preset (Low/Medium/High) → mapping hardware.
- **Build validation**: script check shader variant count, texture size trước khi build.

## 4. Workflow & Collaboration
- **Git LFS cho .png/.fbx/.wav**, .gitignore chuẩn (không commit Library, Temp).
- **Scene GUID locking**: dùng UnityYAMLMerge hoặc tool merge scene để tránh conflict.
- **Code Review Template**: checklist logic, null ref, performance, architecture.
- **PlayMode/Editor Tests**: ít nhất smoke test cho hệ thống core.
- **Documentation**: mỗi feature folder có README với flow chart, dependency.

## 5. Build & Release
- **Build script** (`BuildPipeline.BuildPlayer`) chạy CI, auto bump version.
- **Symbol upload** cho crash analytics (Backtrace, Unity Cloud Diagnostics).
- **Changelog** ghi rõ tác động FPS/memory.
- **Feature flag / Remote Config** để rollback nhanh.
- **Telemetry**: log scene load time, FPS, error vào [Unity Impact Metrics](../metrics/unity-impact-metrics.md).

## 6. Checklist trước merge
- [ ] Code follow naming + folder convention.
- [ ] Không còn `Debug.Log` spam trong build.
- [ ] Asset reference qua Addressables khi cần hotfix.
- [ ] Performance capture đính kèm PR nếu thay đổi hệ thống nặng.
- [ ] README/Notion cập nhật nếu flow thay đổi.

## 7. Liên kết hữu ích
- [Unity Clean Code & SOLID](./unity-clean-code-solid.md)
- [Architecture Patterns](./architecture-patterns.md)
- [Optimization Techniques](./optimization-techniques.md)
- [Profiler Dev Build Mastery](./profiler-dev-build-mastery.md)