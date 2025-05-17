from uuid import uuid4
from sqlalchemy import UUID, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from app.core.consts import USER_NAME_MAX_LENGTH
from app.core.types import UserRole
from app.models.base import BaseORM


class User(BaseORM):
    id: Mapped[UUID] = mapped_column(Uuid(), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String(USER_NAME_MAX_LENGTH), nullable=False)
    role: Mapped[UserRole] = mapped_column(default=UserRole.USER, nullable=False)
    api_key: Mapped[UUID] = mapped_column(Uuid(), unique=True, nullable=False)
    deactivated: Mapped[bool] = mapped_column(default=False, nullable=False)
