import psutil
from pydantic import BaseModel, Field, ConfigDict

from app.sensors.sensor import SensorABC


class MemoryInfo(BaseModel):

    total: int
    available: int
    percent: float = Field(ge=0, le=100)
    used: int
    free: int

    model_config = ConfigDict(
        from_attributes=True,
    )


class MemoryAvailableSensor(SensorABC[MemoryInfo]):

    title = 'Memory avaliable'

    @classmethod
    def value(cls) -> MemoryInfo:
        return MemoryInfo.model_validate(psutil.virtual_memory())

    @classmethod
    def format(cls, value: MemoryInfo) -> str:

        return '{available} MB/{total} MB ({percent:.1f} %)'.format(
            total=int(value.total / 2024**2),
            available=int(value.available / 2024**2),
            percent=value.percent,
        )
