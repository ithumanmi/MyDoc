# 🎓 Supervised Learning: Học có Giám sát (Classic ML)

> [← Back to Classic ML Hub](./README.md) | [← AI/ML Roadmap](../README.md)

Supervised Learning là xương sống của hệ thống AI trong sản xuất: dự đoán doanh thu, phân loại khách hàng, phát hiện gian lận. Bạn đưa vào dữ liệu **đã có nhãn**, mô hình học quy luật để dự đoán cho dữ liệu mới.

---

## 0. TL;DR & Mindset

- Xác định **bài toán** (Regression vs Classification) trước khi chọn thuật toán.
- Luôn có **baseline nhanh** (Linear/Logistic) trước khi thử mô hình phức tạp.
- Tách **train/validation/test** rõ ràng + bật tracking (MLflow/W&B).
- Song song học **Feature Engineering + Model Selection** để tối ưu pipeline.

---

## 1. Core Workflow

1. **Problem Framing:** business metric → ML metric (RMSE, F1, ROC-AUC...).
2. **Data Audit:** missing values, imbalance, leakage, outliers.
3. **Feature Engineering:** scaling, encoding, domain features (xem thêm [feature-engineering.md](./feature-engineering.md)).
4. **Split & Cross-validation:** Stratified K-Fold cho classification, TimeSeriesSplit cho chuỗi thời gian.
5. **Baseline Model:** Linear/Logistic + simple tree để biết mức performance tối thiểu.
6. **Experiment Loop:** thử các thuật toán phía dưới, tune hyperparameter, log kết quả.
7. **Evaluation & Explainability:** confusion matrix, feature importance/SHAP.
8. **Deployment Checklist:** export model, pack pipeline (sklearn Pipeline / ONNX) + monitoring.

> 🧪 Notebook gợi ý: [Hands-on Labs](./hands-on-labs.md) → Regression → Classification mini projects.

---

## 2. Regression Playbook (Dự đoán giá trị liên tục)

| Nhánh | Khi nào dùng | Notes |
|-------|--------------|-------|
| **Linear/Ridge/Lasso/ElasticNet** | Quan hệ tuyến tính hoặc gần tuyến tính, ít feature | Ridge giảm variance; Lasso để loại bớt feature. Kiểm tra multicollinearity (VIF). |
| **Polynomial & Basis Expansion** | Có quan hệ cong nhẹ, vẫn muốn giữ mô hình giải thích được | Chuẩn hóa feature trước khi thêm bậc cao để tránh exploding gradients. |
| **SVR / Gaussian Process** | Dataset nhỏ, cần boundary mượt hoặc ước lượng uncertainty | Kernel trick cho dữ liệu phi tuyến, GPR khá tốn compute. |
| **Tree-based (Decision Tree, Random Forest)** | Feature phi tuyến, tương tác mạnh | Không cần scaling, bắt được interaction tốt, dễ song song hóa. |
| **Gradient Boosting (XGBoost, LightGBM, CatBoost)** | Cần accuracy cao, dữ liệu vừa đến lớn | Early stopping + regularization (`min_child_weight`, `lambda`) để tránh overfit. |

**Metrics quan trọng:** MAE (chịu outlier tốt), RMSE (phạt lỗi lớn mạnh hơn), MAPE (khi dữ liệu dương), R² (so sánh với baseline trung bình).

---

## 3. Classification Playbook (Dự đoán nhãn)

### 3.1 Linear & Probabilistic Models
- **Logistic Regression / Softmax:** baseline mạnh, giải thích được, hỗ trợ regularization + class weight để xử lý imbalance nhẹ.
- **Naive Bayes (Gaussian/Multinomial/Bernoulli):** cực nhanh cho text, cần giả định độc lập feature.

### 3.2 Distance & Kernel Methods
- **k-Nearest Neighbors:** không huấn luyện, chỉ cần metric + k; phù hợp datasets nhỏ, cần scaling trước.
- **Support Vector Machine (SVM):** tìm hyperplane tối đa margin, kernel RBF/poly để xử lý phi tuyến; chú ý tuning `C`, `gamma`.

### 3.3 Tree-based & Ensembles
- **Decision Tree:** dễ explain nhưng overfit → pruning hoặc dùng ensemble.
- **Random Forest:** bagging hàng trăm cây + voting (xem chi tiết [ensemble-methods.md](./ensemble-methods.md)).
- **Gradient Boosting (XGB/LGBM/CatBoost):** chuẩn vàng Kaggle cho tabular.

### 3.4 Multi-class & Multi-label
- Dùng chiến lược **One-vs-Rest**, **One-vs-One**, hoặc native multi-class (LightGBM, CatBoost).
- Multi-label: logistic regression nhiều nhãn, hoặc tree-based với objective chuyên biệt (Binary relevance, Classifier chains).

**Metrics quan trọng:** Precision/Recall/F1, ROC-AUC, PR-AUC, Matthews Correlation Coefficient (MCC) khi dữ liệu mất cân bằng.

---

## 4. Xử lý Thách thức Dữ liệu

| Vấn đề | Cách xử lý |
|--------|------------|
| **Imbalanced Classes** | Stratified split, class weight, oversampling (SMOTE, ADASYN), undersampling, focal loss (cho boosting). |
| **Feature Scaling** | Chuẩn hóa (Standard/MinMax) cho model dựa trên khoảng cách (SVM, kNN) hoặc gradient (Linear); dùng `Pipeline` để tránh leakage. |
| **Categorical High-cardinality** | Target encoding, CatBoost encoder, hashing.
| **Data Leakage** | Giữ pipeline strict: fit scaler/encoder chỉ trên train, cẩn thận với thời gian (lag features). |
| **Concept Drift** | Monitoring metric theo thời gian, retrain định kỳ, dùng online learning (River, Vowpal Wabbit). |

---

## 5. Evaluation & Experiment Tracking

- **Confusion Matrix:** đọc FP/FN để ưu tiên tối ưu hoá.
- **Cross-validation:** Nested CV khi so sánh model + tuning hyperparameter.
- **Learning Curve / Validation Curve:** phát hiện underfit/overfit.
- **Calibration:** Platt scaling / Isotonic để có xác suất "thật" (credit scoring, medical).
- **Tracking:** MLflow, W&B, Neptune để log params/metrics/artifacts → reproducibility.

> 📌 Checklist: Metric phù hợp business? Có báo cáo kèm Confidence Interval? Có log seed & version dữ liệu?

---

## 6. Tooling & Practice

- **Libraries:** scikit-learn, LightGBM, XGBoost, CatBoost, Statsmodels, Optuna/Ray Tune.
- **Pipelines:** sklearn `ColumnTransformer`, `Pipeline`, feature store (Feast) cho production.
- **Hands-on:** [practice-exercises.md](./practice-exercises.md) + [benchmark-datasets.md](./benchmark-datasets.md).
- **Deployment:** xem [deployment-templates.md](./deployment-templates.md) + [experiment-tracking.md](./experiment-tracking.md).

---

## 7. Next Steps

1. Làm 1 project regression + 1 project classification end-to-end.
2. Đọc kết quả explainability (SHAP/Permutation) → tạo insight business.
3. Chuẩn bị nâng cấp sang [Unsupervised Learning](./unsupervised-learning.md), [Semi-supervised](./semi-supervised-learning.md), và [Ensemble Methods](./ensemble-methods.md) để dựng pipeline mạnh hơn.
