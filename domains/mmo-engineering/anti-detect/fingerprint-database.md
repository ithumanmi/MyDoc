# 🗃️ Fingerprint Database

## 1. Purpose
- Lưu trữ fingerprint thực tế (Desktop/Mobile) để inject vào anti-detect profile.

## 2. Data Schema
```json
{
  "id": "persona_us_win10_001",
  "device": {
    "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
    "platform": "Win32",
    "languages": ["en-US", "vi-VN"],
    "screen": { "width": 1920, "height": 1080, "dpr": 1.25 }
  },
  "hardware": {
    "cpu": "Intel(R) Core(TM) i5-10400",
    "gpu": "NVIDIA GeForce GTX 1650",
    "audio": "Realtek High Definition Audio"
  },
  "fonts": ["Arial", "Calibri", "Times New Roman"],
  "extensions": ["uBlock", "LastPass"],
  "webgl": {
    "vendor": "Google Inc.",
    "renderer": "ANGLE (NVIDIA GeForce GTX 1650)",
    "extensions": ["OES_texture_float", "WEBGL_debug_renderer_info"]
  },
  "canvas_hash": "1c5f...",
  "audio_hash": "bc39...",
  "sensors": { "has_accelerometer": false },
  "updated_at": "2026-03-01"
}
```

## 3. Collection Pipeline
1. Dùng agent trên thiết bị thật → thu thập fingerprint (script JS + native info).
2. Validate uniqueness (AmiUnique score < 0.3 collision).
3. Encrypt & store trong Vault/S3 (AES-256, access audit).

## 4. Persona Tagging
- `persona_mobile_sea_01`: Android/Chrome, fonts Noto Sans SEA.
- `persona_desktop_us_02`: Win10 + gaming GPU.
- `persona_mac_eu_01`: MacBook Air M1.

## 5. Usage
- Anti-detect browser đọc JSON → map field sang hook.
- Rotation logic: assign fingerprint based on campaign (ads, ecom, crypto).
- Track usage count để tránh reuse quá nhiều.

## 6. Maintenance
- Refresh dataset mỗi 3 tháng.
- Retire fingerprint nếu score trùng >5% (theo log detection).
- Versioning (git/LFS) + changelog.

## 7. Checklist
- [ ] Fingerprint thu từ thiết bị thật (không synthetic).
- [ ] Encrypt at rest và audit access.
- [ ] Mapping script được test với browser automation.