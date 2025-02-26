from typing import Annotated
import requests
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException

from fastapi import (
    APIRouter,
    Depends,
)
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from core.models import db_helper
from core.schemas.weather import (
    WeatherRequest,
    WeatherResponse,
    HistoryResponse,
)
from crud import weather as weather_crud
from crud.weather import get_weather_history, create_weather_record, kelvin_to_celsius

weather_key = settings.weather.key
weather_url = settings.weather.url

router = APIRouter(tags=["Weather"])


@router.get("/city/", response_model=WeatherResponse)
async def get_weather(
        city: str,
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
):
    params = {"q": city, "appid": weather_key, "units": "metric", "lang": "ru"}
    response = requests.get(weather_url, params=params)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())

    data = response.json()

    temperature_kelvin = data["main"]["temp"]
    temperature_celsius = kelvin_to_celsius(temperature_kelvin)

    weather_data = WeatherResponse(
        city=data["name"],
        temperature=data["main"]["temp"],
        description=data["weather"][0]["description"],
        timestamp=datetime.utcnow()
    )

    await create_weather_record(session, weather_data)

    return weather_data


@router.get("/history/", response_model=HistoryResponse)
async def get_history(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
):
    return await get_weather_history(session)