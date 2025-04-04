from typing import Sequence

from fastapi import Depends

from core.exceptions import (
    news_category_already_exists_exceptions,
    news_category_not_found_exceptions,
)
from db.repository.news_category import NewsCategoryRepository
from schemas.news_category import (
    GetNewsCategorySchema,
    UpdateNewsCategorySchema,
)


class NewsCategoryService:
    def __init__(self, news_category_repo: NewsCategoryRepository = Depends()):
        self._news_category_repo = news_category_repo

    async def get_news_categories(self) -> Sequence[GetNewsCategorySchema]:
        categories = await self._news_category_repo.get_categories()

        return [GetNewsCategorySchema.model_validate(category) for category in categories]

    async def get_news_category_by_id(self, category_id: int) -> GetNewsCategorySchema:
        news_category = await self._news_category_repo.get_category_by_id(category_id=category_id)

        if news_category is None:
            raise news_category_not_found_exceptions

        return GetNewsCategorySchema.model_validate(news_category)

    async def create_news_category(self, news_category: UpdateNewsCategorySchema) -> None:
        current_news_category = await self._news_category_repo.get_category_by_name(category_name=news_category.name)

        if current_news_category:
            raise news_category_already_exists_exceptions

        return await self._news_category_repo.create_category(news_category=news_category)

    async def update_news_category(self, category_id: int, news_category: UpdateNewsCategorySchema) -> None:
        current_news_category = await self._news_category_repo.get_category_by_id(category_id=category_id)

        if current_news_category is None:
            raise news_category_not_found_exceptions

        return await self._news_category_repo.update_category(category_id=category_id, news_category=news_category)

    async def delete_news_category_by_id(self, category_id: int):
        news_category = await self._news_category_repo.get_category_by_id(category_id=category_id)

        if news_category is None:
            raise news_category_not_found_exceptions

        return await self._news_category_repo.delete_category_by_id(category_id=news_category.id)
