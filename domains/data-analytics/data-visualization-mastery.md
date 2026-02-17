# 🎨 Data Visualization Mastery: Nghệ Thuật Kể Chuyện Bằng Dữ Liệu

> [← Back to Data Analytics Roadmap](./README.md)

## Tại sao Data Viz quan trọng?
Não bộ con người xử lý hình ảnh nhanh hơn văn bản 60.000 lần. Một biểu đồ tốt có thể thay thế hàng ngàn dòng dữ liệu.
Tuy nhiên, ranh giới giữa một biểu đồ "biết nói" và một biểu đồ "gây lú" rất mong manh.

> *"The goal of visualization is to aid our understanding of data by leveraging the human visual system's highly tuned ability to see patterns, spot trends, and identify outliers."*

---

## 1. Nguyên Tắc Cốt Lõi: Data-Ink Ratio 🖋️
Edward Tufte, cha đẻ của Data Viz hiện đại, đưa ra khái niệm **Tỷ lệ Mực/Dữ liệu**.
*   **Nguyên tắc:** Mọi nét mực trên biểu đồ nên phục vụ việc hiển thị dữ liệu mới.
*   **Hành động:** Loại bỏ tất cả những thứ rườm rà (Chart junk):
    *   ❌ Gridlines quá đậm.
    *   ❌ Hiệu ứng 3D (làm sai lệch nhận thức).
    *   ❌ Màu nền lòe loẹt.
    *   ❌ Chú thích (Legend) dư thừa (nếu có thể dán nhãn trực tiếp).

---

## 2. Chọn Biểu Đồ Đúng (Chart Selection Guide) 📊

### So sánh (Comparison)
*   **Bar Chart (Thanh ngang):** Tốt nhất khi tên danh mục dài (VD: Tên quốc gia).
*   **Column Chart (Cột dọc):** Tốt khi số lượng danh mục ít (< 10) hoặc có yếu tố thời gian ngắn.

### Xu hướng (Trend)
*   **Line Chart (Đường):** Vua của dữ liệu thời gian (Time-series).
*   **Area Chart (Vùng):** Khi muốn nhấn mạnh tổng lượng tích lũy.

### Thành phần (Part-to-whole)
*   **Stacked Bar:** So sánh tỷ lệ trong các nhóm khác nhau.
*   **Pie/Donut Chart:** ⚠️ **DÙNG HẠN CHẾ**. Chỉ dùng khi có < 5 miếng và tổng bằng 100%. Mắt người so sánh diện tích rất tệ.

### Phân phối (Distribution)
*   **Histogram:** Xem tần suất xuất hiện.
*   **Box Plot:** Xem phân phối, trung vị và giá trị ngoại lai (Outliers).

### Mối quan hệ (Relationship)
*   **Scatter Plot (Biểu đồ phân tán):** Xem tương quan giữa 2 biến số (VD: Giá và Doanh số).

---

## 3. Sử Dụng Màu Sắc (Color Theory) 🎨
Màu sắc không phải để trang trí, mà là một tín hiệu dữ liệu.
1.  **Sequential (Tuần tự):** Dùng 1 màu từ nhạt đến đậm để thể hiện cường độ (VD: Doanh thu thấp -> cao).
2.  **Diverging (Phân kỳ):** Dùng 2 màu đối lập để thể hiện giá trị âm/dương hoặc so với trung bình (VD: Đỏ = Lỗ, Xanh = Lãi).
3.  **Categorical (Phân loại):** Dùng các màu khác nhau cho các danh mục không liên quan (VD: Nam/Nữ).

> **Lưu ý:** 10% nam giới bị mù màu. Hãy dùng các bảng màu thân thiện (Colorblind-safe) hoặc dùng thêm ký hiệu/nhãn dán.

---

## 4. Nguyên Tắc Gestalt Trong Thiết Kế 🧠
*   **Proximity (Gần nhau):** Các vật thể gần nhau được coi là cùng một nhóm. -> Sắp xếp các biểu đồ liên quan ở gần nhau.
*   **Similarity (Tương đồng):** Các vật thể giống nhau (màu, hình dáng) được coi là cùng loại. -> Dùng màu nhất quán cho cùng 1 đối tượng trên toàn dashboard.
*   **Enclosure (Bao quanh):** Đóng khung các nhóm liên quan để tạo sự phân cách rõ ràng.

👉 **[Mẫu thực hành: Dashboard Design Checklist](./templates/dashboard-design-checklist.md)**
