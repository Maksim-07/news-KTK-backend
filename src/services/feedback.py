from typing import Sequence

from fastapi import Depends

from db.repository.feedback import FeedbackRepository
from db.repository.user import UserRepository
from schemas.feedback import GetFeedbackSchema, UpdateFeedbackSchema


class FeedbackService:
    def __init__(self, feedback_repo: FeedbackRepository = Depends(), user_repo: UserRepository = Depends()) -> None:
        self._feedback_repo = feedback_repo
        self._user_repo = user_repo

    async def get_feedbacks(self) -> Sequence[GetFeedbackSchema]:
        feedbacks = await self._feedback_repo.get_feedbacks()

        feedbacks_schemas: list[GetFeedbackSchema] = []

        for feedback in feedbacks:
            user = await self._user_repo.get_user_by_id(user_id=feedback.user_id)

            if user:
                feedbacks_schemas.append(
                    GetFeedbackSchema(
                        id=feedback.id,
                        username=user.username,
                        email=user.email,
                        description=feedback.description,
                        is_completed=feedback.is_completed,
                    )
                )

        return feedbacks_schemas

    async def create_feedback(self, feedback: UpdateFeedbackSchema) -> None:
        return await self._feedback_repo.create_feedback(feedback=feedback)
