from typing import Sequence

from sqlalchemy import delete, insert, select, update

from db.models import User
from db.repository.base import BaseDatabaseRepository
from schemas.user import CreateUserSchema, UpdateUserSchema


class UserRepository(BaseDatabaseRepository):
    async def get_users(self) -> Sequence[User]:
        query = select(User)
        result = await self._session.execute(query)

        return result.scalars().all()

    async def get_user_by_id(self, user_id: int) -> User | None:
        query = select(User).where(User.id == user_id)
        result = await self._session.execute(query)

        return result.scalar_one_or_none()

    async def get_user_by_username(self, username: str) -> User | None:
        query = select(User).where(User.username == username)
        result = await self._session.execute(query)

        return result.scalar_one_or_none()

    async def get_user_by_email(self, email: str) -> User | None:
        query = select(User).where(User.email == email)
        result = await self._session.execute(query)

        return result.scalar_one_or_none()

    async def create_user(self, user: CreateUserSchema) -> None:
        query = insert(User).values(**user.model_dump())
        await self._session.execute(query)
        await self._session.commit()

    async def update_user(self, user: UpdateUserSchema) -> None:
        query = (
            update(User)
            .where(User.id == user.id)
            .values(
                {
                    User.username: user.username,
                    User.email: user.email,
                    User.last_name: user.last_name,
                    User.first_name: user.first_name,
                    User.password: user.new_password,
                }
            )
        )
        await self._session.execute(query)
        await self._session.commit()

    async def delete_user_by_id(self, user_id: int) -> None:
        query = delete(User).where(User.id == user_id)
        await self._session.execute(query)
        await self._session.commit()
