# 🧭 Platform Playbooks

Chi tiết SOP cho từng nền tảng chính: Facebook, TikTok, Google.

## Structure

### Facebook
- [account-creation.md](./facebook/account-creation.md)
- [warming-schedule.md](./facebook/warming-schedule.md)
- [ads-manager-access.md](./facebook/ads-manager-access.md)
- [checkpoint-recovery.md](./facebook/checkpoint-recovery.md)

### TikTok
- [device-registration.md](./tiktok/device-registration.md)
- [content-strategy.md](./tiktok/content-strategy.md)
- [monetization-path.md](./tiktok/monetization-path.md)

### Google
- [gmail-creation.md](./google/gmail-creation.md)
- [google-ads-warming.md](./google/google-ads-warming.md)
- [play-store-developer.md](./google/play-store-developer.md)

## Checklist
- [ ] SOP sync với captcha/proxy modules.
- [ ] Log template cho từng nền tảng.
- [ ] Review định kỳ khi policy thay đổi.

## Áp dụng cho nền tảng khác
- Dùng cùng cấu trúc 4 phần: **Account Creation → Warming → Access/Monetization → Recovery**.
- Map tín hiệu trust riêng từng nền tảng (Snapchat, Twitter/X, Pinterest...) dựa trên policy docs.
- Reuse module hỗ trợ (proxy, captcha, device farm) để giảm thời gian build SOP mới.