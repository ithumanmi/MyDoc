# Lab: Viết Load Balancer & API Reverse Proxy bằng Go

> [← Quay lại Backend Labs](./README.md)

Mục tiêu: hiểu reverse proxy + round-robin và tự triển khai API Gateway cơ bản bằng Go (`net/http/httputil`).

---

## 📐 Kiến trúc

1) Client gửi request vào gateway `http://localhost:8080`.
2) 3 service giả lập chạy local (3001, 3002, 3003).
3) Gateway chọn backend round-robin và forward request.

---

## ⚙️ Thực hành

Khởi tạo project Go:
```bash
mkdir go-api-gateway && cd go-api-gateway
go mod init go-api-gateway
touch main.go
```

Code `main.go` (tập trung round-robin + reverse proxy):

```go
package main

import (
    "log"
    "net/http"
    "net/http/httputil"
    "net/url"
    "sync/atomic"
)

var backends = []string{
    "http://localhost:3001",
    "http://localhost:3002",
    "http://localhost:3003",
}

var counter uint64

func nextBackend() string {
    idx := atomic.AddUint64(&counter, 1)
    return backends[idx%uint64(len(backends))]
}

func proxyHandler(w http.ResponseWriter, r *http.Request) {
    target := nextBackend()
    targetURL, _ := url.Parse(target)

    log.Printf("Gateway chuyển tiếp tới: %s", target)

    proxy := httputil.NewSingleHostReverseProxy(targetURL)

    // Gắn header trace ID (ví dụ đơn giản)
    r.Header.Set("X-Request-ID", "demo-trace-id")

    proxy.ServeHTTP(w, r)
}

func main() {
    http.HandleFunc("/", proxyHandler)

    port := ":8080"
    log.Printf("API Gateway đang lắng nghe %s", port)

    if err := http.ListenAndServe(port, nil); err != nil {
        log.Fatalf("Gateway lỗi: %v", err)
    }
}
```

Chạy thử và kiểm tra log:

```bash
go run main.go
```

Dùng curl/gửi vài request liên tiếp:

```bash
curl -v http://localhost:8080
```

Quan sát log: request sẽ lần lượt tới 3001 → 3002 → 3003 (round-robin). Thêm backend mới chỉ cần thêm vào `backends`.
