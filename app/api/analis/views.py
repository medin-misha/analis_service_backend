from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from core import database
from .schemes import CreateAnalis, ReturnAnalis
from .options import (
    create_analis,
    get_analis,
    get_analis_list,
    delete_analis,
    get_analis_by_name_and_user_id,
)

router = APIRouter(prefix="/analis", tags=["analis"])


@router.post("/")
async def create_analis_view(
    analis_data: CreateAnalis, session: AsyncSession = Depends(database.get_new_session)
) -> ReturnAnalis:
    return await create_analis(session=session, analis_data=analis_data)


@router.get("/")
async def get_analis_list_view(
    session: AsyncSession = Depends(database.get_new_session),
) -> List[ReturnAnalis]:
    return await get_analis_list(session=session)


@router.get("/{analis_id}")
async def get_analis_view(
    analis_id: int, session: AsyncSession = Depends(database.get_new_session)
) -> ReturnAnalis:
    object = await get_analis(session=session, analis_id=analis_id)
    if object is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return object


@router.get("/name/{analis_name}/{user_id}")
async def get_analis_by_name_and_user_id_view(
    analis_name: str,
    user_id: int,
    session: AsyncSession = Depends(database.get_new_session),
) -> ReturnAnalis:
    object = await get_analis_by_name_and_user_id(
        session=session, name=analis_name, user_id=user_id
    )
    if object is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return object


@router.delete("/{analis_id}")
async def delete_analis_view(
    analis_id: int, session: AsyncSession = Depends(database.get_new_session)
):
    object = await delete_analis(session=session, analis_id=analis_id)
    if object is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
