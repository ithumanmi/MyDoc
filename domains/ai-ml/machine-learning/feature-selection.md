## 🎯 Feature Selection Chuyên sâu

> [← Back to AI/ML Roadmap](../README.md)

Feature selection giúp model đơn giản hơn, tránh overfitting, tăng interpretability và giảm chi phí inference. Đây là toolkit chuyên sâu cho Classic ML.

---

## 1. Phân loại phương pháp

1. **Filter Methods:** Chọn feature dựa trên thống kê độc lập với model.
2. **Wrapper Methods:** Dùng model để đánh giá subset feature.
3. **Embedded Methods:** Feature selection diễn ra trong quá trình train (regularization, tree-based).
4. **Hybrid / Stability:** Kết hợp nhiều kỹ thuật để đảm bảo kết quả ổn định.

---

## 2. Filter Methods

*   **Correlation / Mutual Information:** Loại bỏ feature tương quan cao hoặc không liên quan đến target.
*   **Chi-Square / ANOVA F-test:** Cho categorical/continuous.
*   **Information Gain / Entropy:** Dùng trong text mining.
*   **Variance Threshold:** Loại feature ít biến thiên.

**Khi dùng:** Là bước nhanh trước khi chạy model đắt đỏ.

---

## 3. Wrapper Methods

*   **Forward / Backward Selection:** Thử thêm/bớt feature từng bước.
*   **Recursive Feature Elimination (RFE):** Train model → loại feature quan trọng thấp → lặp.
*   **Genetic Algorithms / Bayesian Optimization:** Tối ưu subset một cách heuristic.

**Ưu:** Thường cho kết quả tốt vì model-aware. **Nhược:** Tốn tài nguyên.

---

## 4. Embedded Methods

*   **L1 Regularization (Lasso):** Ép trọng số về 0 => chọn feature.
*   **Elastic Net:** Kết hợp L1 + L2 để vừa select vừa ổn định.
*   **Tree-Based Importance:** Random Forest, Gradient Boosting, XGBoost gain.
*   **SHAP / Permutation Importance:** Đo ảnh hưởng khi hoán đổi feature.

**Tip:** Với tree-based, chú ý bias khi feature có nhiều level/tính liên tục khác nhau.

---

## 5. Stability Selection

1. Subsample dữ liệu nhiều lần.
2. Chạy feature selection (ví dụ Lasso) trên mỗi subset.
3. Chọn feature xuất hiện nhất quán qua nhiều lần.

**Ưu:** Giảm rủi ro chọn feature “ăn may”.

---

## 6. Time-Series & Streaming Considerations

*   Tránh leakage bằng cách giữ thứ tự thời gian (no random shuffle khi cross-validate).
*   Dùng lag/rolling features, sau đó RFE hoặc L1 để giảm số lượng.
*   Theo dõi drift—feature quan trọng hôm nay có thể mất tác dụng ngày mai.

---

## 7. Workflow đề xuất

1. Làm sạch & feature engineering.
2. Filter sơ bộ (correlation, variance).
3. Chạy embedded/wrapper (L1, RFE với model mục tiêu).
4. Kiểm tra stability + interpretability (SHAP, Permutation).
5. Log kết quả, tái sử dụng trong pipeline.

---

## 8. Tooling

*   **scikit-learn:** `SelectKBest`, `RFE`, `RFECV`, `SelectFromModel`.
*   **Featuretools + AutoML:** Kết hợp selection trong quá trình search.
*   **SHAP, ELI5, Alibi:** Explainability.
*   **Optuna/Hyperopt:** Tối ưu hyper-parameters + feature subset.

---

## 9. Checklist

- [ ] Đảm bảo không có leakage khi đánh giá feature.
- [ ] So sánh model baseline vs. model sau khi chọn feature.
- [ ] Theo dõi ảnh hưởng tới latency/inference cost.
- [ ] Document lý do giữ/bỏ feature để team hiểu.

> 📌 Tip: Với dữ liệu tabular phức tạp, kết hợp nhiều phương pháp và ưu tiên feature vừa hiệu quả vừa dễ giải thích. Đừng bỏ qua domain knowledge.
