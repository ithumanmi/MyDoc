# Lab 2: Xây Dựng AI Micro-SaaS Với Vercel AI SDK (Next.js)

> [← Back to Labs AI/ML Focus](./README.md) | [Home](../../../README.md)

Lý thuyết về thiết kế hệ thống AI SaaS đã được trình bày tại [AI Engineering for SaaS](../advanced/ai-saas-engineering.md). Lab này đưa bạn từ số 0 đến việc dựng một UI tương tác y hệt ChatGPT có khả năng Stream text liên tục trên Next.js App Router mượt mà.

## 🛠️ Bước 1: Khởi Tạo Dự Án (Boilerplate)

Sử dụng cỗ máy `create-next-app`:
```bash
npx create-next-app@latest ai-micro-saas
# Các Tùy Chọn: 
# - TypeScript: Yes 
# - ESLint: Yes 
# - Tailwind CSS: Yes 
# - App Router: Yes
cd ai-micro-saas
```

Cài đặt package thần thánh `ai` (Vercel AI SDK) và `@ai-sdk/openai`:
```bash
npm install ai @ai-sdk/openai
```

Tạo file biến môi trường gốc `.env.local` ở thư mục dự án và vứt API Key của bạn (nạp tiền $5 vào openai trước nhé):
```env
OPENAI_API_KEY=sk-xxxxxx...
```

---

## ⚡ Bước 2: Setup API Route (Backend Endpoint)

Chúng ta không bao giờ gọi OpenAI trực tiếp từ Frontend (lộ API Key). Frontend gọi Backend của Next.js -> Backend gọi OpenAI, rồi *stream (trả về từng chữ)* về Frontend. Mở đầu bằng sự kiện `Edge Runtime`.

Tạo file: `app/api/chat/route.ts`

```typescript
import { openai } from '@ai-sdk/openai';
import { streamText } from 'ai';

// Tùy chọn Edge Runtime để response siêu nhanh
export const maxDuration = 30; // 30s max cho Vercel Hobby

export async function POST(req: Request) {
  // Bóc tách mảng messages (lịch sử chat) từ body do Frontend gửi tự động
  const { messages } = await req.json();

  // Route gọi lên OpenAI - Bạn đổi thành mô hình GPT-4o-mini cho siêu rẻ
  const result = await streamText({
    model: openai('gpt-4o-mini'),
    messages,
    // [Tuỳ CHỌN]: Đây là sức mạnh của Vercel SDK, bạn vứt thêm system prompt vào
    system: "Bạn là trợ lý ảo chỉ trả lời câu hỏi bằng tiếng Việt ngắn gọn tóm tắt trong vòng 3 câu.",
  });

  // Hồi trả theo chuẩn stream HTTP tiêu chuẩn! Mọi thứ còn lại Vercel AI lo!
  return result.toDataStreamResponse();
}
```

---

## 🎨 Bước 3: Giao Diện Chat (Frontend) & Custom State

Hệ thống cung cấp hook `useChat` quản lý nguyên cục state rườm rà "loading", "lịch sử chat", "append message".

Chỉnh sửa file giao diện chính `app/page.tsx`:

