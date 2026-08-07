# Lab: ESP32 Hello IoT

> [← Labs](./README.md) | [MQTT primer](../connectivity/mqtt-and-protocols.md)

## Mục tiêu
Đọc cảm biến (hoặc mock temp) và publish MQTT QoS1 tới broker local/cloud.

## Setup
```bash
# ESP-IDF
idf.py set-target esp32
idf.py menuconfig   # Wi-Fi + broker URI
idf.py build
idf.py -p COM3 flash monitor
```

## Acceptance
- [ ] Device connect Wi-Fi
- [ ] Publish JSON `{"temp":...}` mỗi 5s lên `devices/demo/telemetry`
- [ ] Thấy message trên MQTTX / mosquitto_sub
- [ ] Serial log reconnect khi tắt broker 10s rồi bật lại

## Snippet ý tưởng
```c
esp_mqtt_client_publish(client, "devices/demo/telemetry",
  "{\"temp\":24.5}", 0, 1, 0);
```

## Extension
Thêm FreeRTOS queue: sensor task → mqtt task (không gọi network trong ISR).

> **Last Updated:** August 2026
