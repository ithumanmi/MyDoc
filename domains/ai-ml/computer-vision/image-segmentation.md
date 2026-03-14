---
title: Image Segmentation Overview
description: Task framing, model families, metrics, và lộ trình thực chiến.
---

# 🖼️ Image Segmentation

## Bức tranh chung
- **Semantic Segmentation:** gán nhãn cho từng pixel (không phân biệt instance).  
- **Instance Segmentation:** phân biệt từng đối tượng riêng lẻ.  
- **Panoptic Segmentation:** kết hợp semantic + instance.

## Ứng dụng
- Y tế (phân vùng cơ quan/khối u), xe tự lái (lane, road, object), nông nghiệp (đếm cây/cỏ dại), bản đồ (satellite), sản xuất (defect detection).

## Kiến trúc tiêu biểu
- **CNN-based:** FCN, U-Net/U-Net++, DeepLab (v3/v3+), PSPNet, HRNet.  
- **Transformer/Hybrid:** SegFormer, Mask2Former, BEiT-FT, UViT; SAM (Segment Anything) cho zero-shot mask proposal.  
- **Instance/Panoptic:** Mask R-CNN, SOLO/CondInst, YOLACT, DETR/Mask2Former.

## Quy trình triển khai
1) **Dữ liệu & Annotation:** COCO/VOC format; kiểm tra class imbalance, quality mask.  
2) **Augmentation:** flip/scale/crop, color jitter; CutMix/Mosaic cho instance; copy-paste objects.  
3) **Model chọn nhanh:**
   - Edge/nhẹ: DeepLabv3+ (MobileNet), SegFormer-B0, BiSeNet.  
   - Chính xác cao: DeepLabv3+ (ResNet101), HRNet, SegFormer-B2/B4.  
   - Panoptic/instance: Mask R-CNN, Mask2Former.  
   - Zero/low-shot: SAM + prompt, kèm refinement nhỏ.  
4) **Loss:** CrossEntropy + Dice/Focal cho class imbalance; Lovasz-Softmax cho IoU.  
5) **Metric:** mIoU, Dice score, AP (instance), PQ (panoptic).  
6) **Tối ưu:** LR schedule (poly/cosine), mixed precision, crop size phù hợp VRAM, sliding window/tiling cho ảnh lớn.  
7) **Evaluation:** multi-scale + flip test (nếu cần), kiểm tra per-class IoU để xử lý class khó.  
8) **Deployment:** export ONNX/TensorRT; quantization/int8; crop-then-stitch cho ảnh rất lớn.

## Pitfalls
- Mask quality kém → model ceiling thấp; ưu tiên cải thiện annotation trước.  
- Class imbalance → cần focal/dice/lovasz hoặc re-weight.  
- Ảnh độ phân giải lớn dễ tràn VRAM; dùng tiling/sliding window.  
- Leakage augment: giữ phân tách train/val theo đối tượng/ngữ cảnh nếu cùng scene.

## Bộ nhớ nhanh
- **mIoU** = IoU trung bình trên class.  
- **Dice** nhạy với lớp hiếm; tốt cho medical.  
- **Poly LR**: lr = lr0 * (1 - iter/iter_max)^power.  
- **SAM**: dùng để gợi ý mask, cần post-process cho class.

## Liên quan
- [Vision Transformers](./vision-transformers.md)
- [CNN Architectures](./cnn-architectures.md)
- [Segmentation Guide](./segmentation-guide.md)