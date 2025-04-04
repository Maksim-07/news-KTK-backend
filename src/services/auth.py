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
    user_not_found_exceptions,
)
from db.repository.user import UserRepository
from schemas.token import TokenDataSchema, TokenSchema
from schemas.user import CurrentUserSchema


class AuthService:
    __ctx = CryptContext(schemes=["bcrypt"])

    def __init__(self, user_repo: UserRepository = Depends()):
        self._user_repo = user_repo

    async def login_user(self, response: Response, user: OAuth2PasswordRequestForm):
        current_user = await self._user_repo.get_user_by_username(username=user.username)

        if not current_user:
            raise user_not_found_exceptions

        if self.__verify_password(password=user.password, hash_password=current_user.password):
            access_token = self.__create_access_token(data=CurrentUserSchema.model_validate(current_user))
            refresh_token = self.__create_refresh_token(data=CurrentUserSchema.model_validate(current_user))

            response.set_cookie(
                key="refresh_token",
                value=refresh_token,
                httponly=True,
                secure=False,
                max_age=settings().REFRESH_TOKEN_EXPIRE_DAYS,
            )

            return TokenSchema(access_token=access_token, token_type="bearer")

        raise incorrect_password_exceptions

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

            access_token = self.__create_access_token(data=CurrentUserSchema.model_validate(current_user))
            refresh_token = self.__create_refresh_token(data=CurrentUserSchema.model_validate(current_user))

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

    def __verify_password(self, password: str, hash_password: str) -> bool:
        return self.__ctx.verify(password, hash_password)

    @staticmethod
    def __create_access_token(data: CurrentUserSchema) -> str:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings().ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode = TokenDataSchema(user_id=data.id, sub=data.username, exp=expire)
        encoded_jwt = jwt.encode(to_encode.model_dump(), key=settings().SECRET_KEY, algorithm=settings().ALGORITHM)

        return encoded_jwt

    @staticmethod
    def __create_refresh_token(data: CurrentUserSchema) -> str:
        expire = datetime.now(timezone.utc) + timedelta(seconds=settings().REFRESH_TOKEN_EXPIRE_DAYS)
        to_encode = TokenDataSchema(user_id=data.id, sub=data.username, exp=expire)
        encoded_jwt = jwt.encode(to_encode.model_dump(), key=settings().SECRET_KEY, algorithm=settings().ALGORITHM)

        return encoded_jwt
