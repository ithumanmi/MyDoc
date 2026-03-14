# 3. Game Market Research (Deep Dive)

> [← Back to Market Research](./README.md)

## Phân tích thị trường trên Steam

### 1. Sử dụng SteamDB
*   **Theo dõi "Upcoming" tab:** Xem các game sắp ra mắt cùng thể loại.
*   **Follower Count:** Số lượng follower là chỉ số quan trọng dự báo doanh số (Conversion rate thường là 1 follower ~ 2-3 sales năm đầu).
*   **Concurrent Users (CCU):** Xem game có giữ chân người chơi tốt không.

### 2. Sử dụng Gamalytic / VGInsights
*   **Ước tính Revenue:** Xem các game Indie trong niche của bạn kiếm được bao nhiêu.
    *   *Lưu ý:* Đừng chỉ nhìn top 1%. Hãy nhìn **Median** (Trung vị) để có kỳ vọng thực tế.
*   **Review Analysis:** Đọc review để hiểu "Why they buy".

### 3. Tìm "Blue Ocean" (Đại dương xanh)
*   **Red Ocean (Đỏ):** Thị trường cạnh tranh khốc liệt (Ví dụ: 2D Platformer, Puzzle đơn giản).
*   **Blue Ocean (Xanh):** Thị trường ngách, ít đối thủ nhưng nhu cầu cao.
    *   *Cách tìm:* Kết hợp 2 Genre lạ (Ví dụ: Roguelike + Poker = Balatro).
    *   *Cách tìm:* Phục vụ một nhóm đối tượng cụ thể (Ví dụ: Game mô phỏng lái xe tải cho người thích chill).

### 4. Tính toán Quy mô Thị trường (TAM/SAM/SOM)
*   Để có con số cụ thể về doanh thu tiềm năng, hãy xem hướng dẫn thực hành chi tiết:
    *   👉 **[Game Market Sizing Practice](./game-market-sizing-practice.md)** (Hướng dẫn từng bước với số liệu Steam thực tế).

---

## Phân tích thị trường Mobile (tóm tắt)

- **ASO (App Store Optimization):** Nghiên cứu keyword mà đối thủ đang rank top.
- **Top Charts:** Xem xu hướng game Hyper-casual hay Hybrid đang lên ngôi.
- **Creative Analysis:** Xem quảng cáo của đối thủ (TikTok/Meta Ads Library) để biết họ đánh vào tâm lý gì.

> Chi tiết: xem **[Mobile Game Market Research](./mobile-game-market-research.md)** (ASO cho game, creative analysis, genre lifecycle hyper vs hybrid, benchmark CPI/LTV, link sizing practice & ad monetization).

## Genre Analysis Framework (Khung Phân Tích Thể Loại)

Trước khi bắt đầu, hãy tự hỏi: **Thị trường này đang ở giai đoạn nào?**

### Ma trận Thị trường (Market Matrix)

| Giai đoạn | Đặc điểm | Chiến lược phù hợp |
| :--- | :--- | :--- |
| **Emerging (Mới nổi)** | Cung < Cầu. Ít đối thủ. | **Speed is key:** Ra mắt nhanh để chiếm thị phần. (VD: Vampire Survivors clones năm 2022). |
| **Growing (Tăng trưởng)** | Cung ≈ Cầu. Đối thủ bắt đầu xuất hiện nhiều. | **Innovation:** Cải tiến gameplay, thêm tính năng mới. |
| **Mature (Trưởng thành)** | Cung > Cầu. Nhiều đối thủ lớn (Big players). | **Niche Down:** Tập trung vào ngách nhỏ, phục vụ fan cứng (Hardcore). |
| **Declining (Thoái trào)** | Cung >> Cầu. Người chơi chán nản. | **Avoid:** Tránh xa, trừ khi bạn có ý tưởng đột phá hoàn toàn. |

### Trend vs Fad (Xu hướng vs Nhất thời)
*   **Trend (Xu hướng dài hạn):** Tăng trưởng bền vững (VD: Roguelike, Cozy Games). An toàn hơn để đầu tư.
*   **Fad (Nhất thời):** Bùng nổ nhanh rồi tắt ngúm (VD: NFT Games, Only Up clones). Rủi ro cao nếu bạn chậm chân.
*   **Cách phân biệt:** Dùng Google Trends xem biểu đồ 5 năm. Trend đi lên từ từ. Fad là đường thẳng đứng rồi rơi tự do.

---

## 🔬 Case Studies (Phân tích thực tế)

Chúng ta hãy áp dụng Framework để phân tích 2 ví dụ điển hình:

### Case Study 1: Vampire Survivors (The Trendsetter)
*   **Genre:** Reverse Bullet Hell / Roguelite.
*   **Bối cảnh (2021):**
    *   Thị trường PC chưa có game nào khai thác tốt cơ chế "tự động đánh + di chuyển né đạn" (dù Mobile đã có Magic Survival).
    *   Nhu cầu "game giải trí nhanh, giá rẻ, gây nghiện" đang cao sau đại dịch.
*   **Market Strategy:**
    *   **Blue Ocean:** Tạo ra một sub-genre mới trên Steam.
    *   **Pricing:** $3 (Cực rẻ) -> Rào cản mua bằng 0 -> Viral nhanh.
    *   **Gameplay Loop:** Cực kỳ đơn giản nhưng thỏa mãn (Dopamine hit liên tục).
*   **Kết quả:** Doanh thu hàng chục triệu đô, mở ra kỷ nguyên "Survivor-likes".

### Case Study 2: Balatro (The Innovator)
*   **Genre:** Roguelike Deckbuilder (Thẻ bài).
*   **Bối cảnh (2024):**
    *   Thị trường Roguelike Deckbuilder đã **Bão hòa** (Red Ocean) với Slay the Spire clones.
    *   Người chơi cần một luồng gió mới, không muốn chơi lại lối mòn Fantasy đánh quái.
*   **Market Strategy:**
    *   **Innovation:** Kết hợp Poker (cực kỳ quen thuộc) + Roguelike mechanic.
    *   **Theme:** Khác biệt hoàn toàn (Casino, Psychedelic) so với Fantasy truyền thống.
    *   **Audience:** Thu hút cả fan Poker lẫn fan Roguelike.
*   **Kết quả:** 1 triệu bản bán ra trong tháng đầu tiên.
*   **Bài học:** Trong thị trường đỏ (Red Ocean), sự sáng tạo lai tạo (Hybrid Innovation) là chìa khóa.

---

## Phân tích thị trường Mobile
