from typing import Sequence

from sqlalchemy import delete, insert, select

from db.models import News
from db.repository.base import BaseDatabaseRepository
from schemas.news import UpdateNewsSchema


class NewsRepository(BaseDatabaseRepository):
    # TODO Добавить по категории
    async def get_news(self) -> Sequence[News]:
        query = select(News)
        result = await self._session.execute(query)

        return result.scalars().all()

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
