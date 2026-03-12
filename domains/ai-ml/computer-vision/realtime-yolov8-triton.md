## 📹 Realtime Inference — YOLOv8 + Triton + Camera Stream

> [← Back to Object Detection Guide](./object-detection-guide.md)

Hướng dẫn dựng pipeline real-time: Camera → Triton Inference Server → Dashboard.

---

## 1. Kiến trúc tổng quan

```
Camera / RTSP ---> Client App (Python) ---> Triton Inference Server (YOLOv8) ---> Metrics / Dashboard
```

1. **Client**: Lấy frame từ webcam/RTSP, preprocess, gửi request gRPC/HTTP.
2. **Triton Server**: Chạy YOLOv8 ONNX/TensorRT.
3. **Dashboard**: Stream kết quả + log metrics (latency, FPS).

---

## 2. Chuẩn bị model

```bash
pip install ultralytics onnx

yolo export model=yolov8m.pt format=onnx imgsz=640 dynamic=True

trtexec --onnx=yolov8m.onnx --saveEngine=yolov8m.plan --fp16
```

Tạo folder Triton:

```
yolov8/
├── 1/
│   ├── model.plan
│   └── config.pbtxt
└── config.pbtxt
```

**config.pbtxt**

```
name: "yolov8"
platform: "tensorrt_plan"
max_batch_size: 4
input {
  name: "images"
  data_type: TYPE_FP32
  dims: [3, 640, 640]
}
output {
  name: "output0"
  data_type: TYPE_FP32
  dims: [84, 8400]
}
dynamic_batching {
  preferred_batch_size: [1,2,4]
  max_queue_delay_microseconds: 1000
}
```

---

## 3. Chạy Triton

```bash
tritonserver --model-repository=./yolov8 --http-port=8000 --grpc-port=8001
```

---

## 4. Client Python (gRPC stream)

```python
import cv2
import numpy as np
from tritonclient.grpc import InferenceServerClient, InferInput

client = InferenceServerClient(url="localhost:8001")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    img = preprocess(frame)  # resize, normalize
    inputs = [InferInput("images", img.shape, "FP32")]
    inputs[0].set_data_from_numpy(img)
    result = client.infer("yolov8", inputs)
    detections = postprocess(result.as_numpy("output0"))
    render(frame, detections)
    cv2.imshow("YOLOv8", frame)
    if cv2.waitKey(1) == 27:
        break
```

---

## 5. Monitoring & Dashboard

*   Enable Triton metrics `--metrics-port=8002`, scrape bằng Prometheus.
*   Dùng Streamlit/FastAPI để hiển thị video stream + stats (FPS, latency).
*   Log prediction vào Kafka/S3 để audit.

---

## 6. Tips

*   **Latency**: Dùng TensorRT FP16 hoặc INT8.
*   **Scaling**: Autoscale Triton pods bằng HPA (GPU utilization).
*   **Edge deployment**: Dùng Jetson + DeepStream.

> ⚡ Tip: Với workload multi-model, dùng Triton Model Ensemble để chain preprocessing → YOLO → tracking trong server.
