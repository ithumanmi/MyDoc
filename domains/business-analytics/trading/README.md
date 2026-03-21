# 🏦 Quantitative Trading & Financial Engineering (Giao Dịch Định Lượng)

> [← Back to Business Analytics Hub](../README.md)

Chào mừng bạn bước vào Khối Vận Hành Của Máu Chó Wall Street Đầu Não - **Quantitative Finance (Tài Chính Định Lượng)**.
Nếu ở Tầng **Business Analytics**, bạn dùng Dữ Liệu Khách Hàng (LTV) để đoạt Doanh Thu StartUp Công Nghệ. Thì ở nhánh ngách **Trading** siêu phàm này, Bạn Dùng Dữ Liệu Giá Cổ Phiếu Cuộn (Tick Data/ Market Data) để Rút Tiền Tươi Máu Sống Ra Khỏi Miệng Hố Sàn Khốc Liệt Toàn Cầu.

> **Tuyên Thệ Rạch Ròi Từ Đây:** Chấm đứt hoàn toàn thói ngồi Nhìn Vẽ Cản (Price Action Vẽ Bậy Vẽ Bạ). Kịch bản Cảm Tính: "Tao Cảm Thấy Con Bitcoin Nó Đang Lực Yếu Chắc Tụt Xẻ!". Nơi Đây Là Vương Quốc Bất Bại Của Kỹ Sư Công Nghệ: **Viết Code Backtest Quá Khứ Python & Nắm Trọn Thuật Toán Thống Kê Định Rủi Ro Số Tuyệt Lệnh Bất Kể Sóng Tăng Giảm Bạo Đứt.**

---

## 🗺️ TÂN BINH BẮT ĐẦU TẠI ĐÂY: Kinh Thánh Lộ Trình (The Master Roadmap)
Nếu bạn chưa biết bắt đầu từ đâu, hãy đi theo Lộ Trình 5 Giai Đoạn được rèn đúc khốc liệt này để biến mình từ tay ngang thành Kỹ Sư Quant (Toán, C++, Python, Data) thực thụ:
👉 **[Master Roadmap: Tẩy Não Trở Thành Thiết Giáp Kỹ Sư Quant](./quant-learning-roadmap.md)** (⭐ **BẮT BUỘC ĐỌC ĐẦU TIÊN**)

---

## 🧠 Lộ Trình Study Nhanh (7 Bước Thực Chiến)
1) **Nền tảng & Kỷ luật rủi ro**: đọc [Quant Fundamentals](./fundamentals-of-quant-trading.md).  
2) **Dữ liệu thị trường**: làm [Market Data Engineering](./market-data-engineering.md) + chọn 1 lab data (vectorized backtest hoặc pairs).  
3) **Alpha cơ bản (Stat-Arb)**: xem [Alpha Research & Stat-Arb Checklist](./advanced/alpha-research-checklist.md) + code thử [Stat-Arb Cointegration Snippet](./advanced/stat-arb-cointegration-snippet.md).  
4) **Khớp lệnh & chi phí**: học [Execution Algorithms](./execution-algorithms.md) → [Execution & TCA Playbook](./execution-tca-playbook.md); chạy lab [Execution/TCA Simulator](./labs/lab-execution-tca-simulator.md) hoặc [Notebook Template](./labs/lab-execution-tca-notebook-template.md).  
5) **Risk & guardrails**: áp dụng [Risk & Portfolio Engineering](./risk-portfolio-engineering.md) và YAML [Guardrails](./advanced/guardrails-config-examples.md).  
6) **Microstructure & venue**: đọc [Microstructure Feature Cookbook](./advanced/microstructure-feature-cookbook.md) và mini-case [Multi-Venue Router](./advanced/execution-router-multi-venue-case.md).  
7) **Mở rộng nâng cao**: chọn nhánh [AI/ML trong trading](./advanced/ai-machine-learning-in-trading.md), [HFT microstructure](./advanced/hft-market-microstructure.md), hoặc [DeFi MEV](./advanced/defi-mev-flash-loans.md).

