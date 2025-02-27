from db.session import get_session
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession


class BaseDatabaseRepository:
    _session: AsyncSession

    def __init__(self, session: AsyncSession = Depends(get_session)) -> None:
        self._session = session
