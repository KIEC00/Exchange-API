from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import BaseModel
from typing import Literal
import uuid


from app.models.orders import Order, OrderSide
from app.dependencies.db import get_db

router = APIRouter()

class OrderRequest(BaseModel):
    instrument: str
    side: Literal["buy", "sell"]
    quantity: float
    price: float

class OrderResponse(BaseModel):
    order_id: int
    status: str

# Заглушка для текущего пользователя
def get_current_user():
    return "user123"

@router.post("/orders", response_model=OrderResponse)
async def create_order(
    order: OrderRequest,
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(get_current_user)
):
    db_order = Order(
        user_id=user_id,
        instrument=order.instrument,
        side=order.side,
        quantity=order.quantity,
        price=order.price
    )
    db.add(db_order)
    await db.commit()
    await db.refresh(db_order)
    return {
        "order_id": db_order.id,
        "status": "created"
    }