Checklist tự học:
- [ ] Hoàn thành đọc nền tảng + ghi chú risk (Kelly, DD caps).  
- [ ] Kéo 1 lab backtest (vectorized hoặc pairs) chạy được với dữ liệu mẫu.  
- [ ] Tính IS/VWAP/arrival cho 1 lệnh và so sánh TWAP/VWAP.  
- [ ] Thiết lập guardrails tối thiểu (caps, kill-switch, drift).  
- [ ] Triển khai 1 feature microstructure (OBI/OFI) và kiểm tra leak.  
- [ ] Chọn 1 nhánh nâng cao và làm thêm 1 lab tương ứng.  

### Gợi ý mốc thời gian (6 tuần)
- Tuần 1: Quant Fundamentals, thiết lập môi trường, làm sạch 1 tập tick/ohlcv nhỏ.  
- Tuần 2: Market Data Engineering + chạy lab vectorized backtest đơn giản.  
- Tuần 3: Stat-arb cơ bản (cointegration), hoàn thành 1 backtest pairs.  
- Tuần 4: Execution & TCA (TWAP/VWAP/POV/IS), tính IS/VWAP/arrival cho 1 trade.  
- Tuần 5: Risk & Guardrails (caps, kill-switch, drift monitor) + áp dụng YAML mẫu.  
- Tuần 6: Microstructure & router đa venue; chọn 1 nhánh nâng cao (AI/HFT/DeFi) và làm 1 lab.  

### Starter kit (dataset & notebook)
| Thành phần | Gợi ý | Link nội bộ |
| --- | --- | --- |
| Dataset OHLCV mẫu | 1-2 năm daily/5m một cặp cổ phiếu hoặc BTCUSDT | (tự bổ sung data vào `data/ohlcv_sample.csv`) |
| Tick/L2 demo nhỏ | 1 ngày tick hoặc level-2 depth nhỏ để thử OBI/OFI/VPIN | (tự bổ sung data vào `data/tick_sample.csv`) |
| Backtest vectorized | Notebook/lab vectorized backtest | [Lab Backtesting Vectorized](./labs/lab-python-vectorized-backtesting.md) |
| Pairs & cointegration | Notebook/lab stat-arb | [Lab Pairs Trading](./labs/lab-statistical-arbitrage-pairs.md) + [Cointegration Snippet](./advanced/stat-arb-cointegration-snippet.md) |
| Execution & TCA | Notebook mô phỏng TWAP/VWAP/POV/IS | [Notebook Template Execution & TCA](./labs/lab-execution-tca-notebook-template.md) |
| Microstructure features | VPIN/OFI/OBI demo | [Microstructure Feature Cookbook](./advanced/microstructure-feature-cookbook.md) |
| Guardrails YAML | Caps, kill-switch, drift monitor | [Guardrails Config Examples](./advanced/guardrails-config-examples.md) |

> File data mẫu (tự đặt vào repo): 
> - OHLCV: `./data/ohlcv_sample.csv` (ví dụ BTCUSDT 5m, 1-2 năm).  
> - Tick/L2: `./data/tick_sample.csv` (1 ngày tick hoặc depth gọn).  
> Nếu bạn cung cấp file thật, cập nhật link nội bộ tới đường dẫn đó để tiện mở từ README.

### Hướng dẫn setup nhanh (venv + notebook)
```bash
# 1) Tạo và kích hoạt venv (Python 3.10+)
python -m venv .venv
./.venv/Scripts/activate  # Windows PowerShell: .venv\\Scripts\\Activate.ps1

# 2) Cài gói tối thiểu cho labs/notebook
pip install -U pandas numpy matplotlib seaborn jupyter statsmodels vectorbt

# 3) Chạy notebook
jupyter notebook  # hoặc: jupyter lab
```
Gợi ý: tạo file `.env` hoặc config riêng cho đường dẫn data, tránh commit dữ liệu lớn.

## 🧭 Cẩm Nang Lý Thuyết & Giao Khứa Định Mệnh Rủi Ro (The Core Rules)

