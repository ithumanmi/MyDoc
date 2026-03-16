# 🛠️ Smart Contracts & DApp Development (Level 3)

> [← Back to Blockchain Roadmap](../README.md)

Smart Contract là trái tim của DeFi, NFT và DApps.

---

## 0. Modules

- [Solidity Deep Dive](solidity-deep-dive.md)
- [Web3 Frontend](web3-frontend.md)
- [Smart Contract Testing](smart-contract-testing.md)
- [Testing Strategies](testing-strategies.md)
- [Deployment Patterns](deployment-patterns.md)
- [Solana Development](solana-development.md)
- [Move Development](move-development.md)

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

### **C. Move (Aptos/Sui)**
*   **Hệ sinh thái:** Aptos, Sui.
*   **Đặc điểm:** Resource-oriented, bảo vệ tài sản tốt, module reuse rõ ràng.
*   **Use-case:** Payments, social, game với throughput cao.

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

### **D. Anchor / Sealevel (Solana)**
*   Macro hữu ích để viết smart contract Rust (program) nhanh hơn.
*   IDL tự sinh để frontend (React, Typescript) dùng @project-serum/anchor.

### **E. Sui/Aptos CLI + Move**
*   Dev cần cài Move CLI, viết module `.move`, unit test với Move Prover.
*   Bản địa hỗ trợ object storage, event.

---

## 3. Quy trình phát triển (Dev Lifecycle)

1.  **Write:** Viết code Solidity (`.sol`).
2.  **Compile:** Dịch sang Bytecode (để chạy trên EVM) và ABI (để Frontend gọi).
3.  **Test:** Viết Unit Test (Mocha/Chai hoặc Foundry). Test từng hàm một.
4.  **Deploy (Testnet):** Đẩy lên mạng thử nghiệm (Sepolia, Goerli).
5.  **Verify:** Xác thực code trên Etherscan để mọi người đọc được.
6.  **Audit:** Thuê công ty bảo mật (Certik, Hacken) tìm lỗi.
7.  **Mainnet:** Đẩy lên mạng chính thức (Tốn tiền thật).

**Bonus:**
*   **Static Analysis:** Slither, MythX, Echidna.
*   **Formal Verification:** Certora, Scribble/VerX.
*   **Test coverage:** đừng bỏ qua property/fuzz test (Foundry, Echidna).

---

## 4. ERC Standards (Tiêu chuẩn Token)

Không cần phát minh lại bánh xe. Hãy theo chuẩn.

*   **ERC-20:** Token nấm (Fungible Token) - Tiền tệ (USDT, UNI).
*   **ERC-721:** Token không nấm (Non-Fungible Token - NFT) - Mỗi token là duy nhất (Tranh ảnh, Giày ảo).
*   **ERC-1155:** Đa token (Multi Token) - Vừa là ERC-20 vừa là ERC-721 (Dùng trong Gamefi tiết kiệm gas).

---

## 5. Web3 Frontend (DApp UX)

### **Stack**
*   **UI:** Next.js/React, Tailwind hoặc Chakra UI.
*   **Wallet:** wagmi + RainbowKit (EVM), WalletConnect, MetaMask SDK.
*   **State:** Zustand/Recoil + TanStack Query để cache call RPC.
*   **Data:** The Graph/Subgraph, Moralis, Alchemy SDK, viem/ethers v6.

### **Patterns**
1. **Connect Wallet Flow:** multi-chain, network guard (switch network), session persistence.
2. **Gas Estimation & Simulation:** show Fee + use `eth_estimateGas` or Tenderly simulation.
3. **TX Lifecycle UI:** Pending → Success/Fail, link Etherscan, handle `userRejected` gracefully.
4. **Sign-In with Ethereum (SIWE):** `eth_sign` message + nonce backend.

### **Security**
*   Validate user input server-side, never trust client-supplied addresses.
*   Use `eth_call` read-only, chainID check, support RPC fallback.

---

## 6. Testing Strategy

| Layer | Tool | Notes |
| --- | --- | --- |
| Unit | Hardhat + Mocha/Chai, Foundry | Cover logic, revert, events |
| Property/Fuzz | Foundry `forge test --fuzz-runs`, Echidna | Tìm edge case (overflow, invariant) |
| Integration | Hardhat Network fork mainnet, Anvil | Simulate DeFi state, mainnet forking |
| UI/E2E | Cypress/Playwright + viem/mocked RPC | Fake wallet provider, test connect/sign flow |
| Deployment | Scripts + `hardhat-deploy`, Foundry `forge script` | Include sanity test post-deploy |

**DevOps:**
*   CI chạy `forge fmt`, `slither .`, `forge test`, `pnpm lint` (frontend).
*   Auto verify Etherscan `hardhat verify` hoặc Foundry `forge verify-contract`.

---

## 7. Deployment & Environments

1. **Local:** Anvil (Foundry) hoặc Hardhat node.
2. **Testnet:** Sepolia/Holesky (EVM), Devnet/Solana Testnet.
3. **Preview:** Deploy staging DApp (Vercel) + pointing testnet contract.
4. **Mainnet:** Multi-sig sign (Safe), timelock, upgrade scripts (OpenZeppelin upgrade plugin).

**Secrets:**
*   ENV vault (Doppler, Vault) cho private key/RPC.
*   Hardware wallet khi deploy mainnet.

**Monitoring:** Tenderly, Etherscan alerts, Blocknative mempool monitoring.

---

## 8. Specific Frameworks & Patterns

*   **OpenZeppelin Contracts:** upgradeable proxies, AccessControl, Governor.
*   **Account Abstraction (ERC-4337):** paymaster, bundler, EIP-7702 (EOA contracts).
*   **Subgraphs (The Graph):** index event, expose GraphQL cho frontend.
*   **Wallet infra:** Safe (Gnosis), Biconomy SDK, Dynamic.

---

## 9. Checklist

- [ ] Lựa chọn framework (Hardhat/Foundry/Anchor) phù hợp chain.
- [ ] Thiết lập test suite (unit + fuzz + fork) và chạy trong CI.
- [ ] Thiết kế Web3 frontend: connect wallet, tx lifecycle, SIWE.
- [ ] Chuẩn bị script deploy/testnet/mainnet + verify.
- [ ] On-chain monitoring + alert (Tenderly/Etherscan) sau deploy.

