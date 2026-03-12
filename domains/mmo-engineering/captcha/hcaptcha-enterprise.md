# 🛡️ hCaptcha Enterprise Flow

## 1. Architecture
- Enterprise sites sử dụng `pass` token + backend risk engine.
- Client script: `https://hcaptcha.com/1/api.js` với custom params (`rqdata`, `sitekey`).
- Khi hoàn thành challenge, client gửi `h-captcha-response` + `pass` tới backend.

## 2. Token Validation
1. Backend gọi `https://hcaptcha.com/siteverify` với secret.
2. Response chứa `success`, `hostname`, `credit` (captcha solved), optional `score`.
3. Enterprise có thể enable remote attestation → bind token với IP/user agent.

## 3. Enterprise Features
- **Adaptive challenges:** tăng độ khó dựa trên behavior.
- **Bot management API:** cho phép gửi thêm context (`user_id`, `behavior_id`).
- **Webhooks:** notify fail/pass events.

## 4. Bypass Strategies
- **Token brokering:** dùng solving service có worker human.
- **Headless automation:** chạy Playwright với stealth + fingerprint align (canvas, audio, fonts).
- **`rqdata` forging:** trong một số site, `rqdata` là payload mã hóa định nghĩa challenge; nếu capture + replay có thể reuse challenge (hiếm).
- **Session tying:** ensure cookie + storage sync giữa automation steps để token hợp lệ.

## 5. Operational Tips
- Rotate proxy + profile theo site policy.
- Log `credit` để estimate chi phí captcha.
- Khi gặp Enterprise fallback (hard challenge) → trigger manual solve queue.

## 6. Checklist
- [ ] Backend verify `hostname` khớp domain.
- [ ] Log `pass` token + timestamp để debug fail.
- [ ] Có fallback solving service.