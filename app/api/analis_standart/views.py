from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from core import database
from .schemes import CreateAnalisStandart, ReturnAnalisStarndart, PatchAnalisStarndart
from .options import (
    create_analis_standart,
    get_analis_standart,
    get_analis_standart_list,
    patch_analis_standart,
    delete_analis_standart,
)


router = APIRouter(prefix="/analis/standart", tags=["analis standart"])


@router.post("/")
async def create_analis_standart_view(
    analis_data: CreateAnalisStandart,
    session: AsyncSession = Depends(database.get_new_session),
) -> ReturnAnalisStarndart:
    return await create_analis_standart(session=session, analis_data=analis_data)


@router.get("/")
async def get_analis_standart_list_view(
    session: AsyncSession = Depends(database.get_new_session),
) -> List[ReturnAnalisStarndart]:
    return await get_analis_standart_list(session=session)


@router.get("/{analis_id}")
async def get_analis_standart_view(
    analis_id: int, session: AsyncSession = Depends(database.get_new_session)
) -> ReturnAnalisStarndart:
    object = await get_analis_standart(session=session, analis_id=analis_id)
    if object is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return object


@router.patch("/{analis_id}")
async def patch_analis_standart_view(
    analis_id: int,
    analis_data: PatchAnalisStarndart,
    session: AsyncSession = Depends(database.get_new_session),
) -> ReturnAnalisStarndart:
    object = await patch_analis_standart(
        session=session, analis_data=analis_data, analis_id=analis_id
    )
    if object is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return object


@router.delete("/{analis_id}")
async def analis_standart_view(
    analis_id: int, session: AsyncSession = Depends(database.get_new_session)
):
    object = await delete_analis_standart(session=session, analis_id=analis_id)
    if object is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
