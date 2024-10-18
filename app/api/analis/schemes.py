from pydantic import BaseModel, PositiveInt


class BaseAnalis(BaseModel):
    user_id: PositiveInt
    name: str
    unit: str


class CreateAnalis(BaseAnalis):
    pass


class ReturnAnalis(BaseAnalis):
    id: PositiveInt
