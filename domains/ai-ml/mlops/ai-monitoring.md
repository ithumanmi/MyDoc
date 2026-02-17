# 🩺 AI Monitoring: Theo Dõi Sức Khỏe Mô Hình AI

> Trong phần mềm truyền thống, "Monitoring" là theo dõi CPU, RAM, Latency.
> Trong AI, "Monitoring" còn là theo dõi **"Mô hình có đang ngu đi không?"** (Model Decay).

---

## 1. Tại Sao Cần AI Monitoring?
Mô hình AI học từ dữ liệu quá khứ để dự đoán tương lai. Nhưng thế giới thực luôn thay đổi.
*   **Model Decay:** Hiệu năng mô hình giảm dần theo thời gian.
*   **Silent Failures:** Mô hình không báo lỗi (crash), vẫn trả về kết quả, nhưng kết quả đó **SAI**.

---

## 2. Bốn Trụ Cột Của AI Monitoring

### a. Service Health (Sức khỏe hệ thống)
Giống như phần mềm thông thường.
*   **Latency:** Thời gian phản hồi (p95, p99).
*   **Throughput:** Số request/giây (RPS).
*   **Error Rate:** Tỷ lệ lỗi 4xx, 5xx.
*   **Resource Usage:** GPU Memory, CPU utilization.

### b. Data Quality (Chất lượng dữ liệu)
Kiểm tra dữ liệu đầu vào (Input data) trước khi đưa vào mô hình.
*   **Missing Values:** Tỷ lệ null/NaN tăng đột biến?
*   **Type Mismatch:** Input là string thay vì int?
*   **Schema Change:** Số lượng cột thay đổi?

### c. Data Drift (Trôi dữ liệu)
Sự thay đổi trong phân phối dữ liệu đầu vào (Input distribution shift) so với dữ liệu huấn luyện.
*   *Ví dụ:* Train model dự đoán giá xe trên dữ liệu 2019-2022. Năm 2023 lạm phát, giá xe tăng vọt -> Data Drift.
*   *Dấu hiệu:* Giá trị trung bình (Mean), phương sai (Variance) của các feature quan trọng thay đổi lớn.

### d. Model Performance (Concept Drift)
Sự thay đổi trong mối quan hệ giữa Input và Output.
*   *Ground Truth Delay:* Trong thực tế, chúng ta thường không biết ngay kết quả dự đoán đúng hay sai (ví dụ: dự đoán nợ xấu cần 6 tháng mới biết).
*   *Proxy Metrics:* Theo dõi sự thay đổi phân phối của Output (Prediction Drift) như một dấu hiệu sớm.

---

## 3. Phương Pháp Phát Hiện Drift 📉

Sử dụng các kiểm định thống kê để so sánh **Reference Dataset** (Dữ liệu train) và **Current Dataset** (Dữ liệu production).

1.  **PSI (Population Stability Index):**
    *   Phổ biến trong tài chính/ngân hàng.
    *   PSI < 0.1: Ổn định.
    *   PSI > 0.25: Drift nặng -> Cần train lại.
2.  **KS Test (Kolmogorov-Smirnov):** So sánh sự khác biệt giữa 2 phân phối xác suất.
3.  **KL Divergence:** Đo độ lệch giữa 2 phân phối.
4.  **Wasserstein Distance:** Đo khoảng cách giữa 2 phân phối (thường dùng cho Image/Embedding drift).

---

## 4. Quy Trình Phản Ứng (Alerting & Remediation)

Khi phát hiện Drift, hệ thống làm gì?

1.  **Alerting:** Gửi thông báo cho Data Scientist (Slack/Email).
2.  **Investigation:** Dùng dashboard để xem feature nào bị drift.
3.  **Automated Actions:**
    *   **Retrain:** Trigger pipeline huấn luyện lại với dữ liệu mới nhất.
    *   **Rollback:** Quay lại phiên bản model trước đó (nếu model mới bị lỗi).
    *   **Fallback:** Chuyển sang dùng Rule-based system tạm thời.

---

## 5. Công Cụ Hỗ Trợ 🛠️

| Loại | Công cụ | Đặc điểm |
| :--- | :--- | :--- |
| **System Monitoring** | Prometheus + Grafana | Chuẩn công nghiệp cho metrics hệ thống. |
| **Model Monitoring** | **Evidently AI** | Open-source, report đẹp, chuyên sâu về Drift. |
| | **Arize AI** | Platform chuyên nghiệp, root cause analysis. |
| | **WhyLabs** | Sử dụng whylogs (privacy-preserving profiling). |
| | **Fiddler** | Giải thích model (Explainability) + Monitoring. |

---

## 6. Ví Dụ Cấu Hình (Evidently AI)

```python
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

# Tạo báo cáo so sánh
report = Report(metrics=[
    DataDriftPreset(), 
])

report.run(reference_data=train_df, current_data=prod_df)
report.save_html('data_drift_report.html')
```
