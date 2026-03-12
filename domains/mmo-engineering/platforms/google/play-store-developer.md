# 🛠️ Google Play Store Developer Setup

## 1. Prerequisites
- Gmail đã 2FA (xem Gmail SOP).
- Thẻ tín dụng quốc tế để trả phí đăng ký $25.
- Company info (tên pháp lý, địa chỉ, hotline).

## 2. Registration Steps
1. Vào [Play Console](https://play.google.com/console/signup).
2. Chọn loại tài khoản (Individual/Organization).
3. Nhập thông tin pháp lý, upload logo.
4. Thanh toán phí một lần $25.
5. Xác minh danh tính (ID + selfie) nếu được yêu cầu.

## 3. App Publishing Hygiene
- Tạo app draft, điền Store Listing (mô tả, screenshot).
- Ký APK/AAB bằng key chuẩn, enable App Integrity.
- Thiết lập Privacy Policy, content rating.

## 4. Compliance & Review
- Log mọi lần submit, version, changelog.
- Nếu bị reject → đọc policy violation, sửa, resubmit.
- Tối đa 3 lần reject liên tiếp sẽ bị flag.

## 5. Automation/Monitoring
- Sử dụng Play Developer API để check status build, download review report.
- Alert nếu có policy warning mới.

## 6. Checklist
- [ ] Phí đăng ký trả thành công.
- [ ] Identity verification hoàn tất.
- [ ] App key + keystore lưu an toàn.
- [ ] Privacy policy host ổn định.