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
    id: int
    old_password: str
    new_password: str


class CreateUserSchema(UserSchema):
    password: str
