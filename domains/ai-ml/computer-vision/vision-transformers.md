---
title: Vision Transformers (ViT) Quick Guide
description: Tổng quan kiến trúc, biến thể phổ biến và mẹo thực thi.
---

# 🧠 Vision Transformers

## Cốt lõi kiến trúc
- Chia ảnh thành patch (p×p), flatten → linear projection thành patch embeddings.  
- Thêm positional embedding (learnable hoặc sinusoidal).  
- Transformer encoder stack: Multi-Head Self-Attention + MLP, kèm LayerNorm, residual.  
- Token phân loại (`[CLS]`) hoặc pool trung bình để dự đoán.

## Biến thể tiêu biểu
- **ViT/DeiT:** baseline; DeiT dùng distillation token + training mạnh cho dữ liệu vừa.  
- **Swin Transformer:** cửa sổ trượt (shifted window) giảm độ phức tạp O(N^2) → O(N).  
- **ConvNeXt-hybrid:** kết hợp ưu điểm Conv (inductive bias) + Transformer.  
- **SegFormer/Mask2Former:** head nhẹ cho segmentation/panoptic.  
- **SAM (Segment Anything):** dùng ViT-H/G cho image encoder, promptable masks.

## Khi nào dùng
- Cần hiệu năng cao trên dataset lớn hoặc pretrain sẵn.  
- Yêu cầu biểu diễn linh hoạt, ít inductive bias hơn CNN.  
- Tác vụ dense (detection/segmentation) với backbone Transformer hiện đại (Swin/ViTDet/Mask2Former).

## Tips huấn luyện
- **Dữ liệu:** ViT cần nhiều dữ liệu; nếu data nhỏ, dùng mạnh augment (RandAugment), regularization (Mixup/CutMix, DropPath).  
- **Optimizer:** AdamW với weight decay chuẩn; LR cosine + warmup.  
- **Label smoothing** + **stochastic depth** cho mô hình lớn.  
- **Patch size:** patch nhỏ → tốt cho chi tiết nhưng tốn compute; patch lớn → nhanh hơn nhưng mất chi tiết.

## Inference & tối ưu
- Dùng **fp16**/AMP, **TensorRT/ONNX** cho sản xuất.  
- Với Swin/Windowed attention: chú ý kích thước ảnh chia hết kích thước cửa sổ.  
- Distillation hoặc knowledge distill từ ViT lớn sang mô hình nhẹ nếu cần edge.

## Pitfalls
- Data nhỏ + ViT thuần → dễ overfit, kém hơn CNN.  
- Positional embedding phụ thuộc kích thước patch/ảnh; resize sai có thể giảm chất lượng (cần interpolate PE).  
- Chi phí O(N^2) của self-attention với ảnh lớn; cân nhắc Swin/window attention.

## Liên quan
- [CNN Architectures](./cnn-architectures.md)
- [Image Segmentation](./image-segmentation.md)
- [Architectures Zoo](../deep-learning/architectures-zoo.md)