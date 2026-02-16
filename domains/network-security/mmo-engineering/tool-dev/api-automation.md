# ⚡ API Automation: Tốc độ và Ẩn danh (Level 1)

> [← Back to Network Security](../../README.md)

Khi bạn muốn kiểm tra trạng thái của 10.000 tài khoản, dùng Browser Automation là "chết chắc" (nặng, chậm, dễ crash).
Giải pháp: **API Automation**. Gửi thẳng HTTP Request đến Server. Nhanh gấp 100 lần.

---

## 1. Requests (Thư viện thần thánh)

Cấu hình `requests` cơ bản cho MMO.

### **Session Management (Quan trọng)**
Luôn dùng `requests.Session()` để tự động quản lý Cookies (đăng nhập 1 lần, request sau tự có cookie).

```python
import requests

session = requests.Session()

# 1. Login
login_url = "https://example.com/api/login"
payload = {"username": "user1", "password": "password123"}
response = session.post(login_url, json=payload)

# 2. Check Profile (Cookie đã tự động lưu trong session)
profile_url = "https://example.com/api/profile"
profile_data = session.get(profile_url).json()
print("Hello,", profile_data['name'])
```

---

## 2. Header Analysis (Fake Browser)

Server sẽ biết bạn là Python nếu gửi Request trần trụi.

### **Các Header quan trọng:**
*   **User-Agent:** Fake thành Chrome/Firefox mới nhất.
*   **Referer:** Fake nguồn truy cập (đến từ Google.com, Facebook.com).
*   **Accept-Language:** Fake ngôn ngữ trình duyệt (vi-VN, en-US).
*   **Sec-Ch-Ua:** (Client Hints) Fake thông tin trình duyệt chi tiết hơn (Mobile/Desktop).

```python
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://www.google.com/",
    "Accept-Language": "en-US,en;q=0.9",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors"
}
session.headers.update(headers)
```

---

## 3. Captcha Solving (Giải mã hình ảnh)

Khi gặp Captcha (ReCaptcha, HCaptcha, Cloudflare Turnstile), API bó tay? Không.

### **Giải pháp: Dùng dịch vụ bên thứ 3 (API Service)**
Gửi ảnh/site-key lên Server của họ -> Họ giải giúp -> Trả về Token -> Bạn submit Token.

*   **2Captcha / Anti-Captcha:** Giải mọi loại Captcha.
*   **CapSolver:** Chuyên trị ReCaptcha V2/V3, HCaptcha Enterprise.

```python
# Ví dụ giả tưởng (Pseudo-code)
def solve_recaptcha(site_key, url):
    task_id = api.create_task(site_key, url)
    while True:
        result = api.get_result(task_id)
        if result['status'] == 'ready':
            return result['token']
        time.sleep(1)

token = solve_recaptcha("SITE_KEY_CUA_WEB", "URL_CUA_WEB")
# Submit token này cùng với form login
session.post(login_url, data={"g-recaptcha-response": token, ...})
```

---

## 4. Bỏ qua SSL Verification (Nguy hiểm nhưng cần thiết)

Khi dùng Proxy hoặc bắt gói tin (Sniffing) bằng Charles/Fiddler, bạn cần tắt xác thực SSL.

```python
requests.get("https://example.com", verify=False) # Tắt check chứng chỉ
```
*Lưu ý: Chỉ dùng khi Debug hoặc khi Proxy yêu cầu. Dễ bị lộ data nếu dùng mạng public.*
