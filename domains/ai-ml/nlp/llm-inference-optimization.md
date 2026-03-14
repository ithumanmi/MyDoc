---
title: LLM Inference Optimization Guide
description: Giảm độ trễ và chi phí khi suy luận LLM ở production.
---

# 🚀 LLM Inference Optimization

## Mục tiêu
- Giảm độ trễ (latency) và chi phí hạ tầng.  
- Giữ chất lượng đầu ra khi áp dụng tối ưu/quantization.

## Đòn bẩy chính
- **Model size & quantization:** INT8/INT4 (GPTQ, AWQ, GGUF), FP8 trên GPU mới.  
- **Serving stack:** vLLM, TensorRT-LLM, TGI, FasterTransformer.  
- **Batching & scheduling:** dynamic batching, continuous batching (vLLM), multi-tenant.  
- **Caching:** KV-cache reuse, prompt caching, spec decoding.  
- **Parallelism:** tensor/sequence/pipeline parallel; sử dụng multiple GPU hoặc multi-node.  
- **Distillation:** mô hình nhỏ hơn kế thừa mô hình lớn.

## Quy trình gợi ý
1) **Chọn mô hình & định dạng:** xem xét kích thước, support quant (AWQ/GPTQ), tokenizer.  
2) **Quantization:** thử INT8/INT4; đánh giá chất lượng sau quant.  
3) **Chọn runtime:**
   - **vLLM:** continuous batching, PagedAttention, tốt cho throughput.  
   - **TensorRT-LLM:** tối ưu GPU NVIDIA, cần build engine; tốt cho latency thấp.  
   - **TGI/FT:** dễ tích hợp, hỗ trợ GPU/CPU.  
4) **Cấu hình batching:** max batch size, max tokens/sec; tune `max_model_len`, `max_tokens_per_batch`.  
5) **KV cache:** bật và cấu hình đủ VRAM; xem xét **paged attention** để tránh phân mảnh.  
6) **Speculative decoding / Medusa:** dùng model nhỏ dự đoán trước; fallback model lớn xác nhận.  
7) **Monitoring:** p50/p95 latency, throughput, OOM, reject rate, quality metrics (eval set), token utilization.

## Mẹo nhanh
- **Short prompt:** rút gọn system prompt; dùng "prompt compression" nếu cần.  
- **Stop tokens rõ ràng** để kết thúc sớm.  
- **Max new tokens** hợp lý theo use-case.  
- **Pinned memory & NUMA affinity** cho CPU inference.  
- **GPU:** đảm bảo `torch.set_default_device("cuda")`, bật `torch.backends.cuda.matmul.allow_tf32=True` nếu phù hợp.

## Pitfalls
- Quant quá mạnh → giảm chất lượng; cần A/B test.  
- Context quá dài → bùng nổ KV cache; xem xét sliding window/attention sinks.  
- Batching cực lớn có thể tăng p95 mặc dù tăng throughput; cân bằng SLA.

## Liên quan
- [LLM Fine-tuning](./llm-fine-tuning.md)
- [Transformers & LLM](./transformers-llm.md)
- [MLOps - LLMOps](../mlops/llmops.md)