from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import db

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async for session in db.session_maker():
        yield session