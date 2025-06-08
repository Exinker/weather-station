import psutil

import pytest

from app.sensors.cpu_load_sensor import CPULoadSensor


def test_format(
    cpu_load: float,
):
    sensor = CPULoadSensor()

    assert str(sensor) == 'CPU load: {value:.2f} %'.format(
        value=cpu_load,
    )
