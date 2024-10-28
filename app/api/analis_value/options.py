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


async def get_analis_value(
    session: AsyncSession, analis_id: int
) -> ReturnAnalisValue | None:
    stmt = select(AnalisValue).where(AnalisValue.id == analis_id)
    result: Result = await session.execute(stmt)
    return result.scalar()

async def get_analis_value_by_analis_id(
    session: AsyncSession, analis_id: int
) -> list[ReturnAnalisValue] | None:
    stmt = select(AnalisValue).where(AnalisValue.analis_id == analis_id)
    result: Result = await session.execute(stmt)
    return result.scalars().all()

async def patch_analis_value(
    session: AsyncSession, analis_id: int, analis_data: PatchAnalisValue
) -> ReturnAnalisValue | None:
    async with session.begin():
        analis_value_model = await session.get(AnalisValue, analis_id)

        if analis_value_model is None:
            return

        for key, value in analis_data.model_dump(exclude_unset=True).items():
            setattr(analis_value_model, key, value)

        await session.commit()

    await session.refresh(analis_value_model)
    return ReturnAnalisValue(**analis_value_model.__dict__)


async def delete_analis_value(session: AsyncSession, analis_id: int) -> int | None:
    analis_model = await session.get(AnalisValue, analis_id)
    if analis_model is None:
        return
    await session.delete(analis_model)
    await session.commit()
    return 204
