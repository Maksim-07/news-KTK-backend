from typing import Sequence

from fastapi import Depends

from db.repository.fcm_token import FCMTokenRepository
from schemas.fcm_token import FCMTokenSchema, GetFCMTokenSchema


class FCMTokenService:
    def __init__(self, fcm_token_repo: FCMTokenRepository = Depends()) -> None:
        self.fcm_token_repo = fcm_token_repo

    async def get_tokens(self) -> Sequence[GetFCMTokenSchema]:
        tokens = await self.fcm_token_repo.get_tokens_with_all_info()

        return [GetFCMTokenSchema.model_validate(token) for token in tokens]

    async def save_token(self, user_id: int, token: FCMTokenSchema) -> None:
        return await self.fcm_token_repo.save_token(user_id=user_id, token=token)
