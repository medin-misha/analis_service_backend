from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from .base import Base

class Analis(Base):
    name: Mapped[str]
    unit: Mapped[str]
