---
title: "Alpha Research & Stat-Arb Checklist"
---

# Alpha Research & Stat-Arb Checklist

> [← Back to Quantitative Trading Hub](./README.md)

Checklist nhanh khi nghiên cứu alpha/stat-arb để tránh bias và overfit.

## 1) Data hygiene & PIT
- [ ] Point-in-time: không dùng dữ liệu sau cutoff; disable auto-forward-fill vượt sự kiện.  
- [ ] Survivorship bias: giữ cả delisted; dùng symbol mapping.  
- [ ] Corporate actions: adjust splits/dividends chuẩn; xử lý outlier.  
- [ ] Lag/align: feature lùi 1 bar/1 ngày; đồng bộ timezone.  

## 2) Labeling & target
- [ ] Horizon rõ ràng (k bars/days); tránh chồng lấn nếu không dùng purged CV.  
- [ ] Label: return, residual (beta/sector neutral), hoặc spread của pair/portfolio.  
- [ ] Meta-labeling nếu cần giảm false positive.  

## 3) Feature design
- [ ] Stationary/residual signals: z-score, half-life decay.  
- [ ] Regime-aware: vol, spread, liquidity regimes.  
- [ ] Detrend & neutralize: beta/sector/market neutral.  
- [ ] Capacity-aware: ADV %, turnover, borrow/fee nếu short.  

## 4) Validation
- [ ] Walk-forward hoặc purged k-fold (embargo).  
- [ ] Split theo thời gian (train/val/test), tránh leak.  
- [ ] White’s Reality Check / SPA hoặc PBO để chống data snooping.  
- [ ] Out-of-sample và paper trading song song trước live.  

## 5) Metrics
- [ ] Sharpe/Sortino, t-stat alpha.  
- [ ] Hit ratio, payoff ratio.  
- [ ] Turnover, TCost, slippage thực tế giả lập.  
- [ ] Max DD, tail risk (ES/VaR).  
- [ ] Capacity & decay (half-life).  

## 6) Deployment readiness
- [ ] Latency budget đủ cho horizon?  
- [ ] Risk caps: gross/net/beta, DD cap, turnover cap.  
- [ ] Kill-switch & circuit breaker.  
- [ ] Monitoring: drift, PnL attribution, borrow cost.  

## 7) Stat-arb cụ thể
- [ ] Pairs/cross-sectional: kiểm tra cointegration/ADF, hedge ratio, regime stability.  
- [ ] Mean-reversion window/half-life; stop khi vol/spread regime đổi.  
- [ ] Dollar/vol scaling, cap %ADV, borrow availability.  
- [ ] Basket-neutral thay vì cặp đơn để giảm idiosyncratic risk.  

## 8) Pre-trade & post-trade TCA
- [ ] Ước lượng impact/fee vào kỳ vọng alpha.  
- [ ] Post-trade: IS, VWAP slippage, borrow/financing cost.  

## 9) Robustness hacks
- [ ] Shuffle time blocks / permute để kiểm leak.  
- [ ] Stress test: vol spike, spread widen, borrow fee tăng.  
- [ ] Sensitivity: thay đổi tham số nhỏ xem alpha còn không.  
- [ ] Subsample theo regime, sàn giao dịch, khung giờ.  