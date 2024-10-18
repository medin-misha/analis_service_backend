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
    analis_values_models: List[AnalisValue] = (
        await get_analis_value_by_user_and_analis_id(
            session=session,
            user_id=user_and_analis_ids.user_id,
            analis_id=user_and_analis_ids.analis_id,
        )
    )

    if user_model is None or analis_model is None or analis_values_models is None:
        return
    elif False in [
        analis_value.value.isdigit() for analis_value in analis_values_models
    ]:
        return "No"

    analis_dates: List = [
        analis_value.date.strftime("%Y-%m-%d") for analis_value in analis_values_models
    ]
    analis_values: List = [
        int(analis_value.value) for analis_value in analis_values_models
    ]

    weight = len(analis_dates) * 5
    height = weight * 0.7

    title_font_size: int = weight * 2
    grid_linewidth: int = weight / 16.6
    xylabel_fontsize: float = weight * 1.5
    xticks_fontsize: float = weight * 0.9
    yticks_fontsize: float = weight * 1.2
    node_font_size: float = weight * 0.9
    plot_line_width: float = weight / 10
    plot_markersize: float = weight * 0.66

    plt.figure(figsize=(weight, height))
    plt.title(analis_model.name, fontsize=title_font_size)
    plt.grid(True, linewidth=grid_linewidth)
    plt.xlabel("дата анализа", fontsize=xylabel_fontsize)
    plt.ylabel(f"{analis_model.unit}", fontsize=xylabel_fontsize)
    plt.xticks(rotation=30, fontsize=xticks_fontsize)
    plt.yticks(fontsize=yticks_fontsize)

    for x, y in zip(analis_dates, analis_values):
        plt.text(x, y, str(y), ha="left", fontsize=node_font_size)

    plt.plot(
        analis_dates,
        analis_values,
        "-o",
        color="#94007b",
        linewidth=plot_line_width,
        markersize=plot_line_width,
    )
    byte_io = BytesIO()

    plt.savefig(byte_io, format="png")
    byte_io.seek(0)
    plt.close()
    return StreamingResponse(byte_io, media_type="image/png", status_code=200)
