__all__ = ("BaseModel", "User", "News", "NewsCategory")

from db.models.base import BaseModel
from db.models.news import News
from db.models.news_category import NewsCategory
from db.models.user import User
