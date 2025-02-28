from typing import Sequence

from fastapi import APIRouter, Depends, status

from schemas.news import GetNewsSchema, UpdateNewsSchema
from services.news import NewsService

router = APIRouter(prefix="/news", tags=["News"])


@router.get("", status_code=status.HTTP_200_OK, response_model=Sequence[GetNewsSchema])
async def get_news(category_id: int | None = None, news_service: NewsService = Depends()):
    return await news_service.get_news(category_id=category_id)


@router.post("", status_code=status.HTTP_200_OK, response_model=None)
async def create_news(news: UpdateNewsSchema, news_service: NewsService = Depends()):
    return await news_service.create_news(news=news)


@router.delete("/{news_id}", status_code=status.HTTP_200_OK, response_model=None)
async def delete_news_by_id(news_id: int, news_service: NewsService = Depends()):
    return await news_service.delete_news_by_id(news_id=news_id)
