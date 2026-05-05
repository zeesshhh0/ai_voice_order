import uuid
from datetime import datetime
from sqlalchemy import String, Float, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.src.services.database import Base

class VoiceSession(Base):
    __tablename__ = "voice_sessions"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    audio_url: Mapped[str] = mapped_column(String(500))
    transcript: Mapped[str] = mapped_column(Text, nullable=True)
    confidence_score: Mapped[float] = mapped_column(Float, nullable=True)
    created_at: Mapped[datetime] = mapped_column(datetime, default=datetime.utcnow)

    user: Mapped["User"] = relationship(back_populates="sessions")
    order: Mapped["Order"] = relationship(back_populates="session", uselist=False)
