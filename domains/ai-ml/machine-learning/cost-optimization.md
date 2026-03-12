## 💸 Cost Optimization Tips cho Classic ML

> [← Back to AI/ML Roadmap](../README.md)

Giữ performance tốt nhưng vẫn tối ưu chi phí dataset, compute, storage và vận hành.

---

## 1. Dữ liệu & Lưu trữ

*   **Sampling thông minh:** Dùng stratified sampling để giảm size mà vẫn giữ phân phối.
*   **Feature Store chia sẻ:** Tái sử dụng features giữa use-case để tránh ETL lặp.
*   **Compression:** Parquet + ZSTD, Delta/Apache Iceberg để giảm dung lượng.
*   **Lifecycle Policy:** Xóa/archiving dữ liệu cũ (S3 Glacier, Azure Archive).

---

## 2. Training & Compute

*   **Spot/Preemptible Instances:** Dùng AWS Spot, GCP Preemptible cho training batch.
*   **Auto-scaling Notebooks:** Dừng kernel khi idle.
*   **Lightweight Models:** Ưu tiên XGBoost/LightGBM/Linear thay vì deep nếu đạt KPI.
*   **Hyperparameter Search tiết kiệm:** Random Search + early stopping; Optuna pruning.
*   **Caching:** Lưu intermediate (preprocessed) để không xử lý lại.

---

## 3. Inference & Serving

*   **Batch over Real-time:** Nếu SLA cho phép, gộp request vào batch scoring.
*   **Serverless:** AWS Lambda, Cloud Functions cho traffic thấp.
*   **ONNX/Quantization:** Giảm model size, tăng tốc.
*   **Autoscaling policy:** Đặt min replicas = 0 cho dịch vụ ít truy cập.

---

## 4. Monitoring chi phí

*   **Cost Dashboard:** Grafana + Cloud cost APIs.
*   **Tagging:** Gắn tag project/model để theo dõi.
*   **Alert:** Thiết lập ngưỡng chi tiêu hàng ngày/tuần.

---

## 5. Checklist

- [ ] Review chi phí hàng tháng theo hạng mục (data, compute, storage).
- [ ] Dùng instance phù hợp workload (memory optimized vs compute optimized).
- [ ] Kiểm tra “zombie resources”: notebook mở, cluster idle.
- [ ] Tối ưu pipeline (ví dụ: gộp step ETL + training nếu cùng cluster).
- [ ] Benchmark model nhỏ hơn trước khi scale lên lớn.

> 💡 Tip: Ghi lại cost-per-experiment để biết khi nào một thử nghiệm worth it. Đôi khi cải thiện 0.1% accuracy không đáng nếu gấp đôi chi phí.
