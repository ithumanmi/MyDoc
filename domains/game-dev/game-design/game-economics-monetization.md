# Game Economics & Monetization (Cân Bằng Tiền Tệ & F2P)

> [← Back to Game Design](../README.md) | [Home](../../../README.md)

Lập trình game hay tới đâu mà "Hệ thống kinh tế" gãy nát, lạm phát siêu mãnh liệt, người cày chay out-trình dân nạp tiền, hoặc Game quá khó ép nạp khiến user chửi bới gỡ App... thì Game chết yểu ở tháng đầu ra mắt. 

Bài viết đào sâu cách design các mô hình "Vắt chanh" tinh tế của dòng Free-to-Play, Life-service.

---

## 💧 1. Nguồn Bơm (Sources) & Bồn Rút (Sinks)

Bất kỳ hệ sinh thái kinh tế nào (như Võ Lâm, Genshin, hay Nông Trại) đều tồn tại Luật Nguồn và Bồn Rút.

### Sources (Vòi xả Tiền/Vàng vào Game)
Dòng vàng được in ra từ server chia làm 2 loại chính tác động KPI:
*   **Active Sources (Chủ động cày):** Giết quái rơi vàng, mở rương, Clear Dungeon. Hành động này yêu cầu User online -> *Mang lại chỉ số CCU, Retention, Time-spend.*
*   **Passive Sources (Thụ động):** Vàng sinh ra khi offline trại khai thác, Daily Quests Login Bonus. -> *Mồi nhử bắt user quay lại (D0, D1, D7 Retention).*

### Sinks (Rút tiền Xóa sổ)
Phải có thứ để Đốt. Nếu không đốt, tiền tích trong acc sẽ đẻ lên 1 Tỷ Vàng. Lạm phát! Game hết ý nghĩa.
*   **Soft Sinks (Tiền tiêu hao liên tục):** Mua máu (Potions), Sửa độ bền vũ khí, Trả phí di chuyển cổng dịch chuyển (Teleport). Vòi tiêu thụ chầm chậm nhịp dốc dốc xuống.
*   **Hard/Progression Sinks (Hố Đen Tiêu Tiền):** Nâng cấp vũ khí (Tỉ lệ xịt 50% đốt mẹ 10 triệu vàng), Đập khảm nạm. Tiến trình đập đồ là cái Sink hoàn hảo nhất lịch sử Game RPG.

**Công thức Cân bằng Tối Thượng:** 
Ở Level trung bình (Ví dụ Lev 30), Lượng Vàng In Ra Gấp 1.2 Lần Lượng Nhỏ Giọt (Bơm nhỉnh hơn Hút hờ hờ, User cảm giác GÀU LÊN TỪ TỪ).
Nhưng chạm Level End-Game (Lev 80). Sink phải phình lên Siêu bự, Hút tiền cực gắt, Vàng bắt đầu thiếu Thốn -> **Đó là điểm Chốt Hạ (Monetization Point) để Kích nạp cào thẻ!**

---

## 🎲 2. Gacha Rate & Pity System (Học Thuyết Máy Bán Hàng)

Game Hàn/Trung/Nhật kiếm Hàng Tỷ đô 1 tháng bằng Cơ chế Gacha (Quay hòm súng, Bóc thẻ bài nhân vật 5 sao). Nếu bạn thả tỷ lệ Real-random 1%, người chơi trượt 300 lần sẽ đi thắt cổ.

### Hệ Thống Pity (Sự Bố Thí Thương Hại)
Đừng tin vào Xác Xuất ngẫu nhiên. Coder phải Fake cái ngẫu nhiên đó vì cảm xúc con người.
*   **Soft Pity (Mồi nhử):** Tỉ lệ nổ 5 Sao gốc là `0.6%`. Từ lần quay hụt thứ 70 trở đi, Coder bắt đầu gian lận tăng ngầm rate lên `20%` ở lần 70, `50%` ở lần 80.
*   **Hard Pity (Cam Kết Tức Thời):** Quay đến lượt thứ 90. Trúng Tướng 5 sao Mặc định 100%. (Mechanic đảm bảo user Nạp đủ cọc tiền Tối Thiểu 100$ luôn mua được 1 Tướng).

### Sức Khỏe Tinh Thần của Whale (Cá Voi)
Cá Voi nạp Vạn Đô. Đừng cho Cá Voi 1 phát Trúng Đích Tướng Xịn ngay ở lần 1 rồi Nghỉ. Hãy băm nhỏ mục tiêu Thành mảnh vỡ (Shards). Cần 1 Mảnh 5 sao để mờ khóa, Và cần **20 Mảnh Đứa Đó giống Hệ Trùng lặp** để đút cho nó ăn Lên Cấp 6 Sao Trắng Xoá Thiên Sứ. Cái Hố Không Đáy này là máy in tiền thực sự của F2P.

---

## 📊 3. Lập Mô Hình Excel (Economy Modeling) Trước Khi Code

Coder ngáo gõ số `.DropRate = 0.5f` bậy bạ. Designer Xịn làm File Excel Giả Lập Economy 3 tháng chơi trước khi gõ dòng lệnh đầu tiên.

### Dựng Macro Excel: Hành Trình 30 Ngày Người Chơi 1
1.  **Cột A (Ngày 1 -> 30)**
2.  **Cột B, C (Sources):** Tổng Stamina x Số Vàng rớt 1 round = Thu Nhập Vàng.
3.  **Cột D (Sinks Ước Tính):** Nâng Vũ khí Level hôm đó tốn bao Nhiêu.
4.  **Cột E (Gia Tài Net Worth):** Cột B - D = Vàng Nợ Tồn/Dư Dả của User.

Hãy chỉnh Thông Số Cơ sở Vàng Rơi xuống cho đến khi ở Ngày thứ 14, Cột E Nhảy Sang Số ÂM. Nghĩa là tới Tuần T2, Game Thủ Mệt Mỏi, Hết Vàng, Bi Đát Không Qua màn được tháp địa ngục.
Thêm 1 ô: **Giá Gói Khuyến Mãi Đầu Tiên: $0.99 Bán Chổi Rẻ + 10k Vàng bù đắp**. BOOM! Thiết kế vòng lặp kinh tế Perfect!

> *Tip: Có một Tool siêu Mệnh Mẽ hơn Excel để thiết kế luồng Kinh Tế Game là [Machinations.io](https://machinations.io/) UI Dạng Bản Đồ đường Ống, chạy giả lập (Simulate) bằng sức mạnh Logic. Nên học!*
