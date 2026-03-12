## 🧩 Computer Vision — Segmentation Guide

> [← Back to AI/ML Roadmap](../README.md)

Tổng hợp các kỹ thuật segmentation từ classical đến deep learning, workflow triển khai và tips tối ưu.

---

## 1. Loại bài toán

1. **Semantic Segmentation:** Phân loại từng pixel vào một class (ví dụ đường, tòa nhà).
2. **Instance Segmentation:** Phân biệt từng đối tượng (person #1, person #2).
3. **Panoptic Segmentation:** Kết hợp semantic + instance.

---

## 2. Mô hình kinh điển

| Mô hình | Ý tưởng chính | Khi nào dùng |
| --- | --- | --- |
| **UNet** | Encoder-Decoder + skip connection | Medical, ảnh nhỏ/trung bình |
| **UNet++** | Dense skip connections | Khi cần gradient tốt hơn |
| **DeepLabv3+** | Atrous convolution + ASPP | Độ chính xác cao, đa scale |
| **Mask R-CNN** | Faster R-CNN + nhánh mask | Instance segmentation |

---

## 3. Workflow triển khai

1. **Chuẩn bị dữ liệu:** Annotation dạng mask (PNG, RLE). Tools: Labelbox, CVAT.
2. **Augmentation:** Albumentations (flip, scale, elastic transform) để tăng data.
3. **Huấn luyện:** Sử dụng frameworks như PyTorch, MMsegmentation.
4. **Evaluation:** IoU, mIoU, Dice coefficient.
5. **Deployment:** ONNX, TensorRT, NVIDIA Triton cho real-time.

---

## 4. Code snippet (PyTorch + UNet)

```python
import segmentation_models_pytorch as smp
import torch

model = smp.Unet(
    encoder_name="resnet34",
    encoder_weights="imagenet",
    in_channels=3,
    classes=1,
)

criterion = smp.losses.DiceLoss(smp.losses.BINARY_MODE, from_logits=True)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)
```

---

## 5. Tips & Best Practices

*   **Class imbalance:** Dùng weighted loss (Dice, Focal).
*   **Patch-based training:** Khi ảnh quá lớn.
*   **Post-processing:** Morphological operations, CRF.
*   **Active learning:** Annotate thêm vùng model hay sai.

---

## 6. Resources

*   [Papers With Code — Segmentation Leaderboards](https://paperswithcode.com/area/computer-vision/segmentation)
*   [MMsegmentation](https://github.com/open-mmlab/mmsegmentation)
*   [Fastai Medical Imaging Course](https://course.fast.ai/videos/?lesson=4)

> 🧠 Tip: Với dataset nhỏ, freeze encoder (pretrained) và chỉ fine-tune decoder để tránh overfitting.
