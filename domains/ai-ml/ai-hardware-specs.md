# 📊 AI Hardware Technical Specs (2026)

Bảng số liệu nhanh cho các accelerator, hệ thống inference và edge kit phục vụ AI. Dữ liệu cập nhật Q1/2026 (tham khảo whitepaper vendor).

## 1. Training GPU/ASIC – Thông số chính

| Model | Kiến trúc | FP16/BF16 TFLOPS* | FP8 TFLOPS | HBM | Băng thông HBM | Interconnect | TDP | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NVIDIA H100 SXM | Hopper | ~2000 | 4000 | 80GB HBM3 | 3.35 TB/s | NVLink4 (900GB/s), NVSwitch | 700W | Tensor Core FP8, hỗ trợ MIG |
| NVIDIA H200 SXM | Hopper+ | ~2400 | 4800 | 141GB HBM3e | 4.8 TB/s | NVLink4 | 700W | Context dài, tăng băng thông 1.4x |
| AMD Instinct MI300X | CDNA3 | 1638 | 3276 | 192GB HBM3 | 5.3 TB/s | Infinity Fabric | 750W | APU (CPU+GPU), ROCm |
| Intel Gaudi3 | Gaudi | 1835 BF16 | 3669 | 128GB HBM2e | 3.7 TB/s | 24×100GbE RoCE on-die | 600W | NIC tích hợp, HL-325L |
| Google TPU v5p | Systolic | 2750 BF16 | - | 95GB HBM | 3.7 TB/s | TPU interconnect 400G | ~450W | Pod 256 chip, Cloud TPU |
| Cerebras WSE-3 | Wafer-scale | 1250 BF16 | - | 44GB SRAM on-chip | 20 PB/s on-chip | SwarmX | 20 kW/system | Xử lý sparse, wafer nguyên tấm |

>*TFLOPS lý thuyết mỗi thiết bị. Thực tế phụ thuộc kernel/precision.

## 2. Inference & Data Center Cards

| Model | Kiến trúc | FP16 TFLOPS | INT8 TOPS | Memory | Form factor | TDP | Điểm nổi bật |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NVIDIA L40S | Ada Lovelace | 181 | 362 | 48GB GDDR6 | PCIe 4.0 x16 | 350W | TensorRT-LLM, hỗ trợ FP8 |
| NVIDIA L4 | Ada | 61 | 121 | 24GB GDDR6 | PCIe low-profile | 72W | Inference tiết kiệm điện |
| Intel Gaudi2 | Gaudi | 128 BF16 | 256 | 96GB HBM2e | OAM/PTX | 450W | Giá cạnh tranh 40–60% H100 |
| TPU v5e | Systolic | 1000 BF16 | - | 95GB HBM | Cloud TPU | - | Tối ưu inference/training vừa |
| AWS Inferentia2 | Neuron | 190 BF16 | 380 | 32GB HBM | AWS instance | 220W | EC2 Inf2, latency thấp |

## 3. Edge & On-device SoC

| Thiết bị | TOPS (INT8) | GPU/NPU | RAM tối đa | Công suất | Nhiệt độ hoạt động | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| NVIDIA Jetson Orin AGX 64GB | 275 | Ampere GPU + 2×NVDLA | 64GB LPDDR5 | 15–60W | -25°C → 80°C | Hỗ trợ CUDA/ROS2 |
| NVIDIA Jetson Orin Nano | 40 | 1024 CUDA + 1×NVDLA | 8GB LPDDR5 | 7–15W | -25°C → 80°C | Edge robotics nhỏ |
| Google Coral Dev Board Micro | 4 | Edge TPU | 1GB LPDDR4 | 1–2W | 0°C → 85°C | Vision inference |
| Qualcomm Snapdragon X Elite | 45 (NPU) | Adreno GPU + Hexagon NPU | 64GB LPDDR5x | 10–40W | Laptop/desktop | AI PC SoC |
| Apple M3 Max | 92 (ANE) | GPU 40-core + Neural Engine | 48GB unified | 30–60W | Laptop | On-device LLM |

## 4. Networking & Storage Specs

| Thành phần | Thông số | Ghi chú |
| --- | --- | --- |
| InfiniBand NDR | 400Gbps/port, latency ~0.6µs | Switch 64–256 port, dùng cho DGX SuperPOD |
| Ethernet 800G | 800Gbps QSFP-DD, dùng RoCEv2 | Cần PFC/ECN tuning, spine >51.2Tbps |
| NVSwitch | 900GB/s per GPU | Kết nối 8–18 GPU nội bộ node |
| NVMe PCIe 5.0 | 14GB/s đọc, 12GB/s ghi | SSD U.2/U.3 15.36TB |
| GPUDirect Storage | Throughput 100GB/s/node | GDS driver + RDMA NIC |

## 5. Power & Cooling Reference

| Hệ thống | Công suất trung bình | Cooling khuyến nghị | Ghi chú |
| --- | --- | --- | --- |
| 8×H100 SXM node | 6–7kW | Direct-to-chip liquid | Cần water loop 30–35°C |
| 32-node (256 GPU) pod | 250–280kW | Liquid + aisle containment | Tính PUE ~1.2 |
| L40S rack 16 node | 30–35kW | Air/liquid hybrid | Có thể dùng rear-door heat exchanger |
| Jetson Orin edge box | 15W | Passive/fan nhỏ | Case IP65, chống rung |

## 6. Storage Capacity Planning (tham khảo)

| Workload | Dataset | Định dạng | Băng thông cần thiết | Lưu ý |
| --- | --- | --- | --- | --- |
| LLM 2T tokens | 15TB (text) | Parquet / Megatron binary | 40–60GB/s | Tiền xử lý sharding theo node |
| Video pretraining | 500TB | WebDataset (tar) | 80–120GB/s | Dùng DALI + NVDEC |
| Edge vision | 5TB | ONNX/tflite + dataset ảnh | 1–2GB/s | Lưu trữ local SSD + sync đám mây |

## 7. Thuật ngữ & viết tắt chính
- **TFLOPS/TOPS:** Trillion floating-point/integer operations per second.
- **HBM:** High Bandwidth Memory – đặt sát die, băng thông >1TB/s.
- **NVLink/NVSwitch:** Interconnect tốc độ cao giữa GPU.
- **OAM/PTX:** Form factor module mở (Open Accelerator Module/PCIe eXtended).
- **TDP:** Thermal Design Power – công suất nhiệt tối đa.
- **TOPS/W:** Hiệu năng trên watt, quan trọng cho edge.

> 📌 *Dữ liệu có thể thay đổi tùy SKU hoặc cấu hình OEM. Khi lập kế hoạch mua sắm, luôn đối chiếu datasheet chính thức và benchmark MLPerf/PoC nội bộ.*