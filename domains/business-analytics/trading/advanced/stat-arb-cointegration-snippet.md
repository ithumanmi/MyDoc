---
title: "Stat-Arb: Cointegration & Hedge Ratio Snippet"
---

# Stat-Arb: Cointegration & Hedge Ratio Snippet

> [← Back to Quantitative Trading Hub](./README.md)

Code mẫu kiểm tra cointegration cho cặp/pair và ước lượng hedge ratio, sau đó tạo spread & z-score.

```python
import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.stattools import coint

# prices: DataFrame với cột 'A','B' (giá đóng cửa hoặc mid)

# 1) Hedge ratio bằng OLS (A ~ beta*B)
Y = prices['A']
X = sm.add_constant(prices['B'])
model = sm.OLS(Y, X).fit()
beta = model.params['B']

# 2) Kiểm tra cointegration (Engle-Granger)
t_stat, pvalue, _ = coint(prices['A'], prices['B'])
print(f"p-value cointegration: {pvalue:.4f}")

# 3) Spread & z-score
spread = prices['A'] - beta * prices['B']
z = (spread - spread.mean()) / spread.std()

# 4) Half-life ước lượng (Ornstein-Uhlenbeck)
spread_lag = spread.shift(1)
delta = spread - spread_lag
df = pd.concat([spread_lag, delta], axis=1).dropna()
df.columns = ['spread_lag','delta']
res = sm.OLS(df['delta'], sm.add_constant(df['spread_lag'])).fit()
halflife = -np.log(2) / res.params['spread_lag']
print(f"Half-life (bars): {halflife:.2f}")

# 5) Tín hiệu đơn giản
entry_z = 2
exit_z = 0
signals = pd.Series(0, index=prices.index)
signals[z > entry_z] = -1  # short spread (short A, long B)
signals[z < -entry_z] = 1  # long spread (long A, short B)
signals[(z > -exit_z) & (z < exit_z)] = 0
```

Checklist nhanh:
- [ ] p-value cointegration < 0.05 và ổn định theo rolling window.  
- [ ] Hedge ratio cập nhật định kỳ; kiểm tra stability (rolling beta).  
- [ ] Z-score/half-life dùng cho sizing và exit; thêm cap %ADV và borrow.  
- [ ] Backtest kèm TCost, borrow fee; stress test theo regime vol/spread.  