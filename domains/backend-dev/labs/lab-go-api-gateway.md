# Lab: Tự Code Load Balancer & API Reverse Proxy Bằng Golang Nguyên Bản

> [← Back to Backend Labs](./README.md)

Nginx là một phần mềm C viết sẵn Load Balancer đỉnh cao. Nhưng bạn CÓ HIỂU thuật toán chia tải dưới vỏ bọc C đó Tự Vận Hành Ra Sao Để Viết API Gateway Dành Riêng Không?
Hãy dùng `net/http/httputil` Của Golang Tự Tạo Mặt Kính Này. Golang Đỉnh Chóp Sinh Ra Từ Google Để Ném Mọi Network Lệnh Nhờ Cơ Chế Giao Địch Rẽ Coroutine (Goroutines).

---

## 📐 Kiến Trúc Rọt: 

1. Chúng ta sẽ có Mọt Mảnh Client (Trang Web/Postman) Cháy Request Gọi Cổng `http://localhost:8080` Mù Quáng (Server Proxy Golang).
2. Chúng Vừa Có 3 Trạm Fake Microservice Ếu Kém Chạy Trống Trên Máy Local Backend Giả Bộ Réo Kêu (Cổng 3001, 3002, 3003). 
3. Code Golang Sẽ Mưu Đồ Trả Phân Vào Gí Bằng Hàm (Xắp Lượt Điểm Giao) Round-Robin Vô Luồng Lướt 3 Cổng Vòng.

---

## ⚙️ Bắt Tay Làm Bụi Đất System

Khởi tạo Go module:
```bash
mkdir go-api-gateway && cd go-api-gateway
go mod init go-api-gateway
touch main.go
```

Dìm Bộ Thủ Đoạn Vào Code `main.go`. Móc Nhúng Thư Viện Chắn HTTP Sẵn Lọc Golang:

```go
package main

import (
	"fmt"
	"log"
	"net/http"
	"net/http/httputil"
	"net/url"
	"sync"
	"sync/atomic"
)

// List Hệ Băng Danh Sach Backend Đang Nhốt Góc Trọ Lặng Lẽ 
var DanhSachCumTuServer = []string{
	"http://localhost:3001",
	"http://localhost:3002",
	"http://localhost:3003",
}

// Giữ Máy Trục Hiện Trạng Vòng Đếm Chống Sai Lock Sợ Concurrent. 
var CuaQuayTuThienTai uint64 = 0

// Thuat TOÁN Xích Vòng Trượt Đếm Lược Cho Đếm Búa Round Robin (Trả Đếm Lấy 1 Server Index Để Chia Tải Đều Nhóm Góc)
func BatGiamThangServerTiepTheoToiDien() string {
	LuotTruc := atomic.AddUint64(&CuaQuayTuThienTai, 1) // Atomically Tăng An Toàn Đội Threads Tới Nghẽn Kẻo Cụng Lỗi Xé RAM
	BocKhoaTungServerDiVaoThongKinh := LuotTruc % uint64(len(DanhSachCumTuServer))
	return DanhSachCumTuServer[BocKhoaTungServerDiVaoThongKinh]
}

// Cầu Thủ Hút Giao Đầu Lọc Mọi Request Gởi Server Proxy Gặp Kê Ở Đây 
func BanCuaProxyDaoHuongTraServerQuen(w http.ResponseWriter, r *http.Request) {
	// Lọc Thuật Đoán Mốc Quay Vòng Gặp Máy Cũ Đi Thằng Node Tới Máy Kia Load Nặng:
	DuongDanCongMayKhachBiMat := BatGiamThangServerTiepTheoToiDien()
	TruongDuongToaDoHopLuaGo, _ := url.Parse(DuongDanCongMayKhachBiMat)

	// In Ra Cửa Chờ Log Console Go Phé Lỗ Xem Đứa Gateway Đẩy Phân Nào Trúng Dòng Tên Chắn API Load Banlance
	log.Printf("[TRẠM GATEWAY NHẬN LỆNH] Client Đích Hướng Nát Rớt Request Dẫn Vào Đuôi Trạm: %s\n", DuongDanCongMayKhachBiMat)

	// Gọi Tướng Đỡ Proxy Tốc Lọc (ReverseProxy Built-in Thuộc Golang Cấm Rút Tốc Kinh Khủng Nhờ Socket Thẳng Tiêu Hủy Nhanh!)
	VongXoayTheThanChongLaiProxy := httputil.NewSingleHostReverseProxy(TruongDuongToaDoHopLuaGo)

	// Bùa Tiên Gateway Bắn Gắn Header TRACING Thần Tốc Theo Dõi Logging Lạch Mạch User (Kẹp Data Riêng Giữa Bụi Thám Xông).
	r.Header.Set("X-Trace-Id-Gateway-Chuc", "Mã_Định_Lược_Dấu_Thâm_76AXYZ")

	// Thực Cầu Xuyên Hành Tới Nơi Đích 
	VongXoayTheThanChongLaiProxy.ServeHTTP(w, r)
}

func main() {
	// Rẽ Góc Chết Phục Tường Kính Ở Đâu Cũng Đi Cổng Này:
	http.HandleFunc("/", BanCuaProxyDaoHuongTraServerQuen)
	
	CONG_LUAN_MAY_CHU_GO := ":8080"
	log.Printf("== API GATEWAY ĐANG ĐỨNG CANH TẠI QUẦY THU HTTP CỔNG %s ==\n", CONG_LUAN_MAY_CHU_GO)
	
	// Khựng Run Đóng Ràng Chết Lỗi Server Không Drop Exit Tắt Rừng Main Độc Đứng: 
	if loiXayCat := http.ListenAndServe(CONG_LUAN_MAY_CHU_GO, nil); loiXayCat != nil {
		log.Fatalf("Server Cheết Máy Dập Dạng Nát: %v", loiXayCat)
	}
}
```

Kiểm Tra Lại Bằng Lệnh `go run main.go`. Dùng Terminal Bắn Nhanh Vài Tíu Tiền Request Bằng Tường Cửa Lưới Curl Lạch Xịch Rộng:
`curl -v http://localhost:8080`
Chớp Mắt Thấy Tụ Màn Console Quay Log Thay Đổi: Trật Máy Đưa Rớt Node 3001, Giao Tiếp Qua Tụ Vào 3002 Xong 3003 Thỏa Phân Chia API Thẳng Bước Sang Kiến Trúc Chằng Chắn Microservice Go API Nhận! Không Run Chạy Xuyên Bão Tải Go Mật!
