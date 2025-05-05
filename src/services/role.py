from typing import Sequence

from fastapi import Depends

from core.exceptions import (
    role_already_exists_exceptions,
    role_not_found_exceptions,
)
from db.repository.role import RoleRepository
from schemas.role import CreateRoleSchema, GetRoleSchema


class RoleService:
    def __init__(self, role_repo: RoleRepository = Depends()):
        self._role_repo = role_repo

    async def get_roles(self) -> Sequence[GetRoleSchema]:
        roles = await self._role_repo.get_roles()

        return [GetRoleSchema.model_validate(role) for role in roles]

    async def get_role_by_id(self, role_id: int) -> GetRoleSchema:
        role = await self._role_repo.get_role_by_id(role_id=role_id)

        if role is None:
            raise role_not_found_exceptions

        return GetRoleSchema.model_validate(role)

    async def create_role(self, role: CreateRoleSchema) -> None:
        current_role = await self._role_repo.get_role_by_name(role.name)

        if current_role:
            raise role_already_exists_exceptions

        return await self._role_repo.create_role(role=role)
