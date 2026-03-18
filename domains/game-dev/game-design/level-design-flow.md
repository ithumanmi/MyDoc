# Level Design Flow: Dòng Chảy Màn Chơi & Tâm Lý Học

> [← Back to Game Design](../README.md) | [Home](../../../README.md)

Làm sao để người chơi không bao giờ bị Lạc đường, nhưng vẫn có cảm giác Game Thế Giới Mở vĩ đại tự do khám phá? Đó là ma thuật của **Level Design Flow** (Khơi gợi Dòng Chảy). Nghệ thuật này dắt mũi người chơi mà không cần vẽ một cái Mũi tên UI ngu ngốc nào ra màn hình.

---

## 📈 1. Biểu đồ Căng Thẳng - Giải Tỏa (Tension & Release)

Con người không thể chịu căng thẳng ở tim 140 BPM liên tục quá 5 phút. Game kinh dị thất bại nhất là game luôn hù dọa mỗi bước chân. Tâm lý sẽ "Cấm nín" và đâm ra Vô cảm (Desensitized).

### Đường Cong Độ Khó Hoàn Hảo (Pacing)
1.  **Hook (Câu Nhử):** Bắt đầu nhẹ nhàng (Căn phòng trống, học lách tránh hố hẹp).
2.  **Escalation (Mồi Lửa):** Thả 3 con quái cận chiến vào không gian hẹp. Tim đập nhanh lên!
3.  **Climax (Cao Trào):** Thả thêm 1 con Quái Bắn Tỉa xa và 1 con Mini-Boss Cầm cưa bự. Bắt Player kết hợp Né, Chém, Bắn. Đổ mồ hôi 100%.
4.  **Release (Giải Tỏa - QUAN TRỌNG NHẤT):** Tiếng cửa sắt mở ra. Ánh bình minh lọt vào một căn Safe Room (như Resident Evil). Nhạc Piano du dương cất lên. Con Tim đập chậm lại. Người chơi thở phào cái "Bịch".

*Đừng bao giờ thiết kế chuỗi Màn 1 Đánh Đấm, bước qua cửa gặp Màn 2 Khó Gấp Đôi. Hãy cho một điểm Trũng để nghỉ ngơi đi loot đồ (Looting Room).*

---

## 🍞 2. Kỹ Thuật Bánh Mì Vụn (Breadcrumbing)

Làm sao để người chơi biết phải đi về hướng Cúp Vàng giữa cái rừng rậm khổng lồ?

*   **Trái Tim Ánh Sáng (Lighting Weenies):** Mắt người mặc định luôn luôn ngước nhìn về những nguồn sáng Ấm (Vàng, Đỏ) trong một môi trường Tối/Xanh Lạnh. Hãy đặt ngọn đuốc lập lòe dọc theo hành lang là con đường đúng. Các hành lang Tối Ngỏ cụt là đường phụ tìm Secret Kho Báu. (Kỹ thuật đỉnh cao của Walt Disney).
*   **Vụn Tiền Vàng:** Có lý do tại sao Mario/Sonic đặt các dải xu vàng uốn lượn. Người chơi sẽ có bản năng nhặt xu tới cùng trời cuối đất. Vẽ đường cho hươu chạy bằng Tiền/Đồ rớt.
*   **Landmarks (Biểu tượng khổng lồ):** Dù đi lạc chỗ nào trong cái lâu đài của Elden Ring, hãy đảm bảo ngước đầu lên là thấy cái Đỉnh Tháp Sáng Rực Rỡ. Đó là mỏ neo phương hướng Não Bộ.

---

## 🚪 3. Điểm Nghẽn & Phòng Bơm (Choke Points & Arenas)

Map đa phần được build qua Tỉ Lệ Không Gian:

### Không Gian Rộng (Combat Arena)
Khi bạn muốn một Combat hỗn loạn, bạn vẽ cái Phòng Rộng, Tròn hoặc Vuông, thả Cục Đá/Cây làm Cover (Vật cản đạn).
*   **Design Rủi Ro:** Phải khóa cửa sau người chơi (Lock-in) để ép phải diệt hết 10 quái mới mở cửa đi tiếp. Nếu bạn không block cửa, player sẽ lách tránh lết qua (Speedrun Bỏ Qua Trải nghiệm bạn tốn 10 tiếng làm!).

### Điểm Nghẽn Cổ Chai (Choke Point)
Một cây cầu độc mộc. Một dãy hành lang hẹp chỉ tiến không lùi được.
*   **Mục đích Tâm lý:** Ép người chơi phải Đụng Mặt Trực Diện sự sợ hãi. Rất thích hợp đặt 1 con xe tăng quái chặn hẻm núi ép dùng Vũ Khí Trọng Pháo (Dạy người chơi đổi vũ khí đạn kẹ thay vì súng thường).

---

> 🛠️ **Checklist cho Level Designer Mới Vào Nghề (Blockout Phase)**
> Khoan lấy Maya hay Blender đắp Cây Thập tự giá/Đá lên Cảnh.
> 1. Vẽ toàn khối Hộp Xám (Grey-boxing / Blockout). Bỏ chạy thử từ điểm Start đến End có bị kẹt mô hình Không?
> 2. Đặt Quái Hộp Đỏ, Đạn Hộp Xanh.
> 3. Tự chơi không xài máu. Có Chỗ Nào Cover Không?
> 4. Chỉ đắp Mỹ Thuật sau tuần Thử nghiệm Gameplay thuần Mộc Thành công. Đắp Art sớm sửa Model khóc Thét!
