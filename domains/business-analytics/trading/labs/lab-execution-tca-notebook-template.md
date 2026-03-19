---
title: "Template Notebook: Execution & TCA Simulation"
---

# Template Notebook: Execution & TCA Simulation

> [← Back to Quant Labs](../README.md)

Gợi ý khung notebook (Jupyter) để mô phỏng TWAP/VWAP/POV/IS, impact/fee, TCA.

## 1) Chuẩn bị dữ liệu giả lập
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

T = 120  # 120 phút
np.random.seed(0)
mid = 100 + np.cumsum(np.random.randn(T) * 0.02)
spread = np.clip(np.random.randn(T) * 0.01 + 0.02, 0.005, 0.05)
vol = np.random.lognormal(mean=7, sigma=0.5, size=T)  # volume profile giả

path = pd.DataFrame({
    'mid': mid,
    'spread': spread,
    'vol': vol,
})

target_qty = 1_000_000  # khối lượng cần giao dịch
adv = 50_000_000

# Plot path giả lập
fig, ax1 = plt.subplots(figsize=(8,4))
ax1.plot(mid, label="mid")
ax1.set_ylabel("Price")
ax2 = ax1.twinx()
ax2.bar(range(T), vol, alpha=0.2, color="orange", label="vol")
ax2.set_ylabel("Vol")
ax1.legend(loc="upper left")
ax2.legend(loc="upper right")
plt.title("Synthetic mid & volume path")
plt.show()
```

## 2) Hàm mô phỏng khớp lệnh
```python
def execute(path, target_qty, strategy, adv, part=0.1, k=0.3, g=0.1, fee_bps=1):
    remaining = target_qty
    fills = []
    spread_mean = path['spread'].mean()
    for t, row in path.iterrows():
        if remaining <= 0:
            break
        mid, spread, vol = row.mid, row.spread, row.vol
        if strategy == "TWAP":
            slice_qty = target_qty / len(path)
        elif strategy in ("VWAP", "POV"):
            slice_qty = part * vol
        else:  # IS: adaptive theo spread/vol
            slice_qty = min(part * vol * (spread_mean/spread if spread>0 else 1), remaining)

        slice_qty = min(slice_qty, remaining)
        temp_impact = k * np.sqrt(slice_qty / adv)
        perm_impact = g * (slice_qty / adv)
        exec_px = mid + 0.5*spread + temp_impact + perm_impact
        fee = fee_bps * 1e-4 * slice_qty * exec_px
        fills.append((t, exec_px, slice_qty, fee, spread))
        remaining -= slice_qty
    return pd.DataFrame(fills, columns=['t','px','qty','fee','spread'])
```

## 3) Tính TCA: IS, VWAP, arrival
```python
def tca_metrics(path, fills):
    arrival = path['mid'].iloc[0]
    vwap_bench = (path['mid'] * path['vol']).sum() / path['vol'].sum()
    notional = fills['qty'].sum()
    avg_px = (fills['px'] * fills['qty']).sum() / notional
    fees = fills['fee'].sum()

    is_bps = (avg_px - arrival) / arrival * 1e4
    vwap_slip_bps = (avg_px - vwap_bench) / vwap_bench * 1e4
    return {
        'avg_px': avg_px,
        'arrival': arrival,
        'vwap_bench': vwap_bench,
        'IS_bps': is_bps,
        'VWAP_slip_bps': vwap_slip_bps,
        'fees': fees,
    }
```

## 4) Chạy so sánh nhanh
```python
strategies = ["TWAP", "VWAP", "POV", "IS"]
results = []
for s in strategies:
    fills = execute(path, target_qty, s, adv)
    metrics = tca_metrics(path, fills)
    metrics['strategy'] = s
    results.append(metrics)

pd.DataFrame(results)
```

## 5) Checklist notebook
- [ ] Sinh path giá/khối lượng và tham số ADV.  
- [ ] Thực hiện 4 chiến lược TWAP/VWAP/POV/IS.  
- [ ] Tính IS, VWAP slippage, arrival, fees.  
- [ ] Vẽ biểu đồ path và các fills theo thời gian.  
- [ ] So sánh bảng kết quả giữa chiến lược.  
- [ ] Thử thay đổi spread regime/vol profile/fee để thấy khác biệt.  