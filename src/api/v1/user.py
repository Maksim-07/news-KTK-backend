from typing import Sequence

from fastapi import APIRouter, Depends, status

from core.auth import oauth2_scheme
from schemas.user import (
    CreateUserSchema,
    CurrentUserSchema,
    GetUserSchema,
    UpdateUserDataSchema,
    UpdateUserPasswordSchema,
    UpdateUserRoleSchema,
)
from services.user import UserService

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("", status_code=status.HTTP_200_OK, response_model=Sequence[GetUserSchema])
async def get_users(user_service: UserService = Depends()) -> Sequence[GetUserSchema]:
    return await user_service.get_users()


@router.get("/me", status_code=status.HTTP_200_OK, response_model=CurrentUserSchema)
async def get_current_user(
    token: str = Depends(oauth2_scheme), user_service: UserService = Depends()
) -> CurrentUserSchema:
    return await user_service.get_current_user(token=token)


@router.post("", status_code=status.HTTP_200_OK, response_model=None)
async def create_user(user: CreateUserSchema, user_service: UserService = Depends()) -> None:
    return await user_service.create_user(user=user)


@router.put("/{user_id}", status_code=status.HTTP_200_OK, response_model=None)
async def update_user_data(user_id: int, data: UpdateUserDataSchema, user_service: UserService = Depends()) -> None:
    return await user_service.update_user_data(user_id=user_id, data=data)


@router.patch("/{user_id}/password", status_code=status.HTTP_200_OK, response_model=None)
async def update_user_password(
    user_id: int, data: UpdateUserPasswordSchema, user_service: UserService = Depends()
) -> None:
    return await user_service.update_user_password(user_id=user_id, data=data)


@router.patch("/{user_id}/role", status_code=status.HTTP_200_OK, response_model=None)
async def update_user_role(user_id: int, data: UpdateUserRoleSchema, user_service: UserService = Depends()) -> None:
    return await user_service.update_user_role(user_id=user_id, data=data)


@router.delete("/{user_id}", status_code=status.HTTP_200_OK, response_model=None)
async def delete_user_by_id(user_id: int, user_service: UserService = Depends()) -> None:
    return await user_service.delete_user_by_id(user_id=user_id)
