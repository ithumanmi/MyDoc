# ⚙️ Distributed Training Playbook

> [← Advanced Topics](./README.md)

Huấn luyện mô hình lớn đòi hỏi chia nhỏ bài toán cho nhiều GPU/TPU. Module này tóm tắt các chiến lược (data/model/pipeline parallelism), framework (DeepSpeed, FSDP, Megatron-LM) và checklist vận hành.

---

## 1. Chiến lược chính

| Strategy | Khi sử dụng | Ưu/Nhược |
| --- | --- | --- |
| **Data Parallelism** | Dataset lớn, model vừa fits GPU | Đơn giản (DDP), cần all-reduce → bottleneck khi model lớn. |
| **Model Parallelism** | Model không fit 1 GPU | Tensor parallel (Megatron), pipeline parallel; phức tạp hơn. |
| **Zero Redundancy Optimizer (ZeRO)** | Giảm memory optimizer state | DeepSpeed ZeRO stage 1-3 tách gradients/optimizer/params. |
| **Fully Sharded Data Parallel (FSDP)** | PyTorch native sharding | Shard params + gradients + optimizer, hỗ trợ activation checkpoint. |

---

## 2. Tech Stack Quick View

- **PyTorch DDP / FSDP** — Native APIs.
- **DeepSpeed** — ZeRO, 3D parallel (Data + Tensor + Pipeline), offload CPU/NVMe.
- **Megatron-LM** — Tensor + pipeline parallel cho LLM >10B.
- **Colossal-AI** — Booster cho MoE, heterogeneous memory.
- **Ray Train / Lightning Fabric** — High-level orchestration.

---

## 3. DeepSpeed cấu hình mẫu

```json
{
  "train_batch_size": 4096,
  "gradient_accumulation_steps": 8,
  "zero_optimization": {
    "stage": 3,
    "redundancy_level": 1,
    "overlap_comm": true
  },
  "bf16": {"enabled": true},
  "activation_checkpointing": {
    "partition_activations": true,
    "contiguous_memory_optimization": true
  }
}
```

---

## 4. Checklist vận hành

1. **Profiling:** dùng `torch.profiler`, Nsight Systems để xác định bottleneck (compute vs comm).
2. **Overlap comm/compute:** bật `gradient_as_bucket_view`, `overlap_comm` để giảm idle time.
3. **Mixed Precision:** BF16/FP16 + loss scaling.
4. **Activation Checkpointing:** giảm memory đổi lấy compute.
5. **Elastic Training:** TorchElastic/KubeFlow để tự recover khi node fail.

---

## 5. Pipeline triển khai

1. **Plan topology:** nvidia-smi topo, NVLink vs PCIe.
2. **Config parallelism:** tensor parallel size, pipeline stages, global batch.
3. **Launch:** `torchrun` hoặc `deepspeed` CLI.
4. **Monitor:** Prometheus (GPU util, bandwidth), DeepSpeed logs.
5. **Tune:** Adjust micro-batch, checkpoint save interval, gradient accumulation.

> 🎯 Lab gợi ý: fine-tune LLaMA-13B với DeepSpeed ZeRO-3 trên 4 GPU — đo memory footprint và throughput trước/sau.
