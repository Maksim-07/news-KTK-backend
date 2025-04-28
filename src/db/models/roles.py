from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from db.models import BaseModel
from db.models.mixins import CreatedAtMixin, IDMixin


class Role(BaseModel, IDMixin, CreatedAtMixin):
    __tablename__ = "roles"

    name: Mapped[str] = mapped_column(String, nullable=False)
    can_edit_news: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_edit_categories: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_edit_admins: Mapped[bool] = mapped_column(Boolean, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False)
