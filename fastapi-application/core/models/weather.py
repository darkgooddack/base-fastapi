from datetime import datetime

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base
from .mixins.int_id_pk import IntIdPkMixin


class WeatherRecord(IntIdPkMixin, Base):
    city: Mapped[str]
    temperature: Mapped[float]
    description: Mapped[str]
    timestamp: Mapped[datetime]