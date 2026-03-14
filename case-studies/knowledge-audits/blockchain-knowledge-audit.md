# 🔗 Blockchain & Web3 Knowledge Audit: Thử thách "DeFi Protocol Architect"

> **Mục đích:** Đo lường năng lực thiết kế hệ thống phi tập trung, lập trình Smart Contract an toàn, tối ưu hóa kinh tế học token (Tokenomics) và giải quyết các bài toán mở rộng (Scaling).
> **Phiếu trả lời:** [Tải mẫu tại đây](../answer-templates/blockchain-answer-template.md)
> 
> **Kịch bản:** Bạn là **Lead Blockchain Architect** cho "NexusFinance" - một giao thức DeFi đa chuỗi (Multi-chain) kết hợp giữa Sàn giao dịch phi tập trung (DEX), Giao thức cho vay (Lending) và Hệ thống quản trị DAO. Giao thức đang quản lý 1 tỷ USD (TVL) và vừa bị tấn công hụt bởi một hacker mũ trắng.

---

## 🛠️ Thử thách 1: Smart Contract Security & Gas Optimization (An toàn & Hiệu năng)
*Đo lường năng lực lập trình Solidity/Rust và hiểu biết sâu về EVM.*

**Tình huống:** Hàm `withdraw()` trong hợp đồng Lending của NexusFinance đang bị nghi ngờ dính lỗi **Reentrancy**. Đồng thời, chi phí Gas để thực hiện giao dịch đang quá cao khi mạng lưới tắc nghẽn.

**Câu hỏi:**
1.  Bạn sẽ sử dụng kỹ thuật gì để ngăn chặn triệt để lỗi **Reentrancy** (ngoại trừ việc dùng `ReentrancyGuard`)? Giải thích mô hình **Checks-Effects-Interactions**.
2.  Làm thế nào để tối ưu hóa Gas cho một Smart Contract xử lý mảng dữ liệu lớn? (Ví dụ: Sử dụng `uint256` vs `uint8`, kỹ thuật **Bitmasking**, hoặc thay thế `Storage` bằng `Memory/Calldata`).

**Thước đo:**
*   **🟢 Beginner:** Biết viết Smart Contract cơ bản, hiểu Gas là gì nhưng chưa biết tối ưu sâu.
*   **🔴 Expert:** Thành thạo các lỗi bảo mật nâng cao (Flash loan attack, Oracle manipulation), hiểu cách EVM lưu trữ dữ liệu (Slots) để tối ưu Gas ở mức bytecode.

---

## 📉 Thử thách 2: DeFi Mechanics & Oracle Integration (Cơ chế DeFi & Dữ liệu)
*Đo lường tư duy thiết kế sản phẩm tài chính on-chain.*

**Tình huống:** NexusFinance cần tích hợp giá của một Token mới niêm yết. Nếu dùng giá trực tiếp từ một DEX nhỏ, giao thức có nguy cơ bị tấn công thao túng giá (Price Manipulation).

**Câu hỏi:**
1.  Tại sao việc sử dụng giá trực tiếp từ `slot0` của Uniswap V3 lại nguy hiểm? Bạn sẽ chọn giải pháp **Oracle** nào (**Chainlink**, **Pyth**, hay **TWAP**) để đảm bảo an toàn? Tại sao?
2.  Thiết kế cơ chế **Liquidation (Thanh lý)** cho giao thức Lending: Làm thế nào để đảm bảo hệ thống không bị nợ xấu (Bad debt) khi thị trường sụp đổ nhanh (Flash crash)?

**Thước đo:**
*   **🟢 Beginner:** Hiểu Lending/Borrowing cơ bản, biết gọi giá từ Oracle đơn giản.
*   **🔴 Expert:** Thiết kế được hệ thống thanh lý đa tầng, hiểu sâu về **Concentrated Liquidity** và các mô hình **Interest Rate Model** phức tạp.

---

