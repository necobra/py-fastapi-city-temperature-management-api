from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from temperature_app import models, schemas


async def get_temperatures_list(
    db: AsyncSession, city_id: int = None, skip: int = 0, limit: int = 10
) -> list[schemas.Temperature]:
    query = select(models.Temperature)

    if city_id:
        query.where(models.Temperature.city_id == city_id)

    return await db.scalars(query.offset(skip).limit(limit)).all()


async def create_temperatures(
    db: AsyncSession, temperatures: list[schemas.TemperatureCreate]
):
    db_temperatures = []
    for temperature in temperatures:
        db_temperature = models.Temperature(**temperature.dict())
        db_temperatures.append(db_temperature)
        db.add(db_temperature)
    await db.commit()
    await db.refresh(db_temperatures)
    return db_temperatures
