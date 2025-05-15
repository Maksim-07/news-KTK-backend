from fastapi import APIRouter, Depends, Form, Request, Response, status
from fastapi.security import OAuth2PasswordRequestForm

from schemas.token import TokenSchema
from schemas.user import UserRegisterFormSchema
from services.auth import AuthService

router = APIRouter(prefix="/auth", tags=["Authorization"])


@router.post("/user/login", status_code=status.HTTP_200_OK, response_model=TokenSchema)
async def login_user(
    response: Response, user: OAuth2PasswordRequestForm = Depends(), auth_service: AuthService = Depends()
) -> TokenSchema:
    return await auth_service.login_user(response=response, user=user)


@router.post("/admin/login", status_code=status.HTTP_200_OK, response_model=TokenSchema)
async def login_admin(
    response: Response, user: OAuth2PasswordRequestForm = Depends(), auth_service: AuthService = Depends()
) -> TokenSchema:
    return await auth_service.login_admin(response=response, user=user)


@router.post("/user/register", status_code=status.HTTP_200_OK, response_model=None)
async def register_user(user: UserRegisterFormSchema = Form(...), auth_service: AuthService = Depends()) -> None:
    return await auth_service.register_user(user=user)


@router.post("/refresh", status_code=status.HTTP_200_OK, response_model=TokenSchema)
async def refresh_token(request: Request, response: Response, auth_service: AuthService = Depends()) -> TokenSchema:
    return await auth_service.refresh_token(request=request, response=response)
