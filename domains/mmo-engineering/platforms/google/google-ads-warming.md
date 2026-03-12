# 📈 Google Ads Warming Plan

## 1. Goal
- Đưa tài khoản Ads mới lên chi tiêu $200/day trong 30 ngày, tránh suspension.

## 2. Timeline
| Day | Action |
| --- | --- |
| 1-3 | Profile hygiene: login Gmail, bật 2FA, add billing profile. |
| 4-10 | Campaign Discovery hoặc Search brand keyword, budget $10/day. |
| 11-20 | Thêm Conversion tracking, tăng budget 20% mỗi 3 ngày. |
| 21-30 | Scale Performance Max, giữ chất lượng ad. |

## 3. Payment & Billing
- Sử dụng card BIN nội địa khớp IP.
- Add secondary payment ngay từ đầu.
- Monitor `payment_profile_status` qua API.

## 4. Trust Signals
- Connect domain (DNS verified), chạy ads tới landing sạch.
- Maintain policy compliance, tránh keyword nhạy cảm.

## 5. Automation
- Google Ads API script check `account_status`, `policy_summary`.
- Alert nếu `policy_summary.approval_status != APPROVED`.

## 6. Checklist
- [ ] Billing info verified.
- [ ] Conversion tracking hoạt động.
- [ ] Domain verified, SSL ok.
- [ ] Spend log ghi nhận.