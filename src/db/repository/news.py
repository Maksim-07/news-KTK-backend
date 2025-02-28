from typing import Any, Sequence

from sqlalchemy import delete, insert, join, select, true

from db.models import News, User
from db.repository.base import BaseDatabaseRepository
from schemas.news import GetNewsSchema, UpdateNewsSchema


class NewsRepository(BaseDatabaseRepository):
    async def get_news(self, category_id: int | None) -> Sequence[Any]:
        query = (
            select(
                News.id,
                News.image,
                News.title,
                News.content,
                News.category_id,
                News.author_id,
                News.created_at,
                User.username,
            )
            .select_from(News)
            .join(User, News.author_id == User.id)
            .filter(News.category_id == category_id if category_id else true())
        )
        result = await self._session.execute(query)

        return result.all()

    async def get_news_by_id(self, news_id: int) -> Any | None:
        query = (
            select(
                News.id,
                News.image,
                News.title,
                News.content,
                News.category_id,
                News.author_id,
                News.created_at,
                User.username,
            )
            .select_from(News)
            .join(User, News.author_id == User.id)
            .filter(News.id == news_id)
        )
        result = await self._session.execute(query)

        return result.one_or_none()

    async def get_news_by_title(self, title: str) -> News | None:
        query = select(News).where(News.title == title)
        result = await self._session.execute(query)

        return result.scalar_one_or_none()

    async def create_news(self, news: UpdateNewsSchema) -> None:
        query = insert(News).values(**news.model_dump())
        await self._session.execute(query)
        await self._session.commit()

    async def delete_news_by_id(self, news_id: int) -> None:
        query = delete(News).where(News.id == news_id)
        await self._session.execute(query)
        await self._session.commit()
