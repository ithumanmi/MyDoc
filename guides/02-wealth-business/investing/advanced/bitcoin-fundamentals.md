---
title: "Bitcoin Fundamentals 2026"
description: "Deep dive về luận điểm đầu tư Bitcoin: nguồn gốc công nghệ, mô hình kinh tế, on-chain metrics và chiến lược vận hành."
tags:
  - bitcoin
  - crypto
  - investing
updated: 2026-03-10
---

# ₿ Bitcoin Fundamentals 2026

> “Bitcoin là sự kết hợp giữa chính sách tiền tệ cố định và mạng lưới phi tập trung có thể đo lường được qua dữ liệu on-chain.”

Tài liệu này tập trung vào 6 phần: **(1) Narrative & lịch sử**, **(2) Cơ chế vận hành**, **(3) On-chain & định giá**, **(4) Chiến lược nắm giữ/hedge**, **(5) Rủi ro & compliance**, **(6) Action plan**.

---

## 1. Narrative & Timeline
| Giai đoạn | Highlight | Narrative chính |
| --- | --- | --- |
| 2008-2012 | Ra mắt whitepaper, khối genesis, Mt.Gox | “Peer-to-peer electronic cash” đối kháng hệ thống ngân hàng. |
| 2013-2016 | Halving đầu, Silk Road, khung pháp lý đầu tiên | “Digital gold” & censorship resistance. |
| 2017-2020 | SegWit, LN launch, halving lần 2 | “Store of value” + tranh luận mở rộng block. |
| 2020-2023 | MicroStrategy/Tesla buy, El Salvador legal tender, Ordinals | “Institutional adoption” và narrative lạm phát. |
| 2024+ | Halving lần 4, Bitcoin ETF spot, Lightning & L2 | “Collateral layer” cho tài chính số & hạ tầng thanh toán. |

**Tác động:** mỗi chu kỳ halving thường dẫn tới phase tích lũy → breakout → phân phối. Tuy nhiên cần kết hợp macro (lãi suất, thanh khoản USD) để tránh áp dụng mô hình tuyến tính.

---

## 2. Monetary & Technical Mechanics

### 2.1 Monetary Policy
- Nguồn cung tối đa **21 triệu BTC** – đảm bảo khan hiếm.
- Halving mỗi ~210.000 block (~4 năm), giảm phần thưởng block 50%.
- Tỷ lệ lạm phát annualized <1% sau năm 2032 → giống “hard money”.

| Halving | Năm | Reward/block | Tỷ lệ lạm phát ước tính |
| --- | --- | --- | --- |
| #1 | 2012 | 25 BTC | ~12% |
| #2 | 2016 | 12.5 BTC | ~4% |
| #3 | 2020 | 6.25 BTC | ~1.8% |
| #4 | 2024 | 3.125 BTC | ~0.8% |

### 2.2 Network & Security
- **Proof-of-Work** với SHA-256, hashrate phản ánh chi phí bảo mật.
- **Difficulty adjustment** mỗi 2016 block (~14 ngày) để ổn định thời gian block.
- **Lightning Network & Layer-2:** mở rộng throughput bằng off-chain channel, giảm phí.

### 2.3 Game Theory
- Miner cần vốn CAPEX (ASIC + điện) → bán BTC để trả chi phí → tạo chu kỳ cung/cầu.
- Người dùng giữ BTC dài hạn giảm lượng cung trôi nổi (liquidity squeeze) → ảnh hưởng giá.

---

## 3. On-chain Metrics & Valuation Lenses

| Chỉ số | Ý nghĩa | Ứng dụng |
| --- | --- | --- |
| **Hashrate & Difficulty** | Sức mạnh mạng, chi phí tấn công | Theo dõi health, phát hiện miner capitulation. |
| **HODL Waves / Coin Days Destroyed** | Tuổi coin, hành vi holder | Nhận diện phân phối hay tích lũy. |
| **Realized Cap / Market Value (MVRV)** | Giá vốn trung bình mạng | Định vùng overheated (>3.5) hoặc discount (<1). |
| **Puell Multiple** | Doanh thu miner / trung bình 365 ngày | Đánh giá áp lực bán miner. |
| **RHODL Ratio, NUPL** | Cảm xúc thị trường | Timing chu kỳ nhưng tránh dùng đơn lẻ. |

