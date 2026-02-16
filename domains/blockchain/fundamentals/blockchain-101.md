# 🔗 Blockchain 101: Nền tảng cốt lõi

> [← Back to Blockchain Roadmap](../README.md)

Trước khi học code, hãy hiểu bản chất. Đừng bắt đầu với Token, hãy bắt đầu với **Distributed Ledger (Sổ cái phân tán)**.

---

## 1. Bản chất của Blockchain

Blockchain = **Block (Khối)** + **Chain (Chuỗi)**.
Nó là một cơ sở dữ liệu (Database) đặc biệt:
*   **Decentralized (Phi tập trung):** Không có server trung tâm (như Google/Facebook). Dữ liệu được lưu trên hàng nghìn máy tính (Node).
*   **Immutable (Bất biến):** Dữ liệu đã ghi vào thì không thể sửa/xóa. (Muốn sửa phải hack >51% mạng lưới).
*   **Transparent (Minh bạch):** Ai cũng có thể kiểm tra lịch sử giao dịch (nhưng danh tính được ẩn danh).

---

## 2. Cấu trúc một Block (Block Structure)

Mỗi khối giống như một trang trong cuốn sổ kế toán. Nó chứa:
1.  **Block Header:**
    *   *Parent Hash:* Mã băm của khối trước (liên kết chuỗi).
    *   *Timestamp:* Thời gian tạo khối.
    *   *Nonce:* Số ngẫu nhiên để giải thuật toán đào (PoW).
    *   *Merkle Root:* Mã băm tóm tắt tất cả giao dịch trong khối.
2.  **Block Body:** Danh sách các giao dịch (Tx).

---

## 3. Consensus Mechanisms (Cơ chế đồng thuận)

Làm sao hàng nghìn máy tính (Node) không quen biết nhau lại thống nhất được cuốn sổ cái là đúng? -> **Consensus**.

### **A. Proof of Work (PoW) - Bitcoin**
*   **Cơ chế:** Các thợ đào (Miner) đua nhau giải bài toán toán học khó (tìm Nonce). Ai giải ra trước được quyền ghi khối mới và nhận thưởng (BTC).
*   **Ưu điểm:** Bảo mật cực cao (cần tốn điện/phần cứng khủng mới tấn công được).
*   **Nhược điểm:** Tốn điện, chậm (Bitcoin ~7 TPS).

### **B. Proof of Stake (PoS) - Ethereum 2.0, Solana**
*   **Cơ chế:** Người tham gia (Validator) đặt cọc (Stake) coin của mình (ETH, SOL). Ai đặt cọc nhiều/lâu hơn có xác suất được chọn để ghi khối cao hơn. Nếu gian lận -> Mất tiền cọc (Slashing).
*   **Ưu điểm:** Tiết kiệm điện, nhanh hơn (Ethereum ~15 TPS, Solana ~65k TPS).
*   **Nhược điểm:** Giàu càng giàu thêm (Centralization risk).

---

## 4. Cryptography (Mật mã học)

Blockchain được xây dựng trên toán học, không phải niềm tin.

### **A. Hash Function (Hàm băm - SHA256, Keccak256)**
*   Biến dữ liệu đầu vào bất kỳ thành một chuỗi ký tự cố định (Hash).
*   *Tính chất 1 chiều:* Không thể suy ngược từ Hash ra dữ liệu gốc.
*   *Tính chất nhạy cảm:* Thay đổi 1 dấu chấm -> Hash thay đổi hoàn toàn (Avalanche effect).

### **B. Public/Private Key (Khóa công khai/bí mật)**
*   **Private Key:** Chìa khóa két sắt (Tuyệt đối giữ bí mật). Dùng để **Ký (Sign)** giao dịch.
*   **Public Key:** Số tài khoản ngân hàng (Công khai). Dùng để nhận tiền và **Xác minh (Verify)** chữ ký.
*   **Digital Signature (Chữ ký số):** Đảm bảo giao dịch thực sự do chủ sở hữu Private Key tạo ra mà không làm lộ Private Key.
