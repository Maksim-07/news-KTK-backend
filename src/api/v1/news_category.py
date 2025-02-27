from typing import Sequence

from fastapi import APIRouter, Depends, status
from schemas.news_category import (
    GetNewsCategorySchema,
    UpdateNewsCategorySchema,
)
from services.news_category import NewsCategoryService

router = APIRouter(prefix="/news-category", tags=["News Category"])


@router.get("", status_code=status.HTTP_200_OK, response_model=Sequence[GetNewsCategorySchema])
async def get_news_categories(news_category_service: NewsCategoryService = Depends()):
    return await news_category_service.get_news_categories()


@router.post("", status_code=status.HTTP_200_OK, response_model=None)
async def create_news_category(
    news_category: UpdateNewsCategorySchema, news_category_service: NewsCategoryService = Depends()
):
    return await news_category_service.create_news_category(news_category=news_category)


@router.delete("/{name}", status_code=status.HTTP_200_OK, response_model=None)
async def delete_news_category(name: str, news_category_service: NewsCategoryService = Depends()):
    return await news_category_service.delete_news_category_by_name(name=name)
