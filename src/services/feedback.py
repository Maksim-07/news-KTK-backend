from typing import Sequence

from fastapi import Depends

from db.repository.feedback import FeedbackRepository
from schemas.feedback import GetFeedbackSchema, UpdateFeedbackSchema


class FeedbackService:
    def __init__(self, feedback_repo: FeedbackRepository = Depends()) -> None:
        self.feedback_repo = feedback_repo

    async def get_feedbacks(self) -> Sequence[GetFeedbackSchema]:
        feedbacks = await self.feedback_repo.get_feedbacks()

        return [GetFeedbackSchema.model_validate(feedback) for feedback in feedbacks]

    async def create_feedback(self, feedback: UpdateFeedbackSchema) -> None:
        return await self.feedback_repo.create_feedback(feedback=feedback)
