import pytest

from app.sensors.python_version_sensor import PythonVersionSensor
from tests.fakes.sensors.python_version import VersionInfo


def test_format(
    version_info: VersionInfo,
):
    sensor = PythonVersionSensor()

    assert str(sensor) == '{major}.{minor}'.format(
        major=version_info.major,
        minor=version_info.minor,
    )


@pytest.mark.parametrize(
    'micro', [{'min_value': 1}], indirect=True,
)
@pytest.mark.parametrize(
    'version_info', [{'releaselevel': 'alpha'}], indirect=True,
)
def test_alpha_of_micro_unmarked(
    version_info: VersionInfo,
):
    sensor = PythonVersionSensor()

    assert str(sensor) == '{major}.{minor}'.format(
        major=version_info.major,
        minor=version_info.minor,
    )


@pytest.mark.parametrize(
    'micro', [{'min_value': 0, 'max_value': 0}], indirect=True,
)
@pytest.mark.parametrize(
    'version_info', [{'releaselevel': 'alpha'}], indirect=True,
)
def test_alpha_of_micro_marked(
    version_info: VersionInfo,
):
    sensor = PythonVersionSensor()

    assert str(sensor) == '{major}.{minor}.0a{serial}'.format(
        major=version_info.major,
        minor=version_info.minor,
        serial=version_info.serial,
    )
