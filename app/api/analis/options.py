from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result
from typing import List
from core import Analis
from .schemes import CreateAnalis, ReturnAnalis


async def create_analis(
    session: AsyncSession, analis_data: CreateAnalis
) -> ReturnAnalis:
    analis = Analis(**analis_data.model_dump())
    async with session.begin():
        session.add(analis)
        await session.commit()
    await session.refresh(analis)
    return ReturnAnalis(**analis.__dict__)


async def get_analis_list(session: AsyncSession) -> List[ReturnAnalis]:
    stmt = select(Analis).order_by(Analis.id)
    result: Result = await session.execute(stmt)
    return result.scalars().all()


async def get_analis(session: AsyncSession, analis_id: int) -> ReturnAnalis:
    stmt = select(Analis).where(Analis.id == analis_id).order_by(Analis.id)
    result: Result = await session.execute(stmt)
    return result.scalar()


async def delete_analis(session: AsyncSession, analis_id: int) -> int:
    async with session.begin():
        await session.delete(await session.get(Analis, analis_id))
        await session.commit()
    return 204
