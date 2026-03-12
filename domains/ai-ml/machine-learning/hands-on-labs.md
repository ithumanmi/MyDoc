## 🧪 Hands-on Labs — Classic ML

> [← Back to AI/ML Roadmap](../README.md)

Lộ trình thực hành với notebook template, project mẫu và hướng dẫn chinh phục Kaggle để không chỉ học lý thuyết.

---

## 1. Notebook Template

```markdown
# Project Title

## 1. Problem Statement
- Business questions & success metric

## 2. Data & EDA
- Data source, schema, quick stats
- Missing values, outliers

## 3. Feature Engineering
- Transformations, encoding, scaling

## 4. Modeling
- Baseline
- Advanced models + hyperparameters

## 5. Evaluation
- Metrics table
- Error analysis

## 6. Deployment Notes
- Feature parity, inference plan

## 7. Next Steps
- Ideas để cải thiện
```

**Template repos:**
- [Classic ML Notebook Template](./notebooks/classic-ml-template.ipynb) — có sẵn cell skeleton, pipeline chuẩn.
- [Jupyter Project Boilerplate](https://github.com/dmatrix/Deep-Learning-Cookbook) (tham khảo cấu trúc)
- [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/)

---

## 2. Sample Project Ideas

| Project | Dataset | Focus |
| --- | --- | --- |
| **SME Credit Risk** | UCI Credit | Class imbalance, cost-sensitive metrics |
| **Retail Demand Forecast** | M5 Dataset | Feature engineering time-series, LightGBM |
| **Customer Segmentation + Personalization** | Wholesale Customers | Clustering + using clusters as features |
| **Fraud Detection** | Kaggle Credit Card Fraud | Anomaly detection + semi-supervised |
| **Housing Price Predictor** | California Housing | Feature engineering + SHAP explainability |

---

## 3. Kaggle Competition Playbook

1. **Scope the problem:** Hiểu metric (LogLoss, RMSE...), format submission.
2. **Baseline fast:** Simple model để thiết lập checkpoint.
3. **Feature notebook:** Từng bước log feature engineering.
4. **Model zoo:** Gradient boosting, linear, stacking.
5. **Validation discipline:** K-fold, time-series split, tránh leakage.
6. **Experiment tracking:** Bám theo template ở [Experiment Tracking](./experiment-tracking.md).
7. **Submit & Review:** Ghi lại public/private leaderboard score.

**Must-read threads & resources:**
*   [Kaggle Starter Repo Template](./kaggle-starter-repo.md) — cấu trúc repo, config và script submit.
*   [How to Win Kaggle Competitions — Top Solutions](https://www.kaggle.com/discussions)
*   [Feature Engineering Guides](https://www.kaggle.com/code) (search “feature engineering” + competition name)
*   [Segmentation & ViT Labs](../computer-vision/segmentation-vit-labs.md) — lab dataset, checklist UNet & ViT.
*   [CV Repo Template](../computer-vision/cv-repo-template.md) — clone để có cấu trúc dự án CV end-to-end.

---

## 4. Lab Journey Checklist

- [ ] Chọn 1 project regression + 1 classification.
- [ ] Dùng template notebook để ghi lại đầy đủ.
- [ ] Submit ít nhất 3 lần cho một Kaggle competition.
- [ ] Deploy demo nhỏ (Streamlit/FastAPI) cho 1 project.
- [ ] Viết retrospective: điều học được, metric đạt.

> 🚀 Tip: Mỗi project nên có README, link demo (nếu có), và folder `reports/` chứa notebook + slide. Đây cũng là portfolio tuyệt vời khi đi phỏng vấn.
