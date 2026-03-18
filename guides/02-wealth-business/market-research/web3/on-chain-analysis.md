# ⛓️ Web3 & On-Chain Market Analysis: Sự Thật Trần Trụi Trên Chuỗi

> [← Back to Market Research](../../README.md) | [Home](../../../README.md)

Nghiên cứu thị trường ở Web2 (SaaS, Game) là đi mò mẫm trong bóng chập tối, dựa vào số liệu ước tính của bên thứ 3 (Similarweb, SensorTower).

Web3 thì ngược lại: Bật đèn sáng choang giữa quảng trường! **Toàn bộ doanh thu, phí giao dịch, số lượng User thực tế của đối thủ đều phơi bày minh bạch 100% trên Blockchain.** Vấn đề duy nhất: Bạn có biết cách đọc dữ liệu "On-chain" để bóc trần những cú lừa (Fake Volume/Airdrop Bots) hay không.

Đây là framework dùng Số Liệu Thật đập vỡ bánh vẽ Công Nghệ trong ngành Crypto/Web3.

---

## 1. TVL (Total Value Locked): Định Giá "Độ Béo" Của Ngách

Trong DeFi (Tài chính phi tập trung), TVL là tổng số tiền của User đang "Khóa" (gửi/cho vay) vào một giao thức (Protocol) hoặc 1 cái App (Dapp). Nó tương đương với chỉ số AUM (Assets Under Management) của ngân hàng.

**Cách Research (Dùng `DefiLlama.com`):**
1.  Vào DefiLlama, check các danh mục (Categories) như *DEX (Sàn giao dịch), Lending, Liquid Staking, Yield Aggregator*.
2.  **Market Sizing:** Ngách "Lending" đang có 30 Tỷ USD khóa vào. Bạn biết đây là cái hồ nước ngọt khổng lồ.
3.  **Competitor Hunting:** Chọn ngách bạn định build (Ví dụ: Perpetual Trading - Sàn phái sinh). Bạn sẽ thấy bảng xếp hạng *dYdX, GMX, Hyperliquid*. Bạn có thể nhìn rõ đối thủ Top 1 đang giữ bao nhiêu tỷ USD, Top 2 giữ bao nhiêu.

**🔴 Cảnh báo (Ăn Cú Lừa): TVL Bơm Hơi (Double Counting):**
*   Một số Protocol khai khống TVL bằng cách cho vay qua lại các Token rác do chính chúng sinh ra. Hãy filter bằng nút *"Exclude Native Tokens"* hoặc dùng tỷ lệ Market Cap / TVL để xem chúng có đang lừa đảo lấy Mỡ Nó Rán Nó không.

---

## 2. Token Terminal: Ai Đang Thực Sự Sản Sinh Tiền (Revenue)?

Trong thịnh vượng giả tạo, các App Web3 đẻ ra Token lạm phát vô tội vạ để trả thưởng cho User nhằm giữ chân họ. Gọi là "Liquidity Mining". Đó là mô hình Ponzi.

**Nghiên cứu Kinh doanh Thực Thụ (Real Yield):**
1.  Truy cập **`TokenTerminal.com`**
2.  Kiểm tra 2 chỉ số sinh tử:
    *   **Fees (Phí giao dịch):** Tổng số tiền người dùng đã TRẢ THẬT để sử dụng Dapp đó.
    *   **Revenue (Doanh thu Protocol):** Phần trăm từ Phí giao dịch được cất vào két sắt của Công Ty (DAO) hoặc phân chia cho Cổ Đông (Đội ngũ dev/Token Holders).
3.  **Bài kiểm tra:** Rất nhiều sản phẩm gào thét công nghệ cao, vốn hóa 1 tỷ USD, nhưng doanh thu mỗi ngày tạo ra... 50 USD. Bỏ qua! Sớm muộn cũng chìm tàu. Cứ lọc App nào có Fees > Thu nhập in token là sống khỏe vững chắc như làm SaaS.

---

## 3. Dune Analytics: Truy Vết Bầy Đàn User & Bot

Người dùng (DAU/MAU) trên Google Analytics thì dễ đo. Trên Blockchain, 1 người (Sybil attacker) có thể chạy 1.000 cái Ví phụ (Wallets) bằng Code để nhận Tiền Thưởng Airdrop. Lấy đó làm KPI báo cáo Quỹ đầu tư.

**Làm sao lật tẩy Bot:**
1.  **`Dune.com`** là thư viện các Dashboard phân tích dữ liệu on-chain do Data Analysts toàn cầu code bằng SQL mở.
2.  **Khám nghiệm Tử thư:** Gõ tên sàn đối thủ lên thanh Tìm kiếm. Tìm các Dashboard có tính năng: `Retroactive / Sybil detection / Real Users`.
3.  **Hành vi thật:** Số ví tương tác chỉ MỘT LẦN DUY NHẤT chiếm 80% (Dấu hiệu User bào Airdrop nhận thưởng rồi vứt rác). Số ví giao dịch ĐỀU ĐẶN hơn 6 tháng bất chấp thị trường sập chiếm 10-20% (Đây chính là ICP - Tệp khách hàng mục tiêu để bạn nghiên cứu cách cướp (vampire attack) khách của họ).

---

## 4. Tokenomics (Đừng Trở Thành Thanh Khoản Cho Tụi VC)

Nếu bạn làm Founder một dự án Web3, bạn sẽ phải ra Token. Tham khảo lịch Mở Khóa Cổ Phần (Vesting/Unlock) của đối thủ quyết định bạn nên build cấu trúc nào.

**Cách Cào Data (Dùng `Token.unlocks.app`):**
1.  Nghiên cứu bánh vẽ (Pie Chart): Thường 20% cho Team, 20% cho Quỹ Đầu Tư (VC), 40% cho Cộng đồng, v.v..
2.  **Vực Thẳm (The Cliff)**: Khác biệt nhất là mốc TGE (Sàn). Thường Dev và VC bị khóa Token 1 năm đầu (Tạo ra mảng mầu hồng lừa đảo User). Bắt đầu đầu năm 2, Đội ngũ bắt đầu được Unlock hàng trăm triệu Token để Xả Lên Đầu Người Dùng (Thu lại vốn). Mốc Vực thẳm Giá - Khủng Hảng Tài Chính (Dump).
3.  Học cách làm cấu trúc lạm phát (Emission) và Burn/Buyback (Đốt Lọc) để mô hình có tính Bền Vững (Sustainable). Cấm copy các mô hình có FDV (Định giá pha loãng hoàn toàn) ảo gấp 10 lần MvC (Vốn hoá trôi nổi thực).

> **Lời Kết:** Làm Web3 dễ ở việc "Gây vốn bằng ý chí", khó nhưng RẤT DỄ ở việc Nghiên Cứu. Bạn không còn phải mông lung đi tìm Báo cáo Tài Chính của Đối thủ bằng giấy tờ mờ ám. Tất cả dữ kiện đều chạy trần truồng 24/7 trên On-Chain. Chỉ cần dùng 4 Tools trên là gỡ bung được mọi chiêu trò.
