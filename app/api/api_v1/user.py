from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException

from app.api.dependencies.auth import current_user
from app.schemas.user import UserResponse


router = APIRouter(prefix="/user", tags=["user"])


@router.get("/profile", summary="Получение информации о текущем пользователе")
async def get_current_profile(
    user: Annotated[UUID, Depends(current_user)],
) -> UserResponse:
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse.model_validate(user)