## 🚀 Thử thách 3: Layer 2 Scaling & Bridging (Mở rộng & Cầu nối)
*Đo lường năng lực triển khai hệ thống đa chuỗi.*

**Tình huống:** Người dùng phàn nàn về phí giao dịch trên Ethereum quá đắt. NexusFinance muốn mở rộng sang Layer 2 (L2) và hỗ trợ nạp/rút từ các chuỗi khác như Solana, Avalanche.

**Câu hỏi:**
1.  So sánh **Optimistic Rollups** (Arbitrum/Optimism) và **ZK-Rollups** (ZKSync/Starknet) về tính bảo mật và thời gian rút tiền (Finality). Bạn sẽ chọn cái nào cho NexusFinance?
2.  Rủi ro lớn nhất của các **Cross-chain Bridges** là gì? Làm thế nào để thiết kế một cơ chế chuyển tài sản giữa các chuỗi mà không dựa vào một nhóm validator tập trung (Trustless bridging)?

**Thước đo:**
*   **🟢 Beginner:** Biết cách dùng Bridge để chuyển tiền, hiểu L2 giúp giảm phí.
*   **🔴 Expert:** Hiểu sâu về **Data Availability**, **Fraud Proofs** vs **Validity Proofs**, và các giao thức nhắn tin đa chuỗi như **LayerZero** hoặc **IBC**.

---

## 🧠 Thử thách 4: Tokenomics & Governance (Kinh tế học & Quản trị)
*Đo lường năng lực thiết kế trò chơi kinh tế và quản trị cộng đồng.*

**Tình huống:** Token quản trị của NexusFinance ($NEX) đang bị lạm phát nặng do phần thưởng Yield Farming quá cao. Cộng đồng đang mất niềm tin và giá token giảm 90%.

**Câu hỏi:**
1.  Bạn sẽ đề xuất mô hình Tokenomics mới nào để giảm áp lực bán? (Ví dụ: **veToken model** của Curve, **Burn mechanism**, hay **Real Yield**).
2.  Làm thế nào để ngăn chặn các cuộc tấn công quản trị (**Governance Attack**), nơi một con cá voi (Whale) vay tiền để chiếm quyền biểu quyết nhằm rút cạn quỹ dự phòng (Treasury)?

**Thước đo:**
*   **🟢 Beginner:** Hiểu Supply/Demand cơ bản, biết cách bỏ phiếu trong DAO.
*   **🔴 Expert:** Thiết kế được các vòng lặp khuyến khích (Incentive loops), thành thạo mô hình **Game Theory** trong quản trị (Nash Equilibrium) và các cơ chế **Time-lock**.

---

## 🛡️ Thử thách 5: Advanced Cryptography & Privacy (Mật mã & Riêng tư)
*Đo lường kiến thức về các công nghệ tiên phong (ZK-Proofs).*

**Tình huống:** Một nhóm khách hàng VIP yêu cầu tính năng giao dịch riêng tư, nơi số dư và lịch sử giao dịch của họ không bị công khai hoàn toàn trên explorer nhưng vẫn đảm bảo tính hợp lệ.

**Câu hỏi:**
1.  **Zero-Knowledge Proofs (ZKP)** giải quyết bài toán này như thế nào mà không cần tiết lộ dữ liệu gốc? Phân biệt giữa **zk-SNARKs** và **zk-STARKs**.
2.  Làm thế nào để tích hợp tính năng riêng tư này mà vẫn tuân thủ các quy định về chống rửa tiền (AML/KYC)?

**Thước đo:**
*   **🟢 Beginner:** Nghe nói về ZK, hiểu nó giúp bảo mật hơn.
*   **🔴 Expert:** Hiểu toán học đằng sau ZKP (Polynomials, Elliptic Curves), biết cách triển khai mạch (Circuits) bằng các ngôn ngữ như **Circom** hoặc **Cairo**.

---

## 📊 Bảng tự chấm điểm (Scoring Rubric)

