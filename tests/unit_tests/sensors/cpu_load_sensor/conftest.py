import psutil

import pytest


@pytest.fixture
def cpu_load(
    faker,
    request,
) -> float:

    fields = dict(min_value=0, max_value=100)
    fields.update(**getattr(request, 'param', {}))

    return faker.pyfloat(**fields)


@pytest.fixture(scope='function', autouse=True)
def setup(
    cpu_load: float,
    monkeypatch: pytest.MonkeyPatch,
):
    monkeypatch.setattr('psutil.cpu_percent', lambda *args, **kwargs: cpu_load)
