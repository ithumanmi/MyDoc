# 🧪 Testing Strategies: Building Confidence in Your Code

> [← Back to Backend Roadmap](./README.md) | [Home](../../README.md)

Developer nghiệp dư viết code rồi "hy vọng" nó chạy. Developer chuyên nghiệp viết test để **chứng minh** nó chạy. Hướng dẫn này giúp bạn ngủ ngon mỗi khi deploy.

---

## 📋 Mục lục

1. [Test Pyramid](#1-test-pyramid-chiến-lược-kiểm-thử)
2. [Unit Testing](#2-unit-testing-kiểm-thử-đơn-vị)
3. [Integration Testing](#3-integration-testing-kiểm-thử-tích-hợp)
4. [E2E Testing](#4-e2e-testing-end-to-end)
5. [Load Testing](#5-load-testing-kiểm-thử-tải)
6. [TDD (Test Driven Development)](#6-tdd-test-driven-development)
7. [Action Plan](#7-action-plan-bắt-đầu-từ-đâu)

---

## 1. Test Pyramid: Chiến lược kiểm thử

Không phải test nào cũng giống nhau. Google/Netflix dùng mô hình Kim tự tháp:

1.  **Unit Tests (70%):** Test từng function/class nhỏ. Chạy cực nhanh (ms). Rẻ.
2.  **Integration Tests (20%):** Test API, Database connection. Chậm hơn (s).
3.  **E2E Tests (10%):** Test luồng người dùng thật (Browser, Full stack). Rất chậm (min). Đắt.

**Sai lầm:** "Ice Cream Cone" (Ít Unit test, toàn test tay/E2E) → Debug ác mộng.

---

## 2. Unit Testing: Kiểm thử đơn vị

Test logic nghiệp vụ thuần túy (Pure functions), không dính đến Database hay Network.

### 2.1. Jest (Node.js) Example

**Code (math.js):**
```javascript
function add(a, b) {
  return a + b;
}
module.exports = add;
```

**Test (math.test.js):**
```javascript
const add = require('./math');

test('adds 1 + 2 to equal 3', () => {
  expect(add(1, 2)).toBe(3);
});
```

### 2.2. Mocking

Khi function gọi external dependencies (DB, API), ta phải **Mock** (làm giả) chúng.

```javascript
// Test userService.getUser(id)
// Không query DB thật, mà giả lập DB trả về user
const mockDb = {
  findUser: jest.fn().mockReturnValue({ id: 1, name: 'Test' })
};

test('getUser returns user name', () => {
  const user = userService.getUser(1, mockDb);
  expect(user.name).toBe('Test');
  expect(mockDb.findUser).toHaveBeenCalledWith(1);
});
```

### 2.3. Code Coverage

Bao nhiêu là đủ?
*   **Junior:** 0% (Không viết test).
*   **Mid:** 100% (Cố gắng test cả getter/setter vô nghĩa).
*   **Senior:** ~80%. Tập trung vào **Critical Path** (Payment, Auth).

---

## 3. Integration Testing: Kiểm thử tích hợp

Test xem các phần (API + DB + Cache) có hoạt động cùng nhau không.

### 3.1. Supertest (Node.js)

Gửi HTTP request thật đến API endpoint.

```javascript
const request = require('supertest');
const app = require('./app');

describe('POST /users', () => {
  it('responds with json', async () => {
    const res = await request(app)
      .post('/users')
      .send({ name: 'john' })
      .set('Accept', 'application/json');
      
    expect(res.status).toEqual(201);
    expect(res.body.id).toBeDefined();
  });
});
```

### 3.2. Testcontainers

Đừng mock Database ở tầng này! Hãy dùng **Docker** để spin up một DB thật, sạch sẽ cho mỗi lần test.
*   Setup: Start Postgres Container.
*   Run Test: Insert data → Call API → Check DB.
*   Teardown: Destroy Container.

---

## 4. E2E Testing: End-to-End

Mô phỏng hành vi người dùng thật sự trên Browser.

### 4.1. Playwright / Cypress

```javascript
// Playwright Example
test('Login flow', async ({ page }) => {
  await page.goto('https://myapp.com/login');
  await page.fill('#email', 'user@example.com');
  await page.fill('#password', 'secret');
  await page.click('#submit');
  
  await expect(page).toHaveURL('https://myapp.com/dashboard');
});
```

---

## 5. Load Testing: Kiểm thử tải

API chạy ngon với 1 user, nhưng 10,000 user thì sao?

### 5.1. k6 (Modern Tool)

Viết test script bằng JavaScript.

```javascript
import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  vus: 100, // 100 Virtual Users
  duration: '30s',
};

export default function () {
  let res = http.get('https://test.k6.io');
  check(res, { 'status was 200': (r) => r.status == 200 });
  sleep(1);
}
```

### 5.2. Metrics cần quan tâm

*   **RPS (Requests Per Second):** Hệ thống chịu được bao nhiêu?
*   **Latency P95/P99:** 95% users nhận phản hồi dưới bao nhiêu ms? (VD: P95 < 200ms).
*   **Error Rate:** % request bị lỗi (500/503).

---

## 6. TDD (Test Driven Development)

Quy trình ngược: Viết Test trước → Viết Code sau.

1.  **Red:** Viết test (nó sẽ fail vì chưa có code).
2.  **Green:** Viết code vừa đủ để pass test.
3.  **Refactor:** Tối ưu code (vẫn giữ test pass).

**Lợi ích:** Code clean hơn, ít bug hơn, design tốt hơn.

---

## 7. Action Plan: Bắt đầu từ đâu

Đừng cố đạt 100% coverage ngay.

1.  **Level 1 (Bắt buộc):** Setup Jest/xUnit. Viết Unit test cho các hàm tiện ích (utils, helpers).
2.  **Level 2 (Quan trọng):** Viết Integration test cho các API quan trọng nhất (Login, Checkout).
3.  **Level 3 (Senior):** Setup CI/CD để tự động chạy test khi Push code.

> **Tư duy:** Test không phải để tìm bug. Test là để **Document** hành vi của code và bảo vệ bạn khi Refactor.
