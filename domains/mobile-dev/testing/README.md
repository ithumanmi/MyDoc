# Testing

Chiến lược test: Unit, Widget/Component, Integration/E2E.

## Nội dung chính
- Unit: logic thuần, use case.
- Widget/Component: UI isolate; stub/mock dependencies.
- Integration/E2E: flow chính, navigation, network mock hoặc sandbox.

## Tooling
- Flutter: `flutter_test`, `bloc_test`, `mocktail`; golden test nếu cần.
- React Native: Jest, React Testing Library, MSW; Detox/Maestro cho E2E.

## Liên quan
- E2E & automation: [e2e-and-automation.md](e2e-and-automation.md)