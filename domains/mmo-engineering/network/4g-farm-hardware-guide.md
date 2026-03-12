# 📡 4G Farm Hardware Guide

## 1. Topologies
- **USB Dongle Rack:** PC/mini server + powered USB hub + 4G dongles.
- **LTE Router Farm:** industrial router (Teltonika, Mikrotik) với nhiều SIM.
- **Mixed (Dongle + Phone):** tận dụng Android cũ với app proxy.

## 2. USB Dongle Models
| Model | Chipset | Bands | Notes |
| --- | --- | --- | --- |
| Huawei E3372h-607 | HiSilicon Balong | LTE Cat4 | Support HiLink (web UI) & Stick mode (AT). OTA unlock được |
| ZTE MF833V | Qualcomm MDM9207 | LTE Cat4 | Có driver tốt trên Windows/Linux |
| Alcatel IK40 | Qualcomm | LTE Cat4 | Rẻ, phổ biến VN |
| Quectel EC25 (Mini PCIe) | Qualcomm | LTE Cat4 | Dùng với USB adapter + anten SMA |

## 3. USB Hub & Power
- Powered hub 10-20 port (Orico, Anker) + adapter 12V/10A.
- Tránh hub rẻ kém chất lượng (nóng → disconnect).
- Wiring: chia nhóm 5 dongle/hub để giảm nhiệt.

## 4. Controller Machines
- **Mini PC:** Intel NUC, Minisforum (8GB RAM) → chạy Windows/Linux.
- **Raspberry Pi 4:** 4GB RAM, dùng `usb_modeswitch` để quản lý dongle.
- **Server + PCIe USB Card:** cho farm >40 dongle.

## 5. Antennas & Signal
- Mua anten SMA/TS9 external (5-9 dBi) cho dongle hỗ trợ.
- Dùng splitter + cáp coax chất lượng.
- Mount anten gần cửa sổ, tránh kim loại chắn.

## 6. Cooling & Physical Layout
- Quạt 12cm thổi ngang rack.
- Monitor nhiệt độ (USB hub >60°C → giảm tải).
- Gắn nhãn từng dongle tương ứng SIM để dễ quản lý.

## 7. Maintenance Checklist
- [ ] Firmware dongle cập nhật, unlock.
- [ ] SIM data plan còn hạn, auto top-up.
- [ ] USB hub nguồn ổn định, không quá tải.
- [ ] Có spare dongle/SIM để thay nhanh.