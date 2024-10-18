from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from .base import Base


class User(Base):
    name: Mapped[str] = mapped_column(unique=True)
    age: Mapped[int]
    weight: Mapped[int]
    gender: Mapped[bool]
