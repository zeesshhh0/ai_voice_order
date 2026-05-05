from typing import TypedDict, List, Optional, Annotated
import operator

class OrderItem(TypedDict):
    name: str
    quantity: int
    size: Optional[str]
    special_instructions: Optional[str]

class OrderDetails(TypedDict):
    items: List[OrderItem]
    restaurant_id: Optional[str]

class AgentState(TypedDict):
    # The user's audio transcript
    transcript: str
    
    # Detected intent (PLACE_ORDER, REORDER, MODIFY, CANCEL, ASK_MENU)
    detected_intent: Optional[str]
    
    # Structured order details
    order_details: OrderDetails
    
    # Historical or session context data
    context_data: dict
    
    # Flag to indicate if the order is ready for confirmation
    is_complete: bool
    
    # Error messages or status updates for the user
    status: Optional[str]
    
    # Confidence score from STT
    confidence_score: float
