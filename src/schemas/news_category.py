from schemas.base import BaseSchema


class NewsCategorySchema(BaseSchema):
    name: str
    description: str


class GetNewsCategorySchema(NewsCategorySchema):
    id: int


class UpdateNewsCategorySchema(NewsCategorySchema): ...
