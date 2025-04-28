from typing import Sequence

from fastapi import APIRouter, Depends, status

from schemas.role import CreateRoleSchema, GetRoleSchema
from services.role import RoleService

router = APIRouter(prefix="/roles", tags=["Roles"])


@router.get("", status_code=status.HTTP_200_OK, response_model=Sequence[GetRoleSchema])
async def get_roles(
    role_service: RoleService = Depends(),
) -> Sequence[GetRoleSchema]:
    return await role_service.get_roles()


@router.post("", status_code=status.HTTP_200_OK, response_model=None)
async def create_role(role: CreateRoleSchema, role_service: RoleService = Depends()) -> None:
    return await role_service.create_role(role=role)
