---
title: "Options: Greeks & Hedging Playbook"
---

# Options: Greeks & Hedging Playbook

> [← Back to Quantitative Trading Hub](./README.md)

Tóm tắt thực chiến về Greeks, chiến lược hedging (delta/gamma/vega), và lưu ý IV vs RV.

## 1. Greeks tốc hành
- **Delta (Δ)**: nhạy cảm giá cơ sở. Delta-long tăng khi giá tăng. 
- **Gamma (Γ)**: nhạy cảm của Delta. Gamma cao → delta biến động nhanh. 
- **Vega (V)**: nhạy cảm biến động hàm ý (IV). Vega-long hưởng lợi khi IV tăng. 
- **Theta (Θ)**: hao mòn thời gian; short option thu Theta, long option trả Theta. 
- **Rho (ρ)**: nhạy cảm lãi suất.

## 2. IV vs RV
- **IV (Implied Vol)**: kỳ vọng biến động từ giá option. 
- **RV (Realized Vol)**: biến động thực tế quan sát.  
- Nếu IV >> RV: cơ hội short vol (nhưng rủi ro tail); nếu IV << RV: cân nhắc long vol.

## 3. Delta Hedge Loop (pseudo-code)
```python
target_delta = 0
rebalance_threshold = 0.05  # ví dụ, hedge khi |delta_port| > 0.05

while market_open:
    delta_port = option_delta * option_position + stock_delta * stock_position
    if abs(delta_port - target_delta) > rebalance_threshold:
        hedge_qty = -(delta_port - target_delta)
        trade_stock(hedge_qty)
```

## 4. Gamma Scalping (gamma-long)
- Mua option (long gamma, short theta), delta-hedge thường xuyên. 
- Khi giá dao động, tái cân bằng delta thu lợi từ biến động; trả phí theta mỗi ngày. 
- Hiệu quả khi realized vol > implied vol đã trả.

## 5. Vega Hedge
- Nếu short vol lớn: mua một phần long vega (long option/variance swap) để giảm tail từ cú nổ vol.
- Quản lý **vol surface**: chú ý skew (risk reversal), term structure; tránh lệch kỳ hạn quá lớn.

## 6. Charm/Vanna (đang chi tiết ngắn)
- **Charm**: delta decay theo thời gian (đặc biệt với near-dated options). 
- **Vanna**: delta nhạy với thay đổi IV, nhất là options OTM; quan trọng với hedging trong thị trường biến động mạnh.

## 7. P&L Attribution đơn giản
- **Delta P&L**: \( \Delta \cdot dS \)
- **Gamma P&L**: \( 0.5 \cdot \Gamma \cdot dS^2 \)
- **Vega P&L**: \( Vega \cdot dIV \)
- **Theta P&L**: hao mòn theo thời gian

## 8. Checklist Hedging
- [ ] Xác định mục tiêu delta (neutral hay partial).  
- [ ] Ngưỡng tái cân bằng (gamma/vol cao → hedge thường xuyên hơn).  
- [ ] Quản lý vega: tránh short vol trần trụi; có hedge phần tail.  
- [ ] Theo dõi vol surface (skew/term).  
- [ ] Tính chi phí hedge: phí giao dịch + hao mòn theta.  
- [ ] Stress test: cú nhảy giá và spike IV.