from app.sensors.cpu_load_sensor import (
    CPULoadSensor,
    LoadInfo,
)


def test_format(
    cpu_load: LoadInfo,
):
    sensor = CPULoadSensor()

    assert str(sensor) == '{value:.2f} %'.format(
        value=cpu_load.percent,
    )
