# 🌍 Geolocation Spoofing & Consistency

## 1. Why It Matters
- Platform kiểm tra IP, timezone, locale, GPS (mobile) để phát hiện bất thường.
- Phải đồng bộ các signal để tránh flag.

## 2. IP-based Geo
- Residential/4G proxy cung cấp location theo ISP.
- Use `ipapi`, `maxmind` để biết city/country → sync profile info.

## 3. Timezone & Locale
- Browser automation: set `Intl.DateTimeFormat().resolvedOptions().timeZone` via anti-detect profile.
- OS level: change system timezone (Windows `tzutil /s "SE Asia Standard Time"`).
- Language headers (`Accept-Language`, `navigator.language`).

## 4. GPS / Mobile Spoofing
- Android: sử dụng `adb shell settings put secure mock_location 1` + app fake GPS.
- Send NMEA data to emulate movement.
- Ensure GPS coordinate khớp với IP city.

## 5. Device Parameters
- Wi-Fi SSID JSON, Bluetooth devices list (Chrome navigator) → generate consistent template.
- Hardware clock vs network time: sync NTP vùng đó.

## 6. Detection Signals
- IP ở VN nhưng timezone US → flag.
- GPS di chuyển >500km trong vài phút → suspicious.
- Payment info region mismatch.

## 7. Checklist
- [ ] IP geo, timezone, locale đồng bộ.
- [ ] Mobile mock location script align với ISP region.
- [ ] Log coordinate/IP per session để audit.