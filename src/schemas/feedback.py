from schemas.base import BaseSchema


class FeedbackSchema(BaseSchema):
    username: str
    email: str
    description: str


class GetFeedbackSchema(FeedbackSchema):
    id: int
    is_completed: bool


class UpdateFeedbackSchema(FeedbackSchema): ...
