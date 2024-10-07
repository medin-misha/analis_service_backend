from pydantic import BaseModel, PositiveInt
from datetime import date


class BaseAnalisValue(BaseModel):
    user_id: PositiveInt
    analis_id: PositiveInt
    value: str


class CreateAnalisValue(BaseAnalisValue):
    pass


class PatchAnalisValue(BaseAnalisValue):
    user_id: PositiveInt | None = None
    analis_id: PositiveInt | None = None
    value: str | None = None


class ReturnAnalisValue(BaseAnalisValue):
    id: PositiveInt
    date: date