# 🎲 Procedural Generation: Thế giới vô tận (Level 10)

> [← Back to Game Development Roadmap](../README.md)

Làm sao Minecraft tạo ra thế giới rộng gấp 8 lần Trái Đất? Làm sao No Man's Sky tạo ra 18 tỷ tỷ hành tinh?
Họ không vẽ tay. Họ dùng thuật toán **PCG (Procedural Content Generation)**.

---

## 1. Noise Algorithms (Thuật toán Nhiễu)

Để tạo địa hình tự nhiên (núi non, sông ngòi), bạn không thể dùng hàm `Random()` (nó quá hỗn loạn). Bạn cần **Coherent Noise** (Nhiễu có tính liên kết).

### **A. Perlin Noise**
*   Tạo ra các giá trị ngẫu nhiên nhưng mượt mà (Smooth).
*   **Ứng dụng:** Độ cao của núi, hình dáng đám mây, vân gỗ.

### **B. Simplex Noise**
*   Phiên bản nâng cấp của Perlin Noise.
*   Nhanh hơn, ít bị lỗi artifact hơn ở không gian chiều cao.

---

## 2. Cellular Automata (Máy tế bào)

Thuật toán mô phỏng sự sống đơn giản.

### **Ứng dụng: Tạo hang động (Caves)**
1.  Khởi tạo một bản đồ ngẫu nhiên (các ô Đất và Đá).
2.  **Quy tắc:** Nếu một ô Đá có quá ít hàng xóm là Đá -> Biến thành Đất (Chết). Nếu một ô Đất có nhiều hàng xóm là Đá -> Biến thành Đá (Sinh sôi).
3.  Lặp lại quy trình này vài lần -> Các ô Đá sẽ tụ lại thành mảng lớn, tạo ra hang động tự nhiên.

---

## 3. Wave Function Collapse (WFC)

Thuật toán "ma thuật" để tạo kiến trúc (Dungeon, Thành phố).

### **Cơ chế:**
1.  Định nghĩa các mảnh ghép (Tiles) và quy tắc nối (Ví dụ: Mảnh "Đường thẳng" chỉ nối được với "Đường thẳng" hoặc "Ngã tư", không nối được với "Tường").
2.  Bắt đầu với trạng thái "mọi ô có thể là bất cứ thứ gì" (Superposition).
3.  Chọn một ô, gán cho nó một mảnh ghép cụ thể (Collapse).
4.  Lan truyền sự thay đổi (Propagate): Các ô xung quanh bị giới hạn lại theo quy tắc.
5.  Lặp lại cho đến khi toàn bộ bản đồ được điền kín.

---

## 4. L-Systems (Lindenmayer Systems)

Tạo cây cối và thực vật.
*   Dùng các quy tắc thay thế chuỗi ký tự (String Rewriting) để mô phỏng sự phát triển của cành cây.
*   Ví dụ: `F -> F[+F]F[-F]` (Thân cây đẻ ra 2 nhánh con).
