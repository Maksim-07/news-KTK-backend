import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.router import v1_router
from core.config import settings

app = FastAPI(
    title="news-KTK",
    openapi_url="/api/openapi.json",
    docs_url="/api/swagger",
)
app.include_router(v1_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host=settings().SERVER_HOST, port=settings().SERVER_PORT)
