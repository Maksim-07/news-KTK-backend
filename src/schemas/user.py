from pydantic.json_schema import SkipJsonSchema

from schemas.base import BaseSchema


class UserSchema(BaseSchema):
    username: str
    password: str
    email: str
    first_name: str
    last_name: str


class CurrentUserSchema(UserSchema):
    id: int


class GetUserSchema(UserSchema):
    id: int


class UpdateUserSchema(UserSchema): ...
