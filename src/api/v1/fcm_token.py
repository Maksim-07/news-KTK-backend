from typing import Sequence

from fastapi import APIRouter, Depends, status

from core.auth import (
    get_user_id_from_any_token,
    verify_admin_token_from_header,
)
from schemas.fcm_token import FCMTokenSchema, GetFCMTokenSchema
from services.fcm_token import FCMTokenService

router = APIRouter(prefix="/fcm-token", tags=["FCM Token"])


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=Sequence[GetFCMTokenSchema],
    dependencies=[Depends(verify_admin_token_from_header)],
)
async def get_tokens(
    fcm_token_service: FCMTokenService = Depends(),
) -> Sequence[GetFCMTokenSchema]:
    return await fcm_token_service.get_tokens()


@router.post("", status_code=status.HTTP_200_OK, response_model=None)
async def save_token(
    token: FCMTokenSchema,
    user_id: int = Depends(get_user_id_from_any_token),
    fcm_token_service: FCMTokenService = Depends(),
) -> None:
    return await fcm_token_service.save_token(user_id=user_id, token=token)
