from typing import Sequence

from fastapi import APIRouter, Depends, status

from core.auth import verify_token_from_header
from schemas.news_category import (
    GetNewsCategorySchema,
    UpdateNewsCategorySchema,
)
from services.news_category import NewsCategoryService

router = APIRouter(prefix="/news-category", tags=["News Category"])


@router.get("", status_code=status.HTTP_200_OK, response_model=Sequence[GetNewsCategorySchema])
async def get_news_categories(
    news_category_service: NewsCategoryService = Depends(),
) -> Sequence[GetNewsCategorySchema]:
    return await news_category_service.get_news_categories()


@router.get("/{category_id}", status_code=status.HTTP_200_OK, response_model=GetNewsCategorySchema)
async def get_news_category_by_id(
    category_id: int, news_category_service: NewsCategoryService = Depends()
) -> GetNewsCategorySchema:
    return await news_category_service.get_news_category_by_id(category_id=category_id)


@router.post("", status_code=status.HTTP_200_OK, response_model=None, dependencies=[Depends(verify_token_from_header)])
async def create_news_category(
    news_category: UpdateNewsCategorySchema, news_category_service: NewsCategoryService = Depends()
) -> None:
    return await news_category_service.create_news_category(news_category=news_category)


@router.put(
    "/{category_id}",
    status_code=status.HTTP_200_OK,
    response_model=None,
    dependencies=[Depends(verify_token_from_header)],
)
async def update_news_category(
    category_id: int, news_category: UpdateNewsCategorySchema, news_categroy_service: NewsCategoryService = Depends()
) -> None:
    return await news_categroy_service.update_news_category(category_id=category_id, news_category=news_category)


@router.delete(
    "/{category_id}",
    status_code=status.HTTP_200_OK,
    response_model=None,
    dependencies=[Depends(verify_token_from_header)],
)
async def delete_news_category(category_id: int, news_category_service: NewsCategoryService = Depends()) -> None:
    return await news_category_service.delete_news_category_by_id(category_id=category_id)
