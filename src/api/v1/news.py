from typing import Sequence

from fastapi import APIRouter, Depends, status

from schemas.news import GetNewsSchema, UpdateNewsSchema
from services.news import NewsService

router = APIRouter(prefix="/news", tags=["News"])


@router.get("", status_code=status.HTTP_200_OK, response_model=Sequence[GetNewsSchema])
async def get_news(news_service: NewsService = Depends()):
    return await news_service.get_news()


@router.post("", status_code=status.HTTP_200_OK, response_model=None)
async def create_news(news: UpdateNewsSchema, news_service: NewsService = Depends()):
    return await news_service.create_news(news=news)


@router.delete("/{title}", status_code=status.HTTP_200_OK, response_model=None)
async def delete_news_by_title(title: str, news_service: NewsService = Depends()):
    return await news_service.delete_news_by_title(title=title)
