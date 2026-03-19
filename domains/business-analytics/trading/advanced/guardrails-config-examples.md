---
title: "Guardrails & Config Examples"
---

# Guardrails & Config Examples

> [← Back to Quantitative Trading Hub](./README.md)

Mẫu config (YAML) cho risk caps, guardrails, rate-limit, kill-switch.

```yaml
strategy: mean_reversion_eq

risk_caps:
  gross_exposure: 1.5        # 150% NAV
  net_exposure: 0.3          # 30% NAV
  beta_exposure: 0.4         # beta-adjusted
  dd_intraday: 0.03          # 3% NAV
  dd_daily: 0.05
  turnover_daily: 1.5        # 150%/day
  adv_limit: 0.02            # 2% ADV per symbol

orders:
  max_orders_per_sec: 20
  max_notional_per_order: 200000
  max_open_orders: 200
  tif_default: IOC

latency:
  warn_ms: 50
  circuit_ms: 150

kill_switch:
  enabled: true
  triggers:
    - name: pnl_intraday
      condition: pnl < -0.02 * nav
    - name: latency_spike
      condition: p99_latency_ms > 150
    - name: reject_rate
      condition: order_reject_ratio > 0.02

monitoring:
  heartbeat_timeout_sec: 5
  quote_staleness_ms: 200
  mark_to_market_drift_bps: 30   # cross-venue drift
  alert_channels: [pagerduty, slack]

logging:
  level: info
  audit_trail: true
  fields: [signal, size, caps, reason, venue, latency_ms]

pnl_attribution:
  enabled: true
  dimensions: [strategy, venue, symbol, side, bucket_intraday]
  drift_monitor:
    price_drift_bps: 50        # chênh L1/L2/mark
    pnl_drift_bps: 20          # khác biệt PnL internal vs broker/venue
    borrow_fee_spike_bps: 30   # tăng phí borrow gây drift PnL
  actions:
    - name: alert_drift
      condition: drift_detected == true
      notify: [pagerduty, slack]
    - name: halt_symbol
      condition: abs(price_drift_bps) > 80 or abs(pnl_drift_bps) > 50
      effect: disable_trading_symbol: true
```

Checklist áp dụng:
- [ ] Giới hạn gross/net/beta, DD, turnover, %ADV.  
- [ ] Giới hạn orders/s, open orders, notional, TIF.  
- [ ] Latency guard: cảnh báo + circuit breaker.  
- [ ] Kill-switch với trigger rõ ràng; nút tắt tay.  
- [ ] Heartbeat/quote staleness; drift giữa venues.  
- [ ] Alert + audit trail để postmortem.  