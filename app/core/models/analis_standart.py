from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from .base import Base


class AnalisStandart(Base):
    analis_id: Mapped[int] = mapped_column(ForeignKey("analiss.id"))
    gender: Mapped[bool]
    age: Mapped[int]
    age: Mapped[int]
    weight: Mapped[int]
    weight: Mapped[int]
    value: Mapped[str]