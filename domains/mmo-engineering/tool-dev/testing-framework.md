# 🧪 Testing Framework for MMO Tools

## 1. Goals
- Đảm bảo tool automation chạy ổn định trước khi release.
- Mock platform để tránh dùng account thật.

## 2. Test Pyramid
- **Unit Tests:** logic parser, scheduling, config loader.
- **Integration Tests:** automation script + mock server (HTTP, WebSocket).
- **System Tests:** run tool end-to-end trong sandbox.

## 3. Mock Servers
- Use Playwright/Puppeteer to spin up fake UI (HTML templates) → simulate login, 2FA, captcha.
- API mock: FastAPI/Express server trả về response như platform thật.
- For mobile automation: Android emulator với fake app build.

## 4. CI Pipeline
1. `lint` (ruff, eslint) + type check.
2. `pytest` với fixtures mock proxy/ADB.
3. Build artifact (PyInstaller/Nuitka).
4. Run smoke test container: launch binary + script automation vào mock platform.
5. Upload artifact + test report (Allure).

## 5. Test Data
- Synthetic accounts, fake cookies, OTP seed mock.
- Secrets trong CI lấy từ Vault (dynamic secret) → xong test revoke.

## 6. Observability
- Capture logs (structured JSON) → GCS/S3.
- Screenshot/video run automation để debug.

## 7. Checklist
- [ ] Mock server cover các case chính (login, captcha, ban response).
- [ ] CI smoke test pass trước khi release.
- [ ] Logs/Screenshot attach vào report.