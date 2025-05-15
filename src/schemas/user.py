from pydantic import Field

from schemas.base import BaseSchema


class UserSchema(BaseSchema):
    username: str
    email: str
    first_name: str
    last_name: str


class CurrentUserSchema(UserSchema):
    id: int
    role_id: int


class GetUserSchema(UserSchema):
    id: int
    role_id: int


class UpdateUserDataSchema(UserSchema): ...


class UpdateUserPasswordSchema(BaseSchema):
    old_password: str
    new_password: str


class UpdateUserRoleSchema(BaseSchema):
    role_id: int


class CreateAdminSchema(UserSchema):
    password: str
    role_id: int


class UserRegisterFormSchema(UserSchema):
    password: str
