# Implementation Plan: Voice-to-Order AI System

**Branch**: `001-voice-to-order` | **Date**: 2025-05-22 | **Spec**: specs/001-voice-to-order/spec.md

## Summary
Build an end-to-end voice ordering system using Next.js (Frontend), FastAPI (Backend), LangGraph (Orchestration), and Google Cloud STT (Transcription). The system will process audio input to extract structured food orders with multi-language support.

## Technical Context

**Language/Version**: Python 3.11+, TypeScript/Next.js  
**Primary Dependencies**: FastAPI, LangGraph, Pydantic v2, Google-Cloud-Speech, SQLAlchemy/Asyncpg  
**Storage**: PostgreSQL  
**Testing**: Pytest (Backend), Jest (Frontend)  
**Target Platform**: Web (Desktop/Mobile)  
**Performance Goals**: <3s end-to-end processing.  
**Constraints**: Strictly asynchronous backend, Agentic-First orchestration.

## Constitution Check

- [ ] **Agentic-First**: AI logic decomposed into 5 LangGraph nodes (Transcription, Intent, Extraction, Context, Validation).
- [ ] **Strict Typing**: Pydantic models used for all STT and LLM outputs.
- [ ] **Async-First**: FastAPI and Asyncpg used for all I/O.
- [ ] **Optimistic UI**: Next.js state management for immediate cart feedback.
- [ ] **Traceability**: LangGraph state logging for each ordering session.

## Project Structure

### Source Code
```text
backend/
├── src/
│   ├── agents/      # LangGraph nodes and graphs
│   ├── models/      # SQLAlchemy models
│   ├── schemas/     # Pydantic models
│   ├── services/    # STT and DB service logic
│   └── api/         # FastAPI endpoints
└── tests/

frontend/
├── src/
│   ├── components/  # Voice recorder and Cart
│   ├── hooks/       # Optimistic UI and API calls
│   └── state/       # Cart management
└── tests/
```

**Structure Decision**: Option 2: Web application (Frontend + Backend).

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| LangGraph | Required for agentic-first mandate | Basic LLM chains are too opaque for complex ordering logic. |
