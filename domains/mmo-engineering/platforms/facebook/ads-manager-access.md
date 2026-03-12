# 💳 Facebook Ads Manager Access

## 1. Business Manager Setup
- Dùng email domain tin cậy (company domain hoặc Gmail aged).
- Tạo Business Manager (BM) với info hợp lệ (địa chỉ, số điện thoại).
- Add 2FA cho owner account.

## 2. Payment Verification
- Thêm thẻ ngân hàng local (BIN phù hợp country IP).
- Chạy charge nhỏ ($5) để confirm.
- Chuẩn bị backup card/PayPal.

## 3. Ad Account Linking
- Trong BM, tạo ad account mới → assign người + quyền.
- Kết nối Page và Pixel (đã setup).
- Limit: mỗi BM mới nên tạo 1-2 ad account, nâng dần khi trust tăng.

## 4. Automation Notes
- Script qua Graph API để kiểm tra spending limit, trạng thái review.
- Alert nếu `spend_cap` bị set quá thấp.

## 5. Checklist
- [ ] BM thông tin đầy đủ, verified.
- [ ] Payment primary + backup.
- [ ] Pixel/Page connected.
- [ ] 2FA bật cho tất cả admin.