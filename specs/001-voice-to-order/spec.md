# Feature Specification: Voice-to-Order AI System

**Feature Branch**: `001-voice-to-order`  
**Created**: 2025-05-22  
**Status**: Draft  
**Input**: Voice-to-Order AI System SRS PDF + Architecture Guidance

## Clarifications

### Session 2025-05-22
- Q: How should the system respond when audio is unintelligible or STT confidence is low? → A: Prompt the user via UI/Voice to "Please repeat your command".
- Q: If a user omits the restaurant, how should the system resolve the ambiguity? → A: Default to the "Last Ordered" restaurant automatically and inform the user.
- Q: How should the "Order Placement" intent be finalized? → A: Agent only drafts: User MUST manually click a button in the UI to finalize.
- Q: How should the system handle "My last restaurant" without authentication? → A: Use a guest "Session ID" that expires after 24 hours.
- Q: How should the user modify a draft order via voice? → A: Natural language re-statement.
- Q: How should the system handle service-level STT failures? → A: Agent state update: `status: STT_FAILED`, then prompt user to "Try again later".
- Q: Which audio capture mechanism should the frontend prioritize? → A: Standard `MediaRecorder` API.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Voice-Based Food Ordering (Priority: P1)

As a hungry user, I want to place a food order by speaking naturally (e.g., "Order 2 paneer pizzas") so that I can order quickly without navigating complex menus.

**Why this priority**: Core functionality that delivers the primary value proposition of the system.

**Independent Test**: User records audio → System transcribes → Detects "Place Order" intent → Extracts items and quantities → Shows in cart.

**Acceptance Scenarios**:
1. **Given** the app is open, **When** I say "Order 2 paneer pizzas", **Then** the cart shows 2 Paneer Pizzas and a "Place Order" button appears.
2. **Given** a previous order exists, **When** I say "from my last restaurant", **Then** the system identifies the restaurant from history.
3. **Given** an item is in the cart, **When** the user clicks "Place Order", **Then** the order is sent to the restaurant.

---

### User Story 2 - Mixed-Language Support (Priority: P2)

As a bilingual user, I want to use Hinglish (e.g., "2 dosa order karna hai") so that I can speak in my most comfortable dialect.

**Why this priority**: Critical for accessibility and user adoption in diverse linguistic regions.

**Independent Test**: User records "2 dosa order karna hai" → System identifies "Place Order" intent and extracts "2 dosa".

---

### User Story 3 - Order Modification & Cancellation (Priority: P3)

As a user who changed my mind, I want to modify or cancel my order via voice before final placement.

**Why this priority**: Essential for a complete commerce experience.

**Acceptance Scenarios**:
1. **Given** an item is in the cart, **When** I say "Cancel my order", **Then** the cart is cleared.
2. **Given** 2 pizzas are in the cart, **When** I say "Actually, make it 3 pizzas", **Then** the cart is updated to show 3 pizzas.

### Edge Cases

- **Unintelligible Audio**: If audio is too noisy or STT confidence is below a defined threshold, the system MUST NOT attempt to guess the order and instead MUST prompt the user to repeat the command.
- **Missing Restaurant**: If the user omits the restaurant, the system SHOULD default to the last-used restaurant (if history exists) and explicitly inform the user: "Ordering from [Restaurant Name]...".
- **Ambiguous Menu Query**: If the user asks "What is on the menu?" without specifying a restaurant, the system MUST default to showing the menu of the last-ordered restaurant.
- **Ambiguous Modification**: If a natural language re-statement is ambiguous (e.g., "Change that"), the system MUST prompt the user for clarification: "Which item should I change?".
- **STT Service Failure**: In the event of an STT API timeout or failure, the system MUST update the agent state to `STT_FAILED` and inform the user to "Try again later".

## Agentic Considerations *(mandatory)*

- **Node Decomposition**: 
    - `TranscriptionNode`: Interface with Google Cloud STT.
    - `IntentNode`: Analyze transcript to classify intent (Order, Reorder, Cancel, etc.).
    - `EntityExtractionNode`: Extract structured details (Items, Qty, Add-ons).
    - `ContextNode`: Fetch user history/last restaurant from PostgreSQL.
    - `ValidationNode`: Verify order completeness using Pydantic.
- **State Management**: `transcript`, `detected_intent`, `order_details` (Pydantic model), `context_data`, `is_complete`.
- **LLM Outputs**: 
    - `IntentModel`: Enum of [PLACE_ORDER, REORDER, MODIFY, CANCEL, ASK_MENU].
    - `OrderModel`: List of `OrderItem` (name, qty, extras).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST capture audio from the user interface using the standard `MediaRecorder` API.
- **FR-002**: System MUST convert audio to text using a high-accuracy speech-to-text service.
- **FR-003**: System MUST detect intents including "Place Order", "Reorder", "Modify", "Cancel", and "Ask Menu".
- **FR-004**: System MUST extract entities: Item Name, Quantity, Restaurant, Size, and Special Instructions.
- **FR-005**: System MUST support mixed-language (English/Hindi) commands.
- **FR-006**: System MUST persist voice sessions and orders in a secure database.
- **FR-007**: System MUST show a parsed order summary in the UI for user confirmation.

### Key Entities

- **User**: Name, Contact, Language Preference.
- **Voice Session**: Audio File link, Transcript, Confidence Score.
- **Order**: Items, Restaurant Ref, Status (Pending/Placed).
- **Extracted Entity**: Item Name, Quantity, Language Type.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can complete a simple order placement in under 30 seconds.
- **SC-002**: Intent detection accuracy reaches 90% for standard ordering phrases.
- **SC-003**: System processes audio and returns the parsed result in under 3 seconds (excluding network latency).

## Assumptions

- High-speed internet is available for Google Cloud STT calls.
- User history is available for "reorder" or "last restaurant" scenarios via a temporary guest Session ID (24-hour expiration).
- The system initially supports English and Hindi/Hinglish.
stem initially supports English and Hindi/Hinglish.
