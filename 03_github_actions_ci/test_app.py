import pytest


@pytest.mark.parametrize("value", [1, 2, 3])
def test_ci(value):
    assert value > 0
