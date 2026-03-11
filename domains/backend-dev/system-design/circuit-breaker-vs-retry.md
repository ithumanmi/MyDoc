---
title: "Circuit Breaker vs Simple Retry"
description: "Vì sao hệ thống lớn cần circuit breaker thay vì chỉ retry API lỗi."
tags:
  - backend
  - system-design
  - reliability
updated: 2026-03-11
---

# 🛑 Circuit Breaker vs Simple Retry

> Retry rất dễ code, nhưng khi phụ thuộc bị lỗi kéo dài, retry không kiểm soát sẽ biến hệ thống thành "tấn công DDoS tự gây ra". Circuit breaker (cầu dao) giúp cô lập lỗi, bảo vệ tài nguyên và cung cấp đường fallback.

## 1. Khi nào retry là đủ?
- Sự cố tạm thời (transient) như network hiccup, timeout ngắn.
- Backend vẫn khỏe, chỉ cần retry 1–2 lần với backoff.
- Lưu ý: retry luôn phải có **limit + backoff** để tránh bùng nổ.

## 2. Vấn đề khi chỉ dùng retry
1. **Amplification**: 1 request lỗi → retry 3 lần → tải nhân 3. Khi hàng nghìn request cùng retry, backend quá tải nhanh hơn.
2. **Thundering Herd**: khi service upstream vừa hồi phục, mọi client retry cùng lúc → traffic spike làm nó sập tiếp.
3. **Queue build-up**: connection/thread giữ chờ đợi, pool cạn → hệ thống không phục vụ được request mới.
4. **Không bảo vệ user experience**: user chờ rất lâu rồi mới thấy lỗi, trong khi hệ thống có thể fallback nhanh.

## 3. Circuit Breaker làm gì?
- **Monitor** tỉ lệ lỗi hoặc latency.
- Khi vượt ngưỡng → chuyển sang trạng thái **Open** (ngắt) → ngừng gọi tới dependency, trả lỗi nhanh/fallback.
- Sau thời gian cool-down → trạng thái **Half-open**: thử một vài request thăm dò. Nếu thành công → Close (đóng), nếu thất bại → Open lại.

```
Closed (bình thường) → Half-open (thử nghiệm) → Open (chặn call)
```

## 4. Lợi ích so với chỉ retry
- **Bảo vệ tài nguyên**: dừng bơm request vô nghĩa vào service đã chết, giữ thread/connection cho tác vụ khác.
- **Giảm cascading failure**: nếu service Payment chết, mọi service khác ngắt call thay vì cùng treo → ngăn domino.
- **Fallback nhanh**: có thể trả thông điệp “Dịch vụ tạm gián đoạn” hoặc dùng cached data thay vì để user chờ timeout.
- **Observability**: circuit breaker phát tín hiệu cảnh báo rõ ràng khi dependency vấn đề.

## 5. Pattern triển khai
- Library: Resilience4j, Hystrix (legacy), Envoy circuit breaker, Istio outlier detection.
- Metric: error rate %, consecutive failures, latency percentile.
- Policy: cho phép 1–5 request thử trong Half-open.
- Kết hợp với retry có kiểm soát (exponential backoff, jitter).

## 6. Ví dụ timeline
1. API Payment bắt đầu timeout.
2. Service Order retry 3 lần → mỗi request = 4 call Payment → CPU tăng.
3. Circuit breaker mở sau khi error rate >50% trong 30s.
4. Order dừng call Payment, trả lỗi nhanh “Thanh toán tạm gián đoạn”.
5. Payment team fix xong, breaker half-open thử 1 vài call.
6. Thành công, breaker close lại → hệ thống hồi phục mượt.

## 7. Checklist áp dụng
- [ ] Thiết lập circuit breaker cho mọi dependency quan trọng.
- [ ] Đặt ngưỡng error rate/thời gian phù hợp, tránh open quá nhạy.
- [ ] Kết hợp retry có giới hạn, backoff + jitter.
- [ ] Định nghĩa fallback rõ ràng (cache, queue, degrade message).
- [ ] Monitor trạng thái breaker để hỗ trợ on-call.

## 8. Liên kết
- [System Design Glossary](./system-design-glossary.md)
- [Realtime Flash Sale Inventory](./realtime-flash-sale-inventory.md)
- Netflix Hystrix design doc (legacy nhưng nhiều insight).