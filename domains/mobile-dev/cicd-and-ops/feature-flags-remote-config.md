# Feature Flags & Remote Config

## Mục tiêu
- Rollout an toàn, A/B testing, bật/tắt tính năng không cần release.

## Giải pháp phổ biến
- Firebase Remote Config, LaunchDarkly, ConfigCat, homemade flags (backend + cache).
- Client caching + TTL; fallback khi offline.

## Thực hành
- Tách flags theo ngữ nghĩa: kill-switch, gradual rollout, experiment.
- Giới hạn số flags active; dọn flags hết hạn.
- Log exposure để phân tích; bảo vệ đường dẫn logic mặc định khi flag lỗi.