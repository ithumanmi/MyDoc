## ⚡ Colab GPU Tips & Cost Saving

> [← Back to Labs](./README.md)

Tối ưu sử dụng GPU miễn phí/Pro trên Google Colab.

---

## 1. Quản lý phiên làm việc

- Sử dụng Colab Pro/Pro+ để có session dài hơn.
- Kích hoạt GPU (Runtime → Change runtime type → GPU).
- Tránh idle: dùng `while True: pass` hoặc auto-keepalive script hợp lý.

Checklist:

- [ ] Tự động lưu checkpoint lên GDrive/Cloud Storage
- [ ] Dọn session cũ để tránh limit
- [ ] Log thời gian sử dụng để tối ưu

---

## 2. Tối ưu dataset & storage

- Mount Google Drive hoặc dùng `gdown` tải dữ liệu nhanh.
- Sử dụng `zip`/`tar` để giảm thời gian copy.
- Cache dataset bằng `huggingface_hub snapshot_download` với `local_dir`.

---

## 3. Tối ưu training

- Mixed precision (`torch.cuda.amp`) giảm VRAM.
- Gradient checkpointing cho mô hình lớn.
- Dùng `batch_size` nhỏ + accumulate gradients.

Example snippet:

```python
scaler = torch.cuda.amp.GradScaler()
with torch.cuda.amp.autocast():
    loss = model(input_ids)
scaler.scale(loss).backward()
scaler.step(optimizer)
scaler.update()
```

---

## 4. Automation & Templates

- Tạo notebook template với sections: setup, data, training, monitoring.
- Dùng `%load_ext tensorboard` để xem metrics trực tiếp.
- Lưu `requirements.txt` + script setup để chạy lại nhanh.

---

## 5. Chiến lược tiết kiệm

- Chạy training nặng vào giờ thấp điểm (US night) để dễ lấy GPU mạnh.
- Snapshot model/checkpoint thường xuyên để resume.
- Kết hợp Colab + local compute (ví dụ training trên Colab, inference local).

> 🎯 Tip: Khi hết quota, chuyển sang Kaggle Notebook hoặc Gradient để tiếp tục training.
