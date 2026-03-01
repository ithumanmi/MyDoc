# 🧠🔋 AI Hardware Landscape – Phần cứng chuyên dụng cho AI

> “Model càng lớn thì hạ tầng càng phải thông minh.” – Tài liệu này giúp bạn hiểu nhanh các lớp phần cứng phục vụ AI từ data center đến edge devices.

## 1. Tổng quan kiến trúc phần cứng AI
- **Compute:** GPU/TPU/ASIC, CPU phối hợp scheduling.
- **Memory:** HBM3/3e, DDR5, SRAM on-die.
- **Interconnect:** NVLink/NVSwitch, PCIe Gen5, InfiniBand NDR, Ethernet RoCE.
- **Storage:** NVMe SSD, object storage (S3/OSS) cho dataset.
- **Power & Cooling:** Liquid cooling, immersion, rack-level power budget 30–60kW.

### Phân lớp triển khai
| Lớp | Mục tiêu | Ví dụ phần cứng |
| --- | --- | --- |
| **Training Cluster** | Huấn luyện foundation model, multi-node | NVIDIA DGX GH200, Google TPUv5p pod, AMD MI300X cluster |
| **Inference DC** | Dịch vụ AI real-time, batch inference | NVIDIA L40S, Intel Gaudi3, TPU v5e |
| **Edge / On-device** | Triển khai gần user, IoT, robotics | NVIDIA Jetson Orin, Google Coral TPU, Apple Neural Engine |

---

## 2. Training Hardware Stack (Deep-dive)

### 2.0 Kiến trúc GPU vs ASIC – nhìn từ Tensor Core & Systolic Array
| Tiêu chí | GPU (Tensor Core) | ASIC (TPU, WSE) |
| --- | --- | --- |
| Độ linh hoạt | Cao – lập trình CUDA/ROCm, hỗ trợ nhiều framework | Trung bình – tối ưu transformer/SOTA kernels cụ thể |
| Precision | FP32, BF16, FP8 linh hoạt | BF16/INT8/FP16 định sẵn |
| Bộ nhớ | HBM3/3e gắn liền GPU | HBM + SRAM on-chip lớn (TPU pod, WSE) |
| Interconnect | NVLink/NVSwitch | Swarm fabric riêng (TPU pod, SwarmX) |
| Use case | Foundation model training/inference hybrid | Training khối lượng cực lớn hoặc task đặc thù |

> **HBM roadmap:** HBM3e (9.2 Gbps pin, ~1.2TB/s) sẵn trên H200; 2026-27 sẽ có HBM4 push băng thông >1.5TB/s, cần thiết cho context >1M token.

### 2.1 GPU-centric
- **NVIDIA Hopper (H100/H200)**: 132 SM, Tensor Core FP8, HBM3 80GB/96GB. Hỗ trợ NVLink 4 & NVSwitch cho 256 GPU trong 1 pod.
- **AMD Instinct MI300X**: APU (CPU+GPU), 192GB HBM3, ROCm stack – tối ưu cho open-source LLM.
- **Intel Gaudi3**: 128GB HBM2e, 24x100GbE RoCE on-chip, mạnh ở throughput training & inference chi phí thấp.

### 2.2 ASIC-specialized
- **Google TPU v5p**: Systolic array + HBM, thiết kế pod 256 chip, throughput cao cho Transformer.
- **Cerebras Wafer-Scale Engine (WSE-3)**: 2.6T transistor trên nguyên wafer, 44GB SRAM on-chip, phù hợp training sparse models.
- **Graphcore IPU-POD**: Hàng chục tỷ transistor, memory in-processor, tối ưu mô hình graph/irregular.

### 2.3 Networking & Storage for Training (chi tiết)
- **Fabric lựa chọn**:
  - *InfiniBand NDR 400G*: latency <1µs, RDMA HW offload. Dùng cho DGX SuperPOD.
  - *Ethernet 800G (RoCEv2)*: tiết kiệm chi phí, yêu cầu tuning QoS (PFC, ECN).
  - *SwarmX / CX7 NVLink*: nội bộ pod, bandwidth >900GB/s giữa GPU.
- **Topology tham chiếu**: 32 node × 8 GPU (256 GPU) dual-rail, cần spine-leaf switch >25.6Tbps.
- **Storage pipeline**:
  - *Hot tier*: NVMe SSD local (U.2/U.3) 15–30TB/node.
  - *Warm tier*: NVMe all-flash array (Pure FlashBlade) hoặc Ceph NVMe.
  - *Cold tier*: Object storage (S3, MinIO) + prefetch tool (NVIDIA DALI, Petastorm).
