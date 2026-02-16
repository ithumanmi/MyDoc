# 🎓 Supervised Learning: Học có Giám sát (Classic ML)

> [← Back to AI/ML Roadmap](../README.md)

Đây là dạng ML phổ biến nhất: Bạn cho máy xem dữ liệu đã có đáp án (Label), và yêu cầu nó học quy luật để đoán đáp án cho dữ liệu mới.

---

## 1. Regression (Hồi quy) - Dự đoán con số

Dự đoán giá nhà, nhiệt độ ngày mai, doanh thu tháng sau.
Output là một số thực liên tục (Continuous Value).

### **A. Linear Regression (Hồi quy Tuyến tính)**
*   Tìm một đường thẳng `y = ax + b` sao cho tổng bình phương khoảng cách từ các điểm dữ liệu đến đường thẳng là nhỏ nhất (Mean Squared Error - MSE).
*   **Hệ số a (Slope):** Độ dốc.
*   **Hệ số b (Intercept):** Điểm cắt trục tung.

### **B. Polynomial Regression (Đa thức)**
*   Dùng đường cong `y = ax^2 + bx + c` để khớp dữ liệu phức tạp hơn.

---

## 2. Classification (Phân loại) - Dự đoán nhãn

Email này là Spam hay Không? Khối u này lành tính hay ác tính?
Output là một nhãn rời rạc (Discrete Label).

### **A. Logistic Regression**
*   Tên là Regression nhưng dùng để phân loại.
*   Dùng hàm Sigmoid để nén kết quả về khoảng `(0, 1)` -> Xác suất.
*   Nếu Xác suất > 0.5 -> Nhãn 1 (Spam). Ngược lại -> Nhãn 0.

### **B. Decision Trees (Cây quyết định)**
*   Hỏi liên tiếp các câu hỏi Yes/No để chia nhỏ dữ liệu.
*   Ví dụ:
    *   Trời có mưa không? -> Có -> Mang ô.
    *   Không -> Có nắng to không? -> Có -> Mang mũ.
*   **Ưu điểm:** Dễ hiểu (Explainable AI).
*   **Nhược điểm:** Dễ bị Overfitting (Học vẹt).

### **C. Random Forest (Rừng ngẫu nhiên)**
*   Tạo ra 100 cây quyết định ngẫu nhiên.
*   Cho cả 100 cây bỏ phiếu (Voting). Kết quả nào được chọn nhiều nhất thì lấy.
*   **Ensemble Learning:** Sức mạnh của đám đông. Giảm Overfitting cực tốt.

### **D. Support Vector Machine (SVM)**
*   Tìm một siêu phẳng (Hyperplane) chia cắt dữ liệu thành 2 phần rõ rệt nhất (Margin lớn nhất).
*   **Kernel Trick:** Biến đổi dữ liệu sang không gian chiều cao hơn để dễ chia cắt (Ví dụ: Từ 2D khó chia -> 3D dễ chia).

---

## 3. Evaluation Metrics (Đánh giá mô hình)

Làm sao biết mô hình tốt hay dở? Đừng chỉ nhìn Accuracy.

*   **Accuracy:** Tỷ lệ đúng (Đúng/Tổng). Dễ bị lừa nếu dữ liệu mất cân bằng (Imbalanced Data).
*   **Precision:** Trong những cái máy đoán là Spam, bao nhiêu cái thực sự là Spam? (Tránh oan sai).
*   **Recall:** Trong tất cả thư Spam thực tế, máy bắt được bao nhiêu cái? (Tránh bỏ lọt).
*   **F1-Score:** Trung bình điều hòa của Precision và Recall.
