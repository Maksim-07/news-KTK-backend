from typing import Sequence, Union

from fastapi import APIRouter, Depends, status

from core.auth import (
    oauth2_admin_scheme,
    oauth2_user_scheme,
    verify_admin_token_from_header,
    verify_superadmin_token,
    verify_superadmin_token_from_header,
    verify_user_token_from_header,
)
from schemas.user import (
    CreateAdminSchema,
    CurrentUserSchema,
    GetUserSchema,
    UpdateUserDataSchema,
    UpdateUserPasswordSchema,
    UpdateUserRoleSchema,
)
from services.user import UserService

router = APIRouter(prefix="/users", tags=["Users"])


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=Sequence[GetUserSchema],
    dependencies=[Depends(verify_superadmin_token_from_header)],
)
async def get_users(role_id: int | None = None, user_service: UserService = Depends()) -> Sequence[GetUserSchema]:
    return await user_service.get_users(role_id=role_id)


@router.get(
    "/user/me",
    status_code=status.HTTP_200_OK,
    response_model=CurrentUserSchema,
    dependencies=[Depends(verify_user_token_from_header)],
)
async def get_current_user(
    user_token: str = Depends(oauth2_user_scheme), user_service: UserService = Depends()
) -> CurrentUserSchema:
    return await user_service.get_current_user(token=user_token)


@router.get(
    "/admin/me",
    status_code=status.HTTP_200_OK,
    response_model=CurrentUserSchema,
    dependencies=[Depends(verify_admin_token_from_header)],
)
async def get_current_admin(
    admin_token: str = Depends(oauth2_admin_scheme), user_service: UserService = Depends()
) -> CurrentUserSchema:
    return await user_service.get_current_user(token=admin_token)


@router.post(
    "", status_code=status.HTTP_200_OK, response_model=None, dependencies=[Depends(verify_superadmin_token_from_header)]
)
async def create_admin(admin: CreateAdminSchema, user_service: UserService = Depends()) -> None:
    return await user_service.create_admin(admin=admin)


@router.put(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=None,
    dependencies=[Depends(verify_superadmin_token_from_header)],
)
async def update_user_data(user_id: int, data: UpdateUserDataSchema, user_service: UserService = Depends()) -> None:
    return await user_service.update_user_data(user_id=user_id, data=data)


@router.patch(
    "/{user_id}/password",
    status_code=status.HTTP_200_OK,
    response_model=None,
    dependencies=[Depends(verify_superadmin_token_from_header)],
)
async def update_user_password(
    user_id: int, data: UpdateUserPasswordSchema, user_service: UserService = Depends()
) -> None:
    return await user_service.update_user_password(user_id=user_id, data=data)


@router.patch(
    "/{user_id}/role",
    status_code=status.HTTP_200_OK,
    response_model=None,
    dependencies=[Depends(verify_superadmin_token_from_header)],
)
async def update_user_role(user_id: int, data: UpdateUserRoleSchema, user_service: UserService = Depends()) -> None:
    return await user_service.update_user_role(user_id=user_id, data=data)


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=None,
    dependencies=[Depends(verify_superadmin_token_from_header)],
)
async def delete_user_by_id(user_id: int, user_service: UserService = Depends()) -> None:
    return await user_service.delete_user_by_id(user_id=user_id)
