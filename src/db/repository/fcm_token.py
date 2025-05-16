from typing import Sequence

from sqlalchemy import insert, select

from db.models import FCMToken
from db.repository.base import BaseDatabaseRepository
from schemas.fcm_token import FCMTokenSchema


class FCMTokenRepository(BaseDatabaseRepository):
    async def save_token(self, user_id: int, token: FCMTokenSchema) -> None:
        query = insert(FCMToken).values(**token.model_dump(), user_id=user_id)

        await self._session.execute(query)
        await self._session.commit()

    async def get_tokens(self) -> Sequence[str]:
        query = select(FCMToken.token)
        result = await self._session.execute(query)

        return result.scalars().all()

    async def get_tokens_with_all_info(self) -> Sequence[FCMToken]:
        query = select(FCMToken)
        result = await self._session.execute(query)

        return result.scalars().all()
