# 🧪 Synthetic Data & Augmentation

> [← Advanced Topics](./README.md)

Synthetic data giúp mở rộng dataset, bảo vệ privacy và tăng coverage cho edge cases. Áp dụng cho CV, NLP, tabular, time-series.

---

## 1. Use Cases

- **Data imbalance:** tạo thêm mẫu cho lớp hiếm.
- **Privacy:** thay thế dữ liệu thật (healthcare, finance).
- **Simulation:** AV, robotics, digital twins.
- **What-if testing:** stress test mô hình trong scenario hiếm.

---

## 2. Techniques & Tools

| Domain | Kỹ thuật | Công cụ |
| --- | --- | --- |
| CV | GAN, Diffusion, NeRF | Stable Diffusion, SyntheticaDETR, Unity Perception |
| NLP | LLM paraphrasing, back-translation | GPT-4, Llama Guard, MarianMT |
| Tabular | CTGAN, TVAE, CopulaGAN | SDV (Synthetic Data Vault) |
| Time-series | TimeGAN, DSGAN, Neural CDE | kats, tsaug |

---

## 3. Workflow chuẩn

1. **Define goal:** cân bằng lớp? mở rộng scenario?
2. **Seed data:** chuẩn hoá dữ liệu thật dùng làm reference.
3. **Generate:** chọn mô hình (GAN/diffusion/LLM) + tham số.
4. **Validate:** so sánh phân phối (KS test, FID, privacy metrics).
5. **Integrate:** mix synthetic + real theo tỷ lệ (ví dụ 30%).

```python
from sdv.tabular import CTGAN
model = CTGAN()
model.fit(real_df)
synthetic = model.sample(5000)
```

---

## 4. Quality & Privacy

- **Utility metrics:** train downstream model với synthetic → đo accuracy.
- **Statistical similarity:** JS divergence, PCA overlay.
- **Privacy:** membership inference test, k-anonymity, DP noise.
- **Human review:** với dữ liệu text/image quan trọng.

---

## 5. Best Practices

- Log seed + config để reproducible.
- Kết hợp rule-based augmentation cho baseline.
- Giữ synthetic ratio <50% nếu chưa đánh giá kỹ.
- Gắn label synthetic trong data lake để tracking.

> 🎯 Lab: dùng SDV tạo thêm dữ liệu bảng tín dụng (class fraud hiếm) → train XGBoost → so sánh F1 với baseline.
