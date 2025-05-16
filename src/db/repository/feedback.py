from typing import Sequence

from sqlalchemy import insert, select

from db.models import Feedback
from db.repository.base import BaseDatabaseRepository
from schemas.feedback import UpdateFeedbackSchema


class FeedbackRepository(BaseDatabaseRepository):
    async def get_feedbacks(self) -> Sequence[Feedback]:
        query = select(Feedback)
        result = await self._session.execute(query)

        return result.scalars().all()

    async def create_feedback(self, user_id: int, feedback: UpdateFeedbackSchema) -> None:
        query = insert(Feedback).values({Feedback.user_id: user_id, Feedback.description: feedback.description})

        await self._session.execute(query)
        await self._session.commit()
