import psutil
from pydantic import BaseModel, Field, ConfigDict

from app.sensors.sensor import SensorABC


class LoadInfo(BaseModel):

    percent: float = Field(min_value=0, max_value=100)

    model_config = ConfigDict(
        from_attributes=True,
    )


class CPULoadSensor(SensorABC[LoadInfo]):

    title = 'CPU load'
    interval: float = 1

    @classmethod
    def value(cls) -> LoadInfo:
        return LoadInfo(percent=psutil.cpu_percent(interval=cls.interval))

    @classmethod
    def format(cls, value: LoadInfo) -> str:

        return '{percent:.2f} %'.format(
            percent=value.percent,
        )
