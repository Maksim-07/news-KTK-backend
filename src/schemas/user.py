from schemas.base import BaseSchema


class UserSchema(BaseSchema):
    username: str
    email: str
    first_name: str
    last_name: str


class CurrentUserSchema(UserSchema):
    id: int
    role: str


class GetUserSchema(UserSchema):
    id: int


class UpdateUserDataSchema(UserSchema): ...


class UpdateUserPasswordSchema(BaseSchema):
    old_password: str
    new_password: str


class CreateUserSchema(UserSchema):
    password: str
    role_id: int
