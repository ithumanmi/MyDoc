## 🧱 Feature Engineering: “Xây nền” cho Classic ML

> [← Back to AI/ML Roadmap](../README.md)

Model tốt chỉ mạnh khi đặc trưng (feature) đúng. Feature Engineering là quá trình biến đổi dữ liệu thô thành những tín hiệu mà model dễ học nhất.

---

## 1. Nguyên tắc vàng

1. **Hiểu domain:** Làm việc với experts để biết yếu tố nào mang ý nghĩa thực tế.
2. **Đơn giản trước:** Feature đơn giản, dễ giải thích thường hiệu quả và bền vững.
3. **Tự động hóa:** Dùng pipeline (sklearn ColumnTransformer, Featuretools) để tái sử dụng.
4. **Giám sát leakage:** Không để thông tin tương lai chảy vào quá trình train.

---

## 2. Quy trình 5 bước

1. **Khám phá dữ liệu (EDA):** Phân phối, outlier, missing values.
2. **Tiền xử lý:** Fill missing (mean/median, model-based), encode categorical.
3. **Tạo feature:** Interaction, aggregation, rolling window, domain heuristics.
4. **Chọn feature:** Filter (correlation, chi-square), wrapper (RFE), embedded (L1/L2, tree importance).
5. **Scale/Normalize:** StandardScaler, MinMax, RobustScaler.

---

## 3. Kỹ thuật phổ biến

### 3.1 Numerical
*   **Polynomial Features:** Kết hợp bậc 2/3 cho các quan hệ phi tuyến.
*   **Binning:** Chia khoảng giá trị để giảm noise.
*   **Log / Box-Cox:** Làm “thẳng” các phân phối lệch.
*   **Rolling / Lag Features:** Cho time-series.
*   **Time-based Features:** `hour`, `dayofweek`, `is_holiday`.

### 3.2 Categorical
*   **One-hot / Target Encoding:** Chọn tùy số lượng category.
*   **Frequency / Count Encoding:** Giữ thông tin mật độ.
*   **Entity Embeddings:** Dùng NN học representation cho categorical lớn.
*   **Weight of Evidence (WOE):** Cho credit scoring.

### 3.3 Text
*   **TF-IDF, Bag-of-Words:** Baseline nhanh.
*   **N-gram:** Tăng ngữ cảnh.
*   **Pretrained Embeddings:** Word2Vec, BERT embeddings, sentence transformers.
*   **Topic Modeling:** LDA để tạo feature topic distribution.

### 3.4 Feature Interaction & Aggregation
*   **Cross Features:** `price * quantity`, `age_bucket * gender`.
*   **Group Aggregation:** Trung bình/tổng dữ liệu theo nhóm.
*   **Ratio:** Lợi nhuận / Doanh thu, debt-to-income.
*   **Window Stats:** mean/max/std theo rolling window cho time-series.

---

## 4. Công cụ & Automation

*   **Pipelines:** scikit-learn `Pipeline`, `ColumnTransformer`, DBT.
*   **Auto FE:** Featuretools (Deep Feature Synthesis), tsfresh, Kats (time-series).
*   **Feature Store:** Feast, Tecton để chia sẻ feature giữa teams.
*   **Experiment Tracking:** MLflow/W&B để log feature set, schema, stats.

---

## 5. Kiểm thử & Đánh giá

1. **Feature Importance:** Permutation, SHAP, gain.
2. **A/B Feature:** So sánh model có/không có feature mới.
3. **Stability:** Kiểm tra drift theo thời gian, đặc biệt domain tài chính.
4. **Explainability:** Feature phải giải thích được cho business. Dùng `shap.dependence_plot` để minh hoạ.

---

## 6. Checklist trước khi deploy

- [ ] Có pipeline sinh feature tự động, reproducible?
- [ ] Feature mới có làm tăng leakage?
- [ ] Đã log metadata (owner, mô tả, công thức)?
- [ ] Feature có drift monitor?

> 🔬 Tip: Đối với tabular data, 50% thành công nằm ở feature engineering. Hãy iterate nhanh với notebook + pipeline reusable để lan tỏa cho team. Lưu lại catalog feature (data lineage, owner) để dễ audit.
