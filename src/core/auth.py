import jwt
from fastapi import Depends, Request
from jwt import InvalidTokenError

from core.config import settings
from core.exceptions import (
    credentials_exceptions,
    invalid_token_exceptions,
    token_not_found_exceptions,
    user_not_found_exceptions,
)
from services.user import UserService


async def verify_token(token: str | None, user_service: UserService) -> None:
    if not token:
        raise token_not_found_exceptions

    try:
        payload = jwt.decode(token, settings().SECRET_KEY, algorithms=[settings().ALGORITHM])
        user_id: int = payload.get("user_id")

        if user_id is None:
            raise credentials_exceptions

        user = await user_service.get_user_by_id(user_id=user_id)

        if not user:
            raise user_not_found_exceptions

    except InvalidTokenError:
        raise invalid_token_exceptions


async def verify_token_from_header(request: Request, user_service: UserService = Depends()) -> None:
    if not settings().USE_KEYCLOAK:
        return

    token = request.headers.get("Authorization")

    await verify_token(token=token, user_service=user_service)
