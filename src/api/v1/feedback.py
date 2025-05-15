from typing import Sequence

from fastapi import APIRouter, Depends, status

from core.auth import oauth2_admin_scheme, oauth2_user_scheme
from schemas.feedback import GetFeedbackSchema, UpdateFeedbackSchema
from services.feedback import FeedbackService

router = APIRouter(prefix="/feedback", tags=["Feedback"])


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=Sequence[GetFeedbackSchema],
    dependencies=[Depends(oauth2_admin_scheme)],
)
async def get_feedbacks(feedback_service: FeedbackService = Depends()) -> Sequence[GetFeedbackSchema]:
    return await feedback_service.get_feedbacks()


@router.post(
    "",
    status_code=status.HTTP_200_OK,
    response_model=None,
    dependencies=[Depends(oauth2_user_scheme), Depends(oauth2_admin_scheme)],
)
async def create_feedback(feedback: UpdateFeedbackSchema, feedback_service: FeedbackService = Depends()) -> None:
    return await feedback_service.create_feedback(feedback=feedback)
