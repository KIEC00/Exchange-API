from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Literal
import uuid

router = APIRouter()

# Заглушка для авторизации
def get_current_user():
    return "user123"  # Здесь будет реальный пользователь ID

# Модель заявки
class OrderRequest(BaseModel):
    instrument: str  # Например: "BTC"
    side: Literal["buy", "sell"]
    quantity: float
    price: float

# Ответ после создания
class OrderResponse(BaseModel):
    order_id: str
    status: str

# Эндпоинт для создания заявки
@router.post("/orders", response_model=OrderResponse)
async def create_order(order: OrderRequest, user: str = Depends(get_current_user)):
    # Здесь будет логика сохранения в БД
    fake_order_id = str(uuid.uuid4())
    return {
        "order_id": fake_order_id,
        "status": "created"
    }