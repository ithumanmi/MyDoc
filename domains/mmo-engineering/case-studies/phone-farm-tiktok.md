# 📱 Case Study: Phone Farm TikTok (50 thiết bị)

## 1. Bối cảnh & Mục tiêu
- Scale 50 tài khoản TikTok cho view/engagement buffer để support campaign affiliate.
- KPI: Survival rate > 90%, ROI > 30%/tháng.

## 2. Kiến trúc & Workflow
- **Hardware:** Note 8 tháo pin, nguồn DC ổn định, rack 3 tầng + quạt.
- **Proxy:** mỗi cụm 5 máy dùng 4G riêng, rotate 20 phút/lần.
- **Control:** ADB cluster + script Python random hành vi (scroll, like, follow) theo schedule YAML.
- **Daily Workflow:**
  1. 07:00 check nguồn + proxy.
  2. 08:00-23:00 chạy session 20 phút, nghỉ 10 phút, random múi giờ.
  3. 00:00 sync log lên monitoring stack.
- **Monitoring:** `farm-dashboard` panel (survival, checkpoint rate, proxy latency).

## 3. Metrics & ROI
| Metric | Value |
| --- | --- |
| Survival Rate | 92% (4 tuần) |
| Checkpoint Rate | 6%/tuần |
| Revenue/account | $7.5 |
| CPA/account | $4.9 |
| ROI | 53% |

## 4. Alert & Auto-remediation
- Alert nếu `survival < 88%/12h` → auto-pause batch.
- Auto-remediation: rotate proxy → cooldown 12h → resume.
- Log aggregator ClickHouse lưu 30 ngày để điều tra.

## 5. Lesson Learned
- SIM expiry là nguyên nhân lớn (8% die) → thêm dashboard SIM expiry.
- Proxy VN2 latency cao gây checkpoint spike 15% → chuyển provider dự phòng.
- Automation script versioning giúp rollback nhanh khi pattern bị detect.