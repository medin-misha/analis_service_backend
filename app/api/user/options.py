from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result, delete
from sqlalchemy.exc import IntegrityError
from typing import List
from .schemas import CreateUser, ReturnUser, PatchUser
from core import User


async def get_all_users(session: AsyncSession) -> List[ReturnUser]:
    stmt = select(User).order_by(User.id)
    result: Result = await session.execute(stmt)
    return result.scalars().all()


async def get_user_by_id(session: AsyncSession, user_id: int) -> ReturnUser | None:
    stmt = select(User).where(User.id == user_id).order_by(User.id)
    result: Result = await session.execute(stmt)
    return result.scalar()


async def get_user_by_user_name(session: AsyncSession, name: str) -> ReturnUser | None:
    stmt = select(User).where(User.name == name)
    result: Result = await session.execute(stmt)
    return result.scalar()


async def create_user(
    session: AsyncSession, user_data: CreateUser
) -> ReturnUser | None:
    try:
        user = User(**user_data.model_dump())

        async with session.begin():
            session.add(user)
            await session.commit()
    except IntegrityError:
        return

    await session.refresh(user)
    return ReturnUser(**user.__dict__)


async def patch_user(
    session: AsyncSession, user_id: int, user_data: PatchUser
) -> ReturnUser | None:
    user = await session.get(User, user_id)
    if user is None:
        return None
    for key, value in user_data.model_dump(exclude_unset=True).items():
        setattr(user, key, value)
    await session.commit()
    await session.refresh(user)
    return ReturnUser(**user.__dict__)


async def delete_user(session: AsyncSession, user_id: int) -> int | None:
    user = await session.get(User, user_id)
    if user is None:
        return
    await session.delete(user)
    await session.commit()
    return 204
