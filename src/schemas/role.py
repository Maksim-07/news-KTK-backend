from schemas.base import BaseSchema


class RoleSchema(BaseSchema):
    name: str
    can_edit_news: bool
    can_edit_categories: bool
    can_edit_admins: bool
    is_active: bool


class GetRoleSchema(RoleSchema):
    id: int


class CreateRoleSchema(RoleSchema): ...
