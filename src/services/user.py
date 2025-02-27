from typing import Sequence

from fastapi import Depends
from passlib.context import CryptContext

from core.exceptions import (
    user_already_exists_exceptions,
    user_not_found_exceptions,
)
from db.repository.user import UserRepository
from schemas.user import GetUserSchema, UpdateUserSchema


class UserService:
    __ctx = CryptContext(schemes=["bcrypt"])

    def __init__(self, user_repo: UserRepository = Depends()):
        self._user_repo = user_repo

    async def get_users(self) -> Sequence[GetUserSchema]:
        users = await self._user_repo.get_users()

        return [GetUserSchema.model_validate(user) for user in users]

    async def create_user(self, user: UpdateUserSchema) -> None:
        current_user = await self._user_repo.get_user_by_username(username=user.username)

        if current_user:
            raise user_already_exists_exceptions

        user.password = self.__get_password_hash(user.password)

        return await self._user_repo.create_user(user=user)

    async def delete_user_by_username(self, username: str) -> None:
        current_user = await self._user_repo.get_user_by_username(username=username)

        if current_user is None:
            raise user_not_found_exceptions

        return await self._user_repo.delete_user_by_id(user_id=current_user.id)

    def __get_password_hash(self, password: str) -> str:
        return self.__ctx.hash(password)
