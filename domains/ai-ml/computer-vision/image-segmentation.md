## 🧩 Image Segmentation Guide

> [← Back to Computer Vision](./README.md)

Nắm rõ sự khác biệt giữa semantic vs instance segmentation và các kiến trúc trụ cột như U-Net, Mask R-CNN.

---

## 1. Semantic vs Instance vs Panoptic

| Loại | Mô tả | Ví dụ |
| --- | --- | --- |
| **Semantic** | Gán nhãn cho từng pixel theo class | Phân vùng đường, cây, toà nhà |
| **Instance** | Phân biệt từng đối tượng cùng class | Đếm xe hơi, theo dõi từng người |
| **Panoptic** | Kết hợp semantic + instance | Autonomous driving, robotics |

---

## 2. U-Net & Biến thể

### U-Net cơ bản
* Encoder-decoder đối xứng với skip connections.
* Hoạt động tốt trên dataset nhỏ (medical imaging).

### Biến thể
* **U-Net++:** Dense skip connections.
* **Attention U-Net:** Thêm attention gates.
* **UNeXt / UNETR:** kết hợp Transformer cho encoder.

> PyTorch snippet: `segmentation_models_pytorch.Unet(encoder_name="resnet34", classes=num_classes)`

---

## 3. Mask R-CNN

* Extension của Faster R-CNN → thêm branch mask.
* Pipeline: Region Proposal Network → ROI Align → classification/bbox/mask.
* Ưu điểm: Instance-level, chính xác; Nhược điểm: chậm hơn so với YOLACT.

---

## 4. Modern Architectures

| Model | Ý tưởng | Use case |
| --- | --- | --- |
| **DeepLab v3+** | Atrous Spatial Pyramid Pooling + decoder nhẹ | Semantic segmentation độ chính xác cao |
| **SegFormer** | Hierarchical Transformer encoder + lightweight MLP decoder | Edge devices, real-time |
| **Mask2Former** | Universal architecture cho segmentation/panoptic | Kết hợp attention + query-based |
| **Segment Anything (SAM)** | Promptable ViT backbone + mask decoder | Labeling, interactive segmentation |

---

## 5. Workflow triển khai

1. **Chuẩn bị dữ liệu:** Annotate bằng CVAT/Label Studio, lưu COCO/Mask format.
2. **Augmentation:** Photometric + geometric, mixup/cutmix hiếm dùng.
3. **Loss functions:** Cross-entropy, Dice loss, Lovasz hinge (class imbalance).
4. **Metrics:** mIoU, Dice, AP (instance).
5. **Inference tricks:** Test-time augmentation, model ensembling, CRF post-processing.

---

## 6. Tools & Resources

* [segmentation_models_pytorch](https://github.com/qubvel/segmentation_models.pytorch)
* [Detectron2](https://github.com/facebookresearch/detectron2)
* [SAM](https://segment-anything.com/)

> 🎯 Tip: Với dataset nhỏ, fine-tune U-Net pretrained (ImageNet encoder) thường hiệu quả hơn train từ đầu.
