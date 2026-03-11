---
title: "Profiling & Optimization"
description: "CPU/memory profiling, flame graphs, benchmarking cho hiệu năng backend."
tags:
  - backend
  - performance
  - profiling
updated: 2026-03-11
---

# 🔬 Profiling & Optimization (L2-L3)

## 1. Quy trình tối ưu
1. **Đặt mục tiêu** (latency P95, throughput).
2. **Đo** (profiling) → xác định bottleneck.
3. **Optimize** từng hotspot.
4. **Đo lại** để xác nhận.

## 2. CPU Profiling
- **Sampling profiler:** Linux `perf`, Go `pprof`, Java Flight Recorder.
- **Flame Graph:** visualize stack sử dụng CPU.
- **Identifying hotspot:** function chiếm % CPU cao → candidate tối ưu.

### Tool ví dụ
- Go: `go tool pprof -http=:8080 cpu.out`
- Java: `jcmd <pid> JFR.start` + JFR UI.
- Node: `0x`, Chrome DevTools.

## 3. Memory Profiling
- **Heap dump**: xem object tạo nhiều.
- **Allocation profiling**: `pprof heap`, VisualVM.
- **GC pressure:** monitor GC pause time.

## 4. Benchmark & Load testing
- **Micro benchmark**: đo từng function (`go test -bench`, JMH, BenchmarkDotNet).
- **System benchmark**: k6, Locust, JMeter.
- **Latency percentile**: P50/P95/P99.

## 5. Optimization patterns
- **Hot path caching**.
- **Avoid alloc** (pool object, reuse buffer).
- **Batching:** gộp DB call.
- **Vectorization** / SIMD khi cần.

## ✅ Apply it
- [ ] Enable profiling flag cho service (pprof/JFR).
- [ ] Chạy load test mô phỏng traffic thực tế.
- [ ] Sinh flame graph cho CPU hot path, document top functions.
- [ ] Tối ưu 1 hotspot (ví dụ: parse JSON, allocate struct).
- [ ] Đo lại metric → log kết quả vào CHANGELOG/Runbook.

## 🔗 Cross-reference
- [high-performance/README.md](./README.md) – overview series.
- [monitoring-observability](../../monitoring-observability.md) – metric + tracing.
- [profiling tooling resources](../../resources/tools.md) – tool tham khảo thêm.