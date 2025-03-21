from fastapi import APIRouter, Depends, Request, Response, status
from fastapi.security import OAuth2PasswordRequestForm

from schemas.token import TokenSchema
from services.auth import AuthService

router = APIRouter(prefix="/auth", tags=["Authorization"])


@router.post("/login", status_code=status.HTTP_200_OK, response_model=TokenSchema)
async def login_user(
    response: Response, user: OAuth2PasswordRequestForm = Depends(), auth_service: AuthService = Depends()
) -> TokenSchema:
    return await auth_service.login_user(response=response, user=user)


@router.post("/refresh", status_code=status.HTTP_200_OK, response_model=TokenSchema)
async def refresh_token(request: Request, response: Response, auth_service: AuthService = Depends()) -> TokenSchema:
    return await auth_service.refresh_token(request=request, response=response)
