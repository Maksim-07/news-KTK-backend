from typing import Sequence

from fastapi import APIRouter, Depends, File, UploadFile, status

from core.auth import verify_token_from_header
from schemas.news import GetNewsSchema, UpdateNewsSchema
from services.news import NewsService

router = APIRouter(prefix="/news", tags=["News"])


@router.get("", status_code=status.HTTP_200_OK, response_model=Sequence[GetNewsSchema])
async def get_news(category_id: int | None = None, news_service: NewsService = Depends()) -> Sequence[GetNewsSchema]:
    return await news_service.get_news(category_id=category_id)


@router.get("/{news_id}", status_code=status.HTTP_200_OK, response_model=GetNewsSchema)
async def get_news_by_id(news_id: int, news_service: NewsService = Depends()) -> GetNewsSchema | None:
    return await news_service.get_news_by_id(news_id=news_id)


@router.post("", status_code=status.HTTP_200_OK, response_model=None, dependencies=[Depends(verify_token_from_header)])
async def create_news(
    news: UpdateNewsSchema = Depends(), image: UploadFile = File(None), news_service: NewsService = Depends()
) -> None:
    return await news_service.create_news(news=news, image=image)


@router.put(
    "/{news_id}", status_code=status.HTTP_200_OK, response_model=None, dependencies=[Depends(verify_token_from_header)]
)
async def update_news(
    news_id: int,
    news: UpdateNewsSchema = Depends(),
    image: UploadFile = File(None),
    news_service: NewsService = Depends(),
) -> None:
    return await news_service.update_news(news_id=news_id, news=news, image=image)


@router.delete(
    "/{news_id}", status_code=status.HTTP_200_OK, response_model=None, dependencies=[Depends(verify_token_from_header)]
)
async def delete_news_by_id(news_id: int, news_service: NewsService = Depends()) -> None:
    return await news_service.delete_news_by_id(news_id=news_id)
