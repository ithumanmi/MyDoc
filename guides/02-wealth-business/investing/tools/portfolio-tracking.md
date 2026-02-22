# 📊 Portfolio Tracking Tools

> [← Back to Investing](../../../README.md)

"Cái gì không đo lường được thì không quản lý được". Đừng để tài sản của bạn nằm rải rác.

---

## 1. Google Sheets (The King)

Miễn phí, tùy biến cao và có hàm tự động lấy giá cổ phiếu.

*   **Hàm Google Finance:**
    *   `=GOOGLEFINANCE("HOSE:FPT", "price")`: Lấy giá FPT hiện tại.
    *   `=GOOGLEFINANCE("CURRENCY:USDVND")`: Lấy tỷ giá USD/VND.
*   **Template cơ bản:**
    *   Cột A: Mã (Ticker).
    *   Cột B: Số lượng (Quantity).
    *   Cột C: Giá vốn trung bình (Avg Cost).
    *   Cột D: Giá thị trường (Market Price - dùng hàm trên).
    *   Cột E: Giá trị hiện tại (Market Value = B * D).
    *   Cột F: Lãi/Lỗ (Profit/Loss = E - (B*C)).

## 2. Dedicated Apps (Ứng dụng chuyên dụng)

Nếu lười làm Excel, hãy dùng App.

*   **FireAnt (Việt Nam):**
    *   Ưu điểm: Dữ liệu Việt Nam đầy đủ, realtime, tin tức nhanh.
    *   Nhược điểm: Giao diện hơi rối, tập trung vào Trading hơn là Investing.
*   **Delta / CoinStats (Crypto & Global Stocks):**
    *   Ưu điểm: Giao diện đẹp, kết nối API trực tiếp với sàn (Binance, Broker) để tự động đồng bộ giao dịch.
    *   Nhược điểm: Dữ liệu cổ phiếu Việt Nam có thể chậm.
*   **Yahoo Finance:**
    *   Kinh điển, miễn phí, cover toàn bộ thị trường thế giới.

## 3. Rebalancing Calculators (Máy tính tái cân bằng)

Khi danh mục bị lệch tỷ trọng, bạn cần biết bán cái nào, mua cái nào.

*   **Nguyên lý hoạt động:**
    1.  Nhập số tiền bạn đang có thêm (Cash injection).
    2.  Nhập tỷ trọng mục tiêu (Target Allocation - VD: 70/30).
    3.  Tool sẽ tính toán: "Hãy dùng tiền mặt mua thêm Trái phiếu, đừng mua Cổ phiếu nữa vì nó đang vượt tỷ trọng".
*   *Mẹo:* Bạn có thể tự code logic này đơn giản trên Google Sheets.
