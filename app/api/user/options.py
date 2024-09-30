from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result, delete
from typing import List
from .schemas import CreateUser, ReturnUser, PatchUser
from core import User


async def get_all_users(session: AsyncSession) -> List[ReturnUser]:
    stmt = select(User).order_by(User.id)
    result: Result = await session.execute(stmt)
    return result.scalars().all()


async def get_user_by_id(session: AsyncSession, user_id: int) -> ReturnUser:
    stmt = select(User).where(User.id == user_id).order_by(User.id)
    result: Result = await session.execute(stmt)
    return result.scalar()


async def create_user(session: AsyncSession, user_data: CreateUser) -> ReturnUser:
    user = User(**user_data.model_dump())

    async with session.begin():
        session.add(user)
        await session.commit()

    await session.refresh(user)
    return ReturnUser(**user.__dict__)


async def patch_user(
    session: AsyncSession, user_id: int, user_data: PatchUser
) -> ReturnUser | int:
    user = await session.get(User, user_id)
    if user is None:
        return 404
    for key, value in user_data.model_dump(exclude_unset=True).items():
        setattr(user, key, value)
    await session.commit()
    await session.refresh(user)
    return ReturnUser(**user.__dict__)


async def delete_user(session: AsyncSession, user_id: int) -> int:
    if user_id == -2:
        async with session.begin():
            stmt = delete(User).where(User.id)
            await session.execute(stmt)
        return 204
    async with session.begin():
        stmt = delete(User).where(User.id == user_id)
        await session.execute(stmt)
        return 204
