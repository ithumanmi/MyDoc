# Fastlane Playbook

## Mục tiêu
- Tự động build, ký, chụp screenshot, upload TestFlight/Play Internal.

## Lane gợi ý
- `build`: build + unit test.
- `screenshots`: chụp màn hình đa ngôn ngữ/kích thước.
- `beta`: upload TestFlight/Play Internal; tăng build number tự động.
- `release`: tag + upload store.

## Best practices
- Quản lý secrets bằng env/CI secrets; không commit cert.
- Match/certificates sync; gradle/xcodeproj version bump tự động.
- Tích hợp CI (GitHub Actions/Bitrise) với cache để giảm thời gian build.