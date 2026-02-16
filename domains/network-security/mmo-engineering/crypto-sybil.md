# 💰 Crypto Airdrop & Sybil Attack Strategies

> [← Back to Network Security](../README.md)

"Làm Airdrop là cuộc đua giữa Thợ săn (Hunter) và Dự án (Project). Bạn cheat, họ bắt. Ai thông minh hơn người đó thắng."

---

## 1. Sybil Attack là gì?

*   **Định nghĩa:** Một người tạo ra hàng trăm, hàng nghìn danh tính giả (Ví Crypto) để thao túng hệ thống hoặc nhận thưởng nhiều lần.
*   **Mục tiêu:** Thay vì nhận 1 suất Airdrop (1.000$), bạn muốn nhận 100 suất (100.000$).

---

## 2. On-chain Footprint (Dấu vết trên chuỗi)

Blockchain là sổ cái công khai. Mọi hành động của bạn đều được lưu lại vĩnh viễn. Các dự án dùng Data Analysis để phát hiện Sybil.

### **Các lỗi chết người (Red Flags):**
1.  **Liên kết ví (Funding Link):**
    *   Ví chính (A) chuyển tiền (Gas fee) cho 100 ví con (B1...B100).
    *   -> **CỤM VÍ (Cluster) phát hiện ngay lập tức.** Toàn bộ 100 ví bị loại.
2.  **Hành động đồng loạt (Timing Analysis):**
    *   100 ví cùng Swap lệnh lúc 10:00:01.
    *   -> Bot làm. Bị loại.
3.  **Số tiền giống hệt nhau:**
    *   Cả 100 ví đều nạp đúng 0.1 ETH.

---

## 3. Chiến lược Sybil Chuyên nghiệp (Anti-Sybil)

### **A. Nguồn tiền sạch (Funding Source)**
*   **Cách làm đúng:** Rút tiền từ CEX (Binance, OKX, Bybit) về từng ví con.
*   **Tại sao:** Sàn CEX dùng ví tổng (Hot Wallet) để chuyển tiền. Dự án không thể biết ví con A và ví con B có cùng chủ sở hữu không (vì cả 2 đều nhận tiền từ ví tổng Binance).
*   *Lưu ý:* Mỗi lần rút một số tiền lẻ ngẫu nhiên (0.12, 0.09, 0.15...).

### **B. Gom tiền về (Consolidation)**
*   **Tuyệt đối KHÔNG:** Gom tiền từ 100 ví con về lại 1 ví chính trực tiếp.
*   **Giải pháp:** Nạp ngược lên sàn CEX (mỗi ví con có một địa chỉ nạp riêng trên sàn - Sub-account Deposit Address).

### **C. Randomize Everything (Ngẫu nhiên hóa)**
*   **Thời gian:** Không làm tất cả trong 1 ngày. Chia ra làm trong 1 tuần.
*   **Volume:** Ví này swap 100$, ví kia swap 500$.
*   **Hành trình:** Ví A: Swap -> Bridge -> NFT. Ví B: NFT -> Bridge -> Swap.

---

## 4. Wallet Management (Quản lý Ví)

Khi có 1000 ví, bạn không thể dùng Metamask thông thường.

*   **Excel/Google Sheets:** (Rủi ro cao).
*   **Script quản lý:** Code Python/Node.js để tự động ký giao dịch (Sign Transaction) bằng Private Key.
*   **Bảo mật:**
    *   Mã hóa file chứa Private Key (AES-256).
    *   Không bao giờ để lộ file này lên mạng/cloud.
    *   Tốt nhất chạy trên máy Offline hoặc VPS riêng.

> **Đạo đức nghề nghiệp:** Sybil Attack làm hỏng hệ sinh thái. Hãy cân nhắc kỹ. Nhiều dự án hiện nay yêu cầu KYC (xác thực khuôn mặt) để chống Sybil triệt để.
