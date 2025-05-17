from uuid import uuid4
from enum import Enum as PyEnum

from sqlalchemy import String, Float, Integer, Enum, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import BaseORM


class OrderSide(str, PyEnum):
    BUY = "buy"
    SELL = "sell"


class Order(BaseORM):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String, index=True)  # Или Mapped[int], если ID числовой
    instrument: Mapped[str] = mapped_column(String, index=True)
    side: Mapped[OrderSide] = mapped_column(Enum(OrderSide), nullable=False)
    quantity: Mapped[float] = mapped_column(Float, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)