import sys
from typing import Literal

from pydantic import BaseModel, ConfigDict

from app.sensors.sensor import SensorABC


class VersionInfo(BaseModel):

    major: int
    minor: int
    micro: int
    releaselevel: Literal['alpha', 'beta', 'final']
    serial: int

    model_config = ConfigDict(
        from_attributes=True,
    )


class PythonVersionSensor(SensorABC[VersionInfo]):

    @staticmethod
    def value() -> VersionInfo:
        return VersionInfo.model_validate(sys.version_info)

    @classmethod
    def format(cls, value: VersionInfo) -> str:

        if (value.micro == 0) and (value.releaselevel == 'alpha'):
            return '{major}.{minor}.0a{serial}'.format(
                major=value.major,
                minor=value.minor,
                serial=value.serial,
            )
        return '{major}.{minor}'.format(
            major=value.major,
            minor=value.minor,
        )
