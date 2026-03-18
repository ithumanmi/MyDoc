# Luyện Kim Dữ Liệu: Chế Ngự Máu Sống Sàn Giao Dịch (Market Data Engineering)

> [← Back to Quantitative Trading Hub](./README.md)

Chào mừng bạn đến với Hầm Mỏ của Giới Quant. Nếu thuật toán là Động Cơ Tên Lửa, thì **Dữ Liệu Mỏ (Market Data)** chính là Nhiên Liệu Rắn. Code thuật toán có xịn đến đâu mà nạp vào dữ liệu rác, nó sẽ đốt rụi tài khoản của bạn nhanh hơn cả một cú trượt tay khi gõ lệnh (Fat Finger).

Trong thế giới Retail (đám đông đánh lẻ), họ chỉ nhìn nến 1h, 1D nén sẵn trên TradingView. Ở thế giới Quant, chúng ta húp **Tick Data** (từng giao dịch đơn lẻ) và **Order Book L2** (Sổ Lệnh Giới Hạn) với khối lượng Terabytes mỗi ngày.

---

## 🗑️ 1. Rác Dữ Liệu Và Những Cú Lừa Cháy Túi (Data Pitfalls)

Khi bạn viết Bot Black-Scholes hay VectorBT, dữ liệu lịch sử tải về từ Yahoo Finance hay một sàn cỏ nào đó không bao giờ là sự thật hoàn mỹ.

### 💀 Survivorship Bias (Lỗi Kẻ Sống Sót)
Bạn backtest một chiến thuật "Bắt Đáy Cổ Phiếu Rơi Của Rổ S&P 500 Năm 2008" và thấy lãi 400%. Tại sao? Vì bộ data S&P 500 hiện tại của bạn CHỈ chứa những công ty còn sống sót đến hôm nay. Những công ty (như Lehman Brothers, Bear Stearns) đã phá sản năm 2008 bị xóa khỏi danh sách. Bot của bạn hoàn toàn không mua dính công ty chết, nên lãi ảo tung nóc!
*   **Cách giải quyết:** Phải mua bộ dữ liệu Point-in-Time (Lịch sử tĩnh) trị giá hàng chục ngàn USD ghi nhận chính xác danh sách những rổ chỉ số tại từng giây phút quá khứ, ôm hết cả những mã bị hủy niêm yết (delisted).

### ⏳ Look-Ahead Bias (Kẻ Nhìn Trộm Tương Lai)
Bạn viết rule: *Nếu giá đóng cửa hôm nay vượt đỉnh ngày mai thì mua.* Python không cấm bạn viết lỗi này! Bạn xài data tương lai (chưa xảy ra tính tại thời điểm đó) để ra quyết định mua hôm nay. Đường cong PnL lúc backtest thẳng đứng lên trời, mang vào Trade thật là Sập.
*   **Cách giải quyết:** Shift Data cẩn thận (df['close'].shift(1)), tách rạch ròi quá trình sinh tín hiệu (Signal Generation) và hàm áp giá khớp lệnh (Execution Engine).

### 💩 Spikes, Drops & Missing Data (Gai Nhiễu)
Đôi khi API của sàn giao dịch (như Binance hay Interactive Brokers) mất kết nối 1 giây. Dữ liệu nến thiếu (NaN) hoặc vô tình có một cú chọc gậy (1 Bitcoin giá $1 văng vào hệ thống). Nếu Bot của bạn nhạy với biến động giá, nó sẽ dốc sạch vốn All-in vào cú nhiễu đó.
*   **Kỹ thuật chà rửa (Data Scrubbing):** Áp dụng thuật toán Median Z-Score hoặc Rolling MAD (Median Absolute Deviation) để loại bỏ các Gai Nhiễu (Outliers) thay vì dùng Average SMA rác. Forward Fill (ffill) cho những tíc tắc dữ liệu bị nghẽn mạng!

---

## 🧱 2. Nội Tạng Sổ Lệnh Mù (L2 Order Book) & Vặn Dữ Liệu Tick-Level

Ở mỏ vàng HFT (High-Frequency Trading) hay Bot Arbitrage chớp nhoáng, nến Candlestick là thứ đồ chơi ném sọt rác. Dân Pro nhìn máu thị trường từ **Order Book** (Sổ Lệnh).

Sổ lệnh L2 có hai chiều: **Bids** (Người chờ mua) & **Asks** (Người chờ bán giá cao). Điểm giao nhau gọi là **Mid-Price**, còn chênh lệch gọi là **Spread**.

*   **Order Book Imbalance (Độ Lệch Trọng Tâm):** Nếu Tường Mua (Bids) dày đặc 100 chữ số không lồ mà Tường Bán (Asks) mỏng tanh, áp lực vỡ trần đánh lên cực mạnh. Kỹ sư Quant quét tỷ lệ `(Bids - Asks) / (Bids + Asks)` từng phần nghìn giây (millisecond) để tung Bot chém lực.
*   **Tick Data Parsing:** Dây chuyền nạp data từ WebSocket về dạng FIX Protocol siêu nhanh, không lưu dạng JSON (quá chậm, quá cồng kềnh). Họ dùng kiến trúc Binary, giải nén từng Packet dữ liệu gốc của Sở Giao Dịch (ví dụ ITCH protocol của sàn NASDAQ).

---

## 💾 3. Kho Báu Data Hồ Chứa Tốc Độ Ánh Sáng: KDB+/q & TimescaleDB

Xài Pandas (Python) lưu mảng file CSV 5GB? Nó sẽ treo cứng RAM máy tính của bạn và Crash thẳng cẳng. SQL thông thường (MySQL, Postgres gốc) truy vấn một bảng nến chạy chục năm sẽ đơ cả phút.

**Ngai Vàng Tối Thượng Của Quant Data Database:**
1.  **KDB+ & Ngôn Ngữ q:** Database bộ nhớ trong (In-Memory Database) quái vật của các Quỹ Hedge Fund Tier 1. Ngôn ngữ `q` trông như ma trận ngoài hành tinh nhưng nó tính trung bình động cho 1 Tỷ dòng (Rows) chỉ mất chưa đầy vài Mili-giây. Sở hữu kỹ năng viết được KDB+/q có thể ấn định mức lương Quant Developer vượt trội $200k+/Năm.
2.  **TimescaleDB / ClickHouse:** Phương án mã nguồn mở (Open Source) mạnh mẽ nhất cho Kỹ sư lẻ (Retail Algo Traders). ClickHouse đớp nhanh dữ liệu chuỗi thời gian siêu khổng lồ để Backtesting Bot (Dạng OLAP - Quét cột tính toán Vector hóa). TimescaleDB mở rộng PostgreSQL nhưng xử lý Data Chuỗi Thời Gian mượt mượt mà.

> **Trọng Trách Máu Lửa Của Kỹ Sư Dữ Liệu Tài Chính:** Hãy luôn nhớ "Garbage In - Garbage Out". Rửa sạch dữ liệu, chặn bế lỗi Survivorship Bias, và đút chính xác Tick-Data vào bộ máy Python Backtest. Đó là thứ quyền năng cấm kỵ tách biệt kẻ đánh bạc khát nước và Quản Lý Quỹ Tinh Lọc Số Liệu Vô Song. 🚀
