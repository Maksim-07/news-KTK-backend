from fastapi import Depends

from db.repository.fcm_token import FCMTokenRepository
from schemas.fcm_token import FCMTokenSchema


class FCMTokenService:
    def __init__(self, fcm_token_repo: FCMTokenRepository = Depends()) -> None:
        self.fcm_token_repo = fcm_token_repo

    async def save_token(self, user_id: int, token: FCMTokenSchema) -> None:
        return await self.fcm_token_repo.save_token(user_id=user_id, token=token)
