---
title: "Lab: Event-Driven Backtester (Python)"
---

# Lab: Event-Driven Backtester (Python)

> [← Back to Quant Labs](../README.md)

Mục tiêu: xây dựng backtester event-driven (giống kiến trúc live) gồm hàng đợi sự kiện, mô-đun data, signal, portfolio, execution và risk. Tránh look-ahead bias, mô phỏng latency, slippage, fee.

## Kiến trúc thành phần
- **Event Queue**: FIFO chứa `MarketEvent`, `SignalEvent`, `OrderEvent`, `FillEvent`.
- **Data Handler**: phát `MarketEvent` (bar/tick), đảm bảo point-in-time, không leak tương lai.
- **Strategy**: nhận `MarketEvent`, phát `SignalEvent` (long/short/size/confidence/time-in-force).
- **Risk/Portfolio**: kiểm tra margin, exposure caps, tạo `OrderEvent`, áp dụng sizing (Kelly/vol-target) và cap %ADV.
- **Execution Handler**: biến `OrderEvent` → `FillEvent` (khớp giá/khối lượng), mô phỏng slippage/impact/latency/fee.
- **Performance**: tính PnL, positions, drawdown, Sharpe/Sortino, turnover, TCost.

## Mô hình sự kiện (dataclass gợi ý)
```python
@dataclass
class MarketEvent:
    symbol: str
    price: float
    size: float
    timestamp: pd.Timestamp

@dataclass
class SignalEvent:
    symbol: str
    direction: str   # 'LONG' / 'SHORT' / 'FLAT'
    strength: float  # 0..1
    timestamp: pd.Timestamp

@dataclass
class OrderEvent:
    symbol: str
    direction: str   # 'BUY' / 'SELL'
    quantity: float
    price: float | None  # limit hoặc None (market)
    tif: str | None      # time-in-force
    timestamp: pd.Timestamp

@dataclass
class FillEvent:
    symbol: str
    direction: str
    filled: float
    price: float
    fee: float
    slippage: float
    timestamp: pd.Timestamp
```

## Vòng lặp chính (pseudo-code)
```python
while data.has_next():
    market_event = data.next()          # MarketEvent
    queue.put(market_event)

    while not queue.empty():
        event = queue.get()

        if isinstance(event, MarketEvent):
            signal = strategy.on_bar(event)
            if signal:
                queue.put(signal)

        elif isinstance(event, SignalEvent):
            order = risk_portfolio.generate_order(event)
            if order:
                queue.put(order)

        elif isinstance(event, OrderEvent):
            fill = execution.fill(order=event)
            if fill:
                queue.put(fill)

        elif isinstance(event, FillEvent):
            risk_portfolio.update_from_fill(fill)
            performance.update(fill, market_event)
```

## Mô phỏng slippage / impact (đơn giản)
```python
def simulate_fill(order, best_bid, best_ask, spread, impact_bps, fee_bps):
    mid = 0.5 * (best_bid + best_ask)
    direction = 1 if order.direction == 'BUY' else -1
    impact = impact_bps * 1e-4 * order.quantity
    px = mid + direction * (0.5 * spread + impact)
    fee = fee_bps * 1e-4 * order.quantity * px
    slippage = direction * (px - mid)
    return FillEvent(
        symbol=order.symbol,
        direction=order.direction,
        filled=order.quantity,
        price=px,
        fee=fee,
        slippage=slippage,
        timestamp=order.timestamp,
    )
```

## Kiểm soát bias & latency
- **Point-in-time**: không dùng dữ liệu tương lai; shift tín hiệu khi cần.
- **Embargo/walk-forward**: tách tập huấn luyện/kiểm thử; áp dụng trong evaluation lặp.
- **Latency**: thêm trễ vào pipeline (data → signal → order → fill) để sát live.

## Chỉ số đánh giá
- PnL, Sharpe/Sortino, max drawdown, Calmar.
- Turnover, TCost (spread + impact + fee), capacity vs. ADV.
- Hit ratio, avg win/loss, expectancy, time-in-market.

## Checklist hoàn thành lab
- [ ] Xây dựng event queue & dataclass cho 4 loại event.  
- [ ] Data handler point-in-time, không leak.  
- [ ] Strategy on_bar trả SignalEvent.  
- [ ] Risk/Portfolio generate_order với sizing + caps.  
- [ ] Execution fill mô phỏng slippage/impact/fee/latency.  
- [ ] Performance tracker: PnL, DD, Sharpe, turnover, TCost.  
- [ ] Test walk-forward/embargo để kiểm soát leak.  
- [ ] Log/alert đủ để debug.