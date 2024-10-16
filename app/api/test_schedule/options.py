from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result
import matplotlib.pyplot as plt
from starlette.responses import StreamingResponse
from io import BytesIO
from core import User, Analis, AnalisValue
from .schemes import GetUserAndAnalis


async def get_user_by_id(session: AsyncSession, id: int) -> User | None:
    model = await session.get(User, id)
    return model


async def get_analis_by_id(session: AsyncSession, id: int) -> Analis | None:
    model = await session.get(Analis, id)
    return model


async def get_analis_value_by_user_and_analis_id(
    session: AsyncSession, user_id: int, analis_id: int
) -> List | None:
    stmt = (
        select(AnalisValue)
        .where(AnalisValue.user_id == user_id and AnalisValue.analis_id == analis_id)
        .order_by(AnalisValue.date)
    )
    analis_values_result: Result = await session.execute(stmt)
    analis_values_objects: List = analis_values_result.scalars().all()

    if len(analis_values_objects) == 0:
        return
    return analis_values_objects


async def get_schedule(
    session: AsyncSession, user_and_analis_ids: GetUserAndAnalis
) -> StreamingResponse | None | str:
    user_model: List[User] = await get_user_by_id(
        session=session, id=user_and_analis_ids.user_id
    )
    analis_model: List[Analis] = await get_analis_by_id(
        session=session, id=user_and_analis_ids.analis_id
    )
    analis_values_models: List[AnalisValue] = await get_analis_value_by_user_and_analis_id(
        session=session,
        user_id=user_and_analis_ids.user_id,
        analis_id=user_and_analis_ids.analis_id,
    )

    if user_model is None or analis_model is None:
        return
    elif False in [analis_value.value.isdigit() for analis_value in analis_values_models]:
        return "No"

    analis_dates: List = [
        analis_value.date.strftime("%Y-%m-%d") for analis_value in analis_values_models
    ]
    analis_values: List = [
        int(analis_value.value) for analis_value in analis_values_models
    ]

    weight = len(analis_dates) * 5
    height = weight * 0.7

    plt.figure(figsize=(weight, height))

    plt.title(analis_model.name, fontsize=weight * 2)

    plt.grid(True, linewidth=weight / 16.6)


    plt.xlabel("дата анализа", fontsize=weight * 1.5)
    plt.ylabel(f"{analis_model.unit}", fontsize=weight * 1.5)

    plt.xticks(rotation=30, fontsize=weight * 0.9)
    plt.yticks(fontsize=weight * 1.2)


    for x, y in zip(analis_dates, analis_values):
        plt.text(x, y, str(y), ha="left", fontsize=weight * 0.9)


    plt.plot(
        analis_dates,
        analis_values,
        "-o",
        color="#94007b",
        linewidth=weight / 10,
        markersize=weight * 0.66,
    )
    byte_io = BytesIO()

    plt.savefig(byte_io, format="jpeg")
    byte_io.seek(0)
    plt.close()
    return StreamingResponse(byte_io, media_type="image/jpeg", status_code=200)
