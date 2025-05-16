from typing import Sequence

from fastapi import APIRouter, Depends, status

from core.auth import (
    get_user_id_from_any_token,
    verify_admin_token_from_header,
    verify_user_token_from_header,
)
from schemas.feedback import GetFeedbackSchema, UpdateFeedbackSchema
from services.feedback import FeedbackService

router = APIRouter(prefix="/feedback", tags=["Feedback"])


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=Sequence[GetFeedbackSchema],
    dependencies=[Depends(verify_admin_token_from_header)],
)
async def get_feedbacks(feedback_service: FeedbackService = Depends()) -> Sequence[GetFeedbackSchema]:
    return await feedback_service.get_feedbacks()


@router.post("", status_code=status.HTTP_200_OK, response_model=None)
async def create_feedback(
    feedback: UpdateFeedbackSchema,
    user_id: int = Depends(get_user_id_from_any_token),
    feedback_service: FeedbackService = Depends(),
) -> None:
    return await feedback_service.create_feedback(user_id=user_id, feedback=feedback)
