# 🛡️ Smart Contract Auditing (Level 5)

> [← Back to Blockchain Roadmap](../README.md)

Smart Contract không thể sửa đổi (Immutable). Nếu có lỗi, hàng tỷ USD sẽ bốc hơi.
Auditor là người tìm ra lỗi trước khi Hacker tìm thấy.

---

## 1. Reentrancy (Kinh điển) - Lỗi của The DAO

### **Mô hình tấn công:**
1.  **Hacker:** Gọi hàm `withdraw()` để rút tiền.
2.  **Contract:** Chuyển ETH cho Hacker.
3.  **Hacker (Contract độc hại):** Trong hàm nhận tiền (`fallback()`), gọi lại hàm `withdraw()` của Contract nạn nhân **trước khi** số dư được cập nhật.
4.  **Kết quả:** Rút hết sạch tiền trong Pool.

### **Cách phòng chống:**
*   **Checks-Effects-Interactions:** Luôn cập nhật số dư (Effect) trước khi chuyển tiền (Interaction).
*   **ReentrancyGuard:** Dùng modifier `nonReentrant` của OpenZeppelin.

---

## 2. Overflow/Underflow (Tràn số)

### **Mô hình:**
*   `uint8` chứa tối đa 255. Nếu 255 + 1 -> 0 (Overflow).
*   Nếu 0 - 1 -> 255 (Underflow).
*   **Hacker:** Gửi 0 token nhưng rút được 2^256 token.

### **Cách phòng chống:**
*   Sử dụng thư viện `SafeMath` (OpenZeppelin) cho phiên bản Solidity < 0.8.
*   Solidity >= 0.8 đã tự động check lỗi này (revert transaction).

---

## 3. Front-running (Chạy trước)

### **Mô hình:**
*   **User:** Gửi giao dịch mua Token A giá rẻ lên Mempool.
*   **Bot (MEV):** Nhìn thấy giao dịch ngon ăn -> Tăng Gas Price cao hơn để được Miner xếp trước User.
*   **Kết quả:** Bot mua trước giá rẻ -> Bán lại cho User giá đắt (Sandwich Attack).

### **Cách phòng chống:**
*   **Commit-Reveal Scheme:** Gửi mã Hash cam kết trước, sau đó mới tiết lộ giá trị thật.
*   **Slippage Tolerance:** User chấp nhận trượt giá thấp (0.5%).

---

## 4. Tools & Process (Quy trình Audit)

### **A. Static Analysis (Phân tích tĩnh)**
*   **Slither (Python):** Quét code Solidity tìm các lỗi phổ biến nhanh chóng.
*   **Mythril:** Phân tích tượng trưng (Symbolic Execution) để tìm các đường đi dẫn đến lỗi.

### **B. Fuzz Testing (Test ngẫu nhiên)**
*   **Foundry / Echidna:** Tự động sinh hàng triệu input ngẫu nhiên để crash Contract.

### **C. Formal Verification (Chứng minh toán học)**
*   Chứng minh bằng toán học rằng Contract **không thể sai** theo đặc tả (Spec). Cực khó và tốn kém.
