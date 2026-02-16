# 🧮 Mathematics for Machine Learning: Ngôn ngữ của AI

> [← Back to AI/ML Roadmap](../README.md)

AI không phải là ma thuật. Nó là **Toán học** chạy trên máy tính.
Bạn không cần là giáo sư toán, nhưng bạn cần hiểu các khái niệm sau để biết tại sao mô hình lại chạy.

---

## 1. Linear Algebra (Đại số tuyến tính)

Dữ liệu trong AI là các con số được sắp xếp gọn gàng.

### **A. Vector (Vectơ)**
*   Mảng số 1 chiều. Ví dụ: `[chiều cao, cân nặng, tuổi]` = `[170, 60, 25]`.
*   Đại diện cho một điểm dữ liệu (Data Point).

### **B. Matrix (Ma trận)**
*   Mảng số 2 chiều (Bảng tính Excel).
*   Ví dụ: Tập dữ liệu của 100 người = Ma trận 100 dòng x 3 cột.
*   **Phép nhân ma trận (Matrix Multiplication):** Cốt lõi của Neural Network. Giúp tính toán song song hàng triệu phép tính cùng lúc (trên GPU).

### **C. Tensor (Ten-xơ)**
*   Mảng số N chiều.
*   Ví dụ: Ảnh màu RGB = Tensor 3 chiều (Chiều cao x Chiều rộng x 3 kênh màu).

---

## 2. Calculus (Giải tích)

Làm sao để dạy máy học? -> Tối ưu hóa hàm số.

### **A. Derivative (Đạo hàm)**
*   Đo độ dốc của hàm số tại một điểm.
*   Ý nghĩa: Nếu tôi thay đổi tham số `w` một chút, thì lỗi (Loss) sẽ tăng hay giảm bao nhiêu?

### **B. Gradient Descent (Xuống đồi)**
*   Thuật toán tối ưu hóa quan trọng nhất.
*   Tưởng tượng bạn đang đứng trên đỉnh núi (Lỗi cao) và muốn xuống thung lũng (Lỗi thấp nhất) trong sương mù.
*   **Gradient:** Hướng dốc nhất. Bạn đi ngược hướng Gradient để xuống núi nhanh nhất.
*   **Learning Rate:** Bước chân của bạn. Bước quá to -> Vượt qua thung lũng. Bước quá nhỏ -> Đi mãi không tới.

---

## 3. Probability & Statistics (Xác suất thống kê)

AI là dự đoán tương lai dựa trên quá khứ. Nó luôn có sai số.

*   **Mean (Trung bình):** Giá trị kỳ vọng.
*   **Variance (Phương sai):** Độ phân tán dữ liệu.
*   **Distribution (Phân phối):** Dữ liệu thường tuân theo quy luật nào? (Phân phối chuẩn - Normal Distribution / Hình chuông).
*   **Bayes' Theorem:** Cập nhật niềm tin khi có dữ liệu mới. (Nền tảng của Naive Bayes Classifier).
