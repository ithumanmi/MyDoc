# 🔌 Broker API Guide (IB vs Alpaca)

| Tiêu chí | Interactive Brokers (IBKR) | Alpaca |
| --- | --- | --- |
| Asset coverage | Equities, options, futures, FX, bonds | US equities/ETFs; crypto (tùy gói) |
| Market access | Global (US, EU, Asia) | Chủ yếu US |
| Order types | Rất phong phú (algo, iceberg, VWAP/TWAP) | Cơ bản (limit/market/stop), bracket/OCO |
| API | TWS/IB Gateway, gRPC, Web API (beta) | REST/WebSocket, đơn giản |
| Paper trading | Có (paper account) | Có |
| Fees | Commission low nhưng có; FX conversion | Zero commission (spread), SEC/FINRA fees áp dụng |
| Data | Real-time tùy gói market data; snapshot/trades | Free polygon-style basic (tùy plan), limited depth |

## Khuyến nghị theo use-case
- **Đa tài sản, cần order đa dạng, routing tốt:** IBKR.
- **US equities, MVP/rapid prototyping:** Alpaca (đơn giản API, paper dễ dùng).
- **Chi phí thấp, paper + live đồng nhất:** Cả hai có paper; IBKR cần set API host qua TWS/Gateway.

## Lưu ý vận hành
- Kiểm tra session/connection limit, keep-alive.
- Kiểm thử latency & slippage theo venue (IBKR: SMART vs direct routing).
- Map trạng thái order (submitted/filled/partial/cancelled) rõ ràng.
- Quản lý timezone, retry/backoff khi mất kết nối.
- Đảm bảo quy trình compliance: PDT (pattern day trading) với tài khoản nhỏ US.

---
> Tiếp: xem các notebook trong `labs/` để hands-on.