- **Data streaming**: TFRecord, WebDataset, Megatron data loader, cần pre-sharding để tránh I/O bottleneck.
- **Scheduler/Orchestrator**: Slurm + Pyxis/Enroot, Kubernetes (Kubeflow/Volcano) + GPU Operator, hỗ trợ MIG/MPS, gang scheduling.

> 🔧 **Checklist training**: Xác định throughput/token target, mô hình dữ liệu (text/image/video), ngân sách điện/cooling trước khi chốt cấu hình.

---

## 3. Inference Data Center Hardware (Deep-dive)

### 3.1 Cards & Accelerators
- **NVIDIA L40S / L4**: FP8 Tensor Core, tối ưu LLM inference (7B–70B), hỗ trợ vLLM/TensorRT-LLM.
- **Intel Gaudi2/3**: Giá cạnh tranh, throughput cao cho batch inference.
- **TPU v5e**: Balanced cost-performance cho inference & training vừa.
- **AWS Inferentia2 / Trainium**: Dành cho cloud khách hàng AWS cần chip riêng.

### 3.2 CPU & Memory
- **Grace CPU Superchip (Arm)** kết đôi NVLink-C2C với H100 – giảm latency copy KV cache.
- **AMD EPYC 9004 (Genoa/Bergamo)**: 128 nhân, hỗ trợ AVX-512, PCIe Gen5 lanes nhiều.
- **Intel Xeon 6 Granite Rapids**: HBM on-package, hỗ trợ Gaudi card.
- **KV cache**: DLLM 8k–32k context cần 128–512GB RAM/node; nên dùng DDR5 4800+ ECC hoặc CXL memory expander.

### 3.3 Deployment Patterns
- **Autoscaling GPU pools**: Kubernetes + KServe/vLLM, dùng cluster autoscaler + GPU reservation để tránh fragmentation.
- **Hybrid pipeline**: Prompt -> H100 (FP8) generate logits -> CPU/Gaudi xử lý completion hoặc rerank.
- **Quantization**: FP8 (Transformer Engine), INT4 (AWQ, GPTQ), cần card hỗ trợ warp-specialized kernels (H100, L40S). Theo dõi accuracy drop qua calibration set.
- **Speculative decoding**: GPU nhỏ (L4) dự đoán, GPU lớn xác nhận – giảm latency ~30%.

---

## 4. Edge & On-device AI Hardware (Expanded)

| Hạng mục | Thiết bị | Use case |
| --- | --- | --- |
| SBC Edge GPU | **NVIDIA Jetson Orin AGX/Nano** | Robotics, vision, ROS2 |
| Dedicated Edge TPU | **Google Coral Dev Board / PCIe** | Vision inferencing 4 TOPS/W |
| AI SoC | **Qualcomm Snapdragon X Elite, Apple M-series** | Laptop AI PC, on-device LLM |
| Microcontroller AI | **STM32 NPU, ARM Ethos-U** | TinyML, IoT sensing |

### Lưu ý vận hành
- Tối ưu hóa model: quantization (INT8/INT4), pruning, distillation để fit edge memory.
- Tích hợp tăng tốc video (NVENC/NVDEC, ISP) để giảm tải GPU chính.
- Cân nhắc tiêu chuẩn IP (IP65) và nhiệt độ môi trường (-20°C đến 70°C) cho robot/outdoor.
- Edge orchestrator: Azure IoT Edge, Nvidia Fleet Command, balenaCloud để OTA update.

---

## 5. Memory, Storage & Cooling Considerations (Deep-dive)

- **HBM vs GDDR**: Training cần HBM3e, inference có thể dùng GDDR6X (RTX 6000 Ada). HBM cung cấp băng thông 3–5x so với GDDR nhưng chi phí cao.
- **CXL Memory Expander**: Cho phép thêm 1–2TB RAM/node để chứa KV cache lớn (các hãng: Astera Labs, Micron).
- **Storage tiering**: Object storage (S3) → NVMe cache → GPU memory. Sử dụng GPUDirect Storage (GDS) để bypass CPU, giảm latency đọc dữ liệu.
- **Cooling**:
  - *Direct-to-chip liquid cooling*: phổ biến cho rack 30–60kW.
  - *Immersion cooling*: cho cụm >100kW/rack, giảm PUE ~0.1–0.2.
  - Theo dõi leak detection, bảo trì pump.
- **Power planning**: UPS + PDUs chịu được đỉnh 2–3x khi boost clock; cần harmonic filter để tránh nhiễu.
- **Facility**: Kiểm tra datacenter tier (TIA-942). AI cluster cần floor loading >2000kg/m².

