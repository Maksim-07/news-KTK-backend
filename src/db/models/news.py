from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import BYTEA
from sqlalchemy.orm import Mapped, mapped_column

from db.models.base import BaseModel
from db.models.mixins import CreatedAtMixin, IDMixin, UpdatedAtMixin


class News(BaseModel, IDMixin, CreatedAtMixin, UpdatedAtMixin):
    __tablename__ = "news"

    title: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    content: Mapped[str] = mapped_column(String, nullable=False)
    image: Mapped[BYTEA] = mapped_column(BYTEA, nullable=True)
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("news_category.id"))
