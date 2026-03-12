# 📱 TikTok Device Registration

## 1. Environment
- Android phone farm hoặc emulator (LDPlayer, MuMu) với anti-detect config.
- Proxy 4G/residential, đồng bộ timezone/location.
- TikTok app bản mới nhất, disable auto-update sau khi ổn định.

## 2. Steps
1. Factory reset device/emulator snapshot.
2. Đăng nhập Google/Apple ID (nếu cần) bằng cùng proxy.
3. Cài TikTok, mở lần đầu để generate device ID.
4. Bind SIM/phone number nếu yêu cầu.

## 3. Device Fingerprint
- Ghi lại `device_id`, `install_id`, `openudid`.
- Đối với emulator: randomize build.prop (model, brand), nhưng giữ nhất quán cho profile.
- Không clone app backup (TikTok detect duplicate ID).

## 4. Automation Tips
- Sử dụng ADB script để login, scroll, like.
- Delay action 2-5s, random swipes.

## 5. Checklist
- [ ] Snapshot device sau khi setup.
- [ ] Lưu device identifiers trong vault.
- [ ] Proxy pinning per device.