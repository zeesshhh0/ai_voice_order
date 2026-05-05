# Research: Voice-to-Order AI System

## Technical Decisions

### Decision: Google Cloud Speech-to-Text (V2)
- **Rationale**: Support for multi-language (English/Hindi) and high-accuracy transcription required for "Hinglish" commands like "2 dosa order karna hai".
- **Alternatives Considered**: OpenAI Whisper (Local) - rejected due to higher resource overhead for near real-time requirements on base server hardware.

### Decision: Pydantic V2 for Validation
- **Rationale**: Strict typing mandate from Constitution. Enables automatic validation of LLM outputs from Gemini within LangGraph nodes.
- **Alternatives Considered**: Manual dict validation - rejected for lack of type safety and schema documentation.

### Decision: FastAPI + Asyncpg
- **Rationale**: High-concurrency requirements and "Async-First" constitution mandate. Perfect for non-blocking I/O during STT and DB operations.

### Decision: LangGraph Orchestration
- **Rationale**: Enables discrete, traceable nodes for transcription, intent detection, and entity extraction. Avoids monolithic prompts as per the Constitution.
