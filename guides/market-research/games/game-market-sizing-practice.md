# 🧮 Game Market Sizing Practice (TAM/SAM/SOM)

> [← Back to Game Market Research](./game-market-research.md) | [Back to Main](./README.md)

Hướng dẫn từng bước (Step-by-step) để tính toán quy mô thị trường cho một dự án Game cụ thể. Chúng ta sẽ dùng dữ liệu thật từ Steam để làm ví dụ.

---

## 1. Case Study: "Cozy Farming Sim" (PC/Steam)

Giả sử bạn muốn làm một game nông trại thư giãn (giống *Stardew Valley* hay *Coral Island*) và muốn biết thị trường này còn kiếm ăn được không.

### Bước 1: Define the Genre & Tags (Định nghĩa Thể loại)
Đừng tìm chung chung là "Simulation". Hãy cụ thể hóa bằng Steam Tags:
*   **Core Tags:** `Farming Sim`, `Life Sim`, `Cozy`, `Cute`.
*   **Platform:** PC (Steam).
*   **Timeframe:** 3 năm gần nhất (để dữ liệu không bị lỗi thời).

### Bước 2: Gather Raw Data (Thu thập dữ liệu thô)
Sử dụng **VGInsights** hoặc **Gamalytic** (bản Free) để lọc:
1.  Vào [VGInsights Explore](https://vginsights.com/games-database).
2.  Filter: Tag = `Farming Sim` AND `Cozy`.
3.  Release Date: From `01/01/2021` to `Now`.
4.  Revenue: `> $10,000` (Để loại bỏ game rác/hobby projects).

### Bước 3: Calculate TAM (Total Addressable Market)
**TAM = Tổng doanh thu của TẤT CẢ game trong niche này (Global).**
*   *Giả sử:* VGInsights tìm được 200 game thỏa mãn điều kiện trên.
*   Tổng doanh thu (Total Revenue) của 200 game này = **$500 Triệu USD**.
*   -> **TAM = $500M**. (Đây là miếng bánh mơ ước nếu bạn độc quyền thị trường).

### Bước 4: Calculate SAM (Serviceable Addressable Market)
**SAM = TAM - (Outliers + Platform không với tới).**
*   **Loại bỏ Outliers (Kẻ khổng lồ):**
    *   *Stardew Valley* kiếm $100M? -> Bỏ ra. Nó là huyền thoại, bạn không thể so sánh với nó.
    *   *Coral Island* kiếm $50M? -> Bỏ ra (nếu bạn là team nhỏ không có vốn $2M để làm art xịn như họ).
    *   *Disney Dreamlight Valley*? -> Bỏ ra (IP lớn).
*   **Thị trường mục tiêu thực tế:**
    *   Chỉ tính các game Indie có team size tương đương bạn (1-5 người).
    *   Chỉ tính các game có đồ họa Pixel Art (nếu bạn làm Pixel Art).
*   *Tính lại:* Sau khi loại bỏ Top 5 game lớn nhất, tổng doanh thu còn lại của 195 game kia là **$50 Triệu USD**.
*   -> **SAM = $50M**. (Đây là thị trường thực tế mà các game Indie đang cạnh tranh).

### Bước 5: Calculate SOM (Serviceable Obtainable Market)
**SOM = Mục tiêu thị phần của BẠN.**
*   Bạn có ngân sách Marketing bao nhiêu?
    *   *Ít ($0 - $1k):* Kỳ vọng chiếm **0.01% - 0.05%** SAM.
    *   *Trung bình ($10k - $50k):* Kỳ vọng chiếm **0.5% - 1%** SAM.
    *   *Cao ($100k+):* Kỳ vọng chiếm **2% - 5%** SAM.
*   *Tính toán:*
    *   Với ngân sách Indie ($5k marketing), bạn đặt mục tiêu **0.5% SAM**.
    *   SOM = $50,000,000 * 0.5% = **$250,000**.
*   **Kết luận:** Nếu làm tốt, game của bạn có thể kiếm được **$250k** (doanh thu trọn đời - Lifetime Revenue).
    *   Sau khi trừ phí Steam (30%), Tax (10%), Refund (10%) -> Bạn cầm về tay khoảng **50%** (~$125k).
    *   Chia cho team 2 người làm trong 2 năm -> Mỗi người kiếm được **$31k/năm** (~60tr VNĐ/tháng).
    *   -> **Dự án KHẢ THI (Feasible).**

---

## 2. Excel Template (Mẫu tính nhanh)

Copy bảng này vào Excel để tự tính cho game của bạn:

| Hạng mục | Công thức | Ví dụ (Farming Sim) | Dự án của Bạn |
| :--- | :--- | :--- | :--- |
| **1. Tổng số Game (Niche)** | Tìm trên VGInsights | 200 games | ... |
| **2. Tổng Doanh thu (TAM)** | Sum revenue | $500,000,000 | ... |
| **3. Doanh thu Top 1-5 (Outliers)** | Sum top 5 | $450,000,000 | ... |
| **4. Thị trường Indie (SAM)** | (2) - (3) | **$50,000,000** | ... |
| **5. Mục tiêu Thị phần (Share)** | Dựa trên Budget | 0.5% | ... |
| **6. Doanh thu Mục tiêu (SOM)** | (4) * (5) | **$250,000** | ... |
| **7. Thực nhận (Net Revenue)** | (6) * 50% | **$125,000** | ... |
| **8. Chi phí Sản xuất (Cost)** | Lương + Outsource | $50,000 | ... |
| **9. Lợi nhuận (Profit)** | (7) - (8) | **$75,000** | ... |
| **10. ROI (Return on Investment)** | (9) / (8) | **150%** | ... |

---

## 3. Data Source Checklist (Nguồn dữ liệu)

Để điền vào bảng trên, hãy dùng các công cụ sau:

1.  **[VGInsights](https://vginsights.com/) (Khuyên dùng):**
    *   *Free:* Xem được doanh thu ước tính, số lượng game, biểu đồ trend.
    *   *Paid:* Xem chi tiết từng game nhỏ.
2.  **[Gamalytic](https://gamalytic.com/):**
    *   *Free:* Tốt nhất để xem doanh thu từng game lẻ. Thuật toán khá chính xác cho game Indie nhỏ.
3.  **[SteamDB](https://steamdb.info/):**
    *   Dùng để xem CCU (Concurrent Users) và Follower count.
4.  **[SteamSpy](https://steamspy.com/):**
    *   Cổ điển, nhưng vẫn tốt để xem phân bố Owners.

---

## 4. Case Study: MMORPG (The Hard Mode)

MMORPG là thể loại rủi ro nhất. Nếu bạn tính toán sai, bạn sẽ phá sản trước khi game ra mắt.

### Vấn đề "The Big 5"
Nếu bạn search `Tag: MMORPG` trên Steam, doanh thu sẽ là hàng tỷ đô la. Nhưng đó là con số vô nghĩa với bạn.
*   **TAM ảo:** Bao gồm *Final Fantasy XIV, Elder Scrolls Online, Black Desert*.
*   **Thực tế:** Bạn không thể cạnh tranh với họ. Người chơi của họ sẽ không bỏ game để chơi game Indie của bạn đâu.

### Tính SAM cho Indie MMORPG (Pixel/Low Poly)
Hãy lọc kỹ hơn:
*   **Tags:** `MMORPG` + `Indie` + `Pixel Graphics` (hoặc `2D`).
*   **Loại bỏ:** Các game có IP lớn hoặc Budget > $10M.
*   **Comparable Titles (Game tham chiếu):**
    *   *Realm of the Mad God* (Bullet Hell MMO).
    *   *Heartwood Online* (Mobile/PC cross-play).
    *   *PokeMMO* (Dù không trên Steam nhưng là ví dụ điển hình).
    *   *Curse of Aros*.
*   **SAM Thực tế:** Thường chỉ khoảng **$5M - $10M** doanh thu hàng năm cho toàn bộ ngách Indie MMO.

### Tính SOM & Chi phí Server (Quan trọng)
Với MMO, doanh thu (Revenue) không quan trọng bằng Lợi nhuận (Profit) vì chi phí duy trì (Maintenance) cực cao.

| Hạng mục | Indie Single-player | Indie MMORPG |
| :--- | :--- | :--- |
| **Doanh thu (Year 1)** | $100,000 | $100,000 |
| **Phí Steam/Tax** | -$50,000 | -$50,000 |
| **Server Cost (AWS/PlayFab)** | $0 | **-$20,000** (Dự kiến) |
| **LiveOps Team (GM/Support)** | $0 | **-$30,000** (Cần người trực 24/7) |
| **Lợi nhuận thực** | **$50,000** | **$0 (Hòa vốn)** |

-> **Kết luận:** Làm MMORPG cần vốn (Runway) gấp 3-5 lần game thường. Nếu SOM dự kiến < $500k/năm -> **Đừng làm.**

---

## 5. Case Study: Casual Mobile Game (Hybrid-Casual)

Khác với Steam (mua 1 lần), thị trường Casual Mobile sống nhờ Quảng cáo (Ads) và IAP. Công thức tính toán hoàn toàn khác.

### The Metric Shift (Chuyển dịch Chỉ số)
Bạn không quan tâm đến "Unit Sold". Bạn quan tâm đến:
*   **LTV (Lifetime Value):** Giá trị vòng đời 1 user.
*   **CPI (Cost Per Install):** Chi phí để có 1 user.
*   **Profit = (LTV - CPI) * Volume.**

### Bước 1: Xác định Niche (Hyper vs Hybrid)
*   *Hyper-casual:* Gameplay siêu đơn giản, chơi 1 tay, đồ họa basic. (VD: *Helix Jump*). -> Cạnh tranh cực cao, LTV thấp ($0.2).
*   *Hybrid-casual:* Gameplay đơn giản nhưng có hệ thống nâng cấp/item như RPG. (VD: *Archero, Survivor.io*). -> LTV cao hơn ($1.0 - $5.0).
*   *Case Study:* Game "Merge Puzzle" (Kết hợp nông trại).

### Bước 2: Tính SOM (Volume Calculation)
*   **TAM:** Hàng tỷ người dùng smartphone.
*   **SAM:** Người chơi Puzzle ở Tier 1 Countries (US, UK, CA, JP).
*   **SOM:** Khả năng chạy Ads của bạn.
    *   Giả sử ngân sách test: **$5,000**.
    *   CPI mục tiêu: **$0.50**.
    *   Số lượng Users (Installs) = $5,000 / $0.50 = **10,000 users**.

### Bước 3: Dự tính Doanh thu (Ad Revenue Calculator)
Sử dụng công thức: `Revenue = DAU * Impressions/User * eCPM / 1000`

| Metric | Giá trị (Ước tính) | Giải thích |
| :--- | :--- | :--- |
| **Installs** | 10,000 | Số user mua được. |
| **Retention D1** | 40% | 4,000 người quay lại ngày 1. |
| **Ads per User** | 5 | Mỗi người xem 5 cái quảng cáo/ngày. |
| **eCPM (Tier 1)** | $20 | Giá 1000 lần hiển thị quảng cáo (US). |
| **Ad Revenue (Day 1)** | 4,000 * 5 * $20 / 1000 = **$400** | Doanh thu ngày đầu. |

*   **eCPM ($)**: Giá trị này có thể tăng gấp đôi nếu biết cách tối ưu. 👉 **[Xem Hướng dẫn Tối ưu eCPM & Ad Monetization](./ad-monetization-ecpm.md)**.
*   **The CPI Wall:** Nếu game bạn làm ra mà test CPI > $0.50 (cho Hyper-casual) hoặc > $1.50 (cho Hybrid) -> **Game chết (Kill Project)**. Không cần tính TAM/SAM nữa vì càng chạy ads càng lỗ.

### Ad Revenue Calculator Template

Copy bảng này để tự tính doanh thu quảng cáo:

| Metric | Giá trị của bạn | Ghi chú |
| :--- | :--- | :--- |
| **A. Installs / Ngày** | 1,000 | Số lượng User mới (Paid + Organic) |
| **B. Retention D1 (%)** | 40% | Tỷ lệ quay lại ngày 1 |
| **C. DAU (Daily Active Users)** | = A * (1 + B + ...) | Công thức đơn giản: ~ Installs * 2.5 |
| **D. Impressions / User** | 5 | Số ads trung bình 1 user xem |
| **E. eCPM ($)** | $15 | Giá ads (US: $15-$25, Global: $5-$10) |
| **F. Doanh thu ngày** | = C * D * E / 1000 | **Tiền về túi** |

---

## 6. Cạm bẫy cần tránh (Common Pitfalls)

*   **Ảo tưởng sức mạnh:** Đừng bao giờ lấy doanh thu của *Hollow Knight* hay *Stardew Valley* làm mốc tham chiếu. Hãy nhìn vào game **Top 50 - Top 100** trong niche đó. Đó là nơi bạn có khả năng thuộc về nhất.
*   **MMO Curse:** Với MMORPG, **CCU < 100** là game chết (Dead Game). Không ai muốn chơi một game online vắng tanh. Bạn cần ngân sách Marketing khổng lồ ngay ngày đầu (Day 1) để lấp đầy server.
*   **Quên trừ chi phí:** Doanh thu $100k nghe to, nhưng trừ phí Steam, Thuế, Publisher share... thì về túi chỉ còn một nửa.
*   **Chọn sai Niche:** Nếu SAM quá bé (VD: Puzzle Game cho người mù màu), dù bạn chiếm 100% thị phần cũng không đủ sống.
