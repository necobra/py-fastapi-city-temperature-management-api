from typing import Optional

from pydantic import BaseModel


class CityBase(BaseModel):
    name: str
    additional_info: str


class CityCreate(CityBase):
    pass


class City(CityBase):
    id: int

    class Config:
        from_attributes = True


class CityUpdate(BaseModel):
    id: int
    name: Optional[str] = None
    additional_info: Optional[str] = None

    class Config:
        from_attributes = True
