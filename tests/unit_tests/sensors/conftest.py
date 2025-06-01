import pytest

from tests.fakes.sensors.python_version import VersionInfo


@pytest.fixture
def major(request) -> int:

    major = 3
    return getattr(request, 'param', major)


@pytest.fixture
def minor(faker, request) -> int:

    fields = dict(min_value=6, max_value=64)
    fields.update(**getattr(request, 'param', {}))

    return faker.pyint(**fields)


@pytest.fixture
def micro(faker, request) -> int:

    fields = dict(min_value=0, max_value=256)
    fields.update(**getattr(request, 'param', {}))

    return faker.pyint(**fields)


@pytest.fixture
def version_info(
    major: int,
    minor: int,
    micro: int,
    faker,
    request,
) -> VersionInfo:

    fields = dict(
        major=major,
        minor=minor,
        micro=micro,
        releaselevel='final',
        serial=faker.pyint(min_value=1, max_value=100),
    )
    fields.update(**getattr(request, 'param', {}))

    return VersionInfo(**fields)


@pytest.fixture(scope='function', autouse=True)
def setup(
    version_info: VersionInfo,
    monkeypatch: pytest.MonkeyPatch,
):
    monkeypatch.setattr('sys.version_info', version_info)
