---
title: "Lab: Execution Simulator & TCA"
---

# Lab: Execution Simulator & TCA

> [← Back to Quant Labs](../README.md)

Mục tiêu: mô phỏng chiến lược khớp lệnh (TWAP/VWAP/POV/IS), đo slippage/impact/fee, triển khai TCA (pre/in/post-trade) và guardrails.

## Thành phần mô phỏng
- **Price/volume path**: chuỗi (mid, spread, vol) theo thời gian bar/minute. 
- **Execution strategy**: TWAP/VWAP/POV/IS; mix limit/market. 
- **Impact model**: tạm dùng \( k \sqrt{Q/ADV} \) + \( g Q/ADV \). 
- **Fee model**: maker/taker bps; rebate nếu có. 
- **Constraints**: cap %ADV, price bands, TIF.

## Pseudo-code
```python
def execute(path, target_qty, strategy, adv, k=0.3, g=0.1, fee_bps=1):
    remaining = target_qty
    fills = []
    for t, (mid, spread, vol) in enumerate(path):
        if remaining <= 0:
            break
        # allocation
        if strategy == "TWAP":
            slice_qty = target_qty / len(path)
        elif strategy == "VWAP" or strategy == "POV":
            slice_qty = 0.1 * vol
        else:  # IS: adaptive theo spread/vol
            slice_qty = min(0.1 * vol * (spread_mean/spread if spread>0 else 1), remaining)

        slice_qty = min(slice_qty, remaining)
        temp_impact = k * np.sqrt(slice_qty / adv)
        perm_impact = g * (slice_qty / adv)
        exec_px = mid + 0.5*spread + temp_impact + perm_impact
        fee = fee_bps * 1e-4 * slice_qty * exec_px
        fills.append((t, exec_px, slice_qty, fee))
        remaining -= slice_qty
    return fills
```

## TCA các bước
- **Pre-trade**: estimate impact (k,g, vol, ADV), chọn chiến lược, cap %ADV, đặt limit/market mix. 
- **In-trade**: log fills, slippage vs mid/VWAP; theo dõi spread regime, queue/latency nếu có LOB. 
- **Post-trade**: Implementation Shortfall, VWAP slippage, arrival slippage, fees/rebates, markout 1s/5s/60s.

## Checklist hoàn thành
- [ ] Mô phỏng path (mid/spread/vol) và tham số ADV.  
- [ ] Implement các chiến lược TWAP/VWAP/POV/IS.  
- [ ] Impact + fee model trong fill price.  
- [ ] Tính TCA: IS, VWAP slippage, arrival, fees, markout.  
- [ ] Guardrails: cap %ADV, spread/widen guard, timeouts.  
- [ ] So sánh kết quả giữa chiến lược; báo cáo bảng/biểu đồ.