```tsx
'use client'; // Client Component bắt buộc vì có hook state 

import { useChat } from 'ai/react';
import { useEffect, useRef } from 'react';

export default function ChatDashboard() {
  const { messages, input, handleInputChange, handleSubmit, isLoading } = useChat({
    api: '/api/chat',  // Gắn đúng dường dẫn Route ban nãy
    initialMessages: [
         { id: '1', role: 'assistant', content: 'Xin chào! Tôi có thể giúp gì cho bạn hôm nay?' }
    ]
  });

  // Auto cuộn màn hình xuống dưới cùng (UX xịn)
  const messagesEndRef = useRef<HTMLDivElement>(null);
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  return (
    <div className="flex flex-col h-screen max-w-2xl mx-auto p-4 font-sans selection:bg-blue-300">
      <header className="py-4 border-b border-gray-200 mb-4 bg-white/70 backdrop-blur top-0 sticky z-10">
        <h1 className="text-xl font-bold text-gray-800 tracking-tight">AI Micro-SaaS Bot <span className="text-2xl">⚡</span></h1>
      </header>
      
      {/* Vùng Lịch Sử Chat */}
      <div className="flex-1 overflow-y-auto mb-4 space-y-4 pt-2 pb-24 px-2 custom-scrollbar">
        {messages.map(m => (
          <div key={m.id} className={`flex ${m.role === 'user' ? 'justify-end' : 'justify-start'}`}>
            <div 
              className={`max-w-[85%] rounded-2xl p-4 shadow-sm text-sm leading-relaxed ${
                m.role === 'user' 
                ? 'bg-blue-600 text-white rounded-br-sm' 
                : 'bg-white border text-gray-800 border-gray-100 rounded-bl-sm ring-1 ring-black/5'
              }`}
            >
              <div className="font-semibold mb-1 opacity-80 text-xs uppercase tracking-wider">
                {m.role === 'user' ? 'Tôi' : 'AI Assistant'}
              </div>
              <div className="whitespace-pre-wrap">{m.content}</div>
            </div>
          </div>
        ))}
        {/* Nơi ref chỉ để cuộn chuột tới */}
        <div ref={messagesEndRef} />
      </div>

      {/* Box Nhập Liệu Cố Định dưới Màn Hình */}
      <div className="fixed bottom-0 box-border p-4 bg-gradient-to-t w-full max-w-2xl mx-auto from-white via-white/95 to-transparent pb-8">
        <form onSubmit={handleSubmit} className="relative flex shadow-md ring-1 ring-gray-200 rounded-full bg-white overflow-hidden transition-all focus-within:ring-2 focus-within:ring-blue-500 focus-within:shadow-lg">
          <input
            className="w-full p-4 pl-6 outline-none bg-transparent placeholder-gray-400 text-gray-800 text-sm"
            value={input}
            placeholder={isLoading ? 'Đang suy nghĩ...' : 'Hỏi bất cứ điều gì (ví dụ: Tóm tắt chiến tranh thế giới)...'}
            onChange={handleInputChange}
            disabled={isLoading}
          />
          <button 
            type="submit" 
            disabled={isLoading || !input.trim()}
            className={`px-6 py-2 m-2 h-10 w-10 shrink-0 text-white rounded-full flex items-center justify-center transition-colors 
              ${(!input.trim() || isLoading) ? 'bg-gray-300 cursor-not-allowed' : 'bg-blue-600 hover:bg-blue-700 active:scale-95'}`}
          >
           ↗ 
          </button>
        </form>
      </div>
    </div>
  );
}
```

Thêm style nhẹ vào `app/globals.css`:
```css
@tailwind base;
@tailwind components;
@tailwind utilities;

body {
  background-color: #fafafa;
}

.custom-scrollbar::-webkit-scrollbar {
  width: 6px;
}
.custom-scrollbar::-webkit-scrollbar-track {
  background: transparent;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background-color: rgba(0,0,0,0.1);
  border-radius: 10px;
}
```

---

## 🚀 Bước 4: Chạy Đồ Án!

Mở Terminal và khởi động Dev Server.

```bash
npm run dev
```
Đến trình duyệt mở `http://localhost:3000`. Cùng kiểm tra, ấn chữ, và bạn sẽ thấy chữ của GPT "phi về dồn dập" nhờ Edge Streaming của App Router API thay vì đợi cục súc nguyên đoạn.

Giao diện mẫu của chúng ta sử dụng Vanilla Tailwind mượt mà, bóng tròn kính viền hiện đại (Glassmorphism), UX auto-scroll yakuza! 😎. 

---

## 🛡️ (Tự luyện tập Plus) Bước 5: Thử Thách Bảo Vệ Hóa Đơn (Rate Limit)

Mã nguồn trên đã là "Sản phẩm", nhưng chưa phải là "Doanh nghiệp (Micro-SaaS)".
Đăng ký thẻ Credit Card và tung link lên Reddit, 2 tiếng sau có **ai đó chạy bot gõ 50K Requests ném vào form**. *Vỡ hoá đơn vì không Limit!*

Bài tập gợi ý: Hãy tích hợp [Upstash Redis Rate limit](https://upstash.com/docs/redis/sdks/ratelimit-ts/features) chèn vào đầu file `route.ts`. 

```typescript
// Ý Tưởng Logic: (Mã giả)
const identifier = req.ip || 'anonymous';
const { success } = await ratelimit.limit(identifier);

if (!success) {
    return new Response('Từ từ thôi bro, rate limit rồi.', { status: 429 });
}
// Vượt qua mới được gọi streamText(..)!
```
