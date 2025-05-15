from schemas.base import BaseSchema


class FCMTokenSchema(BaseSchema):
    user_id: int
    token: str
