from typing import Sequence

from fastapi import Depends

from core.exceptions import (
    news_already_exists_exceptions,
    news_category_not_found_exceptions,
    news_not_found_exceptions,
)
from db.repository.news import NewsRepository
from db.repository.news_category import NewsCategoryRepository
from schemas.news import GetNewsSchema, UpdateNewsSchema
from services.notification import NotificationService


class NewsService:
    def __init__(
        self,
        news_repo: NewsRepository = Depends(),
        news_category_repo: NewsCategoryRepository = Depends(),
        notification_service: NotificationService = Depends(),
    ):
        self._news_repo = news_repo
        self._news_category_repo = news_category_repo
        self._notification_service = notification_service

    async def get_news(self, category_id: int | None) -> Sequence[GetNewsSchema]:
        news = await self._news_repo.get_news(category_id=category_id)

        return [GetNewsSchema.model_validate(news_one) for news_one in news]

    async def get_news_by_id(self, news_id: int) -> GetNewsSchema | None:
        news = await self._news_repo.get_news_by_id(news_id=news_id)

        if news is None:
            raise news_not_found_exceptions

        return GetNewsSchema.model_validate(news)

    async def create_news(self, news: UpdateNewsSchema, image) -> None:
        current_news_category = await self._news_category_repo.get_category_by_id(category_id=news.category_id)

        if current_news_category is None:
            raise news_category_not_found_exceptions

        current_news = await self._news_repo.get_news_by_title(title=news.title)

        if current_news:
            raise news_already_exists_exceptions

        if image:
            news.image = await image.read()

        await self._news_repo.create_news(news=news)

        await self._notification_service.add_news(
            title="Новая новость! 🛎", body=f"{news.title[:25]}" if len(news.title) < 25 else f"{news.title[:25]}..."
        )

        return None

    async def update_news(self, news_id: int, news: UpdateNewsSchema, image) -> None:
        current_news = await self._news_repo.get_news_by_id(news_id=news_id)

        if current_news is None:
            raise news_not_found_exceptions

        if image:
            news.image = await image.read()

        return await self._news_repo.update_news(news_id=news_id, news=news)

    async def delete_news_by_id(self, news_id: int):
        current_news = await self._news_repo.get_news_by_id(news_id=news_id)

        if current_news is None:
            raise news_not_found_exceptions

        return await self._news_repo.delete_news_by_id(news_id=current_news.id)
