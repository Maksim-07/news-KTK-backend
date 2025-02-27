from typing import Sequence

from fastapi import Depends

from core.exceptions import (
    news_already_exists_exceptions,
    news_not_found_exceptions,
)
from db.repository.news import NewsRepository
from schemas.news import GetNewsSchema, UpdateNewsSchema
from schemas.news_category import UpdateNewsCategorySchema


class NewsService:
    def __init__(self, news_repo: NewsRepository = Depends()):
        self._news_repo = news_repo

    async def get_news(self) -> Sequence[GetNewsSchema]:
        news = await self._news_repo.get_news()

        return [GetNewsSchema.model_validate(news_one) for news_one in news]

    async def create_news(self, news: UpdateNewsSchema) -> None:
        current_news = await self._news_repo.get_news_by_title(title=news.title)

        if current_news:
            raise news_already_exists_exceptions

        return await self._news_repo.create_news(news=news)

    async def delete_news_by_title(self, title: str):
        current_news = await self._news_repo.get_news_by_title(title=title)

        if current_news is None:
            raise news_not_found_exceptions

        return await self._news_repo.delete_news_by_id(news_id=current_news.id)
