# API Contracts: Voice-to-Order

## POST /api/v1/voice/process
**Description**: Upload audio and trigger LangGraph processing.

**Request**: `multipart/form-data`
- `audio`: File (WAV/MP3)
- `session_id`: UUID (Optional guest session)

**Response**: `200 OK`
```json
{
  "session_id": "uuid",
  "transcript": "Order 2 paneer pizzas",
  "intent": "PLACE_ORDER",
  "order_draft": {
    "restaurant": "Last Ordered Restaurant",
    "items": [
      {
        "name": "paneer pizza",
        "quantity": 2
      }
    ]
  },
  "confidence": 0.95
}
```

## GET /api/v1/orders/history
**Description**: Fetch recent orders for the guest session.

**Response**: `200 OK`
```json
[
  {
    "order_id": "uuid",
    "restaurant": "Pizza Express",
    "status": "PLACED",
    "created_at": "2025-05-22T..."
  }
]
```
