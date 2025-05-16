from datetime import datetime, timedelta, timezone

import jwt
from fastapi import Depends, Request, Response
from fastapi.security import OAuth2PasswordRequestForm
from jwt import InvalidTokenError
from passlib.context import CryptContext

from core.config import settings
from core.exceptions import (
    credentials_exceptions,
    incorrect_password_exceptions,
    invalid_token_exceptions,
    refresh_token_missing_exceptions,
    role_not_found_exceptions,
    user_already_exists_exceptions,
    user_not_found_exceptions, email_already_exists_exceptions,
)
from db.repository.role import RoleRepository
from db.repository.user import UserRepository
from schemas.token import TokenDataSchema, TokenSchema
from schemas.user import CurrentUserSchema, UserRegisterFormSchema
from services.user import UserService


class AuthService:
    __ctx = CryptContext(schemes=["bcrypt"])

    def __init__(
        self,
        user_repo: UserRepository = Depends(),
        role_repo: RoleRepository = Depends(),
        user_service: UserService = Depends(),
    ):
        self._user_repo = user_repo
        self._role_repo = role_repo
        self._user_service = user_service

    async def login_user(self, response: Response, user: OAuth2PasswordRequestForm):
        current_user = await self._user_repo.get_user_by_username(username=user.username)

        if not current_user:
            raise user_not_found_exceptions

        if await self.__verify_password(password=user.password, hash_password=current_user.password):
            current_user_schema = CurrentUserSchema.model_validate(current_user)

            access_token = await self.__create_access_token(data=current_user_schema)
            refresh_token = await self.__create_refresh_token(data=current_user_schema)

            response.set_cookie(
                key="refresh_token",
                value=refresh_token,
                httponly=True,
                secure=False,
                max_age=settings().REFRESH_TOKEN_EXPIRE_DAYS,
            )

            return TokenSchema(access_token=access_token, token_type="bearer")

        raise incorrect_password_exceptions

    async def login_admin(self, response: Response, user: OAuth2PasswordRequestForm):
        current_user = await self._user_repo.get_user_by_username(username=user.username)

        if not current_user:
            raise user_not_found_exceptions

        current_role = await self._role_repo.get_role_by_id(role_id=current_user.role_id)

        if not current_role or not current_role.can_edit_news:
            raise user_not_found_exceptions

        if await self.__verify_password(password=user.password, hash_password=current_user.password):
            current_user_schema = CurrentUserSchema.model_validate(current_user)

            access_token = await self.__create_access_token(data=current_user_schema)
            refresh_token = await self.__create_refresh_token(data=current_user_schema)

            response.set_cookie(
                key="refresh_token",
                value=refresh_token,
                httponly=True,
                secure=False,
                max_age=settings().REFRESH_TOKEN_EXPIRE_DAYS,
            )

            return TokenSchema(access_token=access_token, token_type="bearer")

        raise incorrect_password_exceptions

    async def register_user(self, user: UserRegisterFormSchema) -> None:
        current_user = await self._user_repo.get_user_by_username(user.username)

        if current_user:
            raise user_already_exists_exceptions

        current_email = await self._user_repo.get_user_by_email(email=user.email)

        if current_email:
            raise email_already_exists_exceptions

        user.password = await self._user_service.get_password_hash(user.password)

        current_role = await self._role_repo.get_role_by_name(name="Пользователь")

        if not current_role:
            raise

        return await self._user_repo.create_user(user=user, role_id=current_role.id)

    async def refresh_token(self, request: Request, response: Response) -> TokenSchema:
        try:
            refresh_token = request.cookies.get("refresh_token")

            if not refresh_token:
                raise refresh_token_missing_exceptions

            payload = jwt.decode(refresh_token, settings().SECRET_KEY, algorithms=[settings().ALGORITHM])
            user_id: int = payload.get("user_id")

            if user_id is None:
                raise credentials_exceptions

            current_user = await self._user_repo.get_user_by_id(user_id=user_id)

            if not current_user:
                raise user_not_found_exceptions

            current_user_schema = CurrentUserSchema.model_validate(current_user)

            access_token = await self.__create_access_token(data=current_user_schema)
            refresh_token = await self.__create_refresh_token(data=current_user_schema)

            response.set_cookie(
                key="refresh_token",
                value=refresh_token,
                httponly=True,
                secure=False,
                max_age=settings().REFRESH_TOKEN_EXPIRE_DAYS,
            )

            return TokenSchema(access_token=access_token, token_type="bearer")

        except InvalidTokenError:
            raise invalid_token_exceptions

    async def __verify_password(self, password: str, hash_password: str) -> bool:
        return self.__ctx.verify(password, hash_password)

    async def __create_access_token(self, data: CurrentUserSchema) -> str:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings().ACCESS_TOKEN_EXPIRE_MINUTES)

        role = await self._role_repo.get_role_by_id(role_id=data.role_id)
        if not role:
            raise role_not_found_exceptions

        to_encode = TokenDataSchema(user_id=data.id, sub=data.username, role=role.name, exp=expire)
        encoded_jwt = jwt.encode(to_encode.model_dump(), key=settings().SECRET_KEY, algorithm=settings().ALGORITHM)

        return encoded_jwt

    async def __create_refresh_token(self, data: CurrentUserSchema) -> str:
        expire = datetime.now(timezone.utc) + timedelta(seconds=settings().REFRESH_TOKEN_EXPIRE_DAYS)

        role = await self._role_repo.get_role_by_id(role_id=data.role_id)
        if not role:
            raise role_not_found_exceptions

        to_encode = TokenDataSchema(user_id=data.id, sub=data.username, role=role.name, exp=expire)
        encoded_jwt = jwt.encode(to_encode.model_dump(), key=settings().SECRET_KEY, algorithm=settings().ALGORITHM)

        return encoded_jwt
