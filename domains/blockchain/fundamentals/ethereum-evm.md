# ⛽ Ethereum & EVM: Máy tính Thế giới (Level 2)

> [← Back to Blockchain Roadmap](../README.md)

Bitcoin chỉ là sổ kế toán (A chuyển B 1 BTC).
Ethereum là một máy tính (A chuyển B 1 ETH và chạy một đoạn code).

---

## 1. EVM (Ethereum Virtual Machine)

EVM là "Bộ não" của Ethereum. Nó là một môi trường cách ly (Sandbox) chạy trên hàng nghìn Node.
*   **Chức năng:** Thực thi Smart Contracts (Mã byte code Solidity).
*   **Trạng thái (State):** Ethereum không chỉ lưu số dư (Balance) mà còn lưu toàn bộ trạng thái của các ứng dụng (Storage, Memory).
*   **Tương thích (EVM Compatible):** Nhiều blockchain khác (BNB Chain, Polygon, Avalanche C-Chain) đều dùng lại code EVM -> Dễ dàng port ứng dụng Ethereum sang.

---

## 2. Gas & Transaction Fee (Phí gas)

Mọi thao tác trên Ethereum đều tốn tài nguyên (CPU, RAM). Để tránh Spam, người dùng phải trả phí.

*   **Gas Limit:** Lượng nhiên liệu tối đa bạn cho phép xe chạy (Ví dụ: 21,000 gas cho chuyển ETH đơn giản).
*   **Gas Price (Gwei):** Giá xăng tại thời điểm đó (Ví dụ: 30 Gwei/gas).
*   **Phí giao dịch (Tx Fee):** Gas Limit * Gas Price.

> **Ví dụ:** Chạy Smart Contract tốn 100,000 gas. Giá gas là 50 Gwei.
> Phí = 100,000 * 50 = 5,000,000 Gwei = 0.005 ETH.

---

## 3. Account Types (Các loại tài khoản)

Trên Ethereum có 2 loại địa chỉ:

1.  **EOA (Externally Owned Account):** Tài khoản người dùng (Ví Metamask).
    *   Có Private Key.
    *   Có thể gửi transaction.
    *   Không chứa code.
2.  **Contract Account:** Tài khoản Smart Contract (Uniswap, USDT).
    *   Không có Private Key.
    *   Được điều khiển bởi code bên trong.
    *   Chỉ gửi transaction khi được EOA gọi tới.

---

## 4. Transaction Lifecycle (Vòng đời giao dịch)

Chuyện gì xảy ra khi bạn bấm "Send" trên Metamask?

1.  **Sign:** Ví dùng Private Key ký giao dịch.
2.  **Broadcast:** Gửi Tx đã ký lên mạng lưới (P2P Network).
3.  **Mempool (Memory Pool):** Tx nằm chờ trong hàng đợi của các Miner/Validator. (Ai trả phí cao được ưu tiên).
4.  **Include in Block:** Miner chọn Tx, đóng gói vào Block mới.
5.  **Confirm:** Block được xác thực và thêm vào Blockchain. Trạng thái số dư được cập nhật.
