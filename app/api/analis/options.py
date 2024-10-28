from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result, delete
from typing import List
from core import Analis, User, AnalisValue
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


async def get_analis_by_name_and_user_id(
    session: AsyncSession, name: str, user_id: int
) -> ReturnAnalis:
    stmt = select(Analis).where(Analis.name == name, User.id == user_id)
    result: Result = await session.execute(stmt)
    return result.scalar()


async def get_analis_by_user_id(
    session: AsyncSession, user_id: int
) -> List[ReturnAnalis]:
    stmt = select(Analis).where(User.id == user_id).order_by(Analis.id)
    result: Result = await session.execute(stmt)
    return result.scalars().all()


async def delete_analis(session: AsyncSession, analis_id: int) -> int | None:
    analis = await session.get(Analis, analis_id)
    stmt = delete(AnalisValue).where(AnalisValue.analis_id == analis_id)
    if analis is None:
        return
    await session.delete(analis)
    await session.execute(stmt)
    await session.commit()
    return 204
