from typing import Sequence

from sqlalchemy import delete, desc, insert, select, true, update

from db.models import Role
from db.repository.base import BaseDatabaseRepository
from schemas.role import CreateRoleSchema, GetRoleSchema


class RoleRepository(BaseDatabaseRepository):
    async def get_roles(self) -> Sequence[Role]:
        query = select(Role)
        result = await self._session.execute(query)

        return result.scalars().all()

    async def get_role_by_id(self, role_id: int) -> Role:
        query = select(Role).where(Role.id == role_id)
        result = await self._session.execute(query)

        return result.scalar_one()

    async def get_role_by_name(self, name: str) -> Role | None:
        query = select(Role).where(Role.name == name)
        result = await self._session.execute(query)

        return result.scalar_one_or_none()

    async def create_role(self, role: CreateRoleSchema) -> None:
        query = insert(Role).values(**role.model_dump())

        await self._session.execute(query)
        await self._session.commit()
