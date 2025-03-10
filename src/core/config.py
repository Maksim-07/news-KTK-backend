import functools
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Класс настроек проекта: импорт параметров из .env
    и установка значений по умолчанию.
    """

    root_dir: Path = Path(__file__).resolve().parent.parent.parent
    src_dir: Path = root_dir.joinpath("src")
    env_file: Path = src_dir.joinpath(".env")

    PROJECT_NAME: str = "news-ktk"

    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 8000

    ENVIRONMENT: str = "local"

    CORS_ALLOW_ORIGIN_LIST: str = "http://127.0.0.1:8000"

    POSTGRES_HOST: str = "news-ktk-db"
    POSTGRES_PORT: int = 5632
    POSTGRES_USER: str = "news-ktk-db"
    POSTGRES_PASSWORD: str = "news-ktk-db"
    POSTGRES_DB: str = "news-ktk-db"

    ALGORITHM: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    REFRESH_TOKEN_EXPIRE_DAYS: int = 90

    @functools.cached_property
    def cors_allow_origins(self) -> list[str]:
        return self.CORS_ALLOW_ORIGIN_LIST.split("&")

    @functools.cached_property
    def postgres_dsn(self) -> str:
        postgres_host = "localhost" if self.ENVIRONMENT == "local" else self.POSTGRES_HOST
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{postgres_host}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    model_config = SettingsConfigDict(env_file=env_file if env_file else None, env_file_encoding="utf-8")


@functools.lru_cache()
def settings():
    return Settings()
