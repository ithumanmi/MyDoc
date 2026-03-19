---
title: "Microstructure Feature Cookbook"
---

# Microstructure Feature Cookbook

> [← Back to Quantitative Trading Hub](./README.md)

Tập hợp các feature microstructure thường dùng cho alpha, execution, market making.

## 1) Order Book Imbalance (OBI)
\( OBI = \frac{V_{bid} - V_{ask}}{V_{bid} + V_{ask}} \) tại top-k levels.  
- Variants: volume-weighted OBI, depth ratio (bid/ask), rolling mean/vol của OBI.  

## 2) Queue Position & Fill Probability (LOB)
- Ước lượng xác suất khớp lệnh limit: \(p_{fill} \approx f(queue\_ahead, cancel\ rate, trade\ intensity)\).  
- Feature: queue_ahead_notional, cancel_rate, trade_intensity (prints/s), imbalance tại price level.  

## 3) Spread & Volatility Regimes
- Spread state: tight/normal/wide (quantile).  
- Micro-price: \( P_{micro} = \frac{P_{ask} V_{bid} + P_{bid} V_{ask}}{V_{bid} + V_{ask}} \).  
- Feature: spread_zscore, microprice - mid, jump indicator khi spread mở rộng nhanh.  
## 4) Trade Signs & Order Flow
- Lee-Ready hoặc tick rule: sign của trade.  
- Order flow imbalance (OFI): \(OFI_t = \Delta V_{bid} - \Delta V_{ask}\) (price & size changes).  
- Cumulative OFI, rolling OFI, VPIN (volume-synchronized probability of informed trading).  

### Code ví dụ OFI
```python
import pandas as pd

# ticks: ['time','side','size','price'] với side in {+1 buy, -1 sell}
ticks['ofi'] = ticks['side'] * ticks['size']
ofi_bar = ticks.resample('1min', on='time')['ofi'].sum().fillna(0)
```

### Code ví dụ VPIN (giản lược)
```python
import numpy as np
import pandas as pd

# ticks: ['time','price','size']; giả định sign ~ price change
ticks = ticks.copy()
ticks['buy'] = (ticks['price'].diff() > 0).astype(int)
ticks['sell'] = 1 - ticks['buy']

V = ticks['size'].sum()
bucket_size = V / 50  # 50 volume buckets

ticks['cum_vol'] = ticks['size'].cumsum()
ticks['bucket'] = (ticks['cum_vol'] / bucket_size).astype(int)

bucket = ticks.groupby('bucket').agg(
    vol=('size','sum'),
    buy_vol=('size', lambda s: (s * ticks.loc[s.index, 'buy']).sum()),
)
bucket['sell_vol'] = bucket['vol'] - bucket['buy_vol']
bucket['imbalance'] = (bucket['buy_vol'] - bucket['sell_vol']).abs()
bucket['vpin'] = bucket['imbalance'] / bucket_size
vpin_series = bucket['vpin'].rolling(10).mean()  # smooth
```

## 5) Volatility & Impact Proxies
- Realized vol (bar/rolling), high-low Parkinson.  
- Kyle lambda proxy: \( \lambda = \frac{cov(\Delta p, q)}{var(q)} \).  
- Hasbrouck impact: regression \( \Delta p = \beta q + \epsilon \).  

## 6) Liquidity & Resiliency
- Depth_k: tổng khối lượng top-k levels; ratio depth_bid/depth_ask.  
- Resiliency: thời gian/spread cần để trở lại mức trung bình sau shock; slope của depth sau trade lớn.  

## 7) Short-Term Reversal / Momentum (Micro)
- Mid return over small windows (1s, 5s) + sign streak.  
- Trigger khi spread rộng và OFI đảo chiều.  

## 8) Toxicity / Informed Trading
- VPIN buckets, probability of informed trading (PIN).  
- Abnormal order size relative to median.  
- Hidden/iceberg detection: nhiều print nhỏ ở cùng giá, depth thay đổi bất thường.  

## 9) Latency & Venue Signals
- Venue-to-venue spread, best-venue slippage.  
- Quote age / staleness; last update time.  
- Cross-venue imbalance; routing signal cho smart order router.  

## 10) Feature hygiene
- Align timestamp và dedup message.  
- Cap/clip outlier; winsorize.  
- Standardize per symbol/regime; tránh leak tương lai.  
- Point-in-time: không dùng thông tin sau thời điểm bar.  