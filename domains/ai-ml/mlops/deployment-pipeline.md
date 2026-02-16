# ⚙️ MLOps: Đưa AI ra Chiến trường (Level 7)

> [← Back to AI/ML Roadmap](../README.md)

Train được mô hình 99% accuracy trên Notebook là chuyện nhỏ.
Đưa nó ra chạy thực tế (Production) cho hàng triệu người dùng mà không sập là chuyện lớn.

---

## 1. Deployment (Triển khai)

### **A. Model Serving (Phục vụ mô hình)**
*   Biến file mô hình (`.pt`, `.h5`) thành một API (RESTful hoặc gRPC).
*   **FastAPI / Flask (Python):** Đơn giản, dễ viết. Nhưng chậm nếu tải cao.
*   **TorchServe / TensorFlow Serving:** Tối ưu hóa cho hiệu suất cao (Batching request, GPU support).
*   **ONNX Runtime:** Chạy mô hình đa nền tảng (Mobile, Browser, Server) cực nhanh.

### **B. Containerization (Đóng gói)**
*   **Docker:** Đóng gói mô hình + thư viện Python + Hệ điều hành vào một cái hộp (Container).
*   Đảm bảo: "Chạy được trên máy tôi thì chạy được trên Server".

### **C. Orchestration (Điều phối)**
*   **Kubernetes (K8s):** Quản lý hàng trăm Container. Tự động scale (thêm máy) khi người dùng đông, tự động restart khi sập.

---

## 2. Monitoring (Giám sát)

Mô hình AI giống như thực phẩm tươi sống. Nó sẽ bị "hỏng" theo thời gian.

### **A. Data Drift (Trôi dữ liệu)**
*   Dữ liệu thực tế thay đổi so với dữ liệu huấn luyện.
*   Ví dụ: Train mô hình nhận diện khuôn mặt năm 2019 (không ai đeo khẩu trang). Năm 2020 Covid (ai cũng đeo khẩu trang) -> Mô hình sai bét.

### **B. Model Drift (Trôi mô hình)**
*   Mối quan hệ giữa Input và Output thay đổi.
*   Ví dụ: Mô hình dự đoán giá nhà. Năm nay bong bóng bất động sản -> Quy luật cũ không còn đúng.

### **C. Giải pháp:**
*   Theo dõi độ chính xác liên tục.
*   Thu thập dữ liệu mới hàng ngày -> Train lại (Retrain) định kỳ (Automated Retraining Pipeline).

---

## 3. CI/CD for ML (Quy trình tự động hóa)

*   **Continuous Integration (CI):** Tự động test code, test dữ liệu đầu vào.
*   **Continuous Delivery (CD):** Tự động đóng gói Docker, deploy lên môi trường Staging/Production.
*   **Continuous Training (CT):** Tự động trigger quy trình train lại khi phát hiện Data Drift.
