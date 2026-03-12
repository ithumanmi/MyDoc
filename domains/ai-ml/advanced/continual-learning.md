# ♾️ Continual & Lifelong Learning

> [← Advanced Topics](./README.md)

Continual learning cho phép mô hình học liên tục khi có dữ liệu mới mà không quên kiến thức cũ (giảm catastrophic forgetting).

---

## 1. Scenario

- **Task Incremental:** thêm nhiệm vụ mới (ví dụ thêm class mới).
- **Domain Incremental:** dữ liệu mới cùng task nhưng domain khác.
- **Class Incremental:** cả domain/class thay đổi theo thời gian.

---

## 2. Phương pháp chính

| Approach | Ý tưởng | Ví dụ |
| --- | --- | --- |
| **Regularization-based** | Thêm penalty giữ thông tin cũ | EWC, SI, LwF |
| **Replay-based** | Lưu subset dữ liệu cũ (memory buffer) | iCaRL, ER, GEM |
| **Dynamic Architecture** | Mở rộng layer/module mới | Progressive Networks, Dynamically Expandable Networks |
| **Prompt-based / Adapter** | Dùng prompt/adapters để phân vùng task | L2P, DualPrompt |

---

## 3. Workflow triển khai

1. **Task scheduler:** định nghĩa sequence nhiệm vụ.
2. **Model design:** chọn backbone + cơ chế continual.
3. **Memory management:** chiến lược chọn mẫu (herding, reservoir).
4. **Evaluation:** Average Accuracy, Forgetting Measure.
5. **Automation:** pipeline update khi có dữ liệu mới (scheduler + retrain).

```python
memory = []
for task in tasks:
    model.train(task.data, replay_buffer=memory)
    memory = reservoir_update(memory, task.data, size=2000)
```

---

## 4. Best Practices

- **Calibrate:** dùng temperature scaling để tránh bias task mới.
- **Metadata:** log version và task ID để truy vết.
- **Eval real-world:** dùng streaming metrics, concept drift detection.
- **Edge cases:** khi không thể lưu dữ liệu cũ → dùng generative replay (GAN sinh lại mẫu).

> 🎯 Lab: triển khai iCaRL cho CIFAR-100 incremental 10 classes/bước, so sánh accuracy giữa replay buffer 2k vs 5k mẫu.
