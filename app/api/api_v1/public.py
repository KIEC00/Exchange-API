from typing import Annotated
from uuid import uuid4
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import db
from app.crud import user_crud
from app.schemas.user import UserRegister, UserResponse


router = APIRouter(prefix="/public", tags=["public"])


@router.post("/register", summary="Регистрация пользователя")
async def register(
    session: Annotated[AsyncSession, Depends(db.session_maker)], user: UserRegister
) -> UserResponse:
    new_user = await user_crud.create(session, name=user.name, api_key=uuid4())
    return UserResponse.model_validate(new_user)
