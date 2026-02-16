# ⚔️ Red Team Lab: SQL Injection (SQLi)

> [← Back to Network Security](../README.md)

"SQL Injection is the cockroach of the internet." - Không thể diệt tận gốc vì developer lười.
Đây là kỹ thuật tấn công phổ biến nhất để đánh cắp dữ liệu.

---

## 1. Cơ chế hoạt động

Hacker lợi dụng việc ứng dụng ghép chuỗi (concatenation) trực tiếp từ input người dùng vào câu lệnh SQL mà không qua bộ lọc.

### **Ví dụ Code Lỗi (PHP):**
```php
$username = $_POST['username'];
$password = $_POST['password'];

// ❌ SAI: Nối chuỗi trực tiếp
$sql = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
```

### **Tấn công (Authentication Bypass):**
Nếu Hacker nhập Username là: `admin' --` (Dấu `--` trong SQL là comment, bỏ qua phần sau).

Câu lệnh trở thành:
```sql
SELECT * FROM users WHERE username = 'admin' --' AND password = '...'
```
-> Database chỉ chạy đoạn `WHERE username = 'admin'`. Phần check password bị biến thành comment.
-> **Kết quả:** Đăng nhập thành công vào tài khoản Admin mà không cần mật khẩu!

---

## 2. Lab thực hành (Giả lập)

### **Mục tiêu:**
Lấy danh sách toàn bộ user trong bảng `users` dù chỉ có quyền xem profile của mình.

### **Kịch bản:**
URL: `http://vulnerable-site.com/profile.php?id=1`
Query backend: `SELECT username, email FROM users WHERE id = 1`

### **Bước 1: Kiểm tra lỗi (Fuzzing)**
Thử thêm dấu nháy đơn `'` vào cuối URL: `?id=1'`
-> Nếu web báo lỗi SQL Syntax Error -> **Có khả năng dính lỗi!**

### **Bước 2: Xác định số cột (ORDER BY)**
Hacker cần biết câu lệnh `SELECT` lấy ra bao nhiêu cột để dùng `UNION`.
*   Thử: `?id=1 ORDER BY 1` (Chạy OK)
*   Thử: `?id=1 ORDER BY 2` (Chạy OK)
*   Thử: `?id=1 ORDER BY 3` (Báo lỗi "Unknown column 3")
-> **Kết luận:** Câu lệnh SELECT lấy ra 2 cột.

### **Bước 3: UNION Attack (Lấy dữ liệu)**
Dùng `UNION SELECT` để ghép thêm kết quả từ bảng khác.
*   Payload: `?id=-1 UNION SELECT database(), user()`
    *   `id=-1`: Để query gốc không trả về gì cả (False).
    *   `UNION SELECT ...`: Để hiển thị dữ liệu chúng ta muốn.
-> **Kết quả trên màn hình:** Thay vì hiện profile user 1, nó hiện Tên Database và User đang chạy DB.

### **Bước 4: Dump toàn bộ User**
*   Payload: `?id=-1 UNION SELECT username, password FROM users`
-> **Kết quả:** Web hiện ra danh sách toàn bộ username và password (thường là hash).

---

## 3. 🛡️ Blue Team Defense (Phòng thủ)

Cách duy nhất để chặn SQLi triệt để là dùng **Prepared Statements** (Parameterized Queries).
Database sẽ coi input của người dùng là **Dữ liệu (Data)** chứ không phải **Mã lệnh (Code)**.

### **Code sửa lỗi (PHP PDO):**
```php
$username = $_POST['username'];
$password = $_POST['password'];

// ✅ ĐÚNG: Dùng Placeholder (?)
$stmt = $pdo->prepare('SELECT * FROM users WHERE username = ? AND password = ?');
$stmt->execute([$username, $password]);
$user = $stmt->fetch();
```

### **Code sửa lỗi (Node.js / TypeORM):**
```typescript
// ✅ ĐÚNG: TypeORM tự động escape
const user = await userRepository.findOne({ 
    where: { username: req.body.username } 
});
```

> **Ghi nhớ:** "Never trust user input." (Không bao giờ tin tưởng dữ liệu người dùng nhập vào).
