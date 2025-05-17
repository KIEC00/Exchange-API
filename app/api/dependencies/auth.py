from typing import Annotated
from uuid import UUID
from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import db
from app.core.consts import AUTH_SCHEME
from app.core.types import UserRole
from app.crud import user_crud
from app.models.user import User
from app.utils.token import token_to_uuid

auth_header = APIKeyHeader(name="Authorization")


async def current_api_key(
    api_key_header: Annotated[str, Depends(auth_header)],
) -> UUID:
    parts = api_key_header.split(maxsplit=2)
    if len(parts) != 2:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authorization header",
        )
    scheme, token = parts
    if scheme.upper() != AUTH_SCHEME:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials %s" % scheme,
        )
    try:
        return token_to_uuid(token)
    except ValueError or TypeError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token %s" % token,
        )


async def current_user(
    session: Annotated[AsyncSession, Depends(db.session_maker)],
    api_key: Annotated[UUID, Depends(current_api_key)],
) -> User:
    user = await user_crud.get_by_api_key(session, api_key)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )
    return user


async def current_admin(
    user: Annotated[User, Depends(current_user)],
):
    if user.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permission denied: admin role required",
        )
    return user