---

## 6. Case Study: Reference Architectures

### 6.1 Mini Foundation Model Cluster (Hyperscaler style)
- **Cấu hình**: 8x NVIDIA H100 SXM + Grace CPU + NVSwitch, 2x 400G IB NIC/node.
- **Networking**: Dual-rail InfiniBand NDR → spine switch 64-port.
- **Storage**: 2x 24-bay NVMe servers (Ceph) + 1PB object storage.
- **Use case**: Fine-tune Llama 70B, RAG retrieval training.
- **Chi phí ước tính**: 2.5–3M USD (bao gồm rack & cooling).

### 6.2 Inference Farm cho SaaS
- **Cấu hình**: 16 node × 4x L40S PCIe, CPU AMD EPYC 9654.
- **Software**: vLLM + TensorRT-LLM, FastAPI gateway, autoscale theo QPS.
- **Networking**: 100G Ethernet spine-leaf, RoCE tuning.
- **Mục tiêu**: 50K token/s LLM, latency P95 <200ms.

### 6.3 Edge AI Kit cho Robotics
- **Thiết bị**: Jetson Orin AGX + camera GMSL, sensor LiDAR.
- **Power**: 24V DC, battery + UPS.
- **Workflow**: ROS2 + Isaac ROS, OTA qua Fleet Command.
- **Use case**: Autonomous inspection, latency <50ms.

---

## 6. Vendor Snapshot

| Vendor | Sản phẩm chính | Điểm mạnh |
| --- | --- | --- |
| NVIDIA | DGX, HGX, Jetson, TensorRT | Ecosystem mạnh, phần mềm tối ưu, hỗ trợ rộng |
| AMD | Instinct MI300X, ROCm | Open-source friendly, giá cạnh tranh |
| Intel | Gaudi2/3, Xeon Max, Habana SDK | Networking on-die, hợp tác OEM |
| Google | TPU v5p/v5e, TPU Edge | Tối ưu Cloud TPU, tích hợp Vertex AI |
| AWS | Trainium, Inferentia | Độc quyền AWS, chi phí inference thấp |
| Cerebras | WSE | Training cực lớn, sparse-friendly |
| Graphcore | IPU-POD | Graph/irregular computation |
| Qualcomm/Apple | Snapdragon X Elite, Neural Engine | On-device AI, hiệu năng/W tốt |

---

## 7. Checklist chọn phần cứng AI (Updated)
- [ ] Xác định workload (training vs inference vs edge).
- [ ] Ước lượng tham số mô hình, batch size, context length.
- [ ] Chọn framework tương thích (CUDA, ROCm, XLA, SYCL).
- [ ] Đánh giá chi phí vận hành: điện, cooling, giấy phép phần mềm.
- [ ] Lên kế hoạch mở rộng: modular rack, fabric scale-out.
- [ ] Kiểm tra supply chain & lead time (H100/H200 6–9 tháng, TPU cloud chờ slot).
- [ ] Đánh giá TCO trong 3–5 năm: CAPEX (phần cứng) + OPEX (điện, bảo trì, license phần mềm).
- [ ] Lập kế hoạch bảo trì: spare parts, SLA với vendor, lịch vệ sinh/làm mát.

---

## 8. Tài nguyên tham khảo nhanh (Mở rộng)
- NVIDIA Datacenter Platform: <https://www.nvidia.com/en-us/data-center/>
- Google Cloud TPU: <https://cloud.google.com/tpu>
- AMD ROCm Docs: <https://rocmdocs.amd.com/>
- Intel Gaudi Software: <https://habana.ai/software/>
- TinyML Foundation: <https://www.tinyml.org/>
- MLPerf Benchmarks: <https://mlcommons.org/en/mlperf/>
- Microsoft MAIA AI Server reference: <https://learn.microsoft.com/en-us/azure/ai-infrastructure/maia>
- Open Compute Project (OCP) AI hardware specs: <https://www.opencompute.org/projects/ai-hardware>
- NVIDIA DGX H100 SuperPOD design guide: <https://resources.nvidia.com/en-us-dgx-systems/dgx-superpod>
- **Bonus:** [AI Hardware Technical Specs](./ai-hardware-specs.md) – bảng số liệu FLOPS/TOPs, HBM, TDP cho các accelerator & edge kit.

> **Tip:** Sử dụng MLPerf và case study của vendor để benchmark sơ bộ, sau đó chạy proof-of-concept với workload thực tế trước khi mua hàng loạt.