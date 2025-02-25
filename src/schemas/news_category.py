from schemas.base import BaseSchema


class NewsCategorySchema(BaseSchema):
    name: str
    description: str


class GetNewsCategorySchema(NewsCategorySchema): ...


class UpdateNewsCategorySchema(NewsCategorySchema): ...
