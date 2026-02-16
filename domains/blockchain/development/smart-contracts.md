# 🛠️ Smart Contracts Development (Level 3)

> [← Back to Blockchain Roadmap](../README.md)

Smart Contract là trái tim của DeFi, NFT và DApps.

---

## 1. Ngôn ngữ Lập trình (Languages)

### **A. Solidity (Vua của Smart Contract)**
*   **Hệ sinh thái:** Ethereum, Binance Smart Chain, Polygon, Avalanche.
*   **Đặc điểm:** Giống Javascript/C++. Hướng đối tượng (Contract-Oriented).
*   **Học:**
    *   CryptoZombies (Học qua Game).
    *   Solidity By Example.

### **B. Rust (Ngôi sao mới nổi)**
*   **Hệ sinh thái:** Solana, Near, Polkadot.
*   **Đặc điểm:** An toàn bộ nhớ (Memory Safety), hiệu suất cực cao.
*   **Khó:** Cú pháp phức tạp hơn Solidity nhiều.

---

## 2. Frameworks (Công cụ phát triển)

Đừng code bằng Notepad. Hãy dùng Framework.

### **A. Hardhat (Javascript/Typescript)**
*   Phổ biến nhất hiện nay.
*   Tích hợp sẵn Ethers.js, Waffle (Test).
*   Console.log ngay trong Smart Contract (Debug sướng).
*   Plugin đa dạng (Deploy, Verify Etherscan).

### **B. Foundry (Rust)**
*   Nhanh nhất thế giới (Viết bằng Rust).
*   Test bằng Solidity (Không cần học JS để viết Test).
*   Fuzz Testing tích hợp sẵn (Tìm lỗi tự động).

### **C. Truffle (Huyền thoại cũ)**
*   Đã lỗi thời (Legacy). Ít người dùng mới.

---

## 3. Quy trình phát triển (Dev Lifecycle)

1.  **Write:** Viết code Solidity (`.sol`).
2.  **Compile:** Dịch sang Bytecode (để chạy trên EVM) và ABI (để Frontend gọi).
3.  **Test:** Viết Unit Test (Mocha/Chai hoặc Foundry). Test từng hàm một.
4.  **Deploy (Testnet):** Đẩy lên mạng thử nghiệm (Sepolia, Goerli).
5.  **Verify:** Xác thực code trên Etherscan để mọi người đọc được.
6.  **Audit:** Thuê công ty bảo mật (Certik, Hacken) tìm lỗi.
7.  **Mainnet:** Đẩy lên mạng chính thức (Tốn tiền thật).

---

## 4. ERC Standards (Tiêu chuẩn Token)

Không cần phát minh lại bánh xe. Hãy theo chuẩn.

*   **ERC-20:** Token nấm (Fungible Token) - Tiền tệ (USDT, UNI).
*   **ERC-721:** Token không nấm (Non-Fungible Token - NFT) - Mỗi token là duy nhất (Tranh ảnh, Giày ảo).
*   **ERC-1155:** Đa token (Multi Token) - Vừa là ERC-20 vừa là ERC-721 (Dùng trong Gamefi tiết kiệm gas).