### Valuation Approaches
1. **Stock-to-Flow (S2F):** mô hình khan hiếm (đã bộc lộ hạn chế sau 2021).
2. **Energy Value / Production Cost:** định giá dựa trên chi phí điện + hiệu suất ASIC.
3. **Metcalfe’s Law / Network Effect:** giá trị ∝ số lượng người dùng, addresses.
4. **Macro Correlation:** BTC tương quan SP500/Nasdaq, DXY, vàng – dùng để đánh giá vị thế hedge.

---

## 4. Strategy Playbook

### 4.1 Accumulation
- **DCA** theo tuần/tháng để giảm ảnh hưởng biến động.
- **Threshold Buy:** mua khi MVRV <1 hoặc Puell Multiple <0.5 (kết hợp thêm macro).
- **Treasury Allocation:** doanh nghiệp mua BTC như MicroStrategy – cần chính sách kế toán, hedging.

### 4.2 Yield & Leverage
- **Bitcoin-backed loans:** dùng BTC làm collateral để vay USD/stablecoin (BlockFi-like) – chú ý LTV & rehypothecation.
- **Covered Call / Cash-secured Put:** dùng options (Deribit, CME) để tạo thu nhập.
- **Liquid Staking trên L2/Lightning:** kiếm phí routing nhưng cần vận hành node.

### 4.3 Hedging
- Short futures/ETF khi muốn bảo vệ downside nhưng vẫn giữ BTC on-chain.
- Sử dụng collar (long put, short call) để giới hạn rủi ro khi lợi nhuận lớn.
- Diversify với vàng/treasury khi BTC chiếm >50% danh mục.

### 4.4 Operational SOP
- Cold storage: multisig (Casa, Unchained) + policy quản lý seed.
- Custody doanh nghiệp: phối hợp với BitGo, Fidelity Digital Asset.
- Theo dõi liquidity venue (CME, Coinbase, Binance) để tránh trượt giá khi giao dịch lớn.

---

## 5. Risks & Compliance
- **Regulatory:** phân loại Security/Commodity; yêu cầu AML/KYC, Travel Rule.
- **Custody:** mất seed, tấn công phishing, MPC misconfiguration.
- **Energy & ESG:** áp lực chính sách do tiêu thụ điện; cân nhắc nguồn năng lượng tái tạo.
- **Fork/Protocol risk:** soft fork tranh cãi (Taproot), hard fork (BCH/BSV) gây nhiễu nhà đầu tư.
- **Stablecoin/Exchange Dependency:** thanh khoản BTC phụ thuộc lớn vào thị trường stablecoin và sàn tập trung – rủi ro nếu bị cấm hoạt động.

> Checklist pháp lý: xem [Tax & Investing Compliance](../../../legal/finance-investing/tax-investing.md) + chuẩn bị báo cáo tài sản số theo yêu cầu địa phương.

---

## 6. 60-Day Focus Plan
| Tuần | Hành động |
| --- | --- |
| 0-2 | Cập nhật thesis BTC, xác định vai trò (store of value, collateral, treasury). |
| 2-4 | Thiết lập custody (hardware wallet, multisig) và bảo hiểm nếu cần. |
| 4-6 | Bắt đầu DCA + xây dashboard on-chain (Glassnode, CryptoQuant). |
| 6-8 | Đánh giá nhu cầu yield/hedge, thử nghiệm options/futures với sizing nhỏ. |
| 8+ | Review hiệu suất, cập nhật policy thuế & báo cáo nội bộ. |

---

## 7. Key Takeaways
- Bitcoin có chính sách tiền tệ minh bạch nhất hiện nay nhờ supply cố định và dữ liệu on-chain mở.
- Chu kỳ giá chịu ảnh hưởng lớn từ halving nhưng phải kết hợp yếu tố macro/liquidity.
- Thành công phụ thuộc vào kỷ luật vận hành: custody, tuân thủ pháp lý và quản trị rủi ro thị trường.

> **Next:** Kết hợp tài liệu này với [Crypto & DeFi Fundamentals](./crypto-defi.md), [Digital Assets Strategy](./digital-assets-strategy.md) và bộ tài liệu pháp lý để xây dựng chiến lược tổng thể.