from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field, field_serializer

from app.core.consts import USER_NAME_MAX_LENGTH
from app.core.types import UserRole
from app.utils.token import add_token_prefix, token_to_uuid


class UserBase(BaseModel):
    name: Annotated[str, Field(min_length=1, max_length=USER_NAME_MAX_LENGTH)]
    model_config = ConfigDict(from_attributes=True)


class UserRegister(UserBase):
    pass


class UserCreate(UserRegister):
    role: UserRole = UserRole.USER
    api_key: Annotated[UUID, BeforeValidator(token_to_uuid)]

    @field_serializer("api_key", when_used="json")
    def serialize_api_key(self, token: UUID) -> str:
        return add_token_prefix(token)


class UserResponse(UserCreate):
    id: UUID
