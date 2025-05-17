from uuid import UUID
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User
from app.schemas.user import UserCreate


class UserCRUD:
    async def create(self, session: AsyncSession, user_create: UserCreate) -> User:
        new_user = User(**user_create.model_dump())
        session.add(new_user)
        await session.flush()
        await session.commit()
        return new_user

    async def get_by_id(self, session: AsyncSession, user_id: UUID) -> User | None:
        return await session.get(User, user_id)

    async def get_by_api_key(self, session: AsyncSession, api_key: UUID) -> User | None:
        stmt = select(User).filter(User.api_key == api_key).limit(1)
        result = await session.execute(stmt)
        user = result.scalar_one_or_none()
        return user
