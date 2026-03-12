# ⚡ Efficient Inference

> [← Advanced Topics](./README.md)

Mục tiêu: giảm latency & chi phí khi phục vụ mô hình lớn. Bao gồm quantization, pruning, distillation và runtime tối ưu.

---

## 1. Levers chính

| Kỹ thuật | Lợi ích | Công cụ |
| --- | --- | --- |
| **Quantization** (INT8/FP8/4bit) | Giảm memory, tăng throughput | GPTQ, AWQ, bitsandbytes, TensorRT-LLM |
| **Pruning** | Giảm tham số, FLOPs | Magnitude pruning, movement pruning, SparseGPT |
| **Distillation** | Model nhỏ học từ model lớn | TinyLlama, DistilBERT, LLaMA Guard |
| **KV Cache + Spec Decoding** | Tăng tốc autoregressive decoding | FlashAttention-2, Medusa, Lookahead Decoding |
| **Serving Runtime** | Batching, streaming, multi-model | vLLM, Ray Serve, Triton, Text Generation Inference |

---

## 2. Workflow tối ưu

1. **Baseline profiling:** đo latency/token/s chi phí GPU.
2. **Chọn target:** latency < 100ms, chi phí <$0.002/request...
3. **Áp dụng quantization:** thử 8-bit → 4-bit, so sánh quality drop.
4. **Prune/Distill:** nếu cần thêm (đặc biệt edge deployment).
5. **Serving stack:** chọn runtime phù hợp (vLLM cho LLM, Triton cho multi-modal).
6. **Monitoring:** theo dõi P95 latency, cache hit ratio.

---

## 3. vLLM snippet

```python
from vllm import LLM, SamplingParams

llm = LLM(model="TheBloke/Llama-2-13B-chat-GPTQ")
params = SamplingParams(temperature=0.7, top_p=0.9, max_tokens=256)

output = llm.generate(["Explain quantization"], sampling_params=params)
print(output[0].outputs[0].text)
```

> Ưu điểm: PagedAttention cho phép batch lớn mà không OOM, hỗ trợ tensor parallel.

---

## 4. Deployment checklist

- **Hardware:** GPU vs CPU vs ASIC (Inferentia, TPUv5e) phù hợp workload.
- **Scaling:** autoscaling theo tokens/s, warm pools để tránh cold start.
- **Caching:** prompt cache, KV cache persistence.
- **Observability:** tracing (OpenTelemetry), GPU metrics, request logging.
- **Safety:** enforce content filter/gating sau khi tối ưu.

> 🎯 Lab: benchmark 7B model trên A10G trước/sau quantization 4-bit + vLLM, đo throughput tokens/s và chi phí.
