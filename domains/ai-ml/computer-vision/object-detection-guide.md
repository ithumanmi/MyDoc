## 🎯 Object Detection Guide

> [← Back to AI/ML Roadmap](../README.md)

Hướng dẫn từ việc chọn kiến trúc detection đến triển khai thực tế.

---

## 1. Các dòng mô hình chính

| Dòng | Ví dụ | Đặc điểm |
| --- | --- | --- |
| **One-stage** | YOLOv5/v8, RetinaNet | Nhanh, phù hợp real-time |
| **Two-stage** | Faster R-CNN | Độ chính xác cao hơn, chậm hơn |
| **Transformer-based** | DETR, DINO | Không cần NMS, kiến trúc đơn giản |
| **Anchor-free** | CenterNet, FCOS | Loại bỏ anchor box tuning |

---

## 2. Workflow triển khai

1. **Dataset:** COCO format (images + annotations). Tool: Label Studio, Roboflow.
2. **Preprocessing & Augmentation:** Albumentations (color jitter, mosaic, mixup).
3. **Training:** Chọn framework (YOLOv8 Ultralytics, MMDetection, Detectron2).
4. **Evaluation:** mAP@50, mAP@50-95, FPS.
5. **Deployment:** TensorRT, ONNX Runtime, NVIDIA Triton.

---

## 3. Ví dụ YOLOv8 Training (CLI)

```bash
pip install ultralytics

yolo detect train \
    model=yolov8m.pt \
    data=data/road-sign.yaml \
    epochs=50 \
    imgsz=640 \
    batch=16
```

---

## 4. Tips & Best Practices

*   **Balanced dataset:** Augment class hiếm.
*   **Hyperparameter tuning:** Learning rate, warmup, weight decay.
*   **Small objects:** Dùng higher resolution, FPN.
*   **Post-processing:** NMS variants (Soft-NMS, DIoU).

---

## 5. Resources

*   [YOLOv8 Docs](https://docs.ultralytics.com/)
*   [MMDetection](https://github.com/open-mmlab/mmdetection)
*   [Detectron2](https://github.com/facebookresearch/detectron2)

> 🚀 Tip: Với dự án enterprise, log toàn bộ training metrics + predictions trong MLflow/W&B để so sánh model qua thời gian.
