---
title: "Localization"
description: "Font systems, LTR/RTL, VO pipeline, locale assets and testing."
tags:
  - localization
  - l10n
  - game-dev
updated: 2026-03-11
---

# 🌐 Localization

> **Goal:** Hỗ trợ đa ngôn ngữ (text + VO), LTR/RTL, font fallback và pipeline asset ổn định cho mobile/console/PC.
> **Deliverables:** String table & font fallback matrix, VO production checklist, asset bundle per locale, pseudo-localization QA report.
> **Success Criteria:** 0 string missing/hardcode, text expansion <40% vẫn không vỡ UI, VO sync lệch <100ms, hotfix locale <50MB.
> **Focus Areas:** Font systems (SDF/fallback), RTL mirroring/lip-sync, VO pipeline, localization QA automation.

## 1) Text & Fonts
- Font fallback chain; subset font để giảm dung lượng.
- RTL support: layout mirroring, bidi, punctuation; số vẫn LTR.
- String table + smart formatting; tránh hardcode line-break.
- Font system: tách font UI và font body; kiểm tra hinting/render trên console/mobile; ưu tiên vector icon thay vì embedded text trong texture.
- Script coverage: CJK, Arabic, Cyrillic, Thai/Vietnamese (dấu) → cần fallback đúng weight; test kerning/ligature.
- LTR/RTL mixed: hỗ trợ bidi marker, xử lý punctuation và số không đảo lộn; mirror layout trừ media controls nếu platform guideline yêu cầu.
- **Font atlas strategy:** SDF atlas riêng cho nhóm Latin/extended, CJK bitmap/SDF dynamic (multi-atlas) để tránh vượt texture limit. Lập bảng “locale → atlas set” và preload hot locale, lazy load khác.
- **Dynamic font download:** cho mobile/consoles, cung cấp CDN font pack khi người chơi chọn locale hiếm để tránh phình build. Cache local và verify checksum.
- **Unity:** dùng TextMeshPro với fallback asset; auto-size off để tránh layout thrash, dùng SDF atlas per locale; bật Right-to-Left support package cho TMP nếu cần. ScriptableObject giữ map locale → font asset. Sử dụng Addressables để tải font/atlas theo locale.

## 2) VO & Audio
- VO pipeline: script → record → file naming/metadata → loudness match.
- Lip-sync/phoneme (nếu cần); timing subtitle theo VO.
- Per-locale audio bank; stream dài, preload ngắn.
- File naming convention: locale + character + line ID; giữ version để diff/patch.
- Loudness: match LUFS theo platform spec; limiter để tránh clip khi downmix.
- Access needs: bật subtitle, SDH (sound description) nếu yêu cầu; sync với VO timing.
- **VO pipeline detail:**
  1. Lock script + placeholder ID.
  2. Casting per locale, ghi âm theo batch (studio local).
  3. QC: pronunciation, emotion, timing.
  4. Integrate: convert format (WAV 48k/16b), normalize -16 LUFS console/-23 broadcast nếu yêu cầu, add metadata (speaker, emotion, context).
- **Localization kit:** chuẩn hóa handoff template (spreadsheet + audio naming) để nhà thầu hiểu. Lưu ý lipsync (Rhubarb phoneme) → update Timeline clip.
- **Unity:** dùng Addressables/AssetBundle cho audio bank per locale; AudioSource output group vào AudioMixer để level match; preload short SFX, stream dài (AudioClip load type Streaming). Nếu lip-sync, có thể dùng SALSA/Rhubarb hoặc marker trong Timeline.

## 3) Assets & UI
- Locale-aware images/icons (ví dụ văn bản trong texture → dùng sprite sheet per locale).
- Safe area & text expansion 30-40%; truncate rules & wrapping.
- Date/time/number/currency format; plural rules.
- Input method: IME/soft keyboard length; kiểm tra truncation với tên người chơi dài.
- Sorting/collation: tuân thủ locale; search nên normalize (NFC/NFD) để khớp.
- **RTL layout mirroring:** test UI components (navigation drawer, progress bar direction, slider) với Unity UI toolkit/Canvas. Dùng layout group flip + sprite mirroring option.
- **Culturalization:** design review với LQA partner để loại bỏ biểu tượng nhạy cảm, màu sắc cấm kỵ; follow rating board (GRAC, IARC, SAR) guideline.
- Color/culture: tránh icon/biểu tượng nhạy cảm vùng; check rating guideline địa phương.
- **Unity:** bật Localization package (String Tables, Asset Tables); dùng Smart String/Plural. Sprite font/icon theo locale qua Asset Table. Test Canvas Scaler + TMP auto-size boundary để tránh overflow. IME: dùng TMP InputField và test trên mobile/console soft keyboard; normalize (FormD/FormC) khi lưu.

## 4) Build & Testing
- Addressables/asset bundle per locale; hotfix patch nhỏ.
- Pseudo-localization để bắt tràn chữ/biến dạng UI.
- Test RTL device; font fallback trên console/mobile/PC.
- Build matrix: mobile/console/PC với font fallback khác nhau; test rendering (SDF vs bitmap) và mipmap blur trên TV.
- Patch size: split audio/text pack; ưu tiên stream VO để giữ size patch nhỏ.
- Automation: lint string key missing, detect hardcoded text; screenshot diff cho UI regression.
- **VO pipeline testing:** verify lip-sync alignment (±100ms), run audio loudness meter per locale, check subtitle timecode.
- **Localization QA:** create checklist per locale (text expansion, grammar, cultural review). Dùng screenshot bot + OCR để so sánh output vs string table.
- **Unity:** dùng Localization package pseudo-localization (accent/lengthen) để bắt overflow; Addressables groups per locale với Build Script Packed Mode; verify cold-load vs warm-load của Addressables font/atlas. CI: chạy localization lint (missing keys), chụp screenshot automation với Unity Test Framework + Graphics Compositor.

## ✅ Apply it
- [ ] Thiết lập string table + font fallback và pseudo-localization.
- [ ] Mirror layout cho RTL và kiểm tra text expansion 40%.
- [ ] VO pipeline với loudness match + subtitle timing + file naming convention.
- [ ] Bundle/Addressable theo locale; test hotfix.
- [ ] QA: format datetime/number/currency; icon/sprite đúng locale; kiểm tra IME/soft keyboard & sorting.
- [ ] Unity: TextMeshPro fallback asset per locale, Localization package (String/Asset tables), Addressables load font/audio per locale, pseudo-localization pass.

## 🔗 Cross-reference
- [UX/UI for Games](../ux-ui/README.md)
- [Console Development](../console-dev/README.md)