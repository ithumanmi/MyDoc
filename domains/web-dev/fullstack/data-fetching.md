# Data Fetching (REST/GraphQL/tRPC)

## Lựa chọn
- REST: đơn giản, cache-friendly (HTTP semantics).
- GraphQL: flexible query, giảm over-fetch; cần schema/server.
- tRPC: typesafe end-to-end cho TS/Next stack.

## Client data layer
- React Query/SWR: caching, revalidation, mutations, optimistic update.
- Server Components (Next): fetch server-side, stream; khi nào dùng client component.

## Thực hành
- Chuẩn hóa error/loading states.
- Retry/backoff, pagination/infinite scroll.
- Cache keys, invalidation.