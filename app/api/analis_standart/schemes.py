from pydantic import BaseModel, PositiveInt, NonNegativeInt


class BaseAnalisStandart(BaseModel):
    analis_id: PositiveInt
    gender: bool
    age_min: NonNegativeInt
    age_max: PositiveInt
    weight_min: NonNegativeInt
    weight_max: PositiveInt
    value: str


class CreateAnalisStandart(BaseAnalisStandart):
    pass


class PatchAnalisStarndart(BaseAnalisStandart):
    analis_id: PositiveInt | None = None
    gender: bool | None = None
    age_min: NonNegativeInt | None = None
    age_max: PositiveInt | None = None
    weight_min: NonNegativeInt | None = None
    weight_max: PositiveInt | None = None
    value: str | None = None


class ReturnAnalisStarndart(BaseAnalisStandart):
    id: PositiveInt
