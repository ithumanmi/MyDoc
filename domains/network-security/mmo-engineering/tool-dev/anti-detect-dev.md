# 🕵️ Anti-Detect Deep Dive: Nghệ thuật Ẩn danh (Level 5)

> [← Back to Network Security](../../README.md)

Làm sao để 100 cái trình duyệt trên cùng 1 máy tính trông như 100 máy tính khác nhau? Đó là Anti-Detect Browser.

---

## 1. Browser Fingerprint (Dấu vân tay số)

Các trang web lớn (Google, Facebook, Amazon) không chỉ check IP. Họ check hàng trăm thông số phần cứng/phần mềm để tạo ra một ID duy nhất cho thiết bị của bạn.

### **Các thông số quan trọng cần Fake:**

1.  **Canvas Fingerprint:** Vẽ một hình ảnh ẩn bằng HTML5 Canvas -> Mỗi card đồ họa vẽ khác nhau -> Hash ảnh -> ID độc nhất.
    *   *Cách Fake:* Thêm nhiễu (Noise) vào dữ liệu pixel trước khi trả về.
2.  **WebGL:** Tương tự Canvas nhưng dùng GPU 3D. Cần fake `Vendor` (NVIDIA/AMD) và `Renderer` (RTX 3060/RX 580).
3.  **AudioContext:** Tạo sóng âm thanh ẩn -> Mỗi driver âm thanh xử lý khác nhau -> ID độc nhất.
    *   *Cách Fake:* Thêm nhiễu vào tần số âm thanh.
4.  **Font Enumeration:** Danh sách font chữ đã cài trên máy. (Windows cài font khác Mac, Linux).
5.  **WebRTC:** Lộ IP thật (Real IP) dù bạn đang dùng Proxy/VPN.
    *   *Cách Fake:* Disable WebRTC hoặc hook API để trả về IP của Proxy.

---

## 2. Chrome DevTools Protocol (CDP)

Selenium/Puppeteer đều điều khiển Chrome qua giao thức này. Bạn có thể dùng CDP để can thiệp sâu (Intercept) vào mọi request.

```python
# Ví dụ dùng Playwright để chặn Request quảng cáo (AdBlock bằng Code)
page.route("**/*", lambda route: route.abort() 
    if route.request.resource_type in ["image", "media", "font"] 
    else route.continue_())
```

---

## 3. Patching Chromium (Hardcore)

Nếu bạn muốn viết một Anti-Detect Browser xịn như Gologin hay Multilogin, bạn không thể chỉ dùng Extension. Bạn phải sửa mã nguồn của trình duyệt (Chromium).

### **Quy trình Build Chromium:**
1.  **Tải Source Code:** Chromium (hàng chục GB).
2.  **Sửa C++:** Tìm các hàm trả về thông tin phần cứng (ví dụ `GetSystemInfo` trong `base/sys_info_win.cc`).
3.  **Inject Hook:** Thay vì trả về RAM thật (16GB), hãy trả về giá trị ngẫu nhiên (4GB, 8GB) hoặc đọc từ file config.
4.  **Build:** Compile ra file `chrome.exe` mới.

-> Đây là level cao nhất của MMO Tool Developer.

---

## 4. Playwright Stealth (Giải pháp Mì ăn liền)

Nếu không đủ trình độ sửa C++, hãy dùng thư viện `playwright-stealth` để tiêm (inject) các đoạn JavaScript giúp che giấu hành vi Bot.

```python
from playwright_stealth import stealth_sync

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    # Kích hoạt chế độ tàng hình
    stealth_sync(page)
    
    page.goto("https://bot.sannysoft.com/")
    page.screenshot(path="stealth_check.png")
```
