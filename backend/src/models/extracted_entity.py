import uuid
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.src.services.database import Base

class ExtractedEntity(Base):
    __tablename__ = "extracted_entities"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    order_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("orders.id"))
    entity_type: Mapped[str] = mapped_column(String(100)) # ITEM, QUANTITY, RESTAURANT, SIZE, SPECIAL_INSTRUCTION
    value: Mapped[str] = mapped_column(String(500))
    language: Mapped[str] = mapped_column(String(10)) # en, hi

    order: Mapped["Order"] = relationship(back_populates="entities")
