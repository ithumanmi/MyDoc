# Xây Dựng Core Loop & Meta-Game Gây Nghiện

> [← Back to Game Design](../README.md) | [Home](../../../README.md)

Làm sao để một người chơi cày *Hades* 300 giờ không chán, trong khi một game hành động đồ họa AAA khác bị xóa chỉ sau 2 tiếng? Bí mật nằm ở **Core Loop (Vòng Lặp Cốt Lõi)** và móc nối của nó với **Meta-Game (Bức Tranh Tổng Thể)**.

---

## 🔁 1. Giải Phẫu Core Loop (Vòng Lặp Cốt Lõi)

Core Loop là tập hợp những hành động bạn làm LẶP ĐI LẶP LẠI từ phút đầu tiên đến phút cuối cùng của game. Nếu cụm hành động này không "Sướng", thêm cốt truyện hay tới mấy game cũng sẽ thất bại.

### The 3 C's của Game Feel (Tính Thỏa Mãn)
Trước khi lập vòng lặp, cái lõi nhỏ nhất phải hoàn hảo:
1.  **Character (Nhân vật):** Phản hồi khi bấm nút (Input responsiveness). Bấm Nhảy là nhân vật Nhảy lên ngay lập tức ở frame đầu tiên. Không có độ trễ Animation.
2.  **Camera:** Camera phải theo sát hành động, rung rẩy mượt mà (Screen Shake) khi có vụ nổ.
3.  **Control (Điều khiển):** Bộ điều khiển trực quan. Đừng bắt người chơi bấm tổ hợp 4 nút để mở cái cửa.

### Ví Dụ: Cấu Trúc Core Loop Của Monster Hunter
*   **Hành động 1:** Nhận Nhiệm Giao (Chuẩn bị vật phẩm, cắm trại).
*   **Hành động 2:** Đi Săn (Đánh quái, chặt đuôi, né đòn) -> Trọng tâm tính Hành Động.
*   **Hành động 3:** Cướp Loot (Đạt phần thưởng sừng rồng, vảy rồng).
*   **Hành động 4:** Nâng cấp/Crafting (Tạo áo giáp mới) -> Vòng lại Hành động 1 mạnh mẽ hơn.

---

## 🗺️ 2. Meta-Game (Lý Do Để "One More Run")

Core Loop giữ user trong **5 Phút**. 
Meta-Game giữ user trong **5 Tháng**.

Meta-Game là Hệ Thống nằm ngoài màn chơi trực tiếp. Nó trả lời câu hỏi: *"Tao đi chặt con quái này để làm cái quái gì nữa?"*

### Case Study: Thiết Kế "Nghiện" Của Hades (Rogue-lite)

Ở các game Rogue-like cổ điển, chết là Mất Hết (Perma-death). Nó gây ức chế. Hades thành công lịch sử vì thiết kế Meta-game đệm vào Core-loop quá xuất sắc.

*   **Core Loop:** Đánh Chém -> Chọn Phòng tiếp theo -> Chọn Boons (Nâng cấp tạm thời) -> Chết!
*   **Meta-Game 1 (Nền tảng Tàn Số):** Khi chết, bạn mất các Boons, nhưng bạn mang Bóng Tối (Darkness) và Chìa Khóa Quỷ về Nhà. Bạn dùng Bóng Tối ĐỂ TĂNG CHỈ SỐ VĨNH VIỄN (Máu cơ bản, Tỉ lệ né hồi sinh).
    *   *Tâm lý người chơi:* "Chết không uổng phí. Run sau mình sẽ Trâu hơn, mình sẽ đánh qua được thằng Boss đó!"
*   **Meta-Game 2 (Cốt truyện Tích lũy):** Mỗi lần bạn chết về nhà, các vị thần/NPC đứng ở vị trí khác nhau và thoại Những Cốt Truyện MỚI.
    *   *Tâm lý người chơi:* Có những lúc người chơi MUỐN CHẾT nhanh để đi về coi cốt truyện của Achilles sẽ diễn ra như thế nào.

---

## 🎣 3. Xung Đột Hệ Thống (Friction) & Neo Kéo Giữ (Anchoring)

Một Game Design xuất sắc không phải là cho người chơi Mọi Thứ họ muốn. Mà là tạo ra *Sự Thiếu Thốn Có Tính Toán* (Calculated Friction).

*   **Energy/Stamina System (Genshin Impact/Game Mobile):** Tại sao bạn có cục Nhựa (Resin)? Không phải chỉ để bán nhựa hút máu. Mà để cấm bạn Cày 24h phá đảo trò chơi trong 2 ngày. Thiết kế bắt bạn chơi 30 phút, thèm thuồng đi ra, ĐỂ THÁNG SAU VẪN VÀO LẠI.
*   **Cơ chế Gacha (Anchoring):** Meta-game tối thượng. Bạn không cày lấy Vàng. Bạn cày lấy Mảnh Ghép Cuốn Sách Gọi Tướng (Primogems). Đây là một tầng Tiền Tệ Trung Gian làm mờ đi Thời gian/Tiền bạc đầu tư của bạn.

> 🛠️ **Mẹo Thực Chiến Kỹ Sư Gameplay:**
> Hãy luôn tách rời Code của Core-Loop và Meta-Game. 
> Core Loop chạy ở 60FPS mượt mà (Nhảy, Bắn, Hitbox). 
> Meta-Game (Kho đồ, Tính điểm, Mua nhà) chạy Async, giao tiếp qua Event System tốn ít CPU, và CÓ THỂ ĐIỀU CHỈNH CHỈ SỐ LẠI từ Server mà không cần App Update!
