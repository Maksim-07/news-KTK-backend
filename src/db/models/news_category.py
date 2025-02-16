from db.models.base import BaseModel
from db.models.mixins import IDMixin
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class NewsCategory(BaseModel, IDMixin):
    __tablename__ = "news_category"

    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    description: Mapped[str] = mapped_column(String, nullable=False)
