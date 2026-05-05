import uuid
from datetime import datetime
from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from backend.src.services.database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(255))
    contact: Mapped[str] = mapped_column(String(255))
    preferred_language: Mapped[str] = mapped_column(String(50), default="mixed")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    sessions: Mapped[List["VoiceSession"]] = relationship(back_populates="user")
    orders: Mapped[List["Order"]] = relationship(back_populates="user")
