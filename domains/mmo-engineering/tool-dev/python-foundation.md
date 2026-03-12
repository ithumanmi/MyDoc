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

```python
import logging

logger = logging.getLogger("mmo_tool")
logger.setLevel(logging.INFO)

handler = logging.FileHandler("logs/tool.log", encoding="utf-8")
handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(handler)

logger.info("Tool started")
```

---

## 6. Anti-Detect Integration (Browser Automation)

### **A. Profile Management (GoLogin/Multilogin API)**

Ví dụ mở 1 profile và kết nối WebDriver:

```python
import requests
from selenium import webdriver

token = "YOUR_GOLOGIN_TOKEN"
profile_id = "xxx-yyy"

resp = requests.get(
    f"https://api.gologin.com/browser/{profile_id}/start",
    headers={"Authorization": f"Bearer {token}"}
)
resp.raise_for_status()
ws_url = resp.json()["wsUrl"]

options = webdriver.ChromeOptions()
options.add_argument("--remote-debugging-port=9222")

driver = webdriver.Remote(command_executor=ws_url, options=options)
driver.get("https://www.facebook.com")
```

### **B. Switch Fingerprint & Proxy Per Profile**
- Mỗi profile có cấu hình proxy riêng -> luôn đồng bộ danh sách proxy/port.
- Khi cần đổi fingerprint, clone profile và cập nhật hardware params (canvas, WebGL) từ API thay vì đổi trực tiếp.

### **C. Stealth Automation Patterns**
- Sử dụng thư viện `undetected-chromedriver` hoặc plugin stealth để giảm dấu hiệu automation.
- Thêm hành vi người dùng: random mouse movement, scroll, typing delay.

```python
import undetected_chromedriver as uc
from helpers.human import random_mouse_move, random_sleep

driver = uc.Chrome(headless=False)
driver.get("https://adsmanager.facebook.com")
random_mouse_move(driver, area=(100, 200))
random_sleep(2, 5)
```

---

## 7. Practical Lab Scripts

### **Lab 1: 4G Proxy Farm – Reset IP via AT Command**

```python
import serial
import time

def reset_dongle(port: str):
    with serial.Serial(port, baudrate=115200, timeout=1) as modem:
        modem.write(b"AT+CFUN=0\r")  # tắt radio
        time.sleep(2)
        modem.write(b"AT+CFUN=1\r")  # bật lại
        time.sleep(10)
        modem.write(b"AT+CGATT?\r")
        print(modem.read_all())

if __name__ == "__main__":
    for port in ["COM5", "COM6", "COM7"]:
        reset_dongle(port)
```

> ⚠️ Cần quyền admin và đảm bảo thiết bị hỗ trợ AT Command.

### **Lab 2: Wallet Batch Signer (Web3.py)**

```python
from web3 import Web3
import json

w3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth"))

with open("data/wallets.json", "r", encoding="utf-8") as f:
    wallets = json.load(f)

tx = {
    "to": "0xRecipient",
    "value": w3.to_wei(0.01, "ether"),
    "gas": 21000,
    "gasPrice": w3.to_wei(20, "gwei"),
    "nonce": None,
    "chainId": 1,
}

for wallet in wallets:
    account = w3.eth.account.from_key(wallet["private_key"])
    tx["nonce"] = w3.eth.get_transaction_count(account.address)
    signed = account.sign_transaction(tx)
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    print(account.address, tx_hash.hex())
```

### **Lab 3: Anti-Detect Health Check**

```python
import requests

def fingerprint_score(profile_id, token):
    resp = requests.get(
        f"https://api.gologin.com/browser/{profile_id}",
        headers={"Authorization": f"Bearer {token}"},
        timeout=10
    )
    resp.raise_for_status()
    data = resp.json()
    return {
        "canvas": data["webGLMetadata"],
        "fonts": len(data.get("fonts", [])),
        "proxy": data.get("proxy", {}).get("type"),
    }

profiles = ["profileA", "profileB"]
for pid in profiles:
    print(pid, fingerprint_score(pid, token))
```

> Lưu kết quả vào file để tạo dashboard theo dõi chất lượng profile.

---

## 8. Deployment & Distribution
- Đóng gói tool bằng `PyInstaller` hoặc `briefcase` để gửi team vận hành.
- Tích hợp auto-update (pull script từ repo private) và license check nếu bán tool.
- Document SOP: cách chạy, yêu cầu proxy, xử lý lỗi.
