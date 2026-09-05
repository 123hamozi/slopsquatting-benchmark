import pytest


def normalize_name(value):
    return value.strip().lower()


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("  Alice  ", "alice"),
        ("BOB", "bob"),
    ],
)
def test_normalize_name(raw, expected):
    assert normalize_name(raw) == expected
