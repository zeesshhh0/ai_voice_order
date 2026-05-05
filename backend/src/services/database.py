import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

# Database URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@localhost/voice_order")

# Create async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create session factory
async_session_pool = async_sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

class Base(DeclarativeBase):
    pass

async def get_db():
    async with async_session_pool() as session:
        yield session
