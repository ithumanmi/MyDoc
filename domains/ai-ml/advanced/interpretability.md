# 🔍 Model Interpretability & Explainability

> [← Advanced Topics](./README.md)

Giải thích quyết định của mô hình là yêu cầu bắt buộc trong tài chính, y tế, pháp lý. Tài liệu này tổng hợp kỹ thuật SHAP/LIME, attention viz và pipeline triển khai explainability.

---

## 1. Techniques Map

| Loại | Kỹ thuật | Dùng khi |
| --- | --- | --- |
| **Global** | Feature importance (Permutation, SHAP global) | Xác định yếu tố ảnh hưởng chung |
| **Local** | LIME, SHAP values | Giải thích cho từng prediction |
| **Surrogate Model** | Train model đơn giản (tree) approximating black-box | Khi model phức tạp (GBDT/NN) |
| **Visualization** | Attention heatmap, Grad-CAM, Integrated Gradients | CV/NLP deep nets |
| **Counterfactual** | Tìm điều kiện tối thiểu để đổi kết quả | Lending, hiring |

---

## 2. SHAP Workflow

```python
import shap
model.fit(X_train, y_train)
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)
shap.summary_plot(shap_values, X_test)
```

1. Train model → tạo explainer.
2. Generate SHAP values cho tập cần giải thích.
3. Plot global (summary) + local (force plot).
4. Log kết quả vào model cards/report.

---

## 3. Attention Visualization (Transformers)

- Dùng `bertviz`, `ecco` để hiển thị attention heads.
- Với vision: Grad-CAM/Score-CAM highlight vùng ảnh.
- LLM: sử dụng `captum` hoặc tool custom overlay attention weights lên token.

---

## 4. Governance Checklist

- **Requirement:** xác định regulation (GDPR, Basel, HIPAA).
- **Documentation:** Model card: data, metrics, explainability method.
- **Automation:** phục vụ API explainability cho auditors.
- **Monitoring:** detect drift → cập nhật explanation baseline.

---

## 5. Tools

- **Open-source:** SHAP, LIME, Captum, Alibi explain, What-If Tool.
- **Cloud services:** AWS Clarify, Google Vertex Explainable AI, Azure Responsible AI dashboard.

> 🎯 Lab: Build dashboard SHAP + counterfactual cho mô hình credit scoring (XGBoost) và publish thành report PDF.
