## ⚡ LLM Inference Optimization

> [← Back to NLP](./README.md)

Tối ưu chi phí & latency khi serve LLM ở production: quantization, batching engine (vLLM) và TensorRT-LLM.

---

## 1. Quantization Basics

| Loại | Đặc điểm | Khi dùng |
| --- | --- | --- |
| **INT8** | Nhẹ, accuracy tốt | CPU/GPU inference |
| **INT4 (NF4)** | Giảm VRAM mạnh, cần calibration | Edge hoặc GPU nhỏ |
| **GPTQ/AWQ** | Post-training quantization tối ưu | Deploy nhanh |

Checklist:

- [ ] Calibration dataset gồm prompt đại diện.
- [ ] Đo perplexity trước/sau quantization.
- [ ] Với QLoRA → merge về FP16 khi cần chất lượng cao.

---

## 2. Serving Engines

### vLLM

* PagedAttention cho phép batching động, throughput cao.
* API compatible với OpenAI, hỗ trợ tensor parallel.

```bash
python -m vllm.entrypoints.api_server \
  --model meta-llama/Llama-2-13b-chat-hf \
  --dtype bfloat16 \
  --tensor-parallel-size 2
```

### TensorRT-LLM

* Tối ưu graph + kernel fusion trên GPU NVIDIA.
* Hỗ trợ FP8/INT8, KV cache optimization.

```bash
trtllm-build --checkpoint_dir llama-7b --output_dir trtllm-engine --gemm_plugin autotune
```

### Text Generation Inference (TGI)

* Multi-GPU, streaming, token streaming via SSE/websocket.

---

## 3. Batching & KV Cache

1. **Continuous batching:** gom yêu cầu đến từ nhiều user.
2. **KV cache reuse:** cache prefix để tăng tốc multi-turn chat.
3. **Speculative decoding:** dùng model nhỏ dự đoán trước tokens.

> Tip: Theo dõi token/s, latency P95/P99.

---

## 4. Deployment Checklist

- [ ] Chọn engine (vLLM/TGI/TensorRT-LLM) phù hợp hạ tầng.
- [ ] Autoscaling theo token throughput (KEDA, Kubernetes HPA).
- [ ] Giới hạn context length phù hợp (4k/8k/32k) để tránh OOM.
- [ ] Bật logging structured (prompt, tokens, latency) → observability.
- [ ] Guardrail: input filtering, output moderation.

---

## 5. Cost Optimization Tips

* Dùng quantized models (GGUF, GPTQ) cho inference offline.
* Triển khai hybrid cloud: GPU on-prem + burst lên đám mây.
* Theo dõi tokens / request → tối ưu prompt để giảm lãng phí.
