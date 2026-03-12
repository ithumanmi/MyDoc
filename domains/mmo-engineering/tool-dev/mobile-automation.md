# 📱 Mobile Farm Automation: Nuôi Nick Tự Động (Level 4)

> [← Back to Network Security](../../README.md)

Khi các nền tảng (TikTok, Facebook) check thiết bị quá gắt, giả lập (LDPlayer, Nox) đều "đi bụi". Giải pháp cuối cùng: **Phone Farm** (Dùng điện thoại thật).

---

## 1. ADB (Android Debug Bridge)

Đây là công cụ giao tiếp giữa máy tính và Android qua cáp USB. Mọi tool nuôi nick đều chạy trên nền tảng này.

### **Các lệnh ADB cơ bản:**
*   `adb devices`: Liệt kê danh sách điện thoại đang cắm.
*   `adb shell input tap x y`: Click vào tọa độ (x, y).
*   `adb shell input swipe x1 y1 x2 y2 duration`: Vuốt màn hình.
*   `adb shell input text "hello"`: Gõ chữ.
*   `adb shell screencap -p /sdcard/s.png`: Chụp ảnh màn hình.

### **Python Wrapper (Pure Python ADB)**
Thay vì gọi `os.system("adb ...")` chậm chạp, hãy dùng thư viện `pure-python-adb`.

```python
from ppadb.client import Client as AdbClient

client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()

if len(devices) == 0:
    print("Không tìm thấy thiết bị nào!")
else:
    device = devices[0]
    print(f"Đang kết nối: {device.serial}")

    # Mở TikTok (Package Name)
    device.shell("monkey -p com.ss.android.ugc.trill 1")

    # Vuốt lên để xem video tiếp theo
    device.shell("input swipe 500 1500 500 500 300")
```

---

## 2. Appium (Standard Automation Framework)

Nếu ADB quá thô sơ (chỉ click tọa độ), Appium cho phép bạn tìm element trong App giống như Selenium tìm element trên Web.

*   **Ưu điểm:** Code clean, dễ bảo trì (khi App đổi giao diện, tọa độ sai, nhưng ID element vẫn đúng).
*   **Nhược điểm:** Cài đặt phức tạp (cần Node.js, Java JDK, Android SDK). Chậm hơn ADB thuần.

```python
from appium import webdriver

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "com.android.settings",
    "appActivity": ".Settings"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

# Click vào menu "Battery"
el = driver.find_element_by_xpath("//*[@text='Battery']")
el.click()
```

---

## 3. Scrcpy (View Màn Hình)

Khi quản lý 50 cái điện thoại, bạn không thể nhìn từng cái được. Scrcpy giúp mirror (phản chiếu) màn hình điện thoại lên PC với độ trễ cực thấp (low latency).

*   **Tích hợp vào Tool:** Bạn có thể nhúng cửa sổ Scrcpy vào tool quản lý của mình (bằng Python `subprocess` hoặc thư viện `scrcpy-client`).
*   **Điều khiển chuột:** Click trên PC -> Tự động gửi lệnh click xuống điện thoại.

---

## 4. Nuôi Nick Quy mô lớn (Farm)

Để vận hành 1 Farm hiệu quả, bạn cần giải quyết các bài toán:

1.  **Nguồn điện:** Dùng Hub USB có nguồn phụ (Powered Hub) để sạc cho 20 máy cùng lúc. Tháo pin, độ nguồn trực tiếp (Battery Eliminator) để chống cháy nổ.
2.  **Mạng (Network):** Mỗi máy 1 SIM 4G hoặc 1 Proxy riêng (cài qua App `College Proxy` hoặc `Postern` trên Android).
3.  **Reset:** Sau khi acc chết, phải Wipe Data (Factory Reset) và đổi thông số máy (Device ID, IMEI, Mac Address) bằng Root.
