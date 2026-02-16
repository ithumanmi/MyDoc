# 🔎 Digital Forensics & Incident Response (DFIR)

> [← Back to Network Security](./README.md)

"Hacker chỉ cần đúng 1 lần. Người phòng thủ phải đúng mọi lúc. Nhưng khi người phòng thủ sai, DFIR sẽ vào cuộc."
DFIR là sự kết hợp giữa Cảnh sát (Forensics) và Cứu hỏa (Incident Response).

---

## 1. Incident Response (Ứng cứu sự cố) - Quy trình PICERL

Khi công ty bị hack, đừng hoảng loạn. Hãy làm theo quy trình:

1.  **Preparation (Chuẩn bị):**
    *   Tạo Policy, Training nhân viên.
    *   Setup hệ thống Log, Backup.
2.  **Identification (Nhận diện):**
    *   Phát hiện sự cố (IDS cảnh báo, User báo cáo).
    *   Xác định mức độ nghiêm trọng (Triage).
3.  **Containment (Khoanh vùng):**
    *   **Short-term:** Rút dây mạng server bị hack (ngắt kết nối C&C server).
    *   **Long-term:** Vá lỗ hổng tạm thời.
4.  **Eradication (Diệt trừ):**
    *   Tìm nguyên nhân gốc (Root Cause).
    *   Xóa Malware, xóa tài khoản Backdoor.
5.  **Recovery (Khôi phục):**
    *   Restore dữ liệu từ bản Backup sạch.
    *   Monitor chặt chẽ xem Hacker có quay lại không.
6.  **Lessons Learned (Rút kinh nghiệm):**
    *   Viết báo cáo (Post-mortem). Tại sao bị hack? Làm sao để không bị lại?

---

## 2. Digital Forensics (Điều tra số)

Giống như CSI (Hiện trường vụ án), nhưng là trên máy tính.
**Nguyên tắc vàng:** KHÔNG BAO GIỜ làm việc trên ổ cứng gốc. Luôn tạo bản sao (Image) để phân tích.

### **A. Memory Forensics (Phân tích RAM)**
*   **Tại sao:** Malware hiện đại thường chạy trên RAM (Fileless) để tránh Antivirus quét ổ cứng.
*   **Dữ liệu:** Danh sách tiến trình đang chạy, kết nối mạng, mật khẩu chưa mã hóa.
*   **Tool:** **Volatility Framework**.
    ```bash
    vol.py -f dump.mem windows.pslist  # Liệt kê tiến trình
    ```

### **B. Disk Forensics (Phân tích Ổ cứng)**
*   **Dữ liệu:** File đã xóa (Deleted files), Lịch sử duyệt web, Windows Event Logs.
*   **Tool:** **Autopsy** (Giao diện dễ dùng), **The Sleuth Kit**.

---

## 3. Malware Analysis Basics (Phân tích Mã độc)

### **A. Static Analysis (Tĩnh)**
*   Phân tích file mà KHÔNG chạy nó.
*   **Check Hash:** Upload lên **VirusTotal** để xem 60+ AV engine nói gì.
*   **Strings:** Trích xuất chuỗi ký tự trong file exe.
    ```bash
    strings malware.exe
    ```
    -> Có thể thấy IP của C&C Server, thông báo lỗi, tên hàm.

### **B. Dynamic Analysis (Động)**
*   Chạy malware trong môi trường Sandbox cô lập (Máy ảo không mạng).
*   **Quan sát:** Nó tạo file gì? Nó kết nối đi đâu? Nó sửa Registry nào?
*   **Tool:** Cuckoo Sandbox, Process Monitor (ProcMon).

> **Cảnh báo:** Phân tích malware rất nguy hiểm. Hãy cẩn thận "vũ khí sinh học" này thoát ra ngoài.
