# 🧠 Neural Networks 101: Mạng Nơ-ron Nhân tạo

> [← Back to AI/ML Roadmap](../README.md)

Lấy cảm hứng từ bộ não con người, Neural Network là trái tim của Deep Learning.
Nó giúp máy tính "nhìn" thấy mèo, "nghe" được giọng nói và "hiểu" được văn bản.

---

## 1. Perceptron (Tế bào thần kinh nhân tạo)

Một nơ-ron đơn giản nhận vào nhiều tín hiệu đầu vào (Inputs), nhân với trọng số (Weights), cộng thêm độ lệch (Bias) và đi qua hàm kích hoạt (Activation Function).

$$ y = f(\sum (w_i * x_i) + b) $$

*   **Inputs ($x$):** Dữ liệu vào (Pixel ảnh).
*   **Weights ($w$):** Tầm quan trọng của input đó (Học được qua quá trình training).
*   **Bias ($b$):** Ngưỡng kích hoạt.

---

## 2. Activation Functions (Hàm kích hoạt)

Quyết định nơ-ron có "bắn" tín hiệu đi tiếp hay không. Giúp mạng học được các hàm phi tuyến tính (Non-linear).

### **A. Sigmoid**
*   Nén giá trị về khoảng `(0, 1)`.
*   **Nhược điểm:** Vanishing Gradient (Đạo hàm tiến về 0 -> Mạng không học được khi quá sâu).

### **B. ReLU (Rectified Linear Unit)**
*   Nếu $x > 0$ thì giữ nguyên, nếu $x < 0$ thì bằng 0.
*   **Ưu điểm:** Đơn giản, tính toán cực nhanh, giải quyết tốt Vanishing Gradient.
*   **Phổ biến nhất hiện nay.**

### **C. Softmax**
*   Dùng ở lớp cuối cùng (Output Layer) cho bài toán phân loại nhiều lớp (Multi-class Classification).
*   Biến đổi vector đầu ra thành vector xác suất (Tổng = 1).

---

## 3. Backpropagation (Lan truyền ngược)

Làm sao để mạng học? -> Tìm cách giảm thiểu sai số (Loss).

1.  **Forward Pass:** Dữ liệu chạy từ Input -> Output -> Ra kết quả dự đoán $\hat{y}$.
2.  **Calculate Loss:** So sánh $\hat{y}$ với nhãn thật $y$ (Loss Function: MSE, Cross-Entropy).
3.  **Backward Pass:** Tính đạo hàm của Loss theo từng trọng số $w$ (Chain Rule).
4.  **Update Weights:** Điều chỉnh $w$ một chút ngược hướng đạo hàm để giảm Loss (Gradient Descent).

---

## 4. Frameworks (PyTorch vs TensorFlow)

Đừng code Backpropagation bằng tay (trừ khi để học). Hãy dùng Framework.

### **A. PyTorch (Facebook/Meta)**
*   **Đặc điểm:** Dynamic Graph (Pythonic), dễ debug.
*   **Cộng đồng:** Researcher yêu thích (Hầu hết paper mới đều dùng PyTorch).
*   **Khuyên dùng cho người mới bắt đầu.**

### **B. TensorFlow / Keras (Google)**
*   **Đặc điểm:** Static Graph, mạnh về Deployment (TensorFlow Lite, TF Serving).
*   **Cộng đồng:** Production, Doanh nghiệp lớn.
*   **Keras:** API cấp cao bọc trên TensorFlow, code cực ngắn gọn.
