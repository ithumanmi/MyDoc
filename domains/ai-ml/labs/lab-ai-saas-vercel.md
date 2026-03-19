# Lab 2: AI Micro-SaaS với Vercel AI SDK (Next.js)

> [← Back to Labs AI/ML Focus](./README.md) | [Home](../../../README.md)

Mục tiêu: dựng UI chat giống ChatGPT trên Next.js (App Router) dùng Vercel AI SDK, streaming từ backend.

## 🛠️ Bước 1: Khởi tạo dự án

Tạo Next.js + Tailwind + TypeScript:
```bash
npx create-next-app@latest ai-micro-saas
# Các Tùy Chọn: 
# - TypeScript: Yes 
# - ESLint: Yes 
# - Tailwind CSS: Yes 
# - App Router: Yes
cd ai-micro-saas
```

Thêm Vercel AI SDK:
```bash
npm install ai @ai-sdk/openai
```

Tạo file biến môi trường gốc `.env.local` ở thư mục dự án và vứt API Key của bạn (nạp tiền $5 vào openai trước nhé):
```env
OPENAI_API_KEY=sk-xxxxxx...
```

---

## ⚡ Bước 2: API route backend (streaming)

Frontend gọi backend; backend gọi OpenAI và stream phản hồi.

Tạo file: `app/api/chat/route.ts`

```typescript
import { openai } from '@ai-sdk/openai';
import { streamText } from 'ai';

// Tùy chọn Edge Runtime để response siêu nhanh
export const maxDuration = 30; // 30s trên Vercel Hobby

export async function POST(req: Request) {
  // Nhận lịch sử messages từ frontend
  const { messages } = await req.json();

  // Route gọi lên OpenAI - Bạn đổi thành mô hình GPT-4o-mini cho siêu rẻ
  const result = await streamText({
    model: openai('gpt-4o-mini'),
    messages,
    // Có thể thêm system prompt
    system: "Bạn là trợ lý ảo chỉ trả lời câu hỏi bằng tiếng Việt ngắn gọn tóm tắt trong vòng 3 câu.",
  });

  // Trả về stream HTTP
  return result.toDataStreamResponse();
}
```

---

## 🎨 Bước 3: Giao diện chat (frontend)

`useChat` quản lý state, streaming, input.

Chỉnh sửa file giao diện chính `app/page.tsx`:

```tsx
'use client'; // Client Component bắt buộc vì có hook state 

import { useChat } from 'ai/react';
import { useEffect, useRef } from 'react';

export default function ChatDashboard() {
  const { messages, input, handleInputChange, handleSubmit, isLoading } = useChat({
    api: '/api/chat',
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
        {/* Ref để auto-scroll */}
        <div ref={messagesEndRef} />
      </div>

      {/* Ô nhập cố định dưới màn hình */}
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

## 🚀 Bước 4: Chạy dev

```bash
npm run dev
```
Mở `http://localhost:3000` và thử chat; streaming hoạt động qua API route.

---

## 🛡️ Bước 5: Rate limit (bài tập thêm)

Thêm Upstash Redis Rate Limit vào `route.ts` để tránh lạm dụng:

```typescript
// Ý Tưởng Logic: (Mã giả)
const identifier = req.ip || 'anonymous';
const { success } = await ratelimit.limit(identifier);

if (!success) {
    return new Response('Từ từ thôi bro, rate limit rồi.', { status: 429 });
}
// Vượt qua mới được gọi streamText(..)!
```
