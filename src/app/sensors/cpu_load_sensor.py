import psutil

from app.sensors.sensor import SensorABC


class CPULoadSensor(SensorABC[float]):

    interval: float = 1

    @classmethod
    def value(cls) -> float:
        return psutil.cpu_percent(interval=cls.interval)

    @classmethod
    def format(cls, value: float) -> str:

        return 'CPU load: {percent:.2f} %'.format(
            percent=value,
        )
