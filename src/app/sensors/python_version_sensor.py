import sys
from typing import TypeAlias

from app.sensors.sensor import SensorABC

VersionInfo: TypeAlias = tuple[int, int, int, str, int]


class PythonVersionSensor(SensorABC[VersionInfo]):

    @staticmethod
    def value() -> VersionInfo:
        return sys.version_info

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
