# Lab: Thẩm Thấu Cảm Xúc Đám Đông - Giao Dịch Bằng Ngôn Ngữ Tự Nhiên (NLP Sentiment)

> [← Back to Quantitative Trading Hub](../README.md)

Chào Mừng Kẻ Thao Túng Tâm Lý Đám Đông. Giá Dầu Giảm Khắp Nơi Không Vì Biểu Đồ Kỹ Thuật MACD Cắt Chéo Cắt Dọc Rác Rưởi Nào Cả, Mà Do Thống Đốc FED Vừa Phát Biểu Một Câu "Diều Hâu" Trên Kênh Truyền Hình Bloomberg Xé Rách Cơn Mơ Của Lãi Suất.

Thao Túng Cảm Xúc Lập Trình Python: **Alternative Data (Dữ Liệu Thay Thế)**. Nơi Dân Quant Bóc Tách Tweets, Tin Tức Nóng, Báo Cáo Tài Chính (10-K, 10-Q), Phân Tích Nó Qua AI (Mạng Nơ-ron NLP), Ra Tín Hiệu Long/Short Siêu Tốc Độ!

---

## 🗞️ 1. Não Bộ Xếp Lớp Ngữ Nghĩa: FinBERT Đọc Hiểu Tài Chính Máy Não

Cào Dữ Liệu (Scraping) Không Khó, Nhét Nó Vào Não Máy Tính Mà Bắt Nó Hiểu Mới Đắng Cay.
*   **"Táo rớt giá kinh hoàng"**: Mô hình BERT chung (Google) có thể xếp loại Negative (Tiêu cực) về một vụ thu hoạch trái cây.
*   **"Apple Inc. rớt giá cổ phiếu kinh hoàng"**: Mô hình **FinBERT** (Đào tạo chuyên biệt bằng Hàng Triệu Văn Bản Wall Street) Hiểu Chính Xác Đây Là Thảm Họa Tài Chính Mảng Bearish! Nhấn Bán Khống (Short)!

FinBERT là trái tim cỗ máy mổ xẻ nội tạng tiếng anh tài chính (Sentiment Analysis Engine).

---

## 🐍 2. Code Lab: Bơm Tiêm Tin Tức Vào Tín Hiệu Cược Python 

Chúng ta sẽ không làm cái việc Ngốc Nghếch Tải Data CSV Và Gõ Vài Lệnh Khớp Lằng Nhằng Đồ Thj Nữa!
Bot Này Xài Thư Viện NLP Cực Mạnh `transformers` Hàm Mặt `HuggingFace`. Chích Điểm Ngay.

```python
from transformers import pipeline

# 1. Bật Lò Luyện AI Đọc Hiểu Ngữ Nghĩa Tài Chính: FinBERT Áp Não Dòng Máu Mù!
# Xé Không Thời Gian Load Mô Hình Pre-trained Chuyên Ngành Mạng Quant!
print("🧠 Khởi Động Não Bộ FinBERT...")
finbert_analyst = pipeline(
    "sentiment-analysis", 
    model="ProsusAI/finbert", 
    tokenizer="ProsusAI/finbert"
)

# 2. Xới Data: Chùm Tin Tức Elon Musk & SEC Gửi Về Bot Của Bạn (Từ Twitter/News API)
news_stream = [
    "Tesla Q3 deliveries crushed expectations, setting a new record for the company.", # Gặt Báo Lãi Tốt
    "The SEC is launching a massive investigation into the CEO for market manipulation.", # Lưỡi Liềm Treo Gáy
    "Interest rates remain unchanged this quarter; market shows muted reaction.", # Nghịch Xé Êm Đề
]

# 3. Ép Nhấn FinBERT Hút Não Cắt Rã Lệnh Mức Long/Short
print("\n🚨 Kích Hoạt Cỗ Khớp Tín Hiệu Sentiment Bot:")
for headline in news_stream:
    # FinBERT Quét Ngữ Nghĩa Cắn Điểm 
    result = finbert_analyst(headline)[0]
    
    label = result['label']       # Kết Quả: positive (Bullish) / negative (Bearish) / neutral
    score = result['score'] * 100 # Độ Tự Tin Toán Học Của AI (Confidence)
    
    print(f"\n📰 Tin Nhận: '{headline}'")
    print(f"   => 🔮 Nhận Định Quant: {label.upper()} (Độ Chuẩn Trí Tuệ Xác Nghĩa Cứu Cược: {score:.2f}%)")
    
    # 4. Gắn Cò Lệnh (Execution Order Trigger)
    if label == 'positive' and score > 85.0:
        print("   ✅ Tín Hiệu Lệnh Bót: [ĐÁNH LONG - MUA TESLA]")
    elif label == 'negative' and score > 85.0:
        print("   ❌ Tín Hiệu Lệnh Bót: [THẢ SHORT - BÁN KHỐNG TESLA Đứt Giây Cắt Lịch!]")
    else:
        print("   ⏸️ Tín Hiệu Đứng Giữa: Tụ Lệnh Kẹt (Không Vào Trade Tạp Chủng Đáy Gãy)")

```

### Cơn Ác Mộng Lỗi Thời Kẹt Code Đọc Báo
Đừng Xài Sentiment Vào Mô Hình 1 Giây! Nếu CNBC Đăng Bài: *"Fed Tăng Lãi"*, Giá Có Thể Đã Đi 1 Trăm Pip Trọng Số Xuyên Hầm Tự 30 Giây Trước Đó Rồi!
Thuật Ngốc Gọi Đây Là **"Giao Dịch Tin Trễ (Stale News)"**. HFT Bots Xịn Nó Dùng Tia Laser Microwave Bắn Dữ Liệu FED Từ Washington Về Quỹ Ở Phố Wall Chỉ Mất 5 Mili-Giây! Nên Đừng Mơ Chạy Bot Đọc Báo Để Đánh Dàn Day Trading Chớp Nhóm Nhanh Ở Tin Trì Giao Ké Thời Đại Oạch Nghẽn Bục Python Của Bác Phá Tài Khoản Phá Sản Tức Thì!! 

> **Chân Lý Đạt Chóp Khách Thống Lĩnh Lõi Não Quant:** Kỹ năng Nép Alternative Data (Dữ liệu vệ tinh kho bãi Walmart, Dữ liệu Nạp Rút Chuỗi Khối On-Chain Tương Phản) Xới Nhọn Alpha Tín Hiệu Suy Ngược Này Mới Chính Là Công Khai Rửa Đào Xén Dữ Mảng Khách Không Thấy Bí Quyết Nhặt Bạc Khối To Bất Tận! 🚀
