# 👟 Case Study: Sneaker Bot Operation

## 1. Mục tiêu
- Automate checkout Nike/SNKRS drop với tỉ lệ thành công > 20% bằng bot + proxy rotation.

## 2. Stack & Setup
- **Bot:** Node.js custom + anti-bot bypass (HMAC, Akamai sensor data).
- **Proxy:** mix residential + ISP, chia pool theo region (US/EU/APAC).
- **Profiles:** 200 profile (billing info unique), stored trong anti-detect browser.
- **Scheduler:** redis queue + worker pool scale theo drop time.

## 3. Workflow
1. Preload sản phẩm ID, size matrix.
2. 5 phút trước drop → warm session (cart ping).
3. Drop: worker lấy task, attach proxy, submit checkout.
4. Post-drop: validate order, auto-cancel duplicate.

## 4. Metrics
| Metric | Goal |
| --- | --- |
| Success Rate | 22% |
| Proxy Fail Rate | <5% |
| Queue Wait Time | <3s |
| Revenue/account | $60/order resale spread |

## 5. Alert & Auto-remediation
- Alert nếu `proxy_fail > 8%` → rotate pool + drop ISP.
- Log aggregator (Loki) tag theo drop để replay.
- Auto-retry 2 lần nếu status 429, random delay 500-1200ms.

## 6. Lessons
- Reuse cookie gây ban hàng loạt → enforce one-time cookie per drop.
- ISP proxy hiệu quả cho checkout nhưng đắt → dùng dynamic scaling (pay-per-use) chỉ trong 15 phút sự kiện.
- Success log + analytics giúp xác định size/region nào ROI cao.