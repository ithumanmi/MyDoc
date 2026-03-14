# Tech Day 68: Tech Interview Question – Scale ML Service

**Câu hỏi:** “Bạn sẽ scale một ML inference service từ vài QPS lên hàng trăm/nghìn QPS như thế nào?”

## 1) Ý chính cần nhấn mạnh
- Nút nghẽn: latency model, I/O (feature store), batch/stream, GPU/CPU mix.
- Khả năng mở rộng: horizontal scaling, autoscaling theo QPS/latency.
- Chi phí: chọn mô hình triển khai (batch vs online), caching, model quantization.

## 2) Flow trả lời gợi ý
1) **Đo & profile**: xác định latency breakdown (preprocess/model/postprocess), chọn batch size tối ưu.
2) **Model serving**: dùng framework chuyên dụng (TensorRT-Serving, TorchServe, vLLM) hoặc FastAPI + ONNX/compiled graph; preload model, warmup.
3) **Hạ tầng**: autoscale (HPA/KEDA theo QPS/latency), load balancing; tách CPU/GPU pool; multi-instance để tránh cold start.
4) **Tối ưu model**: quantization, distillation, caching embedding/result (nếu phù hợp), chọn smaller variant cho realtime.
5) **Data path**: giảm round-trip (batch request khi được), cache feature, precompute hot keys.
6) **Observability**: metrics (p50/p95 latency, throughput, GPU util), tracing; alert khi vượt SLO.
7) **Rollout**: canary/blue-green; fallback model nếu lỗi; circuit breaker.

## 3) Bullet trả lời ngắn gọn (template 30-60s)
- “Tôi profile pipeline để tìm bottleneck, preload model và tối ưu batch size. Dùng server chuyên dụng hoặc FastAPI + ONNX, bật autoscale theo QPS/latency, tách CPU/GPU pool. Tối ưu model (quantization/distill), cache features/kết quả, giám sát p95 latency + error, rollout canary và fallback.”

## 4) Đi sâu nếu bị hỏi thêm
- **GPU/CPU mix:** GPU cho heavy model, CPU cho light/feature; autoscale độc lập.
- **Queue & batch:** Dùng request queue + micro-batching (đặc biệt cho GPU) để giữ latency ổn định.
- **Cost:** Spot instances, scale-to-zero cho traffic thấp, chọn model nhỏ cho realtime.
- **Reliability:** Circuit breaker, retry/backoff, fallback model, idempotency với async jobs.

## 5) Đoạn kết thúc nhấn mạnh (1 câu)
- “Scale ML service = tối ưu pipeline + hạ tầng autoscale + tối ưu model + quan sát p95 và rollout an toàn.”

## Reference / Solution (tùy chọn)
- Checklist: p95 latency budget, autoscale rule, batch size test, quantization experiment log.