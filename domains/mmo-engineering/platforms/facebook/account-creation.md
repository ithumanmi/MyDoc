# 👤 Facebook Account Creation Playbook

## 1. Prereq & Environment
- Residential/4G proxy, pin IP với profile (xem network module).
- Anti-detect browser profile (MultiLogin, AdsPower) với timezone/IP đồng bộ.
- Email domain chuẩn bị: Gmail/Warm domain, có backup alias.

## 2. Steps
1. **Email verify:**
   - Tạo email (hoặc mua aged) → enable recovery options.
   - Login email từ cùng proxy trước khi tạo FB.
2. **Signup flow:**
   - Dùng mobile UA (Android) hoặc web.
   - Profile info thật (tên, DOB hợp lý), tránh copy/paste.
3. **Profile setup:**
   - Upload avatar nhẹ (<500KB), điền bio, add 5-10 friends (nếu có nguồn).
   - Join 2-3 groups, like pages.
4. **Rút gọn automation:**
   - Playwright/Puppeteer max 2 actions/phút, random delay.

## 3. Hygiene
- Device matrix: ghi lại device ID, browser fingerprint.
- Log IP, time của mỗi phiên tạo.

## 4. Checklist
- [ ] Email verified, recovery ok.
- [ ] Proxy + timezone khớp location.
- [ ] Đã hoàn thành avatar/bio.
- [ ] Lưu cookie + token vào vault.