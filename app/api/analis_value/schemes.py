from pydantic import BaseModel, PositiveInt
from typing import Optional
from datetime import date as Date

class BaseAnalisValue(BaseModel):
    user_id: PositiveInt
    analis_id: PositiveInt
    date: Date
    value: str


class CreateAnalisValue(BaseAnalisValue):
    pass


class PatchAnalisValue(BaseModel):
    user_id: PositiveInt | None = None
    analis_id: PositiveInt | None = None
    value: str | None = None
    date: Date | None = None


class ReturnAnalisValue(BaseAnalisValue):
    id: PositiveInt
