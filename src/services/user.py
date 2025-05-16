from typing import Sequence

import jwt
from fastapi import Depends
from jwt import InvalidTokenError
from passlib.context import CryptContext

from core.config import settings
from core.exceptions import (
    credentials_exceptions,
    email_already_exists_exceptions,
    incorrect_password_exceptions,
    invalid_token_exceptions,
    user_already_exists_exceptions,
    user_not_found_exceptions,
    username_already_exists_exceptions,
)
from db.repository.role import RoleRepository
from db.repository.user import UserRepository
from schemas.user import (
    CreateAdminSchema,
    CurrentUserSchema,
    GetUserSchema,
    UpdateUserDataSchema,
    UpdateUserPasswordSchema,
    UpdateUserRoleSchema,
)


class UserService:
    __ctx = CryptContext(schemes=["bcrypt"])

    def __init__(self, user_repo: UserRepository = Depends(), role_repo: RoleRepository = Depends()):
        self._user_repo = user_repo
        self._role_repo = role_repo

    async def get_users(self) -> Sequence[GetUserSchema]:
        users = await self._user_repo.get_users()

        return [GetUserSchema.model_validate(user) for user in users]

    async def get_user_by_id(self, user_id: int) -> GetUserSchema | None:
        user = await self._user_repo.get_user_by_id(user_id=user_id)

        if not user:
            raise user_not_found_exceptions

        return GetUserSchema.model_validate(user)

    async def get_current_user(self, token: str) -> CurrentUserSchema:
        try:
            payload = jwt.decode(token, settings().SECRET_KEY, algorithms=[settings().ALGORITHM])
            user_id: int = payload.get("user_id")

            if user_id is None:
                raise credentials_exceptions

            user = await self._user_repo.get_user_by_id(user_id=user_id)

            if not user:
                raise user_not_found_exceptions

            return CurrentUserSchema.model_validate(user)

        except InvalidTokenError:
            raise invalid_token_exceptions

    async def create_admin(self, admin: CreateAdminSchema) -> None:
        current_user = await self._user_repo.get_user_by_username(username=admin.username)

        if current_user:
            raise user_already_exists_exceptions

        current_email = await self._user_repo.get_user_by_email(email=admin.email)

        if current_email:
            raise email_already_exists_exceptions

        admin.password = await self.get_password_hash(admin.password)

        return await self._user_repo.create_admin(admin=admin)

    async def update_user_data(self, user_id: int, data: UpdateUserDataSchema) -> None:
        current_user = await self._user_repo.get_user_by_id(user_id=user_id)

        if not current_user:
            raise user_not_found_exceptions

        if not current_user.username == data.username:
            if await self._user_repo.get_user_by_username(username=data.username):
                raise username_already_exists_exceptions

        if not current_user.email == data.email:
            if await self._user_repo.get_user_by_email(email=data.email):
                raise email_already_exists_exceptions

        return await self._user_repo.update_user_data(user_id=user_id, data=data)

    async def update_user_password(self, user_id: int, data: UpdateUserPasswordSchema) -> None:
        current_user = await self._user_repo.get_user_by_id(user_id=user_id)

        if not current_user:
            raise user_not_found_exceptions

        if self.__ctx.verify(data.old_password, current_user.password):
            new_password = await self.get_password_hash(data.new_password)

            return await self._user_repo.update_user_password(user_id=user_id, new_password=new_password)

        raise incorrect_password_exceptions

    async def update_user_role(self, user_id: int, data: UpdateUserRoleSchema) -> None:
        current_user = await self._user_repo.get_user_by_id(user_id=user_id)

        if not current_user:
            raise user_not_found_exceptions

        return await self._user_repo.update_user_role(user_id=user_id, role_id=data.role_id)

    async def delete_user_by_id(self, user_id: int) -> None:
        current_user = await self._user_repo.get_user_by_id(user_id=user_id)

        if current_user is None:
            raise user_not_found_exceptions

        return await self._user_repo.delete_user_by_id(user_id=user_id)

    async def get_password_hash(self, password: str) -> str:
        return self.__ctx.hash(password)
