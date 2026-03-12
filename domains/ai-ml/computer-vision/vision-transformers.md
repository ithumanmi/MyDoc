## 🔶 Vision Transformers (ViT) Guide

> [← Back to AI/ML Roadmap](../README.md)

Hiểu kiến trúc ViT, Deit, ứng dụng và cách fine-tune cho bài toán computer vision hiện đại.

---

## 1. Tại sao ViT?

*   Thay thế convolution bằng self-attention, xử lý patch như token.
*   Hiệu quả trên dataset lớn (ImageNet-21k) và tận dụng transfer learning.
*   Dễ mở rộng sang multi-modal (CLIP, Segment Anything).

---

## 2. Kiến trúc tổng quan

1. **Patch Embedding:** Chia ảnh thành patch (16x16), flatten, linear projection.
2. **Positional Encoding:** Thêm thông tin vị trí.
3. **Transformer Encoder:** Multi-head self-attention + MLP blocks.
4. **Class Token:** Aggregate thông tin toàn ảnh.

---

## 3. Hệ sinh thái Vision Transformer

| Model | Architecture | Use Case |
| --- | --- | --- |
| **ViT** | Patch → Linear Embedding → Transformer encoder + class token | Image classification, fine-tune downstream |
| **CLIP** | Image encoder (ViT/ResNet) + Text encoder (Transformer) → Contrastive | Zero-shot classification, multi-modal search |
| **SAM** | Prompt-based ViT encoder + mask decoder | Segment Anything: interactive/promptable segmentation |
| **DINO v2** | Self-supervised ViT với knowledge distillation | Feature extraction, dense prediction, foundation backbone |
| **DeiT** | Data-efficient ViT + distillation token từ CNN teacher | Training trên dataset nhỏ |
| **Swin Transformer** | Hierarchical window attention + shifted windows | Detection/segmentation trong pipeline như Mask2Former |

---

## 4. Fine-tuning Workflow

1. **Chọn backbone:** Ví dụ `vit_base_patch16_224`. (HuggingFace timm)
2. **Thay head:** Linear layer phù hợp số class.
3. **Freeze/unfreeze:** Bắt đầu với head-only, sau đó unfreeze.
4. **Augmentation:** RandAugment, Mixup, Cutmix.
5. **Opt:** AdamW, learning rate warmup + cosine decay.

```python
import timm
import torch.nn as nn

model = timm.create_model("vit_base_patch16_224", pretrained=True)
model.head = nn.Linear(model.head.in_features, num_classes)
```

---

## 5. Ứng dụng

1. **Image Classification:** Fine-tune ViT/DeiT trên dataset domain-specific.
2. **Zero-shot Retrieval/Search:** Dùng CLIP embeddings cho image ↔ text search.
3. **Segmentation/Panoptic:** SAM, Mask2Former, Segment Anything + prompt.
4. **Self-supervised Feature Bank:** DINO v2 để trích feature cho downstream (detection, depth, pose).
5. **Multimodal Agents:** CLIP + LLM (Flamingo, GPT-4V) để reasoning về ảnh.

---

## 6. Hiệu năng & Tối ưu

*   ViT cần dataset lớn → dùng transfer hoặc data augmentation.
*   Lưu ý chi phí (O(N^2)) với độ phân giải cao → patch size lớn hơn hoặc Swin.
*   Distillation (DeiT) giúp train trên dataset nhỏ.

---

## 7. Resources

*   [Vision Transformer](https://arxiv.org/abs/2010.11929)
*   [DeiT: Data-efficient Image Transformers](https://arxiv.org/abs/2012.12877)
*   [CLIP](https://arxiv.org/abs/2103.00020)
*   [Segment Anything](https://arxiv.org/abs/2304.02643)
*   [DINO v2](https://arxiv.org/abs/2304.07193)
*   [timm library](https://github.com/rwightman/pytorch-image-models)
*   [Hugging Face ViT Models](https://huggingface.co/models?search=vit)

> ⚡ Tip: Khi deploy, export ViT sang ONNX/TensorRT và cân nhắc dynamic quantization để giảm latency.
