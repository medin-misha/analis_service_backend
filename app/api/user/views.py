from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from core import database
from .options import get_all_users, create_user, get_user_by_id, delete_user, patch_user
from .schemas import CreateUser, ReturnUser, PatchUser


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
async def get_all_users_view(
    session: AsyncSession = Depends(database.get_new_session),
) -> List[ReturnUser]:
    return await get_all_users(session=session)


@router.get("/{user_id}")
async def get_user_by_id_view(
    user_id: int, session: AsyncSession = Depends(database.get_new_session)
) -> ReturnUser:
    return await get_user_by_id(session=session, user_id=user_id)


@router.post("/")
async def create_user_view(
    user_data: CreateUser, session: AsyncSession = Depends(database.get_new_session)
) -> ReturnUser:
    return await create_user(session=session, user_data=user_data)


@router.patch("/")
async def patch_user_view(
    user_id: int,
    user_data: PatchUser,
    session: AsyncSession = Depends(database.get_new_session),
) -> ReturnUser | int:
    return await patch_user(session=session, user_id=user_id, user_data=user_data)


@router.delete("/")
async def delete_user_view(
    user_id: int, session: AsyncSession = Depends(database.get_new_session)
) -> int:
    return await delete_user(session=session, user_id=user_id)