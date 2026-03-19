---
title: "Latency Stack: Python vs C++/Rust"
---

# Latency Stack: Python vs C++/Rust

> [← Back to Quantitative Trading Hub](./README.md)

So sánh nhanh các lớp latency khi triển khai trading stack.

## Bảng so sánh
| Thành phần              | Python (pandas + websockets)       | C++/Rust (asio/uring)            | Ghi chú |
|-------------------------|------------------------------------|----------------------------------|--------|
| Parsing feed (tick/L2)  | 50–200 µs per msg (Python JSON)    | 5–20 µs per msg (zero-copy/flatbuffers) | Tránh JSON, dùng binary/flatbuffers. |
| Strategy eval           | 50–500 µs (NumPy/Py)               | 5–50 µs (SIMD)                   | Vectorize; hạn chế GIL. |
| Risk checks             | 20–200 µs (Py)                     | 5–30 µs                          | Precompute caps; avoid Python locks. |
| Order send              | 200–800 µs (REST/WS)               | 20–150 µs (FIX/ITCH native)      | Ưu tiên FIX binary, co-location. |
| GC / jitter             | Có (GC/alloc)                      | Ít hơn (arena alloc)             | Python GC gây tail latency. |
| End-to-end (typical)    | 0.5–3 ms                           | 50–400 µs                        | Phụ thuộc venue/network. |

## Khuyến nghị giảm trễ cho Python
- Dọn JSON → binary (flatbuffers/msgpack), giảm parse. 
- Giảm alloc: pre-allocate arrays, tránh tạo object trong vòng lặp. 
- Tách tiến trình cho feed/strategy (multiprocessing) để tránh GIL; hoặc numba/cython cho hotspot. 
- Batch hoặc throttle tín hiệu để tránh spam lệnh. 
- Sử dụng async IO nhưng giới hạn await trong hotspot; benchmark thật. 

## Khi nào cần C++/Rust
- Chiến lược nhạy microstructure, cạnh tranh hàng trăm µs. 
- Cần queue position ưu tiên (market making/HFT nhẹ). 
- Yêu cầu thông lượng cao (hàng trăm nghìn msg/s) với jitter thấp. 

## Guardrails chung
- Đo latency end-to-end; log p50/p90/p99. 
- Circuit breaker khi latency spike; fallback sang chế độ an toàn. 
- Đặt rate-limit và queue size; tránh backlog làm trễ thêm. 