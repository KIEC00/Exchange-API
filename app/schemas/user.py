from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, BeforeValidator, Field, field_serializer

from app.core.consts import USER_NAME_MAX_LENGTH
from app.core.types import UserRole
from app.utils.token import add_token_prefix, strip_token_prefix


class UserBase(BaseModel):
    name: Annotated[str, Field(min_length=1, max_length=USER_NAME_MAX_LENGTH)]


class UserRegister(UserBase):
    pass


class UserResponse(UserBase):
    id: UUID
    role: UserRole
    api_key: Annotated[UUID, BeforeValidator(strip_token_prefix)]

    @field_serializer("api_key")
    def serialize_api_key(self, token: UUID) -> str:
        return add_token_prefix(token)

    class Config:
        from_attributes = True
