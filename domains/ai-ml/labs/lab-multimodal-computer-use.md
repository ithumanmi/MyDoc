# Lab 4: Multimodal Agents - Computer Use (Anthropic demo)

> [← Back to Labs AI/ML Focus](./README.md) | [Home](../../../README.md)

Mục tiêu: chạy demo Computer Use của Anthropic bằng Docker, xem agent điều khiển trình duyệt/app qua VNC.

---

## 🛠️ Bước 1: Điều kiện
1) Docker Desktop.
2) Anthropic API key (Cloud 3.5 Sonnet computer-use-preview).

---

## 🐳 Bước 2: Chạy container demo

Chạy Ubuntu container kèm VNC + Streamlit UI (đổi `YOUR_API_KEY`):

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
Port:
- 8501: Streamlit chat UI
- 6080: noVNC (màn hình VM)
- 8080: proxy UI kết hợp

---

## 🎯 Bước 3: Truy cập UI

Mở trình duyệt: `http://localhost:8080`
- Bên trái: chat (Streamlit)
- Bên phải: màn hình VM (noVNC)

Thử prompt:
- "Mở LibreOffice Calc, điền cột A từ 1..5, copy sang cột C"
- "Mở Firefox, cài UBlock Origin, tra CEO Apple, vào Wikipedia, chụp màn hình lưu tim.png"

---

## 🧠 Bên dưới demo

Mô hình điều khiển qua bộ tool:
1) **ComputerTool**: click/drag/keyboard, screenshot.
2) **EditTool**: đọc/sửa file.
3) **BashTool**: chạy lệnh shell.

---

## ⚡ Bài tập thêm: UI testing bằng agent

Ví dụ prompt:
"Mở web nội bộ, thu hẹp cửa sổ Firefox còn một nửa, đăng nhập với mail demo; nếu form bị lỗi giao diện, chụp màn hình và báo lại."
