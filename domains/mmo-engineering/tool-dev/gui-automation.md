# 🖥️ Desktop GUI Automation: Điều khiển Hệ thống (Level 3)

> [← Back to Network Security](../../README.md)

Nhiều App kiếm tiền chỉ chạy trên Windows (.exe) và không có Web. Lúc này Browser hay API đều vô dụng. Bạn cần **GUI Automation**.

---

## 1. PyAutoGUI (Chuột và Bàn phím ảo)

Điều khiển chuột (Mouse) và bàn phím (Keyboard) ở cấp độ hệ điều hành. Nó không quan tâm bạn đang mở Web hay App gì, cứ tọa độ `(x, y)` là click.

### **Cơ chế hoạt động:**
*   Chụp ảnh màn hình liên tục.
*   Tìm kiếm vị trí của nút bấm trong ảnh.
*   Di chuyển chuột đến đó và click.

```python
import pyautogui
import time

# Chờ 3s để bạn chuyển cửa sổ
time.sleep(3)

# 1. Click vào icon Telegram (tọa độ x=100, y=200)
pyautogui.click(100, 200)

# 2. Gõ tin nhắn
pyautogui.typewrite("Hello world!", interval=0.1) # Gõ từng ký tự

# 3. Enter
pyautogui.press('enter')

# 4. Tìm ảnh trên màn hình (Image Search)
button_location = pyautogui.locateOnScreen('button.png', confidence=0.8)
if button_location:
    pyautogui.click(button_location)
else:
    print("Không tìm thấy nút bấm!")
```
*Lưu ý: `confidence` cần cài thêm `opencv-python`.*

---

## 2. PyWinAuto (Điều khiển Cửa sổ)

Nếu App là dạng WinForms/WPF (Native Windows), bạn có thể "móc" vào các control (Button, TextBox) để điều khiển, thay vì click tọa độ mù.

### **Ưu điểm:**
*   Chính xác hơn PyAutoGUI (không sợ cửa sổ bị che khuất).
*   Có thể chạy ở background (ẩn cửa sổ).

```python
from pywinauto.application import Application

# Mở Notepad
app = Application().start("notepad.exe")

# Chọn cửa sổ chính
dlg = app.UntitledNotepad

# Gõ text vào ô Edit
dlg.Edit.type_keys("Xin chao cac ban!", with_spaces=True)

# Chọn menu File -> Save As
dlg.menu_select("File->SaveAs")

# Lưu file
app.SaveAs.Edit.set_edit_text("test.txt")
app.SaveAs.Save.click()
```

---

## 3. Image Recognition (OpenCV)

Khi App dùng công nghệ lạ (Flutter, Electron, Game Unity) mà PyWinAuto không soi được Control, bạn phải dùng "Mắt thần" OpenCV.

*   Template Matching: So khớp mẫu ảnh nhỏ trong ảnh to.
*   OCR (Tesseract): Đọc chữ từ ảnh (Ví dụ: Đọc mã Captcha số, đọc số dư tài khoản).

```python
import cv2
import pytesseract

# Đọc ảnh chụp màn hình
img = cv2.imread('screenshot.png')

# Chuyển sang đen trắng (Grayscale) để dễ đọc
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Đọc chữ (OCR)
text = pytesseract.image_to_string(gray)
print("Số dư hiện tại:", text)
```
