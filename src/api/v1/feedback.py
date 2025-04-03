from typing import Sequence

from fastapi import APIRouter, Depends, status

from schemas.feedback import GetFeedbackSchema, UpdateFeedbackSchema
from services.feedback import FeedbackService

router = APIRouter(prefix="/feedback", tags=["Feedback"])


@router.get("", status_code=status.HTTP_200_OK, response_model=Sequence[GetFeedbackSchema])
async def get_feedbacks(feedback_service: FeedbackService = Depends()) -> Sequence[GetFeedbackSchema]:
    return await feedback_service.get_feedbacks()


@router.post("", status_code=status.HTTP_200_OK, response_model=None)
async def create_feedback(feedback: UpdateFeedbackSchema, feedback_service: FeedbackService = Depends()) -> None:
    return await feedback_service.create_feedback(feedback=feedback)
