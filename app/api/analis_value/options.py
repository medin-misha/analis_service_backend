from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result
from typing import List
from datetime import date
from core import AnalisValue
from .schemes import CreateAnalisValue, ReturnAnalisValue, PatchAnalisValue


async def create_analis_value(
    session: AsyncSession, analis_data: CreateAnalisValue
) -> ReturnAnalisValue:
    analis_value_model = AnalisValue(**analis_data.model_dump())
    async with session.begin():
        session.add(analis_value_model)
        await session.commit()
    await session.refresh(analis_value_model)
    return ReturnAnalisValue(**analis_value_model.__dict__)


async def get_analis_value_list(session: AsyncSession) -> List[ReturnAnalisValue]:
    stmt = select(AnalisValue).order_by(AnalisValue.id)
    result: Result = await session.execute(stmt)
    return result.scalars().all()


async def get_analis_value(session: AsyncSession, analis_id: int) -> ReturnAnalisValue:
    stmt = select(AnalisValue).where(AnalisValue.id == analis_id)
    result: Result = await session.execute(stmt)
    return result.scalar()


async def patch_analis_value(
    session: AsyncSession, analis_id: int, analis_data: PatchAnalisValue
) -> ReturnAnalisValue:
    async with session.begin():
        analis_value_model = await session.get(AnalisValue, analis_id)
        for key, value in analis_data.model_dump(exclude_unset=True).items():
            setattr(analis_value_model, key, value)
        await session.commit()
    await session.refresh(analis_value_model)
    return ReturnAnalisValue(**analis_value_model.__dict__)


async def delete_analis_value(session: AsyncSession, analis_id: int) -> int:
    async with session.begin():
        await session.delete(await session.get(AnalisValue, analis_id))
        await session.commit()
    return 204
