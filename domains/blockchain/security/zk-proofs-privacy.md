# 🔐 Privacy & Advanced Cryptography: Bảo vệ sự riêng tư (Level 10)

> [← Back to Blockchain Roadmap](../README.md)

Blockchain mặc định là công khai (Public). Ai cũng biết bạn có bao nhiêu tiền.
ZK-Proof sinh ra để giải quyết vấn đề này: Chứng minh bạn đúng mà không cần lộ thông tin.

---

## 1. Zero-Knowledge Proofs (Bằng chứng không kiến thức)

**Bài toán Alibaba:** Ali Baba muốn chứng minh với tên trộm là mình biết mật khẩu mở cửa hang, nhưng không muốn đọc mật khẩu ra.
-> Ali đi vào hang, lấy một vật phẩm ra -> Chứng minh được mình vào được hang (biết mật khẩu) mà tên trộm vẫn không biết mật khẩu là gì.

### **A. zk-SNARKs (Ngắn gọn, Không tương tác)**
*   **Dùng trong:** Zcash, Tornado Cash, zkSync.
*   **Ưu điểm:** Kích thước bằng chứng cực nhỏ (vài trăm byte) -> Xác thực cực nhanh.
*   **Nhược điểm:** Cần Trusted Setup (Lễ thiết lập tin cậy). Nếu khóa bí mật bị lộ lúc tạo -> Hệ thống sập.

### **B. zk-STARKs (Minh bạch, Kháng lượng tử)**
*   **Dùng trong:** Starknet, dYdX.
*   **Ưu điểm:** Không cần Trusted Setup. An toàn trước máy tính lượng tử.
*   **Nhược điểm:** Kích thước bằng chứng lớn hơn SNARKs -> Tốn gas hơn.

---

## 2. Privacy Coins & Mixers (Tiền ẩn danh & Máy trộn)

### **A. Monero (XMR)**
*   Ẩn danh hoàn toàn người gửi, người nhận và số tiền. (Dùng Ring Signature).
*   Là đồng tiền ưa thích của Dark Web. Các sàn CEX (Binance) thường delist vì áp lực pháp lý.

### **B. Tornado Cash (Mixer trên Ethereum)**
*   **Cơ chế:**
    1.  Gửi 1 ETH vào bể chung (Pool). Nhận về một tờ giấy nốt (Note).
    2.  Chờ đợi (để lẫn với tiền người khác).
    3.  Dùng Note để rút 1 ETH ra ở một địa chỉ ví mới tinh.
    4.  Không ai biết ví mới đó liên quan đến ví cũ (đứt mạch on-chain).
*   **ZK-Proof:** Dùng để chứng minh "Tôi có Note hợp lệ" mà không cần lộ Note đó là cái nào (để tránh bị truy vết ngược lại lúc gửi).

---

## 3. Decentralized Identity (DID) - Danh tính số

Chứng minh bạn > 18 tuổi để vào web 18+ mà không cần upload CCCD?
-> Dùng ZK-Proof.

1.  Cơ quan cấp ID (Chính phủ) ký xác nhận vào ví bạn: "Ông này sinh năm 2000".
2.  Bạn tạo bằng chứng ZK: "Tôi có chữ ký của Chính phủ xác nhận năm sinh < 2006".
3.  Website verify bằng chứng -> Cho vào. Website không hề biết bạn tên gì, nhà ở đâu.
