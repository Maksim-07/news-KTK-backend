from typing import Sequence

from fastapi import APIRouter, Depends, File, Form, UploadFile, status

from core.auth import (
    get_user_id_from_admin_token,
    verify_admin_token_from_header,
)
from schemas.news import GetNewsSchema, UpdateNewsSchema
from services.news import NewsService

router = APIRouter(prefix="/news", tags=["News"])


@router.get("", status_code=status.HTTP_200_OK, response_model=Sequence[GetNewsSchema])
async def get_news(category_id: int | None = None, news_service: NewsService = Depends()) -> Sequence[GetNewsSchema]:
    return await news_service.get_news(category_id=category_id)


@router.get("/{news_id}", status_code=status.HTTP_200_OK, response_model=GetNewsSchema)
async def get_news_by_id(news_id: int, news_service: NewsService = Depends()) -> GetNewsSchema | None:
    return await news_service.get_news_by_id(news_id=news_id)


@router.post(
    "", status_code=status.HTTP_200_OK, response_model=None, dependencies=[Depends(verify_admin_token_from_header)]
)
async def create_news(
    title: str = Form(...),
    content: str = Form(...),
    author_id: int = Depends(get_user_id_from_admin_token),
    category_id: int = Form(...),
    image: UploadFile = File(None),
    news_service: NewsService = Depends(),
) -> None:
    news_data = UpdateNewsSchema(title=title, content=content, category_id=category_id, author_id=author_id)

    return await news_service.create_news(news=news_data, image=image)


@router.put(
    "/{news_id}",
    status_code=status.HTTP_200_OK,
    response_model=None,
    dependencies=[Depends(verify_admin_token_from_header)],
)
async def update_news(
    news_id: int,
    title: str = Form(...),
    content: str = Form(...),
    author_id: int = Depends(get_user_id_from_admin_token),
    category_id: int = Form(...),
    image: UploadFile = File(None),
    news_service: NewsService = Depends(),
) -> None:
    news_data = UpdateNewsSchema(title=title, content=content, category_id=category_id, author_id=author_id)

    return await news_service.update_news(news_id=news_id, news=news_data, image=image)


@router.delete(
    "/{news_id}",
    status_code=status.HTTP_200_OK,
    response_model=None,
    dependencies=[Depends(verify_admin_token_from_header)],
)
async def delete_news_by_id(news_id: int, news_service: NewsService = Depends()) -> None:
    return await news_service.delete_news_by_id(news_id=news_id)
