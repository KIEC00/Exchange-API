from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Dict
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.user import User
from app.dependencies.db import get_db

router = APIRouter()

# Модель балансов (название инструмента -> количество)
class BalancesResponse(BaseModel):
    balances: Dict[str, float]

# Заглушка для авторизации (позже будет токен)
def get_current_user():
    # Допустим, фиктивный UUID пользователя
    return "00000000-0000-0000-0000-000000000001"

# Эндпоинт получения балансов
@router.get("/balances", response_model=BalancesResponse)
async def get_balances(
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(get_current_user)
):
    result = await db.execute(
        select(User.balance).where(User.id == user_id)
    )
    balance = result.scalar_one_or_none()
    if balance is None:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
    return {"balances": balance}
