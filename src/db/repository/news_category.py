from typing import Sequence

from db.models import NewsCategory
from db.repository.base import BaseDatabaseRepository
from schemas.news_category import UpdateNewsCategorySchema
from sqlalchemy import delete, insert, select


class NewsCategoryRepository(BaseDatabaseRepository):
    async def get_categories(self) -> Sequence[NewsCategory]:
        query = select(NewsCategory)
        result = await self._session.execute(query)

        return result.scalars().all()

    async def get_category_by_name(self, name: str) -> NewsCategory | None:
        query = select(NewsCategory).where(NewsCategory.name == name)
        result = await self._session.execute(query)

        return result.scalar_one_or_none()

    async def create_category(self, news_category: UpdateNewsCategorySchema) -> None:
        query = insert(NewsCategory).values(**news_category.dict())
        await self._session.execute(query)
        await self._session.commit()

    async def delete_category_by_id(self, category_id: int) -> None:
        query = delete(NewsCategory).where(NewsCategory.id == category_id)
        await self._session.execute(query)
        await self._session.commit()