Chỗ mà Hội Đánh Bài (Retail Trader Liều Mạng) Và Dân Khoa Học Định Lượng Phân Cực Dữ Đoán Sống Chết Phá Sản Thành Công Lỗ Khống:
1. **[Quy Luật Nghề Máu: Lõi Rủi Ro & Cơ Chế Định Lượng Phức Tồn (Quant Fundamentals)](./fundamentals-of-quant-trading.md)** (⭐ **Must Read**). Tại Sao 90% Móc Đáy Trading Rụng Gãy Thành Nước Thủng? Bạn Cần Phải Có Tiêu Chuẩn Phái Quỹ Rủi Ro Tàn Không Thể Rơi Nổi Sóng Xô: (Kelly Criterion Rót Tiền Vốn & Trát Lưới Tỷ Lệ Cọc Rút Đánh Sharpe Ratio Nồng Sát Phạt). 
2. **[Luyện Kim Dữ Liệu: Chế Ngự Máu Sống Sàn Giao Dịch (Market Data Engineering)](./market-data-engineering.md)**. Rửa sạch rác Tick Data, chống lỗi Survivorship Bias nhìn trộm tương lai, và thấu thị sổ lệnh mù L2 (Order Book).
3. **[Lưỡi Dao Khớp Lệnh Chém Sóng (Execution Algorithms)](./execution-algorithms.md)**. Đừng mua All-in để bị trượt giá cháy sàn. Kỹ thuật chẻ nhỏ lệnh tàng hình TWAP, VWAP, POV bám đuôi dấu chân mây cá mập.
4. **[Kỹ Sư Risk & Portfolio: Sizing – Drawdown – Hedging](./risk-portfolio-engineering.md)**. Playbook risk thực chiến: sizing (Kelly/Half/Fractional), drawdown cap, vol targeting, risk parity, hedging, TCost.
5. **[Execution & TCA Playbook: Impact, Slippage, Smart Routing](./execution-tca-playbook.md)**. Mô hình impact (Almgren-Chriss), chiến lược TWAP/VWAP/POV/IS, smart routing, TCA pre/in/post-trade.
6. **[Options: Greeks & Hedging Playbook](./options-greeks-hedging.md)**. Delta/gamma/vega/theta, delta hedge loop, gamma scalping, vega hedge, checklist.
7. **[Latency Stack: Python vs C++/Rust](./advanced/latency-stack-comparison.md)**. So sánh latency, khuyến nghị giảm trễ Python, khi nào cần C++/Rust.
8. **[Alpha Research & Stat-Arb Checklist](./advanced/alpha-research-checklist.md)**. Checklist chống bias/overfit, validation, metrics, stat-arb specifics.
9. **[Microstructure Feature Cookbook](./advanced/microstructure-feature-cookbook.md)**. OBI, OFI, VPIN, micro-price, resiliency, toxicity, venue signals, hygiene.
10. **[Guardrails & Config Examples](./advanced/guardrails-config-examples.md)**. YAML mẫu risk caps, rate-limit, kill-switch, latency guard, monitoring.
11. **[Stat-Arb: Cointegration & Hedge Ratio Snippet](./advanced/stat-arb-cointegration-snippet.md)**. OLS hedge ratio, Engle-Granger p-value, spread z-score, half-life, tín hiệu đơn giản.
12. **[Mini-Case: Multi-Venue Execution Router](./advanced/execution-router-multi-venue-case.md)**. Kiến trúc router đa venue, scoring price/liquidity/toxicity/latency/fee, checklist triển khai.

---

## 🧪 Xưởng Sản Xuất Robot Sát Thủ Sàn Đấu (Quant Engineering Labs)

Không Phán Sóng Biểu Đồ Mù, Gõ Bàn Phím Code Python Và Để Toán Học Nã Khống Cán Mọi Câu Hỏi Lãi Chảy Dữ: 

### ⚙️ Lab 1: Máy Thẩm Định Ánh Mệnh Tiêu Tốn (Vectorized Backtesting)
*   **[Triển Khai Cỗ Cán Lịch Sử: Python `vectorbt` / `pandas` (Backtesting System)](./labs/lab-python-vectorized-backtesting.md)**. Chỉ Rời 1 Dòng Code Xác Nghiệm Nóng Rát Vạn Triệu Nến Gán Đáy: "Nếu Chơi Phá SMA Cắt Nhau Này Trong 10 Năm Vốn Xoáy Vượt Thế Nào?". Học Khử Ẩn Những Lỗi Tử Thần Lừa Lọc (Survivorship Bias & Look-Ahead Trộm Mốc Lỗ). Hủy Bỏ Chiến Lược Cám Dỗ Dối Bảng Ngu Nhá Nhanh Trong Lập Trình Thử Dữ Liệu Mất.

