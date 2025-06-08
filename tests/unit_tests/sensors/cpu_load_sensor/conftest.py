from app.sensors.cpu_load_sensor import LoadInfo

import pytest


@pytest.fixture
def cpu_load(
    faker,
    request,
) -> LoadInfo:

    fields = dict(min_value=0, max_value=100)
    fields.update(**getattr(request, 'param', {}))

    return LoadInfo(
        percent=faker.pyfloat(**fields),
    )


@pytest.fixture(scope='function', autouse=True)
def setup(
    cpu_load: LoadInfo,
    monkeypatch: pytest.MonkeyPatch,
):
    monkeypatch.setattr('psutil.cpu_percent', lambda *args, **kwargs: cpu_load.percent)
