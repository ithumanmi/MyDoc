# Challenge: Solidity Escrow

- **Loại:** project
- **Mảng:** blockchain
- **Mức:** Intermediate
- **Ước lượng:** 1–2 ngày
- **Prerequisites:** [`domains/blockchain/development/`](../../domains/blockchain/development/README.md) (hoặc README blockchain)

## Mục tiêu học tập
- Viết escrow contract an toàn cơ bản (deposit / release / refund)
- Test với Foundry hoặc Hardhat
- Hiểu reentrancy + access control tối thiểu

## Đề bài
Escrow giữa `buyer` và `seller`:
- Buyer deposit ETH/ERC20
- Seller đánh dấu delivered (hoặc oracle giả)
- Buyer `release` → seller nhận fund
- Timeout → buyer `refund`
- Chỉ đúng role gọi đúng hàm

## Acceptance
- [ ] Tests: happy path, double release fail, non-buyer cannot release, timeout refund
- [ ] `nonReentrant` (hoặc pattern tương đương) trên chuyển quỹ
- [ ] README: deploy local + chạy test
- [ ] Không dùng `tx.origin` cho auth

## Gợi ý
Checks-effects-interactions; prefer pull over push nếu mở rộng multi-party.