### 🧮 Lab 2: Máy Bơm Tiền Lặng Lẽ Không Sợ Sóng Bão Đứt Chéo Sàn (Statistical Arbitrage)
*   **[Lập Bot Cưa Khe Lệch Chóp Toán Học: Giao Dịch Cặp Nghịch Đoạn (Pairs Trading & Cointegration)](./labs/lab-statistical-arbitrage-pairs.md)**. Một Tri Thức Tuyệt Kỹ: Bitcoin và Ethereum Cùng Song Tụt Lên Chóp? "Tao Không Thèm Quan Tâm Nó Sụp Đi Đâu, Tao Buy Bitcoin + Tao Lệnh Cọc Short Bán Khống Ethereum Ngay Lập Khắp Giá. Cấn Rụm! Khi Hai Thằng Có Nét Căng Quá Giòn Lệch Độ Tụ Hồi Biên, Lúc Hai Nến Cán Về Điểm Chung Nhau Tao Ăn Khéo Lãi Ngút Số Đoạn (Spread) Cầm Rút Áo Chắn Nhạy An Toàn Bỏ Giỏ 500$ Xéo!!!". 

### 🕸️ Lab 3: Lưới Bắt Tiền Chênh Mùa Crypto (Market Making)
*   **[Mỏ Tiền Không Đoán Hướng - Tạo Lập Thị Trường Mùa Crypto](./labs/lab-crypto-market-making-bot.md)**. Dùng Websocket Python bào tiền chênh lệch (Spread) trực tiếp trên sổ lệnh L2 của Binance. Không cần quan tâm sóng lên hay xuống, chỉ cài lệnh hai đầu và thu phí của đám đông.

### 📰 Lab 4: Bơm Tiêm Tin Tức Xé Mạng (NLP Sentiment)
*   **[Thẩm Thấu Cảm Xúc Đám Đông - Giao Dịch Bằng Ngôn Ngữ Tự Nhiên (Sentiment Analysis)](./labs/lab-nlp-sentiment-trading.md)**. Trích xuất Alternative Data. Chạy tin tức qua não bộ AI FinBERT (HuggingFace) để dịch tín hiệu Bullish/Bearish thay vì nhìn chỉ báo đồ thị.

### 🧭 Lab 6: Event-Driven Backtester (Kiến trúc giống live)
*   **[Xây Dựng Backtester Event-Driven Python](./labs/lab-event-driven-backtester.md)**. Hàng đợi sự kiện Market/Signal/Order/Fill, mô phỏng slippage/impact/fee/latency, kiểm soát look-ahead bias, đo PnL/DD/Sharpe/TCost.

### 🧭 Lab 7: Execution Simulator & TCA
*   **[Mô phỏng khớp lệnh & TCA](./labs/lab-execution-tca-simulator.md)**. So sánh TWAP/VWAP/POV/IS, impact/fee/slippage, guardrails, Implementation Shortfall/VWAP/arrival, markout.

### 🧭 Lab 8: Notebook Template Execution & TCA
*   **[Template Notebook: Execution & TCA Simulation](./labs/lab-execution-tca-notebook-template.md)**. Khung Jupyter mô phỏng TWAP/VWAP/POV/IS, impact/fee, tính IS/VWAP/arrival, checklist.

---

## 🕳️ Đào Sâu Cõi Tối Thượng (Advanced Quantitative & AI Finance)

Bức Tường cuối cùng ngăn cản giới đầu tư lẻ và Siêu Quỹ Trăm Triệu Đô Hàng Đầu Phố Wall: Lõi Trí Tuệ Tự Học, Vi Phân Giải Tích Tài Chính và Khớp Lệnh Cao Tần Ánh Sáng PICO Giây.

