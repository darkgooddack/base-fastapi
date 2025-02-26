from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import WeatherRecord
from core.schemas.weather import WeatherResponse, WeatherRequest, HistoryResponse


async def create_weather_record(
    session: AsyncSession,
    weather_data: WeatherResponse
) -> Sequence[WeatherRecord]:
    record = WeatherRecord(**weather_data.dict())
    session.add(record)
    await session.commit()
    await session.refresh(record)
    return record

async def get_weather_history(
        session: AsyncSession
) -> Sequence[WeatherRecord]:
    stmt = select(WeatherRecord).order_by(WeatherRecord.timestamp.desc())
    result = await session.scalars(stmt)
    return result.all()

def kelvin_to_celsius(kelvin: float) -> float:
    return kelvin - 273.15