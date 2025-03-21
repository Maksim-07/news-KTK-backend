from datetime import datetime

from pydantic import Base64Bytes, Field

from schemas.base import BaseSchema


class NewsSchema(BaseSchema):
    title: str
    content: str
    image: Base64Bytes | None = Field(default=None)
    author_id: int
    category_id: int


class GetNewsSchema(NewsSchema):
    id: int
    username: str
    created_at: datetime


class UpdateNewsSchema(NewsSchema): ...
