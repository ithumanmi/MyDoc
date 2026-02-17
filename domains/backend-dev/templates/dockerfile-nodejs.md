# 🐳 Optimized Dockerfile for Node.js (Multi-stage Build)

> [← Back to DevOps Guide](../devops-sre/docker-k8s-guide.md)

Mẫu Dockerfile này sử dụng kỹ thuật **Multi-stage build** để giảm kích thước image cuối cùng (từ ~500MB xuống ~100MB) và tăng tính bảo mật.

```dockerfile
# ----------------------------
# Stage 1: Build Stage
# ----------------------------
FROM node:18-alpine AS builder

# Thiết lập thư mục làm việc
WORKDIR /app

# Copy package.json và package-lock.json trước
# (Tận dụng Docker cache layers: Nếu không đổi dependencies thì không cần npm install lại)
COPY package*.json ./

# Cài đặt dependencies (bao gồm cả devDependencies để build nếu cần)
RUN npm ci

# Copy toàn bộ source code
COPY . .

# Build ứng dụng (nếu dùng TypeScript/NestJS/React)
RUN npm run build

# ----------------------------
# Stage 2: Production Stage
# ----------------------------
FROM node:18-alpine AS runner

WORKDIR /app

# Chỉ copy những file cần thiết từ Stage 1
COPY --from=builder /app/package*.json ./
COPY --from=builder /app/dist ./dist
# (Nếu không có bước build, copy /src thay vì /dist)

# Chỉ cài đặt production dependencies (bỏ qua devDependencies như eslint, jest)
RUN npm ci --only=production

# Tạo user non-root để tăng bảo mật
RUN addgroup -g 1001 -S nodejs
RUN adduser -S nodejs -u 1001
USER nodejs

# Mở cổng ứng dụng
EXPOSE 3000

# Chạy ứng dụng
CMD ["node", "dist/main.js"]
```

### Tại sao dùng Multi-stage build?
1.  **Small Size:** Image cuối cùng không chứa source code gốc (chỉ chứa file build), không chứa `node_modules` thừa (devDependencies).
2.  **Security:** Không chứa các tool build, compiler, giảm bề mặt tấn công.
3.  **Performance:** Pull image nhanh hơn, deploy nhanh hơn.
