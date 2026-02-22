# 📡 Information Theory (Toán học của Thông tin)

## 1. Entropy (Độ bất định) - Claude Shannon
Thông tin không phải là nội dung (ý nghĩa), mà là độ đo của sự bất ngờ và khả năng giải quyết sự không chắc chắn.

### Công thức Shannon Entropy:
$$H(X) = - \sum_{i=1}^{n} p(x_i) \log_2 p(x_i)$$

*   **Đơn vị:** Bit. Một bit là lượng thông tin cần thiết để giảm sự không chắc chắn đi một nửa (Ví dụ: Tung đồng xu sấp/ngửa -> 1 bit).
*   **Bản chất:**
    *   Sự kiện chắc chắn xảy ra ($p=1$) -> $\log(1) = 0$ -> Entropy = 0 (Không có thông tin mới).
    *   Sự kiện hiếm gặp ($p \approx 0$) -> $-\log(p)$ rất lớn -> Mang nhiều thông tin.
*   **Ứng dụng:** "Mặt trời mọc đằng Đông" (0 bit). "Có người trúng số 100 tỷ" (Nhiều bit).
*   **Bài học:** Trong giao tiếp, hãy nói những gì người nghe *chưa biết*. Đừng nói sáo rỗng (Cliché). Giá trị của lời nói tỷ lệ thuận với độ "mới" (Surprise factor) của nó.

## 2. Tỷ lệ Tín hiệu trên Nhiễu (Signal-to-Noise Ratio - SNR)
Đo lường chất lượng thông tin trong một kênh truyền dẫn.

$$SNR_{dB} = 10 \log_{10} \left( \frac{P_{signal}}{P_{noise}} \right)$$

*   **Thời đại số:** Chúng ta chết đuối trong Nhiễu (Tin rác, Drama, Short video - Noise) và đói khát Tín hiệu (Kiến thức sâu, Sự thật, Nguyên lý - Signal).
*   **Chiến lược:**
    *   **Tăng Signal:** Tìm nguồn tin chất lượng (Sách gốc, chuyên gia hàng đầu, Whitepapers).
    *   **Giảm Noise:** Unfollow tin rác, chặn thông báo, cai nghiện mạng xã hội.
    *   **High-SNR Communication:** Viết ngắn gọn, súc tích, đi thẳng vào vấn đề.

## 3. Nén dữ liệu (Data Compression) & Độ phức tạp Kolmogorov
*   **Nén dữ liệu:** Là quá trình tìm ra các quy luật (patterns) lặp lại để biểu diễn thông tin ngắn gọn hơn.
*   **Độ phức tạp Kolmogorov:** Độ dài của chương trình máy tính ngắn nhất có thể tạo ra chuỗi dữ liệu đó.
    *   Chuỗi "01010101..." -> Quy luật đơn giản -> Dễ nén -> Kolmogorov thấp.
    *   Chuỗi ngẫu nhiên -> Không có quy luật -> Không nén được -> Kolmogorov cao.
*   **Học tập:** Học không phải là nhớ tất cả (Copy file - Rote memorization). Học là nén kiến thức thành các quy luật cốt lõi (Model) để bộ não có thể tái tạo lại kiến thức khi cần. Người hiểu bản chất là người có khả năng "nén" một cuốn sách vào một trang giấy.

## 4. Redundancy (Sự dư thừa) - Sửa lỗi
Tại sao ngôn ngữ con người lại dài dòng? Tại sao tiếng Anh có tới 50% dư thừa?
*   **Mục đích:** Để chống nhiễu (Error Correction). Nếu 1 từ bị nghe nhầm, ngữ cảnh và các từ thừa xung quanh sẽ giúp não bộ tự sửa lỗi.
*   **Mã Hamming (Hamming Code):** Thêm các bit kiểm tra vào dữ liệu để máy tính tự phát hiện và sửa lỗi bit bị sai.
*   **Hệ thống:** Đừng bao giờ để hệ thống chỉ có "Single Point of Failure" (Điểm chết duy nhất). Hãy có Redundancy (Backup server, Quỹ dự phòng, Kỹ năng dự phòng) để hệ thống tự phục hồi khi có sự cố.

## 5. Băng thông (Bandwidth) & Độ trễ (Latency)
*   **Bandwidth:** Độ rộng của ống nước (Làm được bao nhiêu việc cùng lúc). Đơn vị: Mbps.
*   **Latency:** Tốc độ nước chảy từ đầu này sang đầu kia (Mất bao lâu để xong 1 việc). Đơn vị: ms.
*   **Tư duy:** Đừng nhầm lẫn giữa việc "bận rộn" (High Bandwidth, xử lý nhiều việc nhưng chưa xong cái nào) và "hiệu quả" (Low Latency, hoàn thành việc nhanh chóng).
*   **Throughput (Thông lượng):** Kết quả thực tế = Bandwidth / Latency.
