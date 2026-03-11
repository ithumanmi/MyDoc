---
title: "Audio Optimization (Unity)"
description: "Streaming, compression, memory/CPU budget, voice limit, platform tuning cho Unity."
tags:
  - audio
  - optimization
  - unity
updated: 2026-03-11
---

# 🛠️ Audio Optimization (Unity)

## 1) Mục tiêu
- Giữ CPU/Audio thread thấp, tránh voice spike gây drop frame.
- Kiểm soát dung lượng bank/clip, giảm memory peak khi load.
- Đảm bảo chất lượng đủ tốt (music/VO) nhưng tối ưu platform.

## 2) Compression & Import Settings
- Music/VO: Vorbis/ADPCM tùy platform; giữ 48 kHz nếu cần, hoặc 44.1 kHz cho mobile.
- SFX ngắn: PCM/ADPCM để giảm decode cost; preload nếu rất ngắn.
- Force mono cho SFX không cần stereo; keep stereo cho ambience/music.
- Load Type: Streaming cho clip dài; Compressed In Memory nếu vừa phải; Decompress on Load cho SFX rất ngắn.

## 3) Memory & Streaming
- Bank/Addressables: tách theo scene/region/mode; unload khi rời scene.
- Limit concurrent stream: tránh nhiều stream dài cùng lúc; ưu tiên music/ambience.
- Preload critical VO/SFX (UI, combat) vào memory nhỏ; stream ambience/music.

## 4) Voice Management
- Voice cap: đặt max voice; priority per bus (VO > threat SFX > ambience > UI).
- Distance culling: fade-out trước khi cap hit; avoid hard cut.
- One-shot pooling: reuse AudioSource để giảm alloc/GC.

## 5) CPU & DSP
- Giảm effect chain: dùng EQ/LPF/HPF nhẹ; hạn chế convolution reverb runtime (render tail offline nếu được).
- Spatialization: bật binaural chỉ cho cần thiết; UI/2D tắt spatial.
- Update path: tránh tính toán RTPC/parameters mỗi frame, chỉ khi state thay đổi.

## 6) Profiling (Unity)
- Dùng Profiler: Audio module, voice count, Audio thread time, GC alloc.
- Development build: kiểm tra frame time histogram với audio on/off để thấy impact.
- Log peak voice in combat; kiểm tra clip drop/steal sự kiện quan trọng (VO, warning).

## 7) Platform Notes
- Mobile: giảm sample rate (44.1), force mono nhiều SFX, giới hạn stream concurrency; disable reverb nặng.
- Console/PC: giữ chất lượng cao hơn; nhưng vẫn prewarm bank và kiểm tra suspend/resume.
- WebGL: nén mạnh, giới hạn voice và stream; tránh clip dài.

## ✅ Apply it
- [ ] Thiết lập import preset cho SFX/VO/Music (sample rate, stereo/mono, load type).
- [ ] Chia bank/Addressables per scene/region và chiến lược unload.
- [ ] Đặt voice cap + priority + distance culling.
- [ ] Hạn chế effect chain/binaural cho nguồn cần thiết.
- [ ] Profiler: log Audio thread time & peak voice trong combat; kiểm tra stream concurrency.