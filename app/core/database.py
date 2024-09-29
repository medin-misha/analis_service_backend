from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker


class DataBase:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(bind=url)
        self.session_factory = async_sessionmaker(bind=self.engine)

    async def get_new_session(self) -> AsyncSession:
        async with self.session_factory() as session:
            yield session
            await session.close()
