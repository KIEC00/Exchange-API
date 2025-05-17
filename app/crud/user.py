from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.types import UserRole
from app.models import User


class UserCRUD:
    async def create(self, session: AsyncSession, name: str, api_key: UUID) -> User:
        new_user = User(
            name=name,
            role=UserRole.USER,
            api_key=api_key,
        )
        session.add(new_user)
        await session.flush()
        await session.commit()
        return new_user
