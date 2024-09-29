from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Date
from .base import Base


class AnalisValue(Base):
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    analis_id: Mapped[int] = mapped_column(ForeignKey("analiss.id"))
    value: Mapped[str]
    date: Mapped[Date] = mapped_column(Date)
