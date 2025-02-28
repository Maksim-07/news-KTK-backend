from datetime import datetime

from pydantic.json_schema import SkipJsonSchema

from schemas.base import BaseSchema


class NewsSchema(BaseSchema):
    title: str
    content: str
    image: bytes | None = None
    author_id: int
    category_id: int


class GetNewsSchema(NewsSchema):
    id: int
    username: str
    created_at: datetime


class UpdateNewsSchema(NewsSchema): ...
