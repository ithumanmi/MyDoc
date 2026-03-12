## 🧪 Lab: Segmentation & Vision Transformers

> [← Back to Hands-on Labs](../machine-learning/hands-on-labs.md)

Thiết kế lab thực chiến kết hợp segmentation (UNet) và ViT (DeiT/Swin) cho dataset medical + classification.

---

## 1. Lab 1 — Brain Tumor Segmentation (UNet)

| Item | Chi tiết |
| --- | --- |
| Dataset | [BraTS 2021](https://www.kaggle.com/datasets/awsaf49/brats20-dataset-training-validation) |
| Goal | Semantic segmentation các vùng u |
| Steps | 1) Chuẩn bị data (convert NIfTI → PNG) 2) Train UNet (segmentation_models_pytorch) 3) Evaluate Dice/IoU 4) Deploy demo Streamlit |
| Deliverables | Notebook + model checkpoint + deployment notes |

**Checklist:**
- [ ] Log augmentation (flip, contrast)
- [ ] Dùng mixed precision để tăng tốc
- [ ] Visualize overlay mask vs ground truth

---

## 2. Lab 2 — Steel Defect Segmentation + ViT Classification

| Item | Chi tiết |
| --- | --- |
| Dataset | [Severstal Steel Defect](https://www.kaggle.com/c/severstal-steel-defect-detection) |
| Goal | Dual task: (a) Segmentation mask, (b) ViT classification có defect |
| Steps | 1) Train UNet++ cho mask 2) Extract mask stats làm feature 3) Fine-tune ViT/DeiT để phân loại defect type |
| Deliverables | 2 notebook (segmentation & ViT), pipeline `make train_seg`, `make train_vit` |

**Checklist:**
- [ ] Sử dụng [Vision Transformers Guide](./vision-transformers.md) để chọn backbone
- [ ] Transfer learning với frozen backbone trước
- [ ] Export ONNX cho cả hai model

---

## 3. Lab Flow

1. **Setup:** Clone Kaggle starter repo → thêm folder `cv-labs/`.
2. **Experiment Tracking:** Dùng MLflow + tagging (`task=seg`, `task=vit`).
3. **Deployment:** Kết hợp FastAPI endpoint `POST /segment` và `POST /classify`.
4. **Report:** Viết README mô tả architecture, metric, screenshot demo.

---

## 4. Bonus Challenges

*   Implement post-processing (connected components) để lọc noise.
*   Distill ViT sang mobile-friendly model (MobileViT, EfficientFormer).
*   AutoMLOps: Use GitHub Actions để auto-train khi push config mới.

> 🎯 Tip: Ghi lại lesson learned cho từng lab: data issue, metric đạt, thời gian train, cost.
