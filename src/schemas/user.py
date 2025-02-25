from schemas.base import BaseSchema


class UserSchema(BaseSchema):
    username: str
    password: str
    email: str
    first_name: str
    last_name: str


class GetUserSchema(UserSchema): ...
