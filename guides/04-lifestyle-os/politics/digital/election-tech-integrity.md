# 🗳️ Election Tech & Integrity

Khi bầu cử chuyển sang nền tảng số (máy bỏ phiếu điện tử, e-voting, kiểm phiếu tự động), độ tin cậy của hệ thống quyết định sự sống còn của dân chủ. Đây là bản hướng dẫn cô đọng để hiểu các điểm rủi ro.

## 1. Kiến trúc công nghệ bầu cử hiện đại
- **Máy bỏ phiếu trực tiếp (DRE):** Đầu cuối điện tử ghi phiếu. Cần bản in đối chiếu (VVPAT) để kiểm tra độc lập.
- **Optical Scan & Tabulation:** Phiếu giấy nhưng quét bằng máy. Rủi ro nằm ở phần mềm kiểm phiếu.
- **E-voting / Internet Voting:** Cho phép bỏ phiếu từ xa (Estonia). Đòi hỏi hạ tầng PKI, nhận diện sinh trắc, và audit log chặt.

## 2. Những điểm có thể bị thao túng
1. **Đăng ký cử tri:** Database có thể bị sửa/xóa để hạn chế người bỏ phiếu.
2. **Máy bỏ phiếu:** Firmware bị cài mã độc, cập nhật không kiểm soát.
3. **Truyền dữ liệu:** Kết quả gửi về trung tâm bị chặn hoặc sửa (man-in-the-middle).
4. **Kiểm phiếu & công bố:** Hệ thống tổng hợp công bố số liệu sai lệch.

## 3. Chiến lược bảo vệ
- **Paper trail:** Luôn có bản giấy đối chứng để audit.
- **Risk-limiting audit:** Kiểm tra ngẫu nhiên 1 phần phiếu để đảm bảo sai số dưới ngưỡng cho phép.
- **Open-source & Bug bounty:** Công khai mã nguồn / cho phép chuyên gia độc lập kiểm tra.
- **Zero-trust architecture:** Giả định mọi thành phần có thể bị xâm nhập; phân đoạn mạng; ghi log bất biến.

## 4. Integrity trong thời đại AI
- **Synthetic voters:** Bot AI có thể đăng ký / bỏ phiếu trong hệ thống lỏng lẻo → cần xác thực mạnh.
- **Generative propaganda:** Deepfake cá nhân hóa kích động cử tri ở điểm yếu cảm xúc.
- **Realtime manipulation:** AI phân tích data để nhắm mục tiêu micro-second trong ngày bầu cử.

## 5. Các case study đáng học
- **Estonia:** E-voting từ 2005, dùng ID số + card reader, audit độc lập.
- **Ấn Độ:** Máy EVM kết hợp VVPAT, logistic cho hơn 900 triệu cử tri.
- **Mỹ:** Tranh cãi 2020 cho thấy thiếu chuẩn chung → nhiều bang quay lại phiếu giấy + audit risk-limiting.

---
> **Bài tập:** Chọn 1 mô hình bầu cử điện tử, liệt kê 3 rủi ro và thiết kế checklist kiểm tra trước-ngày-bầu-cử.

**Quay lại:** [README Politics](../README.md)