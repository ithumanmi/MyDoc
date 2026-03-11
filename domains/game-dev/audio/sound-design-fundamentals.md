---
title: "Sound Design Fundamentals (Unity)"
description: "Foley, mixing, stems, bus/mixer structure, loudness targets cho Unity."
tags:
  - audio
  - sound-design
  - unity
  - foley
updated: 2026-03-11
---

# 🔊 Sound Design Fundamentals (Unity)

## 1) Goals & Targets
- Loudness: target -16 to -20 LUFS integrated cho gameplay; peak -1 dBFS. UI SFX nhẹ hơn -6 dB so với combat SFX.
- Headroom: giữ headroom cho VO/sidechain music khi ducking.
- Staging: phân lớp music/ambience/SFX/VO, tránh masking tần số.

## 2) Bus/Mixer Structure (Unity Audio Mixer)
- Bố trí bus: Master → Music / SFX / VO / UI / Ambience. Thêm sub-bus Combat, Footstep, Weapon, UI.
- Insert: EQ cắt low (<60 Hz) trên VO/UI; HPF/LPF cho occlusion; compressor/limiter nhẹ ở bus.
- Ducking: Sidechain music khi VO hoặc critical SFX; dùng Ducking effect hoặc sidechain compressor.
- Snapshots: Snapshot cho menu/pause (reduce music), combat (boost SFX), stealth (boost ambience subtle).

## 3) Assets & Stems
- Foley: thu đa lớp (close/room), multiple variations (3-5) để tránh lặp; đặt random pitch ±3%. 
- Stems: Music stem tách (rhythm/harmony/melody/percussion) để blend theo trạng thái; export 48 kHz/24-bit trước khi nén.
- Loop hygiene: zero-crossing, tail reverb render-in; seamless loop (đặt loop region đúng sample).

## 4) Implementation (Unity)
- AudioSource pooling: giảm tạo/destroy, gán qua Object Pool. 
- Mixer routing: route tất cả AudioSource vào group tương ứng; tránh bypass mixer.
- Variations: AudioRandomContainer (tự viết) hoặc simple script random clip/volume/pitch.
- Distance & rolloff: dùng Custom Rolloff curve; tránh Linear quá gắt. Spread cho stereo width.

## 5) Testing & QA
- Loudness check: dùng LUFS meter (plugin bên ngoài) trên stem export; trong Unity dùng test tone + limiter headroom.
- Scenes: test trong môi trường yên tĩnh và ồn; kiểm tra clipping trên device thật (mobile/console).
- Localization: VO per locale, kiểm tra clipping/phoneme; map vào mixer VO bus.

## ✅ Apply it
- [ ] Thiết kế bus/mixer + snapshots cho menu/combat/stealth.
- [ ] Thiết lập ducking music khi VO/critical SFX.
- [ ] Random hóa variation/pitch cho Foley/Footstep/Weapon.
- [ ] Chuẩn hóa stem export (48 kHz/24-bit) và loop hygiene.
- [ ] QA loudness (LUFS), clipping device thật, và routing qua mixer.