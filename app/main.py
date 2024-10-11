from fastapi import FastAPI
from core import settings, Base, database
from api import user_router, analis_router, analis_value_router, analis_standart_router

app = FastAPI()

app.include_router(user_router)
app.include_router(analis_router)
app.include_router(analis_value_router)
app.include_router(analis_standart_router)

@app.get("/make-test-db")
async def make_test_db():
    if settings.is_test:
        async with database.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
    return 200