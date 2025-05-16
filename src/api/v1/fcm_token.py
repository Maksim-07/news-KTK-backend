from fastapi import APIRouter, Depends, status

from core.auth import get_user_id_from_any_token
from schemas.fcm_token import FCMTokenSchema
from services.fcm_token import FCMTokenService

router = APIRouter(prefix="/fcm-token", tags=["FCM Token"])


@router.post("", status_code=status.HTTP_200_OK, response_model=None)
async def save_token(
    token: FCMTokenSchema,
    user_id: int = Depends(get_user_id_from_any_token),
    fcm_token_service: FCMTokenService = Depends(),
) -> None:
    return await fcm_token_service.save_token(user_id=user_id, token=token)
