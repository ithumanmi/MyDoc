# 🏦 DeFi Mechanisms: Tài chính Phi tập trung (Level 4)

> [← Back to Blockchain Roadmap](../README.md)

DeFi (Decentralized Finance) là hệ thống ngân hàng không cần nhân viên. Nó chạy bằng code.

---

## 1. AMM (Automated Market Maker) - Uniswap

Sàn giao dịch tập trung (Binance) dùng sổ lệnh (Order Book) để khớp lệnh mua/bán.
Sàn phi tập trung (DEX) dùng AMM.

### **Công thức:** $$ x * y = k $$
*   **x:** Số lượng Token A trong hồ thanh khoản (Liquidity Pool).
*   **y:** Số lượng Token B trong hồ thanh khoản.
*   **k:** Hằng số không đổi.

Khi bạn mua Token A, bạn ném Token B vào hồ -> Số lượng B tăng -> Giá A tăng để giữ k không đổi.
*   **Slippage (Trượt giá):** Khi giao dịch quá lớn so với hồ thanh khoản, giá sẽ thay đổi mạnh.
*   **Impermanent Loss (Tổn thất vô thường):** Rủi ro khi cung cấp thanh khoản. Nếu giá token thay đổi mạnh, bạn rút về ít tiền hơn so với việc cứ để im (Hodl).

---

## 2. Lending & Borrowing (Vay & Cho vay) - Aave, Compound

### **Cơ chế:**
*   **Người gửi (Lender):** Gửi tiền vào Pool để nhận lãi suất (APY).
*   **Người vay (Borrower):** Thế chấp tài sản (Collateral) để vay tiền.
    *   *Over-collateralization:* Phải thế chấp nhiều hơn số tiền vay (Vay 100$ phải thế chấp 150$ ETH).
    *   *Liquidation (Thanh lý):* Nếu giá tài sản thế chấp giảm xuống dưới ngưỡng an toàn (LTV), Smart Contract sẽ tự động bán tài sản của bạn để trả nợ.

### **Flash Loan (Vay nóng):**
*   Vay hàng triệu USD không cần thế chấp.
*   Điều kiện: Phải trả lại tiền trong cùng 1 Block giao dịch. Nếu không trả, giao dịch bị hủy (revert) như chưa từng xảy ra.
*   *Ứng dụng:* Arbitrage (Kinh doanh chênh lệch giá) giữa các sàn DEX.

---

## 3. Yield Farming (Canh tác năng suất)

*   **Liquidity Mining:** Cung cấp thanh khoản cho DEX (Uniswap) để nhận phí giao dịch + Token thưởng của dự án.
*   **Staking:** Khóa token vào mạng lưới (PoS) hoặc Protocol để nhận phần thưởng lạm phát.

---

## 4. Stablecoins (Đồng ổn định)

Tiền tệ của DeFi.

### **A. Centralized (Tập trung) - USDT, USDC**
*   Được bảo chứng 1:1 bằng USD thật trong ngân hàng.
*   Rủi ro: Công ty phát hành có thể đóng băng tài sản (Blacklist).

### **B. Decentralized (Phi tập trung) - DAI**
*   Được bảo chứng bằng Crypto (ETH, WBTC) thế chấp vượt mức (Over-collateralized).
*   An toàn hơn (không ai có thể đóng băng), nhưng kém hiệu quả vốn.

### **C. Algorithmic (Thuật toán) - UST (Đã sập)**
*   Không có tài sản bảo chứng. Giữ giá bằng cơ chế in/đốt token tự động (Burn/Mint).
*   Rủi ro: Death Spiral (Vòng xoáy tử thần) khi mất niềm tin (Depeg).
