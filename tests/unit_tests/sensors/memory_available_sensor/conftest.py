
import pytest

from app.sensors.memory_available_sensor import MemoryInfo


@pytest.fixture
def total(
    faker,
    request,
) -> int:

    fields = dict(min_value=1, max_value=64*1024)
    fields.update(**getattr(request, 'param', {}))

    return faker.pyint(**fields) * 1024**2


@pytest.fixture
def available(
    total: int,
    faker,
    request,
) -> int:

    fields = dict(min_value=1, max_value=int(total/1024**2))
    fields.update(**getattr(request, 'param', {}))

    return faker.pyint(**fields) * 1024**2


@pytest.fixture
def memory_info(
    total: int,
    available: int,
    request,
) -> MemoryInfo:

    fields = dict(
        total=total,
        available=available,
        percent=100*(total - available)/total,
        used=total - available,
        free=available,
    )
    fields.update(**getattr(request, 'param', {}))

    return MemoryInfo.model_validate(fields)


@pytest.fixture(scope='function', autouse=True)
def setup(
    memory_info: MemoryInfo,
    monkeypatch: pytest.MonkeyPatch,
):
    monkeypatch.setattr('psutil.virtual_memory', lambda: memory_info)
