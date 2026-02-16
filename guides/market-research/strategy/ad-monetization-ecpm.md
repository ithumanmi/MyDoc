# 💸 Ad Monetization & eCPM Optimization Guide

> [← Back to Game Market Research](./game-market-research.md) | [Back to Main](./README.md)

Làm game Mobile không chỉ là làm game hay, mà còn là **nghệ thuật bán quảng cáo**. Nếu bạn tối ưu eCPM tốt, bạn có thể kiếm gấp đôi đối thủ dù có cùng lượng người chơi.

---

## 1. Các thuật ngữ cơ bản (Definitions)

### **eCPM (effective Cost Per Mille)**
*   **Là gì:** Số tiền bạn kiếm được cho mỗi 1,000 lần hiển thị quảng cáo.
*   **Công thức:** `(Tổng Doanh Thu / Tổng Số Lần Hiển Thị) * 1000`.
*   **Tại sao quan trọng:** Nó phản ánh **chất lượng** quảng cáo và **giá trị** người dùng của bạn. User ở Mỹ (Tier 1) có eCPM $20-$30, user ở Việt Nam (Tier 3) có eCPM $1-$5.

### **Fill Rate (Tỷ lệ lấp đầy)**
*   **Là gì:** Tỷ lệ số lần quảng cáo được hiển thị thành công / số lần ứng dụng yêu cầu quảng cáo.
*   **Mục tiêu:** > 95%. Nếu thấp hơn, nghĩa là bạn đang mất tiền vì không có quảng cáo để hiện.

---

## 2. Ad Formats & eCPM Tiers (Các loại quảng cáo)

Không phải quảng cáo nào cũng có giá như nhau.

### **1. Rewarded Video (Video trả thưởng) - 👑 KING**
*   **Cơ chế:** User **chủ động** bấm xem để nhận quà (Hồi sinh, x2 vàng, Item).
*   **eCPM:** Cao nhất ($15 - $30+ ở Tier 1).
*   **Ưu điểm:** User không ghét, thậm chí thích xem. Retention không bị ảnh hưởng.

### **2. Interstitial (Quảng cáo xen kẽ)**
*   **Cơ chế:** Tự động hiện lên khi chuyển màn chơi hoặc hết level. Bắt buộc xem 5s rồi mới tắt được.
*   **eCPM:** Trung bình ($5 - $15).
*   **Nhược điểm:** Gây ức chế. Nếu hiện quá nhiều -> User xóa game.

### **3. Banner / Native Ads**
*   **Cơ chế:** Dải quảng cáo nhỏ ở đáy màn hình.
*   **eCPM:** Rất thấp ($0.2 - $1.0).
*   **Lời khuyên:** Chỉ dùng cho App (Utilities). Với Game, nó làm xấu giao diện và kiếm không bao nhiêu.

---

## 3. The Waterfall Model vs Bidding (Cơ chế đấu giá)

Làm sao để bán quảng cáo với giá cao nhất?

### **Waterfall (Cổ điển)**
Bạn xếp hàng các mạng quảng cáo (Ad Networks) theo thứ tự ưu tiên:
1.  **Facebook Audience Network:** "Mày có mua với giá $20 không?" -> Không.
2.  **AdMob:** "Mày có mua với giá $15 không?" -> Không.
3.  **Unity Ads:** "Mày có mua với giá $10 không?" -> Có -> **Hiển thị**.
*   *Nhược điểm:* Chậm, có thể mất lượt hiển thị giá cao từ mạng xếp sau.

### **In-App Bidding (Hiện đại)**
Tất cả các mạng (Facebook, AdMob, Unity, AppLovin) đấu giá **cùng một lúc** trong thời gian thực. Ai trả cao nhất thì được hiện.
*   *Lợi ích:* Tối đa hóa doanh thu (ARPDAU tăng 10-30%).

---

## 4. Chiến lược Tối ưu eCPM (Optimization Strategies)

### **1. Sử dụng Mediation Platform (Nền tảng trung gian)**
Đừng chỉ gắn mỗi Google AdMob SDK. Hãy dùng **Mediation** để đấu giá nhiều mạng cùng lúc.
*   **AppLovin MAX:** Tốt nhất cho Game Casual hiện nay.
*   **IronSource (Unity LevelPlay):** Mạnh về game Hyper-casual.
*   **Google AdMob Mediation:** Ổn định, dễ dùng.

### **2. Thiết lập Floor Price (Giá sàn)**
*   Đừng bán rẻ. Hãy set giá sàn (ví dụ: $5).
*   Nếu mạng quảng cáo trả < $5 -> Không cho hiện.
*   *Mẹo:* Chia làm nhiều tầng (Multi-floor):
    *   Tầng 1: Giá $20 (High value).
    *   Tầng 2: Giá $10.
    *   Tầng 3: Giá $5.
    *   Tầng 4: All prices (Để vớt vát Fill rate).

### **3. User Segmentation (Phân loại người dùng)**
*   **Nhóm Whales (Nạp tiền):** Tắt hoàn toàn Interstitial Ads. Chỉ để Rewarded Video. Đừng làm phiền họ, họ là nguồn sống chính.
*   **Nhóm Free User:** Hiện nhiều Ads hơn để bù chi phí server.
*   **Nhóm New User (Ngày 1):** Hạn chế Ads để họ không xóa game sớm. Sau ngày 3 mới bắt đầu tăng tần suất Ads.

### **4. Ad Quality (Chất lượng quảng cáo)**
*   Chặn các quảng cáo lừa đảo, cờ bạc, 18+ hoặc quảng cáo của... đối thủ trực tiếp.
*   Quảng cáo chất lượng kém làm user khó chịu -> Xóa game -> Mất LTV.
