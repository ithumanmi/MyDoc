# 🐍 Python for MMO: Nền tảng Kỹ thuật

> [← Back to Network Security](../../README.md)

Để xây dựng Tool MMO "trăm trận trăm thắng", bạn cần một nền tảng Python vững chắc. Code chạy được là chưa đủ, nó phải chạy nhanh, ổn định và dễ quản lý.

---

## 1. Môi trường & Quản lý Dự án (Project Setup)

Đừng cài thư viện lung tung vào máy. Hãy dùng Virtual Environment.

### **A. Virtual Environment (`venv`)**
Giúp cách ly thư viện của từng dự án. Tool A dùng `selenium==4.0`, Tool B dùng `selenium==3.0` mà không đánh nhau.

```bash
# Tạo môi trường ảo
python -m venv venv

# Kích hoạt (Windows)
venv\Scripts\activate

# Cài đặt thư viện
pip install requests selenium
```

### **B. Cấu trúc thư mục chuẩn**
Một dự án Tool chuyên nghiệp nên trông như thế này:

```text
MyMMOTool/
│
├── data/               # Chứa file dữ liệu (accounts.txt, proxies.txt)
├── logs/               # Chứa file log lỗi (error.log)
├── src/                # Source code chính
│   ├── modules/        # Các module chức năng (login, farming, captcha)
│   ├── utils/          # Các hàm tiện ích (random_sleep, read_file)
│   └── main.py         # File chạy chính
├── requirements.txt    # Danh sách thư viện (pip freeze > requirements.txt)
└── config.json         # Cấu hình tool (số luồng, delay)
```

---

## 2. Xử lý Dữ liệu (Data Handling)

MMO là cuộc chơi của dữ liệu lớn (Big Data). Bạn cần quản lý hàng nghìn account.

### **A. Đọc/Ghi File**
*   **TXT:** Dùng cho list đơn giản (Proxy, User-Agent).
*   **CSV:** Dùng cho dữ liệu dạng bảng (User, Pass, Email, 2FA).
*   **JSON:** Dùng cho cấu hình hoặc dữ liệu phức tạp (Cookies, LocalStorage).

```python
import json

# Đọc Cookie từ file JSON
def load_cookies(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)
```

---

## 3. Đa luồng (Multithreading)

Chạy 1 luồng (Single-thread) thì bao giờ mới giàu? Hãy chạy 100 luồng.

### **Threading vs Multiprocessing**
*   **Threading:** Tốt cho I/O Bound (Chờ mạng, chờ Proxy). Tool MMO chủ yếu dùng cái này.
*   **Multiprocessing:** Tốt cho CPU Bound (Giải mã ảnh, xử lý video). Nặng máy hơn.

```python
import threading
import time

def worker(account):
    print(f"Đang chạy acc: {account}")
    time.sleep(2)

accounts = ["Acc1", "Acc2", "Acc3", "Acc4"]
threads = []

for acc in accounts:
    t = threading.Thread(target=worker, args=(acc,))
    threads.append(t)
    t.start()

# Chờ tất cả luồng chạy xong
for t in threads:
    t.join()
```

---

## 4. Error Handling (Xử lý Lỗi)

Mạng rớt, Proxy chết, Web đổi giao diện... Tool phải sống sót qua tất cả.

### **Try-Except-Else-Finally**
Luôn bọc các đoạn code mạng (Requests, Selenium) trong `try-except`.

```python
import requests

def check_proxy(proxy):
    try:
        response = requests.get("http://ip-api.com/json", proxies={"http": proxy, "https": proxy}, timeout=5)
        response.raise_for_status() # Báo lỗi nếu status code != 200
        print("Proxy Live:", response.json()['query'])
    except requests.exceptions.Timeout:
        print("Proxy Timeout (Quá chậm)")
    except requests.exceptions.RequestException as e:
        print(f"Proxy Die: {e}")
```

---

## 5. Logger (Ghi nhật ký)

Thay vì `print()`, hãy dùng `logging`.
*   Ghi lại lỗi vào file để debug sau.
*   Biết được Tool chết lúc mấy giờ, tại sao.
