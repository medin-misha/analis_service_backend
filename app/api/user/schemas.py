from pydantic import BaseModel, PositiveInt, PositiveFloat
from typing import Annotated
from annotated_types import MaxLen, MinLen


class BaseUser(BaseModel):
    name: Annotated[str, MaxLen(100), MinLen(2)]
    age: PositiveInt
    weight: PositiveFloat
    gender: bool


class PatchUser(BaseUser):
    name: Annotated[str, MaxLen(100), MinLen(2)] = None
    age: PositiveInt = None
    weight: PositiveFloat = None
    gender: bool = None


class CreateUser(BaseUser):
    pass


class ReturnUser(BaseUser):
    id: int
