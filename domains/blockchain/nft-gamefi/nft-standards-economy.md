# 🎮 NFT, GameFi & Metaverse (Level 9)

> [← Back to Blockchain Roadmap](../README.md)

GameFi đã biến chơi game thành một nghề nghiệp (Play-to-Earn). Nhưng nếu không hiểu Tokenomics, bạn chỉ là "người chơi bị xả lên đầu".

---

## 1. NFT Standards (Tiêu chuẩn NFT)

NFT không chỉ là ảnh JPEG đắt tiền. Nó là chứng nhận sở hữu số.

### **A. ERC-721 (Chuẩn cơ bản)**
*   Mỗi Token là duy nhất (ID khác nhau).
*   Ví dụ: Bored Ape Yacht Club, CryptoPunks.
*   **Nhược điểm:** Tốn gas nếu mint số lượng lớn (Batch Minting).

### **B. ERC-721A (Azuki sáng tạo)**
*   Tối ưu gas cực tốt cho Batch Minting. Mint 10 NFT tốn gas gần bằng mint 1 NFT.
*   Lưu trữ dữ liệu thông minh hơn trên Blockchain.

### **C. ERC-1155 (Đa Token)**
*   Kết hợp cả Fungible (Vàng, Gỗ) và Non-Fungible (Kiếm thần, Áo giáp) trong cùng một Contract.
*   Tiết kiệm gas cực lớn cho Game. Chuyển 100 loại vật phẩm khác nhau chỉ trong 1 giao dịch.

### **D. Soulbound Token (SBT)**
*   NFT không thể chuyển nhượng (Non-transferable).
*   Gắn liền với ví (Soul). Dùng làm Bằng đại học, Chứng minh thư, Điểm tín dụng on-chain.

---

## 2. GameFi Economy (Kinh tế trong Game)

Làm sao để Game tồn tại lâu dài mà không lạm phát (Hyperinflation)?

### **A. Dual Token Model (Mô hình 2 Token)**
*   **Governance Token (AXS):** Số lượng có hạn. Dùng để biểu quyết, Staking. Giá trị tăng theo sự phát triển của Game.
*   **Utility Token (SLP):** Số lượng vô hạn (Mint ra khi chơi). Dùng để nâng cấp, sinh sản (Breed).
*   **Vấn đề:** Nếu người chơi chỉ bán SLP lấy tiền -> Lạm phát -> Giá SLP về 0 -> Game chết (Death Spiral).

### **B. Play-and-Earn (Chơi và Kiếm)**
*   Tập trung vào trải nghiệm Game (Fun first). Kiếm tiền chỉ là phần thưởng phụ.
*   Thu hút người chơi thật (Gamers), không chỉ là nhà đầu cơ (Speculators).
*   **NFT Sink:** Cơ chế đốt NFT (Ghép thẻ, Nâng cấp rủi ro xịt) để giảm nguồn cung.

---

## 3. Metaverse Infrastructure (Hạ tầng vũ trụ ảo)

Không phải Game 3D nào cũng là Metaverse. Metaverse phải có tính mở (Open) và sở hữu thực sự.

*   **Land (Đất ảo):** NFT đại diện cho tọa độ trong thế giới ảo (Decentraland, Sandbox).
*   **Avatar:** NFT đại diện cho nhân dạng (Identity) của bạn.
*   **Interoperability:** Mang cây kiếm từ Game A sang Game B dùng được. (Chưa làm được).
