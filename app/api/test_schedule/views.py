from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from core import database
from starlette.responses import StreamingResponse
from .schemes import GetUserAndAnalis
from .options import get_schedule

router = APIRouter(prefix="/schedule", tags=["test"])


@router.post("/")
async def get_schedule_view(
    user_and_analis_ids: GetUserAndAnalis,
    session: AsyncSession = Depends(database.get_new_session),
) -> StreamingResponse:
    object = await get_schedule(session=session, user_and_analis_ids=user_and_analis_ids)
    if object is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    elif object == "No":
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    return object