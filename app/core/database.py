from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from .config import settings


class DataBase:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(url=url)
        self.session_factory = async_sessionmaker(
            bind=self.engine, expire_on_commit=False, autoflush=False
        )

    async def get_new_session(self) -> AsyncSession:
        async with self.session_factory() as session:
            yield session
            await session.close()


database = DataBase(url=settings.db_url)
