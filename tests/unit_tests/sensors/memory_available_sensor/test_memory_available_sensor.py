from app.sensors.memory_available_sensor import (
    MemoryAvailableSensor,
    MemoryInfo,
)


def test_format(
    memory_info: MemoryInfo,
):
    sensor = MemoryAvailableSensor()

    assert str(sensor) == '{available} MB/{total} MB ({percent:.1f} %)'.format(
        total=int(memory_info.total / 2024**2),
        available=int(memory_info.available / 2024**2),
        percent=memory_info.percent,
    )
