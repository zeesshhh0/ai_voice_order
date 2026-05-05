# Data Model: Voice-to-Order

## Entities

### User
- `id`: UUID (Primary Key)
- `name`: String
- `contact`: String
- `preferred_language`: String (Default: 'mixed')
- `created_at`: Timestamp

### VoiceSession
- `id`: UUID (Primary Key)
- `user_id`: UUID (Foreign Key)
- `audio_url`: String (Link to blob storage)
- `transcript`: Text
- `confidence_score`: Float
- `created_at`: Timestamp

### Order
- `id`: UUID (Primary Key)
- `user_id`: UUID (Foreign Key)
- `restaurant_id`: String (Reference to external/historical system)
- `items`: JSONB (List of OrderItem)
- `status`: Enum (DRAFT, PLACED, CANCELLED)
- `created_at`: Timestamp

### ExtractedEntity
- `id`: UUID (Primary Key)
- `session_id`: UUID (Foreign Key)
- `entity_type`: String (ITEM, QUANTITY, RESTAURANT, SIZE, SPECIAL_INSTRUCTION)
- `value`: String
- `language`: String (en, hi)

## Relationships
- User (1) <-> (N) VoiceSession
- User (1) <-> (N) Order
- VoiceSession (1) <-> (1) Order (via extraction)
- Order (1) <-> (N) ExtractedEntity
