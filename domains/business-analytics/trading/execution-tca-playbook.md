---
title: "Execution & TCA Playbook: Impact, Slippage, Smart Routing"
---

# Execution & TCA Playbook: Impact, Slippage, Smart Routing

> [← Back to Quantitative Trading Hub](./README.md)

Playbook nâng cao cho khớp lệnh và đo lường chi phí giao dịch (TCA). Bổ sung mô hình impact (Almgren-Chriss), lựa chọn venues, child-order sizing, queue/latency, và checklist TCA.

## 1. Mô hình Impact cơ bản (Almgren-Chriss giản lược)
- **Temporary impact**: \( I_{temp} = k \, \sigma \, \sqrt{\frac{Q}{V}} \), với \(Q\) khối lượng giao dịch, \(V\) khối lượng thị trường, \(\sigma\) vol.
- **Permanent impact**: \( I_{perm} = g \cdot \frac{Q}{V} \).
- **Execution price** (mua): \( P_{exec} = P_{mid} + 0.5 \cdot spread + I_{temp} + I_{perm} \).

## 2. Chiến lược lệnh
- **TWAP**: đơn giản, dễ bị front-run khi pattern đều đặn.
- **VWAP**: bám theo profile khối lượng trong ngày; ẩn lệnh tốt hơn TWAP.
- **POV / Participation**: giữ tỉ lệ % volume thị trường; giảm impact khi thanh khoản giảm.
- **IS/Shortfall**: cân bằng giữa market risk (đợi lâu) và slippage (đi nhanh), tối ưu thời gian/khối lượng động.
- **Limit vs Market mix**: dùng limit để giảm phí và trượt, nhưng có nguy cơ không khớp; market khi cần tốc độ/thoát khẩn cấp.

## 3. Venue Selection & Smart Routing (SOR)
- Chọn venue theo **spread, depth, fee/rebate, fill ratio, latency**.
- **Queue position**: hạn chế nhảy hàng tốn phí; đặt limit cạnh cạnh top-of-book khi spread hẹp.
- **Cross-venue arbitrage**: cẩn trọng với thông tin rò rỉ; tránh “toxic flow”.

## 4. Slippage & Latency
- Slippage gồm: spread/impact/fee/adverse selection. 
- Latency: đo end-to-end (client → gateway → venue). Co-location hoặc route nhanh hơn cho chiến lược nhạy latency.

## 5. TCA Checklist
- **Pre-trade**: ước lượng impact (k, g, vol, ADV), chọn chiến lược (TWAP/VWAP/POV/IS), đặt limit/market mix, cap %ADV, fee model.
- **In-trade**: giám sát fill ratio, slippage vs. bench (mid/VWAP), spread regime, queue position, delay/latency.
- **Post-trade**: tính Implementation Shortfall, VWAP slippage, arrival price slippage, fees & rebates, adverse selection (markout 1s/5s/60s), re-opt tham số.

## 6. Pseudo-code mô phỏng IS vs VWAP
```python
def simulate_execution(path_prices, adv, strategy="VWAP", part=0.1, k=0.3, g=0.1, fee_bps=1):
    fills = []
    remaining = target_qty
    for t, (mid, spread, vol) in enumerate(path_prices):
        if remaining <= 0:
            break
        if strategy == "VWAP":
            slice_qty = part * vol  # theo profile volume
        elif strategy == "POV":
            slice_qty = part * vol
        elif strategy == "TWAP":
            slice_qty = target_qty / T
        else:  # IS: điều chỉnh động theo vol/spread
            slice_qty = min(part * vol * (spread_mean/spread if spread > 0 else 1), remaining)

        slice_qty = min(slice_qty, remaining)
        temp_impact = k * np.sqrt(slice_qty / adv)
        perm_impact = g * (slice_qty / adv)
        exec_px = mid + 0.5 * spread + temp_impact + perm_impact
        fee = fee_bps * 1e-4 * slice_qty * exec_px
        fills.append((exec_px, slice_qty, fee))
        remaining -= slice_qty
    return fills
```

## 7. Metrics nên báo cáo
- Implementation Shortfall, VWAP slippage, arrival slippage.
- Fill rate, cancel/replace ratio, queue time.
- Spread regime vs. slippage, cost per notional, adverse selection (markout).

## 8. Guardrails
- Cap %ADV, cap slippage/IS tối đa, time-in-force, limit price bands.
- Circuit breaker nếu slippage vượt ngưỡng hoặc spread nới rộng bất thường.