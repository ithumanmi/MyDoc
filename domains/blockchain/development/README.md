---
title: "Blockchain Development"
description: "Từ smart contract đến frontend, testing, deployment cho Web3 devs."
tags:
  - blockchain
  - development
updated: 2026-03-16
---

# 🛠️ Blockchain Development Hub

\> **Goal:** Có một trung tâm tài liệu để đi từ viết smart contract → test → build frontend → deploy multi-chain.

## 📚 Module Index
| File | Nội dung | Khi nào dùng |
| --- | --- | --- |
| [smart-contracts.md](./smart-contracts.md) | Tổng quan ngôn ngữ (Solidity, Rust, Move) & lifecycle contract | Khi mới bắt đầu viết DApp |
| [solidity-deep-dive.md](./solidity-deep-dive.md) | Advanced patterns, gas optimizations, storage layout | Nâng cấp từ basic → senior solidity dev |
| [web3-frontend.md](./web3-frontend.md) | Kết nối ví, Ethers.js/Wagmi, UI signing flow | Build dApp UI/UX |
| [testing-strategies.md](./testing-strategies.md) | Hardhat, Foundry, fuzzing, invariant testing | Trước audit, CI/CD |
| [deployment-patterns.md](./deployment-patterns.md) | Upgradeable proxy, multi-chain, relayer | Ship production contract |
| [move-development.md](./move-development.md) & [solana-development.md](./solana-development.md) | Ngăn riêng cho Move/Solana | Khi mở rộng sang chain khác |

## 🚀 Learning Path
1. **Kickoff:** Đọc smart-contracts.md → chọn chain (Ethereum/Solana/Move).
2. **Deepen:** Học solidity-deep-dive hoặc Move/Solana tùy stack.
3. **Frontend:** Triển khai connector (RainbowKit, WalletConnect) + handle session replay attack.
4. **Testing:** Unit + property-based + formal verification snapshot.
5. **Deploy:** Chọn pattern (Transparent proxy, Beacon proxy, CREATE2 deterministic deploy).

## 🔗 Cross-links
- [fundamentals/blockchain-101.md](../fundamentals/blockchain-101.md)
- [security/smart-contract-auditing.md](../security/smart-contract-auditing.md)
- [development/smart-contract-testing.md](./smart-contract-testing.md)
- [deployment-patterns.md](./deployment-patterns.md)