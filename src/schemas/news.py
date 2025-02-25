from datetime import datetime

from schemas.base import BaseSchema


class NewsSchema(BaseSchema):
    title: str
    content: str
    image: bytes | None = None
    author_id: int
    category_id: int


class GetNewsSchema(NewsSchema):
    author_name: str
    created_at: datetime


class UpdateNewsSchema(NewsSchema): ...
