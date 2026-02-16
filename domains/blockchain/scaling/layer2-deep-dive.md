# 📈 Layer 2 Scaling: Mở rộng quy mô Blockchain (Deep Dive)

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
