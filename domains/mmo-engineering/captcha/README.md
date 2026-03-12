# 🧩 Captcha & Challenge Solving Hub

Tập hợp chiến lược xử lý captcha nâng cao cho MMO tools.

## Files
- [recaptcha-v3-internals.md](./recaptcha-v3-internals.md) – Score model, token lifecycle, best practices.
- [hcaptcha-enterprise.md](./hcaptcha-enterprise.md) – Token validation, enterprise features, bypass chiến lược.
- [cloudflare-turnstile.md](./cloudflare-turnstile.md) – Phân tích tín hiệu, flow verify, hướng dẫn harvest token.
- [self-hosted-ocr.md](./self-hosted-ocr.md) – Thiết lập OCR tự host cho text captcha.
- [audio-captcha-bypass.md](./audio-captcha-bypass.md) – Pipeline speech-to-text cho audio challenge.

## Integration Checklist
- [ ] Log kết quả verify (score, hostname) để feedback loop.
- [ ] Proxy/profile hygiene cho từng provider captcha.
- [ ] Có fallback manual solving hoặc third-party API.
- [ ] Monitor success rate và chi phí captcha theo chiến dịch.