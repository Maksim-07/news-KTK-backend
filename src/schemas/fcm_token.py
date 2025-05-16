from schemas.base import BaseSchema


class FCMTokenSchema(BaseSchema):
    token: str


class GetFCMTokenSchema(FCMTokenSchema):
    user_id: int
