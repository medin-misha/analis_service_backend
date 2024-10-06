from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from .base import Base


class AnalisStandart(Base):
    analis_id: Mapped[int] = mapped_column(ForeignKey("analiss.id"))
    gender: Mapped[bool]
    age_min: Mapped[int]
    age_max: Mapped[int]
    weight_min: Mapped[int]
    weight_max: Mapped[int]
    value: Mapped[str]
