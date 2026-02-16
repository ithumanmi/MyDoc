# 📈 Advanced DeFi: Phái sinh & Chiến lược (Level 8)

> [← Back to Blockchain Roadmap](../README.md)

DeFi không chỉ là Swap coin. Nó là thị trường tài chính trị giá nghìn tỷ USD.
Advanced DeFi bao gồm các công cụ phái sinh (Derivatives) phức tạp như Futures, Options, và Yield Farming.

---

## 1. Perpetual Futures (Hợp đồng tương lai vĩnh cửu)

Giao dịch đòn bẩy (Leverage x100) trên Blockchain. Không có ngày hết hạn.

### **Cơ chế Funding Rate:**
Để giá trên sàn (Mark Price) bám sát giá thị trường (Index Price), Long và Short phải trả tiền cho nhau mỗi 8 tiếng.
*   **Funding Rate Dương:** Phe Long trả tiền cho Phe Short (Thị trường Bullish).
*   **Funding Rate Âm:** Phe Short trả tiền cho Phe Long (Thị trường Bearish).
*   **Chiến lược:** Arbitrage Funding Rate (Short trên sàn có Funding dương để ăn phí, Long Spot để Hedge giá).

---

## 2. Options (Quyền chọn) - Opyn, Lyra

Quyền (không bắt buộc) mua/bán tài sản ở mức giá định trước vào một ngày cụ thể.

*   **Call Option:** Mua quyền mua (Cược giá lên).
*   **Put Option:** Mua quyền bán (Cược giá xuống/Bảo hiểm).
*   **DeFi Options Vaults (DOV):** Tự động bán quyền chọn (Selling Calls/Puts) để kiếm thêm lợi nhuận (Yield) từ phí quyền chọn (Premium).
*   *Rủi ro:* Nếu giá biến động quá mạnh ngược chiều dự đoán -> Mất hết tài sản thế chấp.

---

## 3. Flash Loans (Vay siêu tốc)

Vay hàng triệu USD không cần thế chấp, miễn là trả lại trong cùng 1 Block.

### **Ứng dụng:**
1.  **Arbitrage:** Giá ETH trên Uniswap là 2000$, trên SushiSwap là 2010$.
    *   Vay 1000 ETH (2tr$).
    *   Mua ETH rẻ bên Uniswap -> Bán đắt bên SushiSwap.
    *   Trả nợ + Phí vay.
    *   Lãi bỏ túi.
2.  **Collateral Swap:** Đổi tài sản thế chấp (ETH sang WBTC) trên Aave mà không cần trả nợ trước.
3.  **Liquidate:** Vay tiền để thanh lý tài sản của người khác và nhận thưởng.

---

## 4. Real World Assets (RWA) - Token hóa tài sản thực

Đưa Bất động sản, Cổ phiếu, Trái phiếu chính phủ lên Blockchain.
*   **MakerDAO:** Dùng Trái phiếu Mỹ (T-Bill) làm tài sản bảo chứng cho DAI.
*   **Ondo Finance:** Token hóa quỹ trái phiếu BlackRock.
*   *Thách thức:* Pháp lý (KYC/AML) và cơ chế Oracle định giá tài sản thực.
