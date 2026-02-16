# 🗺️ Assumption Mapping Template

> [← Back to RAT Guide](../rat-testing.md)

## Dự án: [Tên Dự Án]
**Ngày:** [Ngày thực hiện]

---

## 1. Danh Sách Giả Định (Assumptions List) 📝
Liệt kê tất cả các giả định của bạn theo 3 nhóm:

### Desirability (Khách hàng muốn?) ❤️
*   [ ] Khách hàng gặp vấn đề X thực sự nghiêm trọng.
*   [ ] Khách hàng thích giải pháp Y hơn giải pháp hiện tại.
*   [ ] ...

### Viability (Kinh doanh được?) 💰
*   [ ] Khách hàng sẵn sàng trả [Số tiền] cho giải pháp này.
*   [ ] Chi phí thu hút khách hàng (CAC) thấp hơn [Số tiền].
*   [ ] ...

### Feasibility (Làm được không?) 🛠️
*   [ ] Chúng ta có đủ công nghệ để làm tính năng Z.
*   [ ] Chúng ta có thể xin giấy phép hoạt động trong 3 tháng.
*   [ ] ...

---

## 2. Bản Đồ Ưu Tiên (Assumption Map) 🎯
Vẽ một trục tọa độ và đặt các giả định vào vị trí tương ứng:

*   **Trục tung (Y):** Mức độ quan trọng (Importance) - Nếu sai thì dự án chết?
    *   *Cao:* Critical (Chết dự án)
    *   *Thấp:* Minor (Không ảnh hưởng mấy)
*   **Trục hoành (X):** Mức độ chắc chắn (Evidence) - Chúng ta đã có bằng chứng chưa?
    *   *Trái:* Unknown (Đoán mò, chưa có dữ liệu)
    *   *Phải:* Known (Đã có dữ liệu chứng minh)

| | **Unknown (Chưa biết)** | **Known (Đã biết)** |
| :--- | :--- | :--- |
| **High Importance (Quan trọng)** | **🛑 VÙNG RỦI RO (Risk Zone)**<br>*(Cần Test ngay lập tức)*<br>Test bằng RAT | **✅ VÙNG AN TOÀN (Safe Zone)**<br>*(Đã xác thực)*<br>Triển khai MVP |
| **Low Importance (Ít quan trọng)** | **⚠️ VÙNG CẦN THEO DÕI**<br>Test sau | **💤 VÙNG KHÔNG ĐÁNG QUAN TÂM**<br>Bỏ qua |

---

## 3. Kế Hoạch Thử Nghiệm (Experiment Plan) 🧪

**Giả định rủi ro nhất:** [Chọn từ vùng Risk Zone]
**Cách kiểm thử (Method):** [Fake Door / Pre-order / Interview / Concierge...]
**Tiêu chí thành công (Success Metric):** [VD: Tỷ lệ click > 5%, Có 10 người đặt trước...]