| Lĩnh vực | Thang điểm (1-10) | Gợi ý tự vấn |
| :--- | :---: | :--- |
| **Smart Contract & Security** | ____ / 10 | Bạn có tự tin viết code giữ 1 tỷ USD mà không cần audit không? |
| **DeFi Mechanics** | ____ / 10 | Bạn có hiểu tại sao các giao thức DeFi sụp đổ không? |
| **Scaling & Multi-chain** | ____ / 10 | Bạn có thể giải thích sự khác biệt giữa các L2 cho một CEO không? |
| **Tokenomics & Game Theory** | ____ / 10 | Hệ thống kinh tế bạn thiết kế sẽ tồn tại được bao lâu? |
| **Cryptography (ZK)** | ____ / 10 | Bạn có thể lập trình được một ứng dụng riêng tư không? |

### 🏆 Xếp hạng năng lực Blockchain Dev:
*   **0 - 15 điểm:** **Web3 Explorer**. Cần nắm chắc các khái niệm tại `domains/blockchain/`.
*   **16 - 30 điểm:** **DApp Developer**. Có thể xây dựng sản phẩm, nhưng cần chú trọng bảo mật và kinh tế học.
*   **31 - 45 điểm:** **Web3 Architect**. Đủ năng lực dẫn dắt một dự án DeFi/Infrastructure lớn.
*   **46 - 50 điểm:** **Blockchain Visionary / Security Researcher**. Bạn thuộc top 1% chuyên gia có thể thay đổi cuộc chơi.

---

## 🔑 Answer Key: Góc nhìn Chuyên gia (Expert Guidelines)

### Thử thách 1: Security & Gas
*   **Security:** Luôn dùng mô hình **Checks-Effects-Interactions** (Kiểm tra điều kiện -> Cập nhật trạng thái nội bộ -> Tương tác bên ngoài).
*   **Gas:** Dùng `Calldata` thay cho `Memory` nếu dữ liệu không thay đổi. Pack biến vào các slot 32-byte (ví dụ 2 biến `uint128` chung 1 slot).

### Thử thách 2: DeFi & Oracle
*   **Oracle:** Luôn dùng các Oracle phi tập trung (Decentralized Oracles) như Chainlink. Tránh dùng giá từ Pool DEX đơn lẻ vì dễ bị Flash loan attack làm thay đổi tỷ giá tạm thời.
*   **Liquidation:** Phải có cơ chế thưởng cho người thanh lý (Liquidator) đủ hấp dẫn để họ tự động hóa việc dọn dẹp nợ xấu.

### Thử thách 3: Scaling & Bridges
*   **Scaling:** ZK-Rollups là tương lai của scaling vì tính bảo mật dựa trên toán học (không cần đợi 7 ngày để rút tiền như Optimistic).
*   **Bridge:** Ưu tiên dùng các cầu nối dựa trên **Light Clients** hoặc **ZKP** để giảm thiểu tin tưởng vào bên thứ ba.

### Thử thách 4: Tokenomics
*   **Tokenomics:** Chuyển từ "Farm & Dump" sang "Lock & Governance" (veModel). Token phải có công dụng thực tế trong hệ thống (Utility) thay vì chỉ để đầu cơ.

### Thử thách 5: Cryptography (ZK)
*   **ZKP:** SNARKs nhỏ gọn hơn nhưng cần "Trusted Setup", STARKs lớn hơn nhưng an toàn trước máy tính lượng tử và không cần setup phức tạp.

---

## 🚀 Tài liệu bổ trợ để "Level Up"
*   **Lộ trình kỹ thuật:** [Blockchain Roadmap](../../domains/blockchain/README.md)
*   **Học bảo mật:** [Ethernaut (OpenZeppelin)](https://ethernaut.openzeppelin.com/)
*   **Dữ liệu on-chain:** [Dune Analytics Docs](https://docs.dune.com/)
*   **ZK-Learning:** [ZK-Learning.org](https://zk-learning.org/)
