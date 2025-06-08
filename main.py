import json
import wsgiref.simple_server
from collections.abc import Mapping, Sequence
from wsgiref.types import StartResponse

from app.sensors import (
    CPULoadSensor,
    MemoryAvailableSensor,
    PythonVersionSensor,
)
from app.sensors.sensor import SensorABC


def get_sensors() -> Sequence[SensorABC]:

    sensors = [
        PythonVersionSensor(),
        CPULoadSensor(),
        MemoryAvailableSensor(),
    ]
    return tuple(sensors)


def show_sensors(
    environ: Mapping[str, str],
    start_responce: StartResponse,
) -> Sequence[bytes]:

    headers = [
        ('Content-type', 'application/json; charset=utf-8'),
    ]
    start_responce('200 OK',  headers)

    data = {}
    for sensor in get_sensors():
        data[sensor.title] = sensor.value().model_dump()

    return [
        json.dumps(data).encode('utf-8'),
    ]


if __name__ == '__main__':
    with wsgiref.simple_server.make_server(
        'localhost',
        8080,
        show_sensors,
    ) as server:
        server.serve_forever()