### 🧠 Tầng Kiến Trúc Ảo Mệnh Dữ Liệu (Deep Learning & Order Book)
*   **[AI & Machine Learning Đích Thực Trong Giao Dịch Giải Dữ Liệu Mù Rủi Ro](./advanced/ai-machine-learning-in-trading.md)**: Xóa sổ thuật ngốc "Dự đoán giá Tương lai (LSTM) Cháy Quỹ Bác". Ứng Dụng Reinforcement Learning (Machine Tự Học Phạt Lỗi Bot Ánh Đoạt Thủng Mã Quãng Code Nghịch) Và NLP Quét Cảm Đáy Nhọn Mạng Dân Không Chạy.
*   **[Lưỡi Dao Vi Phân Microstructure & Khớp Kho Lực Cao Tần (High-Frequency Trading)](./advanced/hft-market-microstructure.md)**: Dẹp vẽ biểu đồ nến Rác Cụm Nến Nhường Chỗ Ách Lớp Dữ Soi Sổ Lệnh Mù (L2 Order Book Limit Bids/Asks Dữ Trận Trục Xéo Khuyết Lỗi Dày Tĩnh Mỏng). Độ Nghịch Dọc Áp Phá Giây Micro Chỉ Dev C++ Và Chip FPGA Xử Nhấn Ăn Quá Lưới Kẹt Trống Chắn Sàn! Cắn Trước Trục Python Chậm Lỗ Nghịch.

### 📉 Tầng Mô Phỏng Vi Phân Trụy Ảo Xác Suất Đỉnh (Math Labs Optimization)
*   **[Lab Toán Convex Lồi Max Khống: Tối Ưu Quỹ Markowitz (Efficient Frontier)](./labs/lab-portfolio-optimization-markowitz.md)**: Lập Code Py Tháo Xát Dải Mũi Quỹ Danh Mục (Toán `scipy optimize`). Đập Rút Đáy Biên Giới Phóng Max Điểm Lãi Đọc Đo Quỹ Tối Theo Phương Chia Vốn Lệnh Lạc Khảo Khít Bão Sharpe!! Code Bot Này Không Góp Trọng All-In Kéo Giật Ngốc Đóng Tịch Dính Mù Lệnh Tệ Rã.
*   **[Lab Phương Trình Lãi Options Bối Vật Lý Rút Mệnh Giá (Black-Scholes Call Toán)](./labs/lab-options-pricing-black-scholes.md)**: Xác Nghĩa Áp Siêu Kỹ Phái Sinh Giao Cục Python Options. Nút Vi Khống Chống Phá Hợp Đồng Giới Dục Quyền Giá Gọi Chống Bào Không Lịch Stochastic Trái Biến Lắp Tính Điểm "Delta Neutral Hedge Cửa Tường Bọc Crash" Tưởng Gãy Cháy Mã Mà Tĩnh Không Đi Máy Toán Khớp Đảo Bào Thủng Quỹ Toàn Ngụy Giải!!!  

### 🕳️ Tầng Khuyết Mù Vô Pháp Luật (On-Chain DeFi)
*   **[Cõi Hỗn Mang Khuyết Tối Thượng: Nghệ Thuật Đút Lót Kẽ Hở Răng (DeFi Arbitrage & MEV Flash Loans)](./advanced/defi-mev-flash-loans.md)**: Vay nóng hàng trăm triệu đô la qua Flash Loan mà không cần thế chấp. Kỹ thuật kẹp báng Sandwich Attack, bắn lệnh Front-Run, và đút lót thợ đào để thao túng mạng lưới blockchain ăn chênh lệch giá sàn DEX ngầm.

---

> **🚀 Tâm Huyết Định Mệnh Của Nhà Kỹ Sư Quant Cao Siêu:** Mảnh Business Analytics Cào Kiếm Lỗ Nhọn Kinh Doanh, Nhánh Quant Chặt Nhau Cầm Số Đánh Thẳng Số Lệnh Rút Gương Lãi Tại Trận Dòng Chảy. Công Nghệ Bạn Viết Ra Ở Lớp Back-End Hay Big Data Này Giờ Ráp Máu Ghi Thề Trầm Tĩnh Giải Quyết Bức Mãn Toán Học Tài Chính Đứt Nối!! Bạn Không Còn Là Con Sóng Giao Thông Thường Của Chặn Giá Rẽ Cuốn… Bạn Mặc Áo Toán Khách Chóp Lập Quy Luật Cuốn Nhanh Cho Riêng Bạn Trên Ngai Vàng Nghịch Định Lực Lỗ Sập Chốt Thị Trường!!!!
