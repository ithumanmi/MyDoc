# 🧠 reCAPTCHA v3 Internals

## 1. Score Model
- reCAPTCHA v3 không hiển thị challenge, trả về score `0.0 - 1.0`.
- Signal chính: interaction pattern (mouse, scroll), navigation timing, history cookie, IP reputation.
- Score threshold phổ biến: 0.5 (Google default), một số dịch vụ nâng lên 0.7.

## 2. Token Lifecycle
1. Client tải script `https://www.google.com/recaptcha/api.js?render=site_key`.
2. JS gọi `grecaptcha.execute(site_key, {action: 'login'})`.
3. reCAPTCHA gửi fingerprint + action lên Google.
4. Server trả token `r=<JWT>` có TTL ~2 phút.
5. Backend verify qua `https://www.google.com/recaptcha/api/siteverify` với secret.

## 3. Best Practices (Bypass)
- **High score farming:** reuse aged Google account cookies, simulate human dwell time trước khi gọi `execute`.
- **Action spoofing:** action name khớp flow thực tế (`signup`, `checkout`). Action mismatch làm giảm score.
- **IP/Fingerprint hygiene:** dùng residential proxy sạch + browser profile ít noise.
- **Score feedback:** backend log score trả về để điều chỉnh threshold.

## 4. Attack Surface
- Token reuse trong TTL (nếu backend không bind IP/user agent).
- Emulator environment detection (WebGL, audio) → cần patch fingerprint.
- Challenge escalation: nếu score thấp, site có thể fallback sang v2 checkbox → chuẩn bị solver.

## 5. Integration Notes
- Khi dùng automation, inject `grecaptcha.enterprise.execute` qua DOM, hoặc intercept XHR để thay token.
- Build middleware để rotate profile nếu score < 0.3.

## 6. Checklist
- [ ] Backend log `score`, `action`, `hostname` từ siteverify.
- [ ] Token binding với session/IP để tránh reuse.
- [ ] Monitor score distribution theo proxy/profile.