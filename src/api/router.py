from api.v1.news_category import router as news_category_router
from core.config import settings
from fastapi import APIRouter

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(news_category_router)

project_router = APIRouter(prefix=f"/{settings().PROJECT_NAME}")
project_router.include_router(v1_router, dependencies=[])

api_router = APIRouter(prefix="/api")
api_router.include_router(project_router)
