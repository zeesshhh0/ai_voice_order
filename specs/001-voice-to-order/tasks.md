---

description: "Task list for Voice-to-Order AI System implementation"
---

# Tasks: Voice-to-Order AI System

**Input**: Design documents from `/specs/001-voice-to-order/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

**Organization**: Tasks are grouped by user story to enable independent implementation and testing.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create backend project structure (api, agents, models, schemas, services)
- [ ] T002 Initialize FastAPI project with LangGraph and Pydantic dependencies in backend/pyproject.toml
- [ ] T003 Create frontend project structure (components, hooks, state)
- [ ] T004 Initialize Next.js project with Tailwind and MediaRecorder hooks in frontend/package.json
- [ ] T005 [P] Configure shared linting and formatting for Python and TypeScript

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure for Agentic nodes and Database connectivity

- [ ] T006 Setup PostgreSQL database and SQLAlchemy asyncpg configuration in backend/src/services/database.py
- [ ] T007 Define base SQLAlchemy models for Users, Sessions, and Orders in backend/src/models/
- [ ] T008 Implement foundational LangGraph state definition in backend/src/agents/state.py
- [ ] T009 [P] Configure Google Cloud STT service client in backend/src/services/stt_service.py
- [ ] T010 [P] Setup basic FastAPI routing and error handling in backend/src/main.py

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Voice-Based Food Ordering (Priority: P1) 🎯 MVP

**Goal**: Place a food order via natural voice commands

**Independent Test**: Speak "Order 2 pizzas" -> Backend transcribes and extracts -> UI shows cart with items.

### Implementation for User Story 1

- [ ] T011 [P] [US1] Define Pydantic models for Order and Extraction in backend/src/schemas/order.py
- [ ] T012 [P] [US1] Implement TranscriptionNode in backend/src/agents/nodes/transcription.py
- [ ] T013 [P] [US1] Implement IntentNode for "Place Order" detection in backend/src/agents/nodes/intent.py
- [ ] T014 [P] [US1] Implement EntityExtractionNode in backend/src/agents/nodes/extraction.py
- [ ] T015 [US1] Orchestrate Story 1 nodes into LangGraph in backend/src/agents/ordering_graph.py
- [ ] T016 [US1] Create FastAPI endpoint for audio upload in backend/src/api/voice_endpoint.py
- [ ] T017 [US1] Implement browser MediaRecorder hook in frontend/src/hooks/useVoiceCapture.ts
- [ ] T018 [US1] Create VoiceRecordButton component in frontend/src/components/VoiceRecordButton.tsx
- [ ] T019 [US1] Implement optimistic cart update in frontend/src/state/cartStore.ts
- [ ] T020 [US1] Build CartSummary component in frontend/src/components/CartSummary.tsx

**Checkpoint**: User Story 1 is functional (MVP Ready)

---

## Phase 4: User Story 2 - Mixed-Language Support (Priority: P2)

**Goal**: Support "Hinglish" commands (e.g., "2 dosa order karna hai")

**Independent Test**: Speak "2 dosa order karna hai" -> System identifies intent and items correctly.

### Implementation for User Story 2

- [ ] T021 [P] [US2] Update Extraction Pydantic model with language indicators in backend/src/schemas/order.py
- [ ] T022 [US2] Refine IntentNode prompt for mixed-language detection in backend/src/agents/nodes/intent.py
- [ ] T023 [US2] Refine ExtractionNode prompt for non-English item extraction in backend/src/agents/nodes/extraction.py
- [ ] T024 [US2] Implement language-aware validation in backend/src/agents/nodes/validation.py

**Checkpoint**: User Stories 1 and 2 work independently

---

## Phase 5: User Story 3 - Order Modification & Cancellation (Priority: P3)

**Goal**: Cancel or modify orders via voice before submission

**Independent Test**: Speak "Cancel my order" -> Cart is cleared in UI.

### Implementation for User Story 3

- [ ] T025 [P] [US3] Implement IntentNode logic for "Cancel Order" in backend/src/agents/nodes/intent.py
- [ ] T026 [P] [US3] Implement IntentNode logic for "Modify Order" in backend/src/agents/nodes/intent.py
- [ ] T027 [US3] Add "Clear Cart" state reconciliation in frontend/src/state/cartStore.ts
- [ ] T028 [US3] Implement order status persistence in backend/src/services/order_service.py

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Tracing and Observability

- [ ] T029 Implement LangGraph state tracing and logging in backend/src/agents/ordering_graph.py
- [ ] T030 Add error reconciliation between Frontend and Backend in frontend/src/hooks/useVoiceCapture.ts
- [ ] T031 Perform end-to-end latency validation against SC-003 (<3s)

---

## Dependencies & Execution Order

- **Phase 2** blocks everything else.
- **User Story 1** is the primary dependency for all following stories.
- **Phase 6** (Observability) is non-blocking but required for production readiness.

## Parallel Example: User Story 1

```bash
# Models and Nodes can start together:
Task: T011 [P] [US1] Define Pydantic models
Task: T012 [P] [US1] Implement TranscriptionNode
Task: T013 [P] [US1] Implement IntentNode
```
