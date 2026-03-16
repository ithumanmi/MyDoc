---
title: "QA & Testing"
description: "Quy trình QA, test plan, automation cho dự án Unity."
tags:
  - qa
  - testing
  - unity
updated: 2026-03-16
---

# ✅ QA & Testing

| File | Nội dung | Khi nào dùng |
| --- | --- | --- |
| test-plan-template.md | Mẫu test plan + scope | Kickoff QA cycle |
| automation-strategy.md | Playmode/Editor tests, CI setup | Khi thêm kiểm thử tự động |
| regression-checklist.md | Checklist smoke/regression build | Trước mỗi milestone release |

## Workflow gợi ý
1. Xác định scope test → chọn ưu tiên (smoke vs regression vs perf).
2. Thiết lập Playmode/Editor tests + CI (game-ci, GitHub Actions).
3. Capture perf & crash metrics → map với [metrics/README.md](../metrics/README.md).
4. Viết checklist release + phân quyền QA/dev review.

## Cross-links
- [Production / Metrics](../metrics/README.md)
- [Unity Deep Dive / Testing](../unity-deep-dive/README.md)
- [Challenges](../../challenges/README.md) – dùng challenge để tạo test scenario khó.