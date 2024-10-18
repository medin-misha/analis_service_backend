from fastapi import FastAPI, HTTPException, status
from core import settings, Base, database
from api import (
    user_router,
    analis_router,
    analis_value_router,
    analis_standart_router,
    schedule_router,
)

app = FastAPI()

app.include_router(user_router)
app.include_router(analis_router)
app.include_router(analis_value_router)
# app.include_router(analis_standart_router)
app.include_router(schedule_router)


@app.get("/make-test-db")
async def make_test_db():
    """этот эндпоинт нужен для того что бы тесты могли создавать базу данных.
    по скольку тестам лучше использовать не главную БД а базу в оперативке эта функция создаёт все таблицы в бд. 
    Он же и не даст запустить тесты на нормальной базе данных"""
    if settings.is_test:
        async with database.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        raise HTTPException(status_code=200)
    raise HTTPException(status_code=400)
    
