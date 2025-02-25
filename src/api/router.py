from fastapi import APIRouter

from api.v1.news_category import router as news_category_router

router = APIRouter(prefix="/api")

v1_router = APIRouter(prefix="/v1")

router.include_router(v1_router)

v1_router.include_router(news_category_router)
