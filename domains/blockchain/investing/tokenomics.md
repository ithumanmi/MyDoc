# 💰 Tokenomics & On-chain Investing Playbook (Level 6)

> [← Back to Blockchain Roadmap](../README.md)

Code giỏi chưa chắc đã giàu. Tokenomics quyết định 80% sự thành bại của dự án.
Tokenomics = **Token** (Tiền) + **Economics** (Kinh tế học).

---

## 1. Supply (Nguồn cung)

### **A. Total Supply vs Max Supply**
*   **Total Supply:** Tổng số token đang tồn tại (đã mint). Có thể tăng thêm nếu hợp đồng cho phép mint.
*   **Max Supply:** Giới hạn cứng (Hard Cap) không bao giờ vượt qua. (Bitcoin = 21 triệu).

### **B. Circulating Supply (Cung lưu thông)**
*   Số token đang được giao dịch tự do trên thị trường.
*   **Market Cap (Vốn hóa):** Price * Circulating Supply.
*   **FDV (Fully Diluted Valuation):** Price * Total/Max Supply. (Giá trị thật sự nếu xả hết token ra).
    *   *Rủi ro:* Dự án có Market Cap thấp (10tr$) nhưng FDV cao (1 tỷ$) -> Lạm phát trong tương lai cực lớn -> Giá sẽ giảm (Dump).

---

## 2. Allocation & Vesting (Phân bổ & Trả token)

Ai nắm giữ bao nhiêu token?

*   **Public Sale (IDO):** Bán cho cộng đồng (Giá cao nhất).
*   **Private/Seed Round:** Bán cho quỹ đầu tư (VC) giá rẻ (x10-x100 lần).
*   **Team:** Dành cho đội ngũ phát triển.
*   **Treasury/Ecosystem:** Dành cho Marketing, Airdrop, Liquidity Mining.

### **Vesting Schedule (Lịch trả):**
*   **Cliff:** Thời gian khóa token (Không được bán). Ví dụ: Cliff 1 năm.
*   **Linear Vesting:** Trả dần theo từng tháng/quý.
*   *Chiến lược:* Tránh mua token vào thời điểm unlock lớn của VC/Team -> Giá sẽ bị xả (Dump).

---

## 3. Utility (Công dụng)

Token dùng để làm gì? (Nếu không có công dụng -> Shitcoin).

*   **Governance (Quản trị):** Voting đề xuất thay đổi protocol (DAO).
*   **Staking/Yield:** Khóa token để nhận lãi.
*   **Gas Fee:** Trả phí giao dịch (ETH, BNB, SOL).
*   **Payment:** Mua bán NFT, vật phẩm game.

---

## 4. Inflation vs Deflation (Lạm phát vs Giảm phát)

### **A. Inflationary (Lạm phát)**
*   Sinh ra thêm token mỗi ngày (Block Reward).
*   Ví dụ: Ethereum (trước EIP-1559), Dogecoin (vô hạn).
*   *Hậu quả:* Nếu nhu cầu mua không tăng kịp nguồn cung -> Giá giảm.

### **B. Deflationary (Giảm phát)**
*   Đốt (Burn) token mỗi khi giao dịch.
*   Ví dụ: BNB (Burn theo quý), ETH (Burn 1 phần phí giao dịch).
*   *Hậu quả:* Nguồn cung giảm dần -> Giá có xu hướng tăng (Scarcity).

---

## 5. Case Study: Ponzi Tokenomics
---

## 6. On-chain Analysis (Đọc dữ liệu trực tiếp)

### **Tools**
*   **Nansen, Dune, Arkham:** wallet label, dashboard custom.
*   **Glassnode, CryptoQuant:** on-chain indicators macro.
*   **Dexscreener, GeckoTerminal:** realtime DEX liquidity + pair info.

### **Metrics**
1. **Active Addresses / New Addresses** → gauge adoption.
2. **CEX/DEX Inflow-Outflow** → detect selling pressure.
3. **Whale Movements:** track smart money accumulation/distribution.
4. **Token Unlock Calendar:** TokenUnlocks, Messari.

### **On-chain Ops**
- Gọi `eth_call`/`eth_getLogs` để track event (transfer, staking).
- Sử dụng The Graph/Substreams để query large dataset.

---

## 7. Trading Strategies

### **A. Trend Following (Momentum)**
*   Dùng MA, RSI, funding rate để xác định trend.
*   On-chain confirm: TVL tăng, stablecoin inflow, stake ratio.

### **B. Mean Reversion / Range Trading**
*   Quan sát funding rate âm/quá cao → bet về mean.
*   Liquidity pool depth (Uniswap v3) để xác định hỗ trợ/kháng cự.

### **C. Event-driven**
*   Catalyst: mainnet, token unlock, upgrade, airdrop.
*   Playbook: mua trước rumor, bán trước sự kiện (buy rumor, sell news).

### **D. Basis / Arbitrage**
*   Chênh lệch giá giữa CEX/DEX, futures vs spot.
*   Dụng cụ: perpetual swap, lending margin (Aave, Gearbox).

### **E. Structured Strategies**
*   Vault Delta-neutral (Ribbon, Friktion) → yield + hedge.
*   Options selling (Dopex, Lyra) → yield nhưng rủi ro tail risk.

---

## 8. Risk Management

1. **Position sizing:** Không quá 5-10% portfolio cho một token alt.
2. **Stop-loss / Alerts:** TradingView + on-chain alert (Tenderly, Nansen).
3. **Counterparty risk:** Check bridge, custodian, custodial risk.
4. **Smart Contract risk:** audit status, TVL, time alive, admin key.
5. **Macro:** USD liquidity (DXY), rates (Fed), regulatory crackdown.

### **Portfolio Construction**
| Bucket | % | Notes |
| Core (BTC/ETH) | 40-60% | DCA, staking | 
| Beta (L2, DeFi bluechip) | 20-30% | Monitor TVL |
| Venture (early stage) | 10-20% | via SAFT/Launchpad |
| Cash/Stable | 10-20% | dry powder |

---

## 9. Checklist

- [ ] Đọc tokenomics: supply, vesting, utility, unlock schedule.
- [ ] Theo dõi dữ liệu on-chain (Nansen/Dune, token unlock calendar).
- [ ] Xác định chiến lược giao dịch (trend, event, arbitrage) + rule risk.
- [ ] Thiết lập alert, quản lý vị thế, baseline portfolio allocation.
- [ ] Review thesis mỗi quý: cập nhật narrative (AI, L2, RWA...).
### **Mô hình "In tiền trả lãi" (Luna/UST, Olympus DAO)**
1.  Người dùng Staking token A lãi suất cao (100.000% APY).
2.  Lãi trả bằng chính token A (được in thêm).
3.  Giá tăng nhờ FOMO (Người mới vào mua A để stake).
4.  Khi không còn người mới -> Giá sập -> APY vô nghĩa (Hyperinflation).
