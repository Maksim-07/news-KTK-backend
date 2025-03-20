from fastapi import APIRouter, Depends

from api.v1.auth import router as auth_router
from api.v1.feedback import router as feedback_router
from api.v1.news import router as news_router
from api.v1.news_category import router as news_category_router
from api.v1.user import router as user_router
from core.auth import verify_token_from_header
from core.config import settings

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(news_category_router)
v1_router.include_router(user_router, dependencies=[Depends(verify_token_from_header)])
v1_router.include_router(news_router)
v1_router.include_router(auth_router)
v1_router.include_router(feedback_router)

project_router = APIRouter(prefix=f"/{settings().PROJECT_NAME}")
project_router.include_router(v1_router)

api_router = APIRouter(prefix="/api")
api_router.include_router(project_router)
