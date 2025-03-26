import pytest

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (2, 3, 5),
    (3, 5, 8)
])
def test_sum(a, b, expected):
    assert a + b == expected
