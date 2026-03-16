---
title: "Cryptography Basics"
description: "Hash, chữ ký số, Merkle tree, BLS vs ECDSA cho blockchain developer."
tags:
  - blockchain
  - cryptography
  - fundamentals
updated: 2026-03-16
---

# 🔐 Cryptography Basics for Blockchain Builders

> **Scope:** Ôn lại các khái niệm mật mã áp dụng trực tiếp vào blockchain: hash, khóa công khai, chữ ký, Merkle tree và multi-signature.

## 1. Hash Functions
- **Tính chất:** Deterministic, Pre-image resistant, Collision resistant, Avalanche effect.
- **Thuật toán phổ biến:** SHA-256 (Bitcoin), Keccak-256 (Ethereum), Poseidon (ZK circuits).
- **Use case:**
  - Tạo block hash (link chain).
  - Merkle root của giao dịch.
  - Address generation (hash public key → account).

### Demo pseudo (Python)
```python
import hashlib
def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

print(sha256_hex(b"vmastery"))
```

## 2. Public-Key Cryptography
- **Cặp khóa:** Private key (bí mật) + Public key (chia sẻ).
- **Elliptic Curve:** secp256k1 (Bitcoin/Ethereum), ed25519 (Solana, Cosmos).
- **Chữ ký số:**
  - **ECDSA:** widely used, yêu cầu R,S values.
  - **EdDSA (ed25519):** deterministic, nhanh hơn.
  - **BLS:** hỗ trợ signature aggregation (Ethereum Altair, EigenLayer AVS).

### Transaction Signing Flow (Ethereum)
1. Encode tx (RLP) → hash Keccak-256.
2. `sig = ECDSA_sign(hash, private_key)`.
3. Attach `(r, s, v)` vào transaction → broadcast.
4. Node verify bằng public key.

## 3. Merkle Tree & Merkle Proofs
- **Merkle Tree:** Cây nhị phân hash → root đại diện toàn bộ data.
- **Merkle Proof:** Chuỗi hash siblings để chứng minh element nằm trong tree mà không reveal toàn bộ data.
- **Ứng dụng:**
  - Bitcoin SPV clients xác minh tx không cần full node.
  - Rollups gửi state root lên L1.

## 4. Commitment Schemes
- **Pedersen Commitment:** `C = rG + mH` → hiding & binding.
- **KZG Commitment:** Dùng trong Danksharding/EIP-4844 để cam kết polynomial.
- **Use case:** Data availability sampling, polynomial proofs.

## 5. Multi-signature & Threshold Signatures
- **Multisig (n-of-m):** Tăng bảo mật ví/treasury.
- **Approaches:**
  - Smart contract (Gnosis Safe) – on-chain logic.
  - Threshold signature (TSS) – off-chain combine partial signatures (Fireblocks, Lit).
- **BLS Aggregation:** Hàng ngàn validator attestation gộp thành 1 chữ ký.

## 6. Zero-Knowledge Primitives (Snapshot)
- **zk-SNARK:** succinct, needs trusted setup (Groth16) hoặc universal (PLONK).
- **zk-STARK:** no trusted setup, proof size lớn hơn.
- **Use case:** Privacy (Zcash), rollups (zkSync, StarkNet), identity (ZK email).

## Checklist Khi Đọc Whitepaper
- [ ] Hash algorithm? Có kháng lượng tử?
- [ ] Key/Signature scheme? (ECDSA, EdDSA, BLS)
- [ ] Data structure: Merkle tree, Verkle tree?
- [ ] ZK proof type? Trusted setup quy mô ra sao?
- [ ] Multisig/TSS requirement?

## 🔗 Cross-links
- [Consensus Mechanisms](./consensus-mechanisms.md)
- [Security - Smart Contract Auditing](../security/smart-contract-auditing.md)
- [Scaling - Danksharding](../scaling/danksharding.md)