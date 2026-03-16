---
title: "RenderDoc Capture Workflow"
description: "Setup RenderDoc cho Unity, capture frame, phân tích draw call."
tags:
  - graphics
  - renderdoc
  - debugging
updated: 2026-03-11
---

# 🕵️ RenderDoc Capture Workflow

## 1) Setup
- Install RenderDoc 1.27+ (support DX12/Vulkan).
- Unity Editor: bật `RenderDoc` integration (Window > Analysis > RenderDoc) hoặc chạy standalone RenderDoc và attach.
- Build: enable development build + script debugging.

## 2) Capture từ Editor
1. Mở `Window > Analysis > RenderDoc Capture`.
2. Chọn target camera/game view.
3. Nhấn `Capture` khi sự kiện cần phân tích diễn ra.
4. RenderDoc mở file `.rdc`.

## 3) CLI Capture (Standalone)

```bash
renderdoccmd capture --exe "Builds/MyGame.exe" --working-dir "Builds" --capture-file "captures/frame1.rdc" --trigger-delay 5
```

- Tự động launch build, chờ 5s, capture frame.
- Use trong CI để capture frame golden sample.

## 4) Phân Tích
- `Pipeline State`: xem shader stage, resource binding.
- `Texture Viewer`: inspect render target (color/depth).
- `Events`: filter theo draw call, search shader name.
- `Statistics`: check draw call count, tri count.
- `Mesh Viewer`: debug vertex data, normals.

## 5) Export Snapshot
- `File > Export > Capture Log` để share.
- Screenshot: `Texture Viewer > Save` để lưu PNG depth/color.
- CLI: `renderdoccmd export capture.rdc --texture 0 --output color.png`.

## ✅ Apply it
- [ ] Thiết lập RenderDoc integration và test capture.
- [ ] Capture frame cho các scene quan trọng (boss fight, city hub).
- [ ] Annotate events (bookmark) để note pass/feature.
- [ ] Export log/screenshot chia sẻ trong review.
- [ ] Lưu trữ capture vào repo (folder `captures/`) hoặc cloud.