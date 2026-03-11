# 📈 Scaling Stack: Layer2, Sharding & Modular Blockchain (Deep Dive)

> [← Back to Blockchain Roadmap](../README.md)

Ethereum (Layer 1) giống như con đường quốc lộ cũ kỹ: kẹt xe (tắc nghẽn) và phí cầu đường đắt đỏ (Gas cao).
Layer 2 là đường cao tốc xây bên trên: Xe chạy nhanh, phí rẻ, rồi gom lại xuống quốc lộ một lần.

---

## 1. Rollups (Cuộn lại)

Cơ chế: Thực hiện hàng nghìn giao dịch ở ngoài chuỗi (Off-chain), nén dữ liệu lại thành một gói nhỏ, rồi gửi bằng chứng (Proof) xuống Layer 1 để lưu trữ.

### **A. Optimistic Rollups (Lạc quan)**
*   **Dự án:** Optimism (OP), Arbitrum (ARB).
*   **Cơ chế:** Giả định mọi giao dịch đều đúng (Lạc quan).
*   **Fraud Proof (Bằng chứng gian lận):** Nếu ai đó phát hiện giao dịch sai, họ có 7 ngày (Challenge Period) để khiếu nại. Nếu đúng là sai, người gửi giao dịch sẽ bị phạt (Slashing).
*   **Ưu điểm:** Dễ tương thích với EVM.
*   **Nhược điểm:** Rút tiền về L1 mất 7 ngày.

### **B. ZK-Rollups (Zero-Knowledge)**
*   **Dự án:** zkSync, Starknet, Polygon zkEVM.
*   **Cơ chế:** Dùng toán học (Zero-Knowledge Proof) để chứng minh giao dịch là đúng ngay lập tức.
*   **Validity Proof (Bằng chứng hợp lệ):** Gửi bằng chứng toán học xuống L1. L1 kiểm tra -> Xong luôn.
*   **Ưu điểm:** Rút tiền tức thì, bảo mật cao hơn.
*   **Nhược điểm:** Tính toán phức tạp (cần máy mạnh), khó tương thích EVM hoàn toàn.

---

## 2. Sidechains (Chuỗi phụ) - Polygon PoS

*   Không phải Layer 2 thuần túy. Nó là một Blockchain riêng biệt chạy song song với Ethereum.
*   Có cơ chế đồng thuận riêng, Validator riêng.
*   **Cầu nối (Bridge):** Chuyển tài sản qua lại giữa L1 và Sidechain.
*   **Rủi ro:** Nếu Sidechain sập, tài sản có thể mất (Không thừa hưởng bảo mật của Ethereum như Rollups).

---

## 3. Data Availability (Tính sẵn sàng dữ liệu)

Vấn đề lớn nhất của Scaling là chỗ chứa dữ liệu.
*   **Ethereum Danksharding (EIP-4844):** Tạo ra một loại transaction mới (Blob) rẻ hơn để chứa dữ liệu Rollup -> Phí L2 giảm 10-100 lần.
*   **Modular Blockchain (Celestia):** Tách lớp Data Availability ra khỏi lớp Execution.

### **DA Layers nổi bật**
| Layer | Vai trò | Dự án |
| --- | --- | --- |
| DA-only | Cung cấp blob storage + consensus | Celestia, Avail |
| Validium DA | Lưu dữ liệu off-chain nhưng có committee | zkSync Validium, StarkEx |
| EigenDA | Sử dụng EigenLayer restaked ETH để bảo mật DA | EigenDA |

**Checklist:**
- [ ] Chọn DA layer (Ethereum blob vs Celestia) dựa trên phí/throughput.
- [ ] Plan fallback nếu DA unavailable (freeze rollup?).
- [ ] Monitor blob fee market; auto adjust batch size.

> Xem thêm:
> - [Modular Blockchain](modular-blockchain.md)
> - [Based Rollups](based-rollups.md)
> - [Appchains](appchains.md)
> - [Danksharding & EIP-4844](danksharding.md)

---

## 4. Sharding & Modular Execution

### **A. Danksharding Roadmap**
1. **Proto-danksharding (EIP-4844):** blob tx, giảm phí L2.
2. **Full Danksharding:** 64 data availability shards, proposer-builder separation.

### **B. Execution Sharding**
*   **Near Nightshade:** shard state + dynamic reshard.
*   **Aptos/Sui:** parallel execution (Block-STM) thay vì sharding state.

### **C. Modular Stack Options**
| Layer | Choices |
| Execution | Rollup VM (EVM, zkEVM, zkVM, MoveVM) |
| Settlement | Ethereum, Bitcoin (via rollups), Solana (future) |
| DA | Ethereum blobs, Celestia, EigenDA, Avail |
| Sequencer | Shared (Espresso, Radius) vs app-specific |

---

## 5. Modular Chains & Shared Sequencers

### **Shared Sequencer**
*   Espresso, Radius: cung cấp sequencing service chung → giảm MEV, chống reorg.
*   App-rollup có thể sử dụng shared sequencer + proof post lên L1.

### **Layer3 / App-specific Rollups**
*   Starknet Appchains, Arbitrum Orbit, zkSync Hyperchains.
*   Tùy chỉnh gas token, privacy, riêng tư.

### **Bridging & Interop**
*   **Canonical Bridge:** do rollup dev vận hành (trust-minimized).
*   **General Bridge:** LayerZero, Wormhole → tiện nhưng trust assumptions khác.

---

## 6. Scaling Checklist

- [ ] Xác định requirement (TPS, latency, finality, phí) → chọn stack (Optimistic vs ZK, DA layer).
- [ ] Thiết kế sequencer (centralized → decentralized roadmap) + fallback.
- [ ] Kế hoạch bridging (canonical, message relayer, proof window).
- [ ] Monitoring: batch success rate, blob fee, proof verification time.
- [ ] User experience: instant withdraw (liquidity providers) vs native bridging.

