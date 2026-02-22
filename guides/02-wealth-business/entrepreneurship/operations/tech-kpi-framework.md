# 🏗️ Tech & Product KPI Framework: Fighting Technical Debt

> [← Back to Operations](./README.md)
> 
> *"Nợ kỹ thuật (Technical Debt) giống như vay nặng lãi. Nếu bạn chỉ lo chạy tính năng mới (Feature) mà không trả lãi (Refactor), hệ thống của bạn sẽ phá sản về mặt năng suất trong tương lai."*

Trong bộ phận Kỹ thuật và Sản phẩm, sai lầm lớn nhất của các Manager là chỉ đo lường **Tốc độ (Velocity)** mà bỏ qua **Độ bền (Stability)**. Điều này dẫn đến việc nhân viên "code ẩu" để đạt KPI, gây ra thảm họa vận hành sau này.

---

## 🏗️ Quy trình 5 bước xây dựng KPI chống "Nợ kỹ thuật"

### Bước 1: Phân bổ nguồn lực (The 70/20/10 Rule)
Đừng bắt Dev làm 100% tính năng mới. Hãy định nghĩa KPI dựa trên tỷ lệ phân bổ thời gian:

*   **70% - Feature Work:** Phát triển tính năng mới để mang lại giá trị kinh doanh.
*   **20% - Technical Debt & Refactoring:** Sửa code cũ, tối ưu DB, cập nhật thư viện.
*   **10% - R&D & Innovation:** Thử nghiệm công nghệ mới hoặc tự do sáng tạo.

> **Hành động:** Nếu tháng nào Feature Work chiếm 100% -> KPI trả nợ kỹ thuật tháng sau phải tăng gấp đôi.

### Bước 2: Thiết lập "Chốt chặn" Vận hành (The Stability Multiplier)
Tương tự như NPS của Sales, Tech cần một chỉ số để bảo vệ chất lượng hệ thống.

*   **Chỉ số kiểm soát:** **Uptime** (Thời gian hệ thống hoạt động) hoặc **Bug Leak Rate** (Tỷ lệ lỗi lọt ra môi trường sản xuất).
*   **Cơ chế thực thi:** 
    *   **Công thức:** `Thưởng hiệu suất = (Thành tích Task) x Hệ số ổn định`
    *   **Kill Switch:** Nếu hệ thống sập > 4 giờ/tháng (do lỗi chủ quan) => Cắt toàn bộ thưởng dự án, bất kể team đã ship bao nhiêu tính năng "khủng".

### Bước 3: Đo lường bằng bộ chỉ số DORA
Đây là tiêu chuẩn vàng toàn cầu để đo lường hiệu quả của đội ngũ kỹ thuật:

1.  **Deployment Frequency:** Tần suất đẩy code mới (Càng nhanh càng tốt).
2.  **Lead Time for Changes:** Thời gian từ lúc code xong đến khi đến tay user.
3.  **MTTR (Mean Time to Recovery):** Thời gian trung bình để sửa chữa khi có sự cố.
4.  **Change Failure Rate:** Tỷ lệ code đẩy lên bị lỗi phải rollback.

### Bước 4: Chỉ số Nợ kỹ thuật (Tech Debt Ratio - TDR)
Làm thế nào để đo lường "Nợ" một cách định lượng?

*   **Công thức:** `TDR = (Thời gian ước tính để fix nợ) / (Thời gian để viết lại toàn bộ hệ thống)`
*   **KPI Mục tiêu:** Giữ `TDR < 5%`. 
*   **Hành động:** Khi TDR vượt ngưỡng, toàn bộ team phải dừng làm tính năng mới để tập trung "trả nợ".

### Bước 5: Review "Chất xám" (The Knowledge Audit)
Để tránh tình trạng "Bus Factor" (Hệ thống sụp đổ nếu 1 người nghỉ việc):

*   **KPI Code Review:** Tỷ lệ code được review chéo bởi các thành viên khác.
*   **KPI Documentation:** Độ phủ của tài liệu hướng dẫn cho các module quan trọng.
*   **Hành động:** Thưởng cho những "Maintainer" (người chăm sóc hệ thống) ngang bằng hoặc cao hơn những "Builder" (người xây mới).

---

## 🧠 Mental Model: Nợ kỹ thuật là Lãi suất kép (Negative Compound)

1.  **Tư duy Tài chính:** Coi code là một tài sản. Code xấu là tài sản đang bị khấu hao nhanh.
2.  **Entropy:** Một hệ thống nếu không được chăm sóc sẽ tự động trở nên hỗn loạn. KPI trả nợ kỹ thuật là nỗ lực chống lại Entropy.

---

## 🔗 Liên kết mở rộng
*   **[Sales KPI Framework](./sales-kpi-framework.md):** So sánh với tư duy điều hướng hành vi Sales.
*   **[System Design Guide](../../03-career-skills/system-design/README.md):** Cách thiết kế hệ thống ít nợ từ đầu.
*   **[Product Management](./product-management.md):** Cân bằng giữa Roadmap kinh doanh và Roadmap kỹ thuật.
