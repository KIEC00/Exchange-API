from uuid import UUID

from app.core.consts import TOKEN_PREFIX

Token = str | UUID


def strip_token_prefix(token: Token) -> UUID:
    if isinstance(token, UUID):
        return token
    if isinstance(token, str):
        return UUID(token.removeprefix(TOKEN_PREFIX))
    raise TypeError(f"Invalid token type {type(token)}, expected {Token}")


def add_token_prefix(token: Token) -> str:
    if isinstance(token, UUID):
        return f"{TOKEN_PREFIX}{token}"
    if isinstance(token, str):
        if token.startswith(TOKEN_PREFIX):
            return token
        return f"{TOKEN_PREFIX}{token}"
    raise TypeError(f"Invalid token type {type(token)}, expected {Token}")
