from typing import Annotated
from uuid import uuid4
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import db
from app.crud import user_crud
from app.schemas.user import UserCreate, UserRegister, UserResponse


router = APIRouter(prefix="/public", tags=["public"])


@router.post("/register", summary="Регистрация пользователя")
async def register(
    session: Annotated[AsyncSession, Depends(db.session_maker)], user: UserRegister
) -> UserResponse:
    new_user_create = UserCreate(**user.model_dump(), api_key=uuid4())
    new_user = await user_crud.create(session, new_user_create)
    return UserResponse.model_validate(new_user, from_attributes=True)
