---
title: "Kỹ Sư Risk & Portfolio: Sizing – Drawdown – Hedging"
---

# Kỹ Sư Risk & Portfolio: Giữ Vốn, Ép Rủi Ro, Mài Lợi Nhuận

> [← Back to Quantitative Trading Hub](./README.md)

Nếu không kiểm soát risk, mọi alpha sẽ bốc hơi. Tài liệu này là playbook thực chiến: từ position sizing, drawdown cap, vol targeting, risk parity, cho đến hedging và budget chi phí giao dịch.

## 1. Position Sizing Thực Chiến
- **Kelly / Half-Kelly / Fractional**: dùng Kelly để tối ưu tăng trưởng, nhưng thực thi Half-Kelly hoặc Fractional-Kelly để giảm drawdown.  
  \( f^* = p - \frac{q}{b} \) với \(p\) xác suất thắng, \(q=1-p\), \(b\) tỉ lệ lãi/lỗ.
- **Sizing theo alpha & risk**: \(\text{size} = k \cdot \frac{\text{signal}}{\sigma}\) (k điều chỉnh bằng risk budget, \(\sigma\) là vol ước lượng).
- **Cap theo liquidity/ADV**: giới hạn %ADV và notional tối đa để tránh impact.

Pseudo-code Half-Kelly:
```python
edge = winrate * payoff - (1 - winrate)
b = payoff
f_kelly = edge / b
f_alloc = 0.5 * max(f_kelly, 0)   # Half-Kelly, không âm
position_notional = f_alloc * portfolio_equity
```

## 2. Drawdown Control & Vol Targeting
- **Max DD cap**: dừng chiến lược hoặc giảm quy mô khi DD chạm ngưỡng (ví dụ 10-15%).
- **Vol targeting**: giữ danh mục ở mức vol mục tiêu (ví dụ 10%/năm).  
  \( w_{t} = w_{t-1} \cdot \frac{\text{target\_vol}}{\text{realized\_vol}} \)
- **Stop logic thông minh**: ưu tiên stop theo regime/vol spike hơn là hard-stop giá đơn giản.

## 3. Risk Parity & Exposure Caps
- **Risk parity**: phân bổ tỉ trọng sao cho mỗi tài sản đóng góp risk tương đương: \( w_i \propto 1/\sigma_i \).
- **Correlation clustering**: gộp tài sản tương quan cao, giới hạn tổng risk theo cụm để tránh “double bet”.
- **Exposure caps**: trần gross, net, beta-adjusted exposure; trần sector/asset-class.

## 4. Turnover & Transaction Cost Budget
- Tính **turnover** hàng ngày/tuần, đặt **TCost budget** (bps) và kiểm tra slippage/fee vs. lợi nhuận kỳ vọng.
- Thêm **hysteresis** hoặc **buffer bands** để giảm churn lệnh.

## 5. Hedging Playbook
- **Delta hedge**: tái cân bằng khi |delta| vượt ngưỡng; tránh over-hedge gây phí.
- **Vega/vol hedge**: dùng options hoặc variance swap khi chiến lược nhạy với biến động.
- **Tail hedge nhẹ**: mua bảo hiểm rẻ (OTM put) cho các sự kiện tail; giới hạn premium.

## 6. Kiểm Soát Rủi Ro Vận Hành (Ops Risk)
- Guardrails: notional tối đa/chiến lược, max orders/giây, circuit breaker khi PnL intraday < -X%.
- Giám sát: heartbeat data feed, trễ kết nối, chênh lệch mark-to-market giữa venues.

## 7. Checklist Risk Layer
- [ ] Có sizing engine (Kelly/Half/Fractional) và cap %ADV.  
- [ ] Vol targeting hoạt động, dùng realized vol cập nhật.  
- [ ] DD cap + chế độ giảm quy mô hoặc tắt chiến lược.  
- [ ] Exposure caps: gross/net/beta, sector/cluster.  
- [ ] Turnover/TCost budget và buffer giảm churn.  
- [ ] Hedging rule: delta/vega; tail hedge nhẹ.  
- [ ] Guardrails & circuit breakers; monitor feed/trễ.  
- [ ] Log & alert đầy đủ để postmortem.

## 8. Live Ops Checklist (Kill-Switch & Monitoring)
- [ ] **Kill-switch**: nút tắt nhanh theo chiến lược + toàn danh mục.  
- [ ] **Heartbeat**: mất dữ liệu/nguồn giá → đóng trạng thái về neutral.  
- [ ] **PnL & DD monitors**: ngưỡng intraday & daily; tự giảm quy mô hoặc dừng.  
- [ ] **Latency/Queue monitors**: cảnh báo spike trễ, drop packet, chênh mark-to-market giữa venues.  
- [ ] **Order rejects**: theo dõi tỷ lệ reject/cancel/replace; fallback hạn chế spam lệnh.  
- [ ] **Capital & margin**: kiểm tra margin headroom; không mở lệnh nếu dưới ngưỡng.  
- [ ] **Audit logs**: ghi lại signal→order→fill, lý do bỏ lệnh, tham số sizing/hedge.  
- [ ] **Config/params versioned**: thay đổi tham số phải log/roll-back được.  
- [ ] **Change window**: không deploy tham số mới ngay trước phiên biến động (FOMC, CPI).  
- [ ] **Chaos/stress drills**: diễn tập mất dữ liệu, mất venue, spike vol, oracle lỗi.