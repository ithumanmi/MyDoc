# Embedded Foundations for IoT

> [← IoT Roadmap](../README.md) | [Home](../../../README.md)
>
> **Maturity note:** Domain 🟡 Drafting · **Level:** 🟢 Beginner

## Mục tiêu
Đủ để flash một board, đọc cảm biến, và gửi telemetry — trước khi chạm cloud phức tạp.

## MCU essentials
| Concept | Cần nắm | Kiểm tra nhanh |
| --- | --- | --- |
| GPIO | Digital in/out, pull-up/down | Blink LED + đọc nút |
| ADC | Resolution, reference voltage | Đọc biến trở → số 0–100 |
| PWM | Duty cycle, frequency | Dim LED / servo pulse |
| Timer / interrupt | Debounce, periodic sample | Sample cảm biến mỗi 1s bằng ISR/timer |
| UART logging | Baud, TX/RX | `printf`/`ESP_LOGI` ra serial |

## Bus cảm biến
- **I2C:** địa chỉ 7-bit, pull-up, SDA/SCL — dùng cho temp/humidity/IMU.
- **SPI:** nhanh hơn, CS riêng — flash ngoài, một số radio.
- **UART:** module LTE/GPS/ESP-AT — cần framing + timeout.

## RTOS tối thiểu (FreeRTOS / Zephyr mindset)
1. **Task** cho sensor đọc và task cho network — đừng block MQTT trong ISR.
2. **Queue** chuyển payload giữa task.
3. **Watchdog** + brown-out: thiết bị field phải tự hồi phục.
4. **Low-power:** deep sleep giữa các chu kỳ gửi nếu chạy pin.

## Toolchain gợi ý
- ESP32 → ESP-IDF hoặc PlatformIO
- STM32 → CubeMX + HAL + FreeRTOS
- Quy tắc: một toolchain → một board → một lab thành công trước khi “đa nền tảng”

## Checklist hoàn thành
- [ ] Flash & serial monitor ổn định
- [ ] Đọc được ≥1 sensor thật
- [ ] Có task/queue tách I/O mạng
- [ ] Log đủ để debug mất kết nối

**Next:** [MQTT & Protocols](../connectivity/mqtt-and-protocols.md) → [Lab ESP32 Hello IoT](../labs/lab-esp32-hello-iot.md)

> **Last Updated:** August 2026
