from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from core import database
from .schemes import ReturnAnalisValue, CreateAnalisValue, PatchAnalisValue
from .options import (
    create_analis_value,
    get_analis_value,
    get_analis_value_list,
    delete_analis_value,
    patch_analis_value,
)


router = APIRouter(prefix="/analis/value", tags=["analis value"])


@router.post("/")
async def create_analis_view(
    analis_data: CreateAnalisValue,
    session: AsyncSession = Depends(database.get_new_session),
) -> ReturnAnalisValue:
    return await create_analis_value(session=session, analis_data=analis_data)


@router.get("/")
async def get_analis_value_list_view(
    session: AsyncSession = Depends(database.get_new_session),
) -> List[ReturnAnalisValue]:
    return await get_analis_value_list(session=session)


@router.get("/{analis_id}")
async def get_analis_value_view(
    analis_id: int, session: AsyncSession = Depends(database.get_new_session)
) -> ReturnAnalisValue:
    return await get_analis_value(session=session, analis_id=analis_id)


@router.patch("/{analis_id}")
async def analis_value_view(
    analis_id: int,
    analis_data: PatchAnalisValue,
    session: AsyncSession = Depends(database.get_new_session),
) -> ReturnAnalisValue:
    return await patch_analis_value(
        session=session, analis_data=analis_data, analis_id=analis_id
    )


@router.delete("/{analis_id}")
async def analis_value_view(
    analis_id: int, session: AsyncSession = Depends(database.get_new_session)
) -> int:
    return await delete_analis_value(session=session, analis_id=analis_id)
