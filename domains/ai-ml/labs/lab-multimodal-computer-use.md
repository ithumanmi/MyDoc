# Lab 4: Multimodal Agents - Computer Use (Điều Khiển Máy Tính) 

> [← Back to Labs AI/ML Focus](./README.md) | [Home](../../../README.md)

Lý thuyết được nêu ở [Multimodal Agents](../agents/advanced/multimodal-agents.md) tưởng chừng viễn tưởng, nhưng tháng 10/2024 Anthropic đã công bố mã nguồn mở tham khảo: **Computer Use Demo**.

Trong bài Lab thực chiến đặc biệt này, ta không tự rặn Code từ số 0 (vì thư viện mô phỏng click màn hình dính tới Ubuntu X11 Server bảo mật phức tạp), mà ta sẽ Setup thẳng **Docker Reference Image** chính chủ của Anthropic, điền API ngập tiền, và ngắm nó tự mở FireFox book vé máy bay.

---

## 🛠️ Bước 1: Điều Kiện Đủ
1.  Máy tính có cài đặt [Docker Desktop](https://www.docker.com/).
2.  Tài khoản Anthropic API Key (Bạn phải nạp Card để có Credit, model Cloud 3.5 Sonnet Computer-use-preview xài tiền tươi).

---

## 🐳 Bước 2: Kéo Môi Trường Giả Lập Ubuntu (Docker Run)

Vì lý do An Ninh (Đừng cho phép Agent AI có quyền bấm màn hình trên Windows Root Máy Mẹ nhà bạn). Ta ném nó vào cỗ máy ảo Ubuntu trên Docker có cài luồng GUI Firefox đồ họa.

Tắt màn hình ngủ và Mở Terminal, dán lệnh:
*(Nhớ đổi `YOUR_API_KEY` của bạn)*

```bash
docker run \
    -e ANTHROPIC_API_KEY=YOUR_API_KEY \
    -v $HOME/.anthropic:/home/computeruse/.anthropic \
    -p 5900:5900 \
    -p 8501:8501 \
    -p 6080:6080 \
    -p 8080:8080 \
    -it ghcr.io/anthropic/computer-use-demo:latest
```

*Quá trình kéo Image nặng 3-4GB có thể tốn 5-10 phút.*

*Giải thích Port:*
*   Port `8501`: Streamlit Chat GUI Web - Là trang Console cho mình Chat Ra lệnh.
*   Port `6080`: noVNC - Khung Giới Hạn Máy Ảo (Màn hình hệ điều hành nhúng chạy thẳng trên Chrome của bạn), để xem lén coi con chuột dịch chuyển thế nào.

---

## 🎯 Bước 3: Xem Màn Biểu Diễn "Ma Thuật Đầu Đời"

Sau khi Docker chạy xong, mở 1 tab Trình duyệt Chrome máy bạn gõ:
```
http://localhost:8080
```
Màn hình Chat UI Streamlit (Khung ra lệnh) + Khung màn ảo VNC Ubuntu đã hiển diện chung trên 1 giao diện web chia đôi.

### Lệnh 1 (Khảo Sát Khó Hiểu UI - Excel/Web):
Ở khung Chat, gõ chỉ thị (Prompt):
> "Mở cái LibreOffice Calc ở máy bàn lên, sau đó gõ số cột A từ 1 đến 5. Copy toàn bộ cột A quét qua cột C."

*Ngồi khoanh tay:*
1. Bạn sẽ thấy cái Terminal nháy. Agent chụp toàn bộ góc nhìn màn hình Ubuntu gửi về Anthropic.
2. Nó Call Tool: Nhãn Click "Mở App".
3. Con chuột di chuyển vào góc trái Logo.
4. Call Tool Keyboard Typing (Đánh số).

### Lệnh 2 (Lướt Lưới Vượt Trở Ngại):
> "Bật Firefox, mày cài Addon UBlock-Origin dùm tao. Sau đó gõ trên Google Tìm Tên ông CEO Apple là ai rồi vào wikipedia screenshot khúc ông đó nói, lưu lưu lại file tên tim.png ra Desktop."

Kinh hoàng chưa? Nó hiểu Ublock cài ở Web Store Firexox. Nó nhận diện tọa độ Nut bấm để điều hướng.

---

## 🧠 Chuyện Gì Đang Xảy Ra Dưới Cái Docker KIA?

Sự tự chủ này đánh bật những đoạn Code Selenium/Puppeteer cổ xưa (Cần DOM ID Web tĩnh mới crawl nổi). Ở Multimodal: Mắt mô hình là người quyết định Click.

Nếu chui vô Core codebase trên [Anthropic Github Repo](https://github.com/anthropic/computer-use-demo), bạn sẽ thấy nó chia ra 3 class cực chất cho AI xài qua Framework gọi `Tool`:
1.  **ComputerTool**: Quyền hạn ra lệnh click chuột `action=left_click`, kéo tọa độ bàn phím, screenshot snapshot máy.
2.  **EditTool**: Đọc mã file, regex Replace code file (Nó có thể tự sửa file code của hệ điều hành chửa lổi).
3.  **BashTool**: Lôi đầu Bash lên gõ lệnh Terminal thô bạo.

---

## ⚡ (Thử Thách Plus): Xây Dựng 1 Pipeline Test Giao Diện App

Đây là đỉnh cao áp dụng Computer Use Agent cho Tester Doanh nghiệp: Bắt AI test UI End-to-End.

Sửa Prompt hệ tư tưởng của Agent:
> "Sếp tôi nghi ngờ Web App ở `http://local-website-cua-ban` (Bật bằng nginx trên ubuntu ảo) rớt khung đăng nhập trên thiết bị Cỡ nhỏ. Thu hẹp chửa sổ Firefox lại thành một nửa. Xong bạn tự đăng nhập mail ảo, nếu Form bị chữ đè ngang nút báo tôi cái Screenshot."

Kết quả: QA Automation Tester mất job nếu chưa học cách Prompter làm Trùm Agent thế này!
