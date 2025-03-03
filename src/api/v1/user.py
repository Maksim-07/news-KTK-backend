from typing import Sequence

from fastapi import APIRouter, Depends, status

from schemas.user import CurrentUserSchema, GetUserSchema, UpdateUserSchema
from services.user import UserService

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("", status_code=status.HTTP_200_OK, response_model=Sequence[GetUserSchema])
async def get_users(user_service: UserService = Depends()):
    return await user_service.get_users()


@router.get("/me", status_code=status.HTTP_200_OK, response_model=CurrentUserSchema)
async def get_current_user(token: str, user_service: UserService = Depends()):
    return await user_service.get_current_user(token=token)


@router.post("", status_code=status.HTTP_200_OK, response_model=None)
async def create_user(user: UpdateUserSchema, user_service: UserService = Depends()):
    return await user_service.create_user(user=user)


@router.delete("/{username}", status_code=status.HTTP_200_OK, response_model=None)
async def delete_user_by_username(username: str, user_service: UserService = Depends()):
    return await user_service.delete_user_by_username(username=username)
