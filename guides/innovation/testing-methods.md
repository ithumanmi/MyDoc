# 🧪 Testing: Kiểm Thử & Tối Ưu Hóa

> [← Back to Design Thinking](./design-thinking.md)

## Testing là gì?
Testing (Kiểm thử) là bước cuối cùng trong vòng lặp Design Thinking, nhưng thực tế nó thường diễn ra song song với các bước khác. Đây là lúc bạn đưa **Prototype** (Bản mẫu) cho người dùng thật sử dụng để xem giải pháp của bạn có thực sự giải quyết vấn đề của họ hay không.

Mục tiêu không phải là để chứng minh bạn đúng, mà là để **học hỏi từ những điểm sai**.

---

## 1. Usability Testing (Kiểm Thử Khả Năng Sử Dụng) 🕵️‍♂️
Đây là phương pháp quan sát người dùng trực tiếp thao tác trên sản phẩm để tìm ra các rào cản (pain points).

### Khi nào dùng?
*   Khi đã có Prototype (Low-fi hoặc High-fi).
*   Muốn biết người dùng có hiểu cách dùng sản phẩm không.

### Cách thực hiện (5 Bước):
1.  **Lập kế hoạch:** Xác định tính năng cần test (VD: Quy trình đăng ký tài khoản).
2.  **Tuyển người dùng:** Mời 5 người dùng đại diện cho [User Persona](./user-persona.md) của bạn. (Nielsen Norman Group chứng minh 5 người là đủ để tìm ra 85% lỗi).
3.  **Kịch bản (Scenario):** Đừng bảo "Hãy bấm nút Đăng ký". Hãy đưa ngữ cảnh: "Bạn muốn mua cái áo này nhưng chưa có tài khoản, bạn sẽ làm gì?".
4.  **Quan sát & Ghi chép:**
    *   Yêu cầu họ **nghĩ thành tiếng** (Think Aloud) khi thao tác.
    *   Ghi lại những chỗ họ ngập ngừng, cau mày, hoặc click sai.
    *   **TUYỆT ĐỐI KHÔNG** hướng dẫn họ, trừ khi họ bỏ cuộc hoàn toàn.
5.  **Phân tích:** Tổng hợp lỗi và xếp hạng mức độ nghiêm trọng.

---

## 2. A/B Testing (Kiểm Thử Phân Tách) ⚖️
Đây là phương pháp so sánh 2 phiên bản (A và B) để xem phiên bản nào hiệu quả hơn dựa trên dữ liệu định lượng.

### Khi nào dùng?
*   Khi đã có sản phẩm chạy thật (Live product) hoặc Landing Page.
*   Muốn tối ưu hóa tỷ lệ chuyển đổi (Conversion Rate).
*   Tranh cãi nội bộ: "Nút màu Đỏ hay Xanh tốt hơn?".

### Cách thực hiện:
1.  **Giả thuyết:** "Đổi nút 'Mua ngay' từ màu Xám sang màu Cam sẽ tăng tỷ lệ click."
2.  **Biến số:** Chỉ thay đổi **DUY NHẤT 1 yếu tố** (màu nút). Nếu đổi cả màu nút lẫn tiêu đề, bạn sẽ không biết cái nào tạo ra kết quả.
3.  **Chia Traffic:** Dùng tool (Google Optimize, Optimizely) để chia ngẫu nhiên 50% khách thấy A, 50% khách thấy B.
4.  **Đo lường:** Chạy trong 1-2 tuần để có đủ dữ liệu (Statistical Significance).
5.  **Kết luận:** Phiên bản nào thắng (Winner) sẽ được áp dụng chính thức.

---

## 3. Feedback Grid (Lưới Phản Hồi) 📝
Sau khi test, bạn sẽ nhận được rất nhiều ý kiến. Hãy dùng khung này để phân loại:

| **(+) Những điều họ thích** | **(Δ) Những điều cần cải thiện** |
| :--- | :--- |
| *VD: "Giao diện sạch sẽ, dễ nhìn."* | *VD: "Font chữ hơi nhỏ, khó đọc trên điện thoại."* |
| **(?) Câu hỏi nảy sinh** | **(💡) Ý tưởng mới** |
| *VD: "Nút này có tính năng gì vậy?"* | *VD: "Sẽ hay hơn nếu có chế độ tối (Dark Mode)."* |

---

## Các Lỗi Thường Gặp Khi Testing ❌
1.  **Giải thích quá nhiều:** Để người dùng tự mò mẫm mới ra vấn đề.
2.  **Hỏi câu hỏi định hướng (Leading Questions):** "Bạn có thấy giao diện này đẹp không?" (Họ sẽ nể và nói có). -> Hãy hỏi: "Bạn cảm thấy thế nào về giao diện này?".
3.  **Test với người nhà/bạn bè:** Họ không phải khách hàng mục tiêu và thường thiên vị bạn.
4.  **Không quay lại sửa đổi:** Test xong để đó thì vô nghĩa. Phải dùng kết quả để quay lại bước **Ideate** hoặc **Prototype**.

> **Tóm lại:** Testing là cầu nối giữa "Ý tưởng hay ho" và "Sản phẩm thực tế". Đừng sợ bị chê, hãy sợ làm ra thứ không ai dùng.
