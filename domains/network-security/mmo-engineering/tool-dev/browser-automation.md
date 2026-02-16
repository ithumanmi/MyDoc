# 🌐 Browser Automation: Tương tác như Người thật (Level 2)

> [← Back to Network Security](../../README.md)

Khi API bị chặn (JavaScript Challenge, WebSocket), bạn buộc phải mở trình duyệt lên. Nhưng làm sao để tự động hóa 100 cái Chrome cùng lúc?

---

## 1. Selenium vs Playwright (Chọn phe)

### **A. Selenium (Ông tổ)**
*   **Ưu điểm:** Cộng đồng lớn, tài liệu nhiều.
*   **Nhược điểm:** Chậm, nặng, dễ bị phát hiện (`navigator.webdriver = true`).
*   **Fix:** Dùng `selenium-stealth` hoặc `undetected-chromedriver`.

### **B. Playwright (Thế hệ mới - Microsoft)**
*   **Ưu điểm:** Nhanh, nhẹ, hỗ trợ giả lập Mobile cực tốt.
*   **Tính năng:** Chụp ảnh màn hình (screenshot), quay video, chặn request quảng cáo.
*   **Chọn:** Nên học Playwright nếu bạn mới bắt đầu.

```python
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        # headless=False để hiện trình duyệt (Debug)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.google.com")
        print(page.title())
        browser.close()

if __name__ == "__main__":
    run()
```

---

## 2. Tìm phần tử (Selectors - Kỹ năng sinh tồn)

Muốn click vào nút "Đăng nhập", bạn phải tìm được nó.

### **A. XPath (Mạnh nhất)**
*   Tìm theo text: `//*[text()='Đăng nhập']`
*   Tìm theo thuộc tính: `//input[@id='username']`
*   Tìm theo cha con: `//div[@class='login-form']//button`

### **B. CSS Selector (Nhanh hơn)**
*   ID: `#username`
*   Class: `.btn-primary`
*   Attribute: `input[name='password']`

---

## 3. Undetected Chromedriver (UC)

Đây là thư viện Python sửa (patch) lại Chromedriver để bypass các hệ thống chống Bot cơ bản (Cloudflare, Akamai).

```python
import undetected_chromedriver as uc
import time

options = uc.ChromeOptions()
# options.add_argument('--headless') # Chạy ngầm

driver = uc.Chrome(options=options)
driver.get("https://nowsecure.nl") # Trang test chống Bot
time.sleep(5)
driver.quit()
```

---

## 4. Hành vi Người dùng (Human Behavior)

Bot đi thẳng tắp, người đi cong cong. Bot click ngay, người do dự.

### **Action Chains (Chuỗi hành động)**
*   Di chuột (Hover) vào menu -> Chờ 1s -> Click item con.
*   Kéo thả (Drag & Drop) thanh trượt xác thực.
*   Gõ phím từng ký tự một (Typewriter effect).

```python
from selenium.webdriver.common.action_chains import ActionChains

actions = ActionChains(driver)
element = driver.find_element("id", "menu")
actions.move_to_element(element).perform() # Hover chuột
```

### **Random Sleep**
Đừng bao giờ `time.sleep(5)` cố định. Hãy `time.sleep(random.uniform(3, 7))`.
