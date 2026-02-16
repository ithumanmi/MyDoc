# 🏛️ DAO & Governance: Quản trị Phi tập trung (Level 11)

> [← Back to Blockchain Roadmap](../README.md)

Làm sao để một tổ chức hoạt động mà không có CEO, không có văn phòng?
-> Code là luật (Code is Law).

---

## 1. Các mô hình DAO (Decentralized Autonomous Organization)

### **A. Protocol DAO (DAO Giao thức)**
*   **Ví dụ:** Uniswap, Compound, MakerDAO.
*   **Mục đích:** Quản lý tham số của giao thức (Phí giao dịch, Lãi suất, Hệ số thế chấp).
*   **Quyền lực:** Token Holder (UNI, COMP, MKR) bỏ phiếu để quyết định thay đổi code.

### **B. Investment DAO (DAO Đầu tư)**
*   **Ví dụ:** The LAO, Flamingo DAO.
*   **Mục đích:** Góp vốn chung (Pooling) để đầu tư vào NFT, Startup Crypto.
*   **Lợi nhuận:** Chia lại cho thành viên theo tỷ lệ góp vốn.
*   **Lợi thế:** Tiếp cận các deal lớn (Private Sale) mà cá nhân không mua được.

### **C. Social DAO (DAO Xã hội)**
*   **Ví dụ:** FWB (Friends With Benefits).
*   **Mục đích:** Tạo cộng đồng cùng sở thích (nghệ thuật, âm nhạc).
*   **Quyền lợi:** Phải hold token mới được vào Discord, tham gia sự kiện độc quyền.

---

## 2. Governance Mechanisms (Cơ chế Quản trị)

Một người = Một phiếu? Hay Một Token = Một phiếu?

### **A. Token Weighted Voting (1 Token = 1 Vote)**
*   Phổ biến nhất hiện nay.
*   **Vấn đề:** Cá voi (Whale) nắm quyền kiểm soát tuyệt đối. 1 người giàu = 1000 người nghèo.
*   **Centralization:** Dễ bị tấn công quản trị (Governance Attack) -> Cá voi rút sạch Treasury.

### **B. Quadratic Voting (Bình phương phiếu bầu)**
*   **Cơ chế:** Để có X phiếu, bạn tốn X^2 token. (1 phiếu tốn 1 token, 10 phiếu tốn 100 token).
*   **Kết quả:** Giảm sức mạnh của cá voi. Người giàu vẫn có quyền hơn, nhưng tốn kém hơn nhiều.

### **C. Rage Quit (Moloch DAO)**
*   Nếu bạn không đồng ý với kết quả bỏ phiếu (Ví dụ: DAO quyết định đầu tư vào dự án rác), bạn có quyền **rút vốn ngay lập tức** trước khi quyết định đó được thực thi.
*   Bảo vệ cổ đông thiểu số (Minority Protection).

---

## 3. Treasury Management (Quản lý ngân khố)

DAO thường có một quỹ chung khổng lồ (Treasury). Làm sao để tiêu tiền đúng?

*   **Multi-sig Wallet (Ví đa chữ ký - Gnosis Safe):** Cần 3/5 người ký mới chuyển được tiền đi.
*   **Diversification:** Đừng giữ 100% Treasury bằng token của dự án (vì giá dễ sập). Hãy đổi 1 phần sang Stablecoin (USDC, DAI) để trả lương dev, marketing.
*   **Legal Wrapper (Vỏ bọc pháp lý):** Đăng ký DAO dưới dạng LLC (Wyoming DAO LLC) để đóng thuế, ký hợp đồng với thế giới thực và bảo vệ thành viên khỏi trách nhiệm pháp lý vô hạn.
