# Testing Frontend

## Phạm vi
- Unit/Component: Vitest hoặc Jest + Testing Library.
- E2E: Playwright hoặc Cypress.

## Chiến lược
- Test theo hành vi (user flows) thay vì chi tiết implementation.
- Mock network hợp lý; tránh over-mock gây giả.
- Kiểm tra a11y cơ bản (axe, aria roles).

## Gợi ý setup
- Vitest + Testing Library: render, userEvent, assertions.
- Playwright: smoke flows (auth, cart, checkout), CI mode headless.

## Liên quan
- Challenges: [challenges/web-ui](../../challenges/web-ui/README.md)