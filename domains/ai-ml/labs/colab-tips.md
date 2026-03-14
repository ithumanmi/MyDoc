---
title: Colab Tips (GPU Budget Saver)
description: Mẹo tối ưu Colab, giữ phiên GPU sống lâu, giảm chi phí thời gian.
---

# ⚙️ Colab Tips (GPU)

> Xem thêm bản chi tiết: [Colab GPU Tips](./colab-gpu-tips.md)

## Mẹo nhanh
- Dọn notebook: hạn chế output log quá dài, clear variables lớn.
- Giữ session: thao tác định kỳ nhẹ; tránh chạy cell trống lặp quá nhanh (dễ bị flag).
- Chọn runtime phù hợp: T4 cho đa số nhiệm vụ nhẹ; A100 cần khi batch lớn/ViT/LLM.
- Dùng `pip install --no-cache-dir` để giảm disk.
- Lưu checkpoint lên Drive/Hub; kiểm tra quota disk trước khi unzip dataset lớn.

## Mẫu thiết lập nhanh (PyTorch)
```python
import torch
torch.backends.cuda.matmul.allow_tf32 = True
torch.backends.cudnn.benchmark = True
```

## Checklist tối thiểu
- [ ] Kiểm tra GPU (`nvidia-smi`).
- [ ] Tắt bảng hiển thị log quá lớn.
- [ ] Lưu checkpoints định kỳ ra Drive/Hub.
- [ ] Dọn `/content` sau khi xong để tránh đầy disk.

## Liên quan
- [Colab GPU Tips (full)](./colab-gpu-tips.md)
- [Kaggle Competition Guide](./kaggle-competition-guide.md)