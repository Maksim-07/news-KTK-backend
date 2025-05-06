from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from db.models.base import BaseModel
from db.models.mixins import CreatedAtMixin, IDMixin


class FCMToken(BaseModel, IDMixin, CreatedAtMixin):
    __tablename__ = "fcm_tokens"

    token: Mapped[str] = mapped_column(String, nullable=False)
