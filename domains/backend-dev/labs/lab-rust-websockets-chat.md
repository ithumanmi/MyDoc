# Lab: Rust WebSockets Chat Server hiệu năng cao (C10K)

> [← Quay lại Backend Labs](./README.md)

Mục tiêu: xây chat server WebSockets bằng Rust + Tokio + Tungstenite, xử lý hàng nghìn kết nối đồng thời với mức RAM thấp.

---

## 🛠️ Chuẩn bị

Tạo dự án:

```bash
cargo new rust-ws-chat
cd rust-ws-chat
```

`Cargo.toml`:

```toml
[dependencies]
tokio = { version = "1", features = ["full"] }
tokio-tungstenite = "0.21"
futures = "0.3"
```

---

## 🏗️ Server WebSockets đơn giản (`src/main.rs`)

```rust
use futures::{StreamExt, SinkExt};
use tokio::net::TcpListener;
use tokio_tungstenite::{accept_async, tungstenite::protocol::Message};

#[tokio::main]
async fn main() {
    let listener = TcpListener::bind("127.0.0.1:9001").await.unwrap();
    println!("WebSocket server listening on 9001");

    while let Ok((stream, addr)) = listener.accept().await {
        println!("New client: {}", addr);
        tokio::spawn(handle_connection(stream));
    }
}

async fn handle_connection(stream: tokio::net::TcpStream) {
    let ws_stream = accept_async(stream).await.unwrap();
    let (write, read) = ws_stream.split();

    // Echo lại các message text/binary
    read
        .filter_map(|msg| async move {
            match msg {
                Ok(m) if m.is_text() || m.is_binary() => Some(m),
                _ => None,
            }
        })
        .forward(write)
        .await
        .ok();
}
```

---

## 🚀 Chạy thử và quan sát

```bash
cargo run
```

Kết nối thử bằng wscat/Postman/browser console:

```javascript
const ws = new WebSocket("ws://127.0.0.1:9001");
ws.onmessage = (e) => console.log(e.data);
ws.onopen = () => ws.send("hello");
```

Mở nhiều kết nối để kiểm tra mức RAM. Rust + Tokio thường giữ footprint thấp ngay cả khi tải cao; có thể mở rộng thêm broadcast channel nếu muốn phòng chat nhiều người.
