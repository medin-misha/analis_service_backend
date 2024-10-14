from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result
from typing import List
from datetime import date
from core import AnalisStandart
from .schemes import CreateAnalisStandart, ReturnAnalisStarndart, PatchAnalisStarndart


async def create_analis_standart(
    session: AsyncSession, analis_data: CreateAnalisStandart
) -> ReturnAnalisStarndart:

    analis_standart_model = AnalisStandart(**analis_data.model_dump())

    async with session.begin():
        session.add(analis_standart_model)
        await session.commit()

    await session.refresh(analis_standart_model)
    return ReturnAnalisStarndart(**analis_standart_model.__dict__)


async def get_analis_standart_list(
    session: AsyncSession,
) -> List[ReturnAnalisStarndart]:
    stmt = select(AnalisStandart).order_by(AnalisStandart.id)
    result: Result = await session.execute(stmt)
    return result.scalars().all()


async def get_analis_standart(
    session: AsyncSession, analis_id: int
) -> ReturnAnalisStarndart:
    stmt = select(AnalisStandart).where(AnalisStandart.id == analis_id)
    result: Result = await session.execute(stmt)
    return result.scalar()


async def patch_analis_standart(
    session: AsyncSession, analis_id: int, analis_data: PatchAnalisStarndart
) -> ReturnAnalisStarndart | None:
    async with session.begin():

        analis_standart_model = await session.get(AnalisStandart, analis_id)
        if analis_standart_model is None:
            return

        for key, value in analis_data.model_dump(exclude_unset=True).items():
            setattr(analis_standart_model, key, value)

        await session.commit()
    await session.refresh(analis_standart_model)
    return ReturnAnalisStarndart(**analis_standart_model.__dict__)


async def delete_analis_standart(session: AsyncSession, analis_id: int) -> int | None:
    analis_standart = await session.get(AnalisStandart, analis_id)
    if analis_standart is None:
        return
    await session.delete(analis_standart)
    await session.commit()
    return 204
