from typing import Sequence

from fastapi import Depends

from core.exceptions import (
    news_already_exists_exceptions,
    news_not_found_exceptions,
)
from db.repository.news import NewsRepository
from db.repository.news_category import NewsCategoryRepository
from schemas.news import GetNewsSchema, UpdateNewsSchema
from schemas.news_category import UpdateNewsCategorySchema


class NewsService:
    def __init__(self, news_repo: NewsRepository = Depends(), news_category_repo: NewsCategoryRepository = Depends()):
        self._news_repo = news_repo
        self._news_category_repo = news_category_repo

    async def get_news(self, category_id: int | None) -> Sequence[GetNewsSchema]:
        news = await self._news_repo.get_news(category_id=category_id)

        return [GetNewsSchema.model_validate(news_one) for news_one in news]

    async def create_news(self, news: UpdateNewsSchema) -> None:
        current_news = await self._news_repo.get_news_by_title(title=news.title)

        if current_news:
            raise news_already_exists_exceptions

        return await self._news_repo.create_news(news=news)

    async def delete_news_by_id(self, news_id: int):
        current_news = await self._news_repo.get_news_by_id(news_id=news_id)

        if current_news is None:
            raise news_not_found_exceptions

        return await self._news_repo.delete_news_by_id(news_id=current_news.id)
