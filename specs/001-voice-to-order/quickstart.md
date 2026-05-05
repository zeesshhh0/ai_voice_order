# Quickstart: Voice-to-Order Validation

## Verification Scenarios

### Scenario 1: Standard Order (MVP)
1. User provides audio: "Order two burgers from McDonald's"
2. **Expectation**: 
    - Intent: `PLACE_ORDER`
    - Items: `[{name: "burger", quantity: 2}]`
    - Restaurant: `McDonald's`

### Scenario 2: Hinglish/Mixed Language
1. User provides audio: "2 dosa order karna hai"
2. **Expectation**:
    - Intent: `PLACE_ORDER`
    - Items: `[{name: "dosa", quantity: 2}]`
    - Language Detected: `mixed`

### Scenario 3: Ambiguous/Unintelligible
1. User provides static/noise.
2. **Expectation**:
    - Response: "Please repeat your command"
    - `confidence` < 0.5
