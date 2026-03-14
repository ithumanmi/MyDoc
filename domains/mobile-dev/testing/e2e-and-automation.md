# E2E & Automation

## Tooling
- Detox (RN), Maestro (cross), Appium.
- Flutter: integration_test + drivers; Maestro cross-platform.

## Thực hành
- Mock/stub network (MSW, interceptors) để ổn định.
- Chọn ít case E2E nhưng cover luồng chính (auth, purchase, checkout).
- Chạy trong CI với emulator/simulator headless.

## CI tips
- Cache build để giảm thời gian.
- Parallel test suites nếu được.