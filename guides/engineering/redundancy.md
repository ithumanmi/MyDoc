# 🔗 Dự phòng (Redundancy) & Điểm chết (SPOF)

## 1. Điểm chết duy nhất (Single Point of Failure - SPOF)
Là một thành phần mà nếu nó hỏng, toàn bộ hệ thống sẽ sụp đổ.
*   **Ví dụ:**
    *   Mạng internet nhà bạn chỉ có 1 đường dây cáp quang. Cá mập cắn -> Mất mạng toàn bộ.
    *   Doanh nghiệp chỉ có 1 khách hàng lớn chiếm 80% doanh thu. Khách hàng bỏ đi -> Phá sản.
    *   Bạn chỉ có 1 nguồn thu nhập (Lương). Bị sa thải -> Khủng hoảng tài chính.
*   **Nhiệm vụ:** Tìm ra tất cả các SPOF trong cuộc sống của bạn và loại bỏ chúng.

## 2. Hệ thống dự phòng (Redundancy)
Thêm các thành phần sao lưu để hệ thống vẫn hoạt động khi thành phần chính gặp sự cố.
*   **Máy bay:** Luôn có ít nhất 2 động cơ. Nếu 1 cái hỏng, cái kia vẫn đủ sức để hạ cánh an toàn.
*   **Dữ liệu:** Quy tắc 3-2-1 (3 bản sao, 2 định dạng, 1 bản off-site).
*   **Sự nghiệp:** Đa dạng hóa kỹ năng. Nếu nghề chính (ngành Du lịch) chết vì dịch bệnh, nghề tay trái (Viết lách/Code) sẽ cứu bạn.

## 3. Dự phòng nóng vs. Dự phòng lạnh
*   **Hot Standby (Nóng):** Hệ thống phụ chạy song song, thay thế ngay lập tức (UPS, Máy phát điện tự động). -> Tốn kém nhưng an toàn cao.
*   **Cold Standby (Lạnh):** Hệ thống phụ đang tắt, cần thời gian để khởi động (Máy phát điện phải giật nổ). -> Rẻ hơn nhưng có độ trễ (Downtime).
*   **Ứng dụng:** Quỹ khẩn cấp (Tiền mặt) là Hot Standby. Bất động sản bán lấy tiền là Cold Standby (thanh khoản chậm).

## 4. Antifragile (Khả năng chống chịu)
Hệ thống dư thừa trông có vẻ lãng phí trong thời bình (tốn tiền nuôi 2 động cơ, tốn tiền mua bảo hiểm), nhưng lại là yếu tố sống còn trong thời loạn. **Sự hiệu quả tối đa (Efficiency) thường giết chết sự bền vững (Resilience).**
