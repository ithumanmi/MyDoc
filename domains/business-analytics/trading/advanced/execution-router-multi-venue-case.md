---
title: "Mini-Case: Multi-Venue Execution Router"
---

# Mini-Case: Multi-Venue Execution Router

> [← Back to Quantitative Trading Hub](./README.md)

Kịch bản: cổ phiếu/crypto niêm yết đa venue. Mục tiêu: giảm slippage, tránh toxic flow, kiểm soát latency.

## Kiến trúc tóm tắt
- Market data aggregator: hợp nhất NBBO/L1/L2, chuẩn hóa timestamp, venue tag.  
- Signal & slicer: nhận target parent order, chia child theo chiến lược (VWAP/POV/IS adaptive).  
- Router: chọn venue theo score.  
- Risk/guardrails: caps, kill-switch, drift monitor.  

## Heuristic chấm điểm venue
- Price edge: best bid/ask, queue depth, spread.  
- Liquidity: depth_k, fill ratio lịch sử, cancel rate.  
- Toxicity: VPIN/OFI tại venue, reject rate, markout 1s/5s.  
- Latency: p99 venue + hop network; staleness.  
- Fee/rebate: taker/maker fees, rebates.  

Pseudo:
```python
score = w_price * price_edge - w_toxic * toxicity + w_liq * depth_score - w_lat * latency_penalty + w_fee * fee_rebate
route_to = argmax(score)
```

## Chiến lược phân bổ child order
- **Best-price first, cap per venue**: gửi phần nhỏ vào best, phần còn lại theo depth ratio.  
- **VWAP/POV cross-venue**: target participation tổng, chia theo trọng số (depth * fill_prob / latency).  
- **Adaptive**: nếu markout xấu ở venue A, giảm weight A tăng B.  

## Đo lường & feedback
- Pre-trade: expected slippage theo impact model từng venue.  
- Post-trade: IS/VWAP per venue, fill ratio, reject ratio, markout 1s/5s.  
- Drift: chênh NBBO vs venue mid; alert nếu staleness > threshold.  

## Checklist triển khai
- [ ] Hợp nhất sổ lệnh đa venue, đồng bộ timestamp, xử lý staleness.  
- [ ] Tính score venue: price edge, depth, toxicity (VPIN/OFI), latency, fee.  
- [ ] Router chọn venue + cap notional/ADV; failover nếu reject cao.  
- [ ] Post-trade TCA per venue; markout ngắn hạn để giảm weight venue xấu.  
- [ ] Guardrails: quote staleness, reject spike, latency spike, drift NBBO vs venue.  