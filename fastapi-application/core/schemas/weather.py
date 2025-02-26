from pydantic import BaseModel

from datetime import datetime

class WeatherRequest(BaseModel):
    city: str

class WeatherResponse(BaseModel):
    city: str
    temperature: float
    description: str
    timestamp: datetime

class HistoryResponse(BaseModel):
    id: int
    city: str
    temperature: float
    description: str
    timestamp: datetime

    id: int