import uuid
from datetime import datetime
from enum import Enum as PyEnum
from sqlalchemy import String, DateTime, ForeignKey, Enum, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional
from backend.src.services.database import Base

class OrderStatus(PyEnum):
    DRAFT = "DRAFT"
    PLACED = "PLACED"
    CANCELLED = "CANCELLED"

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    session_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("voice_sessions.id"), unique=True)
    restaurant_id: Mapped[str] = mapped_column(String(255))
    items: Mapped[dict] = mapped_column(JSON)
    status: Mapped[OrderStatus] = mapped_column(Enum(OrderStatus), default=OrderStatus.DRAFT)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    user: Mapped["User"] = relationship(back_populates="orders")
    session: Mapped["VoiceSession"] = relationship(back_populates="order")
    entities: Mapped[List["ExtractedEntity"]] = relationship(back_populates="order")
