from pydantic import BaseModel, PositiveInt


class GetUserAndAnalis(BaseModel):
    user_id: PositiveInt
    analis_id: PositiveInt
