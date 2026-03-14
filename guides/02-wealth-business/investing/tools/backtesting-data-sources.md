## 🧪 Backtesting & Historical Data Sources (VN focus)

> Dành cho bạn muốn tự kiểm chứng chiến lược (Sector Rotation, Technical Analysis, Momentum) bằng Python/Excel. Luôn kiểm tra chất lượng và tính đầy đủ của dữ liệu.

### 1) Giá cổ phiếu/ETF trong nước (EOD)
- **Nguồn công khai:** fireant, vietstock, cafef (download CSV từng mã), FiinTrade/FiinPro (trả phí, đầy đủ hơn), SSI iBoard API (giá real-time/near real-time qua websocket, cần tự lưu). 
- **CSV thủ công:** cafef → mục "Xuất dữ liệu" cho từng mã (lịch sử giá & KL). Kiểm tra split/dividend để điều chỉnh nếu cần.
- **Python:** dùng `yfinance` cho một số ETF/DR nước ngoài, nhưng mã VN trên yfinance hạn chế; có thể scrape cafef/vietstock (tuân thủ robots/ToS).

### 2) Chỉ số thị trường (VNIndex, VN30, HNX, UPCoM)
- Cafef/vietstock đều cho xuất CSV lịch sử chỉ số.
- Một số CTCK (SSI, VND) cho tải dữ liệu chỉ số qua app/web (cần đăng nhập). 
- Kiểm tra xem chỉ số đã “total return” hay chỉ price; thông thường là price index.

### 3) Lãi suất, trái phiếu, macro phụ trợ
- **Lãi suất liên ngân hàng, OMO, tín phiếu:** SBV website, cafef macro.
- **Lợi suất TPCP VN:** HNX (trái phiếu), cafef/vietstock có bảng yield theo kỳ hạn; có thể scrape.
- **USD/VND, CPI:** GSO, SBV; dùng để chuyển đổi hoặc mô phỏng real return.

### 4) Quy trình backtest đơn giản (gợi ý)
- **Python:** pandas + vectorized backtest; lưu CSV (EOD) theo thư mục `/data/raw/<ticker>.csv`; viết hàm loader hợp nhất chỉ số/lãi suất nếu cần risk-free rate.
- **Excel:** PowerQuery để tải CSV định kỳ; dùng hàm `XLOOKUP`/`INDEX MATCH` ghép chỉ số và lãi suất; tính đường cong vốn, max drawdown, CAGR.
- **Kiểm soát dữ liệu:** loại ngày nghỉ, kiểm tra thiếu gap; điều chỉnh cho cổ tức/split nếu chiến lược cần total return.

### 5) Liên kết tài liệu
- [Sector Rotation Strategy](../advanced/sector-rotation-strategy.md)
- [Technical Analysis](../advanced/technical-analysis.md)
- [Portfolio Tracking Toolkit](./portfolio-tracking.md)
- [Data Sources (Tổng hợp)](./data-sources.md)