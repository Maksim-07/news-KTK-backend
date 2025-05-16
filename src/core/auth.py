import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError

from core.config import settings
from core.exceptions import (
    access_denied_exceptions,
    credentials_exceptions,
    invalid_token_exceptions,
    token_not_found_exceptions,
    user_not_found_exceptions,
)
from services.user import UserService

oauth2_user_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/news-ktk/v1/auth/user/login", scheme_name="UserAuth", description="User token (JWT)"
)

oauth2_admin_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/news-ktk/v1/auth/admin/login", scheme_name="AdminAuth", description="Admin token (JWT)"
)


async def get_user_id_from_any_token(
    user_token: str | None = Depends(oauth2_user_scheme),
    admin_token: str | None = Depends(oauth2_admin_scheme),
) -> int:
    token = user_token if user_token is not None else admin_token
    if token is None:
        raise credentials_exceptions

    try:
        payload = jwt.decode(token, settings().SECRET_KEY, algorithms=[settings().ALGORITHM])
        user_id: int = payload.get("user_id")
        if user_id is None:
            raise credentials_exceptions

        return user_id

    except InvalidTokenError:
        raise invalid_token_exceptions


async def get_user_id_from_admin_token(
    admin_token: str | None = Depends(oauth2_admin_scheme),
) -> int:
    if admin_token is None:
        raise credentials_exceptions

    try:
        payload = jwt.decode(admin_token, settings().SECRET_KEY, algorithms=[settings().ALGORITHM])
        user_id: int = payload.get("user_id")
        if user_id is None:
            raise credentials_exceptions

        return user_id

    except InvalidTokenError:
        raise invalid_token_exceptions


async def verify_superadmin_token(token: str, user_service: UserService = Depends()) -> int:
    try:
        payload = jwt.decode(token, settings().SECRET_KEY, algorithms=[settings().ALGORITHM])
        user_id: int = payload.get("user_id")
        role: str = payload.get("role")

        if user_id is None or role != "Суперадмин":
            raise access_denied_exceptions

        user = await user_service.get_user_by_id(user_id=user_id)
        if not user:
            raise user_not_found_exceptions

        return user_id

    except InvalidTokenError:
        raise invalid_token_exceptions


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


async def verify_admin_token_from_header(
    token: str = Depends(oauth2_admin_scheme), user_service: UserService = Depends()
) -> None:
    await verify_token(token=token, user_service=user_service)


async def verify_superadmin_token_from_header(
    token: str = Depends(oauth2_admin_scheme), user_service: UserService = Depends()
) -> None:
    await verify_superadmin_token(token=token, user_service=user_service)


async def verify_user_token_from_header(
    token: str = Depends(oauth2_user_scheme), user_service: UserService = Depends()
) -> None:
    await verify_token(token=token, user_service=user_service)
