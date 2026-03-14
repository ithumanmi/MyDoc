# 📊 Net Worth Tracking

> "Bạn không thể tối ưu thứ bạn không đo." – Principle

## 1. Khung tài sản ròng

`Net worth = Tổng tài sản (cash, đầu tư, BĐS, hưu trí) – Tổng nợ (vay, thẻ tín dụng)`

## 2. Cadence

- **Monthly:** cập nhật số dư tài khoản, nợ, giá trị danh mục.
- **Quarterly:** đánh giá tăng trưởng % và thay đổi cấu trúc tài sản.
- **Yearly:** so sánh với mục tiêu dài hạn (retirement number).

## 3. Dashboard cần có

| Thành phần | Mục tiêu |
| --- | --- |
| Net worth timeline | Thấy trend dài hạn, drawdown |
| Asset allocation | Equity/Bonds/Cash/Alt |
| Debt schedule | Thời gian trả hết, lãi suất bình quân |
| Liquidity | Cash & equivalents / monthly expense |
| FIRE progress | % đạt mục tiêu nghỉ hưu |

## 4. Công cụ

- **Spreadsheet:** Google Sheet với IMPORTXML/IMPORTHTML lấy giá ETF/cổ phiếu; pivot cho allocation.
- **Notion:** database tài khoản, linked view cho net worth chart.
- **App VN:** Finhay/TCInvest/SSI iBoard (tùy tích hợp), nhưng nên có bản lưu trữ riêng.
- **Tự động:** script Python pull dữ liệu qua API (Alpha Vantage/Yahoo) + CSV bank import.

## 5. Quy tắc dữ liệu

1. Dùng snapshot cuối tháng, tránh update liên tục gây nhiễu.
2. Chuẩn hóa đơn vị tiền (VND hoặc quy USD) và tỷ giá cố định cho kỳ.
3. Lưu version history (tháng/năm) để backtest tiến độ.

## 6. Cảnh báo & guardrail

- Debt/Income > 35% → xem lại nợ.
- Liquidity < 3 tháng chi phí → bổ sung cash.
- Allocation lệch >5-10% so với target → rebalance.

## 7. Template

- Net Worth Tracker (Sheet): tabs Accounts, Debts, Allocation, Charts.
- FIRE Calculator: nhập chi phí năm, SWR, thời gian đến nghỉ hưu.
- Debt Amortization: lịch trả nợ và lãi tích lũy.

---
> Hoàn thành: quay lại README để rà soát checklist.