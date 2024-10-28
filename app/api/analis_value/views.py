from fastapi import APIRouter, Depends, HTTPException, status
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
    get_analis_value_by_analis_id
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


@router.get("/{analis_value_id}")
async def get_analis_value_view(
    analis_value_id: int, session: AsyncSession = Depends(database.get_new_session)
) -> ReturnAnalisValue:
    object = await get_analis_value(session=session, analis_id=analis_value_id)
    if object is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return object

@router.get("/analis/{analis_id}")
async def get_analis_value_by_analis_id_view(
    analis_id: int, session: AsyncSession = Depends(database.get_new_session)
) -> List[ReturnAnalisValue]:
    return await get_analis_value_by_analis_id(session=session, analis_id=analis_id)

@router.patch("/{analis_value_id}")
async def patch_analis_value_view(
    analis_value_id: int,
    analis_data: PatchAnalisValue,
    session: AsyncSession = Depends(database.get_new_session),
) -> ReturnAnalisValue:
    return await patch_analis_value(
        session=session, analis_data=analis_data, analis_id=analis_value_id
    )


@router.delete("/{analis_value_id}")
async def analis_value_view(
    analis_value_id: int, session: AsyncSession = Depends(database.get_new_session)
):
    object = await delete_analis_value(session=session, analis_id=analis_value_id)
    if object is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
