from schemas.base import BaseSchema


class UserSchema(BaseSchema):
    username: str
    email: str
    first_name: str
    last_name: str


class CurrentUserSchema(UserSchema):
    id: int


class GetUserSchema(UserSchema):
    id: int


class UpdateUserSchema(UserSchema):
    password: str
