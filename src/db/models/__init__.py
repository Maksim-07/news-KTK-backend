__all__ = ("BaseModel", "User", "News", "NewsCategory", "Feedback")

from db.models.base import BaseModel
from db.models.feedback import Feedback
from db.models.news import News
from db.models.news_category import NewsCategory
from db.models.user import User
