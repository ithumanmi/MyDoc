# 🔄 CI/CD for AI (MLOps): Tự Động Hóa Quy Trình AI

> **CI/CD** trong phần mềm truyền thống là **Code -> Build -> Test -> Deploy**.
> Trong AI/Machine Learning, quy trình này phức tạp hơn nhiều: **Code + Data + Model -> Train -> Evaluate -> Deploy -> Monitor**.

---

## 1. Sự Khác Biệt Cốt Lõi (DevOps vs MLOps)
*   **DevOps:** Tập trung vào Code. Nếu code không đổi, phần mềm không đổi.
*   **MLOps:** Tập trung vào cả Code, Data và Model.
    *   **Data Drift:** Dữ liệu thực tế thay đổi theo thời gian -> Model cũ bị "lỗi thời" dù code vẫn chạy tốt.
    *   **Continuous Training (CT):** Cần quy trình tự động huấn luyện lại model khi có dữ liệu mới.

---

## 2. Quy Trình CI (Continuous Integration) trong AI

### a. Code Validation
*   **Linting/Testing:** Kiểm tra code Python (Black, Flake8).
*   **Unit Tests:** Test các hàm xử lý dữ liệu, hàm tính toán.

### b. Data Validation (Kiểm tra chất lượng dữ liệu)
*   Kiểm tra dữ liệu đầu vào có đúng schema không?
*   Kiểm tra phân phối dữ liệu (Distribution check) để phát hiện Data Drift sớm.
*   *Công cụ:* Great Expectations, TensorFlow Data Validation (TFDV).

### c. Model Training & Evaluation (CT)
Khi có code mới hoặc dữ liệu mới, pipeline sẽ:
1.  **Model Training:** Tự động chạy script training (Retrain).
2.  **Model Evaluation:** So sánh metric (Accuracy, F1-score) của model mới với model cũ (Baseline) trước khi merge.
3.  **Gatekeeper:** Nếu model mới tốt hơn -> Đóng gói (Package) và đẩy vào Model Registry. Nếu tệ hơn -> Báo lỗi.

---

## 3. Quy Trình CD (Continuous Deployment) trong AI

### a. Model Registry & Versioning
*   Lưu trữ và versioning model (v1.0, v1.1...).
*   Đóng gói model thành Docker Image hoặc API Service.
*   *Công cụ:* MLflow Model Registry, DVC.

### b. Deployment Strategies
Do AI có tính xác suất, chiến lược deploy rất quan trọng:
*   **Canary Deployment:** Triển khai cho 5-10% user trước.
*   **Blue-Green Deployment:** Chạy song song 2 phiên bản.
*   **Shadow Deployment (Quan trọng cho AI):** Chạy model mới song song với model cũ nhưng **không trả kết quả cho user**. Chỉ dùng để so sánh (Log & Compare). An toàn tuyệt đối.

### c. Real-time Monitoring
*   **Drift detection:** Phát hiện Data drift (dữ liệu đầu vào thay đổi) và Concept drift (mô hình dự đoán sai lệch dần).
*   **Feedback Loop:** Thu thập phản hồi để tái huấn luyện.

---

## 4. Công Cụ Phổ Biến (Tech Stack)

| Thành phần | Công cụ |
| :--- | :--- |
| **CI/CD Pipeline** | GitHub Actions, Jenkins, GitLab CI |
| **Model Registry** | MLflow, AWS SageMaker |
| **Orchestration** | Kubeflow, Airflow |
| **Data Versioning** | DVC (Data Version Control) |
| **Monitoring** | Prometheus, Grafana, Evidently AI |

---

## 5. Ví Dụ Workflow
1.  **Push Code/Data:** Dev push thay đổi lên Git.
2.  **CI:** Chạy Test Code + Test Data.
3.  **CT:** Trigger Training Pipeline trên GPU Runner.
4.  **Eval:** Model mới đạt Accuracy > Model cũ?
5.  **CD:** Deploy model vào Registry -> Deploy Shadow -> Deploy Canary -> Deploy Production.
