from typing import Sequence

from sqlalchemy import delete, insert, select, update

from db.models import NewsCategory
from db.repository.base import BaseDatabaseRepository
from schemas.news_category import UpdateNewsCategorySchema


class NewsCategoryRepository(BaseDatabaseRepository):
    async def get_categories(self) -> Sequence[NewsCategory]:
        query = select(NewsCategory)
        result = await self._session.execute(query)

        return result.scalars().all()

    async def get_category_by_id(self, category_id: int) -> NewsCategory | None:
        query = select(NewsCategory).where(NewsCategory.id == category_id)
        result = await self._session.execute(query)

        return result.scalar_one_or_none()

    async def get_category_by_name(self, category_name: str) -> NewsCategory | None:
        query = select(NewsCategory).where(NewsCategory.name == category_name)
        result = await self._session.execute(query)

        return result.scalar_one_or_none()

    async def create_category(self, news_category: UpdateNewsCategorySchema) -> None:
        query = insert(NewsCategory).values(**news_category.model_dump())
        await self._session.execute(query)
        await self._session.commit()

    async def update_category(self, category_id: int, news_category: UpdateNewsCategorySchema) -> None:
        query = update(NewsCategory).where(NewsCategory.id == category_id).values(**news_category.model_dump())
        await self._session.execute(query)
        await self._session.commit()

    async def delete_category_by_id(self, category_id: int) -> None:
        query = delete(NewsCategory).where(NewsCategory.id == category_id)
        await self._session.execute(query)
        await self._session.commit()
