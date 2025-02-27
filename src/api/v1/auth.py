from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from services.auth import AuthService

router = APIRouter(prefix="/auth", tags=["Authorization"])


@router.post("/login", status_code=status.HTTP_200_OK, response_model=None)
async def login_user(user: OAuth2PasswordRequestForm = Depends(), auth_service: AuthService = Depends()):
    return await auth_service.login_user(user=user)
