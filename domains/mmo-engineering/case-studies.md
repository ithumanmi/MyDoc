# 📚 MMO Case Studies

> Các kịch bản thực tế để kết nối kiến thức kỹ thuật với vận hành (phone farm, ad account warm-up).

---

## 1. Phone Farm TikTok (50 thiết bị)

### Mục tiêu
- Nuôi 50 tài khoản TikTok/Facebook song song để làm view/engagement buffer.

### Kiến trúc
- **Hardware:** 50 Android cũ (Note 8) tháo pin + cấp nguồn ổn định, gắn trên rack 3 tầng.
- **Connectivity:** Mỗi cụm 5 máy dùng hub USB riêng, nối vào PC điều khiển; proxy 4G riêng cho từng cụm.
- **Control Plane:**
  - ADB cluster + scrcpy multi-view.
  - Script random hành vi (scroll, like, comment) chạy qua Task Scheduler.
- **Monitoring:** kết nối với stack trong [operations-monitoring.md](./operations-monitoring.md) để nhận heartbeat, cảnh báo nhiệt độ.

### SOP chính
1. **Boot:** kiểm tra nguồn, bật ADB, xác thực proxy.
2. **Daily Run:** random schedule theo múi giờ người dùng; auto-break 15 phút mỗi 2 giờ.
3. **Recovery:** nếu account checkpoint, tool tự động switch sang account dự phòng & gửi alert Telegram.

### Kết quả & Lesson
- Sau 4 tuần: tỷ lệ sống 92%, 8% die do SIM hết hạn → cần dashboard SIM expiry.
- Heatmap giúp phát hiện proxy provider tại VN2 có latency cao, chuyển sang provider khác giảm checkpoint 15%.

---

## 2. Facebook Ads Warm-up (30 ngày)

### Mục tiêu
- Từ tài khoản mới → chạy ads budget $500/day trong 14 ngày mà không bị hạn chế.

### Workflow
1. **Identity Prep:**
   - Hồ sơ anti-detect profile với cookie/history hợp lệ (xem [browser-fingerprinting.md](./browser-fingerprinting.md)).
   - Tài khoản email domain riêng, 2FA hardware.
2. **Payment Staging:**
   - Thêm thẻ ngân hàng phụ, chạy chi tiêu nhỏ ($5-$10) trong 3 ngày.
   - Kết nối Business Manager → chia quyền role rõ ràng.
3. **Activity Simulation:**
   - Manual browsing 30-45 phút/ngày (watch video, join group) để tạo signal người thật.
   - Dùng automation nhẹ (Playwright + human emulation) nhưng giới hạn 3 action/phút.
4. **Ad Launch Ladder:**
   - Ngày 1-3: boost post engagement $5/day.
   - Ngày 4-7: chạy conversion nhỏ (traffic), target broad.
   - Ngày 8-14: tăng ngân sách 20% mỗi ngày, giữ CTR >1.5%.
5. **Risk Controls:**
   - Nếu Quality Score < T threshold hoặc feedback xấu, tạm dừng tăng ngân sách.
   - Alert webhook khi Ads Manager báo “Account Spending Limit Reached”.

### Dashboard/KPI
- Theo dõi trong Grafana: spend/day, approval latency, event match quality.
- Alert nếu `Rejected ads > 2` trong 24h hoặc `Trust Score` tụt.

### Lesson
- Warm-up thất bại chủ yếu do đăng nhập từ IP mới → enforce proxy pinning.
- Payment mismatch (thẻ quốc gia khác) gây review manual → cần list ngân hàng bản địa.

---

## 3. Sneaker Bot Operation
- Chi tiết xem [case-studies/sneaker-bot-operation.md](./case-studies/sneaker-bot-operation.md).

## 4. Crypto Airdrop Postmortem (LayerZero, ZKSync)
- Chi tiết xem [case-studies/crypto-airdrop-postmortem.md](./case-studies/crypto-airdrop-postmortem.md).

## Checklist Case Studies
- [ ] Dữ liệu (số lượng thiết bị, ngân sách) được ẩn danh hóa.
- [ ] Có mapping tới module liên quan (anti-detect, proxy, monitoring).
- [ ] Bổ sung KPI + dashboard tham chiếu.
- [ ] Lesson Learned rõ ràng để reuse.