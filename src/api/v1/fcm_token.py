from typing import Sequence

from fastapi import APIRouter, Depends, status

from schemas.fcm_token import FCMTokenSchema
from services.fcm_token import FCMTokenService

router = APIRouter(prefix="/fcm-token", tags=["FCM Token"])


@router.post("", status_code=status.HTTP_200_OK, response_model=None)
async def save_token(token: FCMTokenSchema, fcm_token_service: FCMTokenService = Depends()) -> None:
    return await fcm_token_service.save_token(token=token)
