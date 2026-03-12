# 📟 AT Commands Reference for 4G Dongles

## 1. Basics
- Giao tiếp qua serial (COM/ttyUSB). Baud 115200.
- Kết thúc mỗi lệnh bằng `\r`.

## 2. Connection Control
| Action | Command |
| --- | --- |
| Reset radio (off/on) | `AT+CFUN=0` / `AT+CFUN=1` |
| Detach/Attach packet service | `AT+CGATT=0` / `AT+CGATT=1` |
| Soft reboot dongle | `AT+RST` (model specific) |

## 3. Network Info
| Info | Command | Notes |
| --- | --- | --- |
| Operator | `AT+COPS?` | trả về MCC/MNC |
| Signal quality | `AT+CSQ` | 0-31 (>=15 tốt) |
| IP address | `AT+CGPADDR` | check WAN IP |
| Cell ID | `AT+CREG?` hoặc `AT+CENG?` | dùng cho geolocation |

## 4. SIM & APN
- `AT+CPIN?` – kiểm tra SIM ready.
- `AT+CGDCONT=1,"IP","internet.viettel"` – set APN.
- `AT+CLCK="SC",0,"1234"` – disable SIM PIN.

## 5. SMS & USSD (top-up)
- Send USSD: `AT+CUSD=1,"*101#",15`.
- Check balance reply qua unsolicited result.

## 6. Automation Tips
- Sử dụng Python `pyserial` để gửi lệnh hàng loạt.
- Thêm delay 1-2s giữa `CFUN` để modem kịp reset.
- Log response để debug (timeout, ERROR).

## 7. Troubleshooting
- `ERROR` ngay lập tức → command không hỗ trợ.
- Không thay đổi IP sau `CFUN` → chờ thêm 30s hoặc đổi SIM.
- Dongle bị lock HiLink mode → dùng `usb_modeswitch` chuyển sang stick.

## 8. Checklist
- [ ] Script reset có retry.
- [ ] Log cell ID & IP sau mỗi lần reset.
- [ ] Theo dõi `CSQ` để tối ưu anten.