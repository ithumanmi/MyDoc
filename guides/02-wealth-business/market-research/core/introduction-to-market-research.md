# 1. Introduction to Market Research

> [← Back to Market Research](./README.md)

## Tại sao Market Research quan trọng?

Nghiên cứu thị trường không chỉ là việc xem đối thủ làm gì. Nó là la bàn giúp bạn:
*   **Giảm rủi ro:** Tránh làm ra sản phẩm không ai cần.
*   **Tiết kiệm nguồn lực:** Tập trung vào tính năng users thực sự muốn.
*   **Tìm cơ hội:** Phát hiện những ngách thị trường chưa được phục vụ tốt.

## Các phương pháp nghiên cứu

### 1. Định lượng (Quantitative Research)
*   **Là gì:** Số liệu, thống kê, khảo sát diện rộng.
*   **Trả lời câu hỏi:** "Bao nhiêu?", "Tần suất như thế nào?".
*   **Ví dụ:**
    *   Dùng Google Trends xem xu hướng tìm kiếm từ khóa.
    *   Xem doanh thu ước tính trên Sensor Tower.
    *   Chạy khảo sát (Survey) với 1000 người.

### 2. Định tính (Qualitative Research)
*   **Là gì:** Phỏng vấn sâu, quan sát hành vi, đọc review.
*   **Trả lời câu hỏi:** "Tại sao?", "Như thế nào?".
*   **Ví dụ:**
    *   Đọc 100 review 1 sao của đối thủ để tìm nỗi đau (pain points).
    *   Phỏng vấn trực tiếp 5 khách hàng tiềm năng.
    *   Tham gia Discord community để hiểu văn hóa người dùng.

## Công cụ cần thiết (Tools) & Hướng dẫn sử dụng

### 1. Game Dev Tools

#### **SteamDB (Steam Database)**
*   **Website:** [steamdb.info](https://steamdb.info/)
*   **Free vs Paid:** Hoàn toàn miễn phí.
*   **Must-Watch Metrics:**
    *   **CCU (Concurrent Users):** Số người chơi cùng lúc.
        *   *Ý nghĩa:* Game có giữ chân người chơi tốt không? Nếu CCU cao nhưng sales thấp -> Game hay nhưng marketing kém (Cơ hội cho bạn).
    *   **Followers:** Số người theo dõi game.
        *   *Công thức:* **1 Follower ≈ 2-3 Wishlists**. Dùng chỉ số này để ước tính wishlist của đối thủ.
    *   **Review Score:** % đánh giá tích cực.
        *   *Chuẩn:* > 90% là xuất sắc (Overwhelmingly Positive). < 70% là có vấn đề nghiêm trọng (Mixed).

#### **Gamalytic / VGInsights**
*   **Website:** [gamalytic.com](https://gamalytic.com/)
*   **Chức năng:** Ước tính doanh thu (Revenue Estimate).
*   **Cách dùng:**
    1.  Nhập tên game đối thủ.
    2.  Xem **Box Office**: Gross Revenue, Net Revenue (sau khi trừ phí Steam & Tax).
    3.  **Quan trọng:** Nhìn vào **Median Revenue** của cả thể loại (Genre) thay vì chỉ nhìn Top 1 game.
    *   *Ví dụ:* Top 1 Survival game kiếm $100M, nhưng Median chỉ là $5k -> Rủi ro cao.

### 2. Mobile App Tools

#### **Sensor Tower / Data.ai (App Annie)**
*   **Free Tier:** Xem Top Charts (Ranking) theo quốc gia và Category.
*   **Cách dùng hiệu quả (Free):**
    *   Đổi Store sang US/UK/JP để xem trend thế giới.
    *   Xem **"Top Grossing"** (Doanh thu cao nhất) để biết mô hình monetization nào đang thắng thế (IAP vs Sub).
    *   Xem lịch sử update version: Đối thủ update tính năng gì gần đây? -> Đó là tính năng user đang cần.

### 3. General Tools

#### **Google Trends**
*   **Cách dùng:** So sánh 2-3 từ khóa (VD: "Roguelike" vs "Metroidvania").
*   **Bộ lọc:** Chọn "Worldwide" và "Past 5 years" để thấy xu hướng dài hạn (Trend) hay chỉ là nhất thời (Fad).

---

## ⚖️ Data Ethics (Đạo đức dữ liệu)

Khi nghiên cứu thị trường, hãy tuân thủ các nguyên tắc sau:

1.  **Public Data Only:** Chỉ thu thập dữ liệu công khai (Publicly available). Không hack, không xâm nhập database nội bộ.
2.  **Tôn trọng Privacy:** Khi phỏng vấn hoặc khảo sát, hãy che tên/thông tin cá nhân của người tham gia (Anonymize data).
3.  **Scraping:** Nếu dùng tool cào dữ liệu (scraping), hãy tôn trọng `robots.txt` của website và không làm sập server của họ (Rate limit).
4.  **Luật pháp:** Tuân thủ GDPR (Châu Âu) hoặc các luật bảo vệ dữ liệu sở tại nếu bạn lưu trữ thông tin người dùng.
