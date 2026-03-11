---
title: "Flashbots Protect & Private Mempools"
description: "Cách gửi giao dịch private, bảo vệ người dùng khỏi sandwich."
tags:
  - flashbots
  - mev
  - rpc
updated: 2026-03-11
---

# 🛡️ Flashbots Protect & Private Mempools

## 1. Problem Statement

Public mempool cho phép bot đọc trước → sandwich/front-run. Private mempool giữ tx bí mật đến khi vào block.

## 2. Flashbots Protect RPC

- Endpoint: `https://protect.flashbots.net/v1/rpc`.
- Features:
  - Gửi tx private, không vào public mempool.
  - Delivers tx tới builder hỗ trợ (Flashbots, Beaverbuild...).
  - Option fallback public nếu không vào block sau X block.

**Usage (ethers.js):**

```ts
const provider = new ethers.providers.StaticJsonRpcProvider({
  url: "https://protect.flashbots.net/v1/rpc",
  headers: {
    "x-flashbots-signature": `${wallet.address}:${signature}`
  }
});
```

## 3. bloXroute, Eden Network, Manifold

- **bloXroute BDN:** pay for private relays, supports SubmitBundle.
- **Eden Network (deprecating)**: slot-based priority.
- **Manifold:** builder/relay stack.

## 4. Strategy for DApps

- Provide custom RPC in wallet modal (Flashbots Protect).
- Default slippage < 1%, allow user toggle private tx.
- Integrate with `eth_sendPrivateTransaction`.

## 5. Limitations

- Not all validators use private relay → tx có thể không được include.
- Gas price still needed; private tx không miễn phí.
- Failure fallback to public mempool (if configured) → risk leak.

## 6. Checklist

- [ ] Cấu hình RPC private trong UI.
- [ ] Cho phép user thấy status (Pending, Included, Failed).
- [ ] Fallback strategy rõ ràng (retry, cancel).
- [ ] Monitor success rate theo relay.
- [ ] Educate user: private tx tăng an toàn nhưng không đảm bảo 100%.