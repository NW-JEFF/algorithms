"""Test."""
import pytest  # noqa E401
from max_subarray1 import find_max_subarray


@pytest.mark.parametrize("arr, low, high, ans", [(
    [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7],
    0, 15, (7, 10, 43)),
    ([1, 3, 8, 2, 5], 0, 4, (0, 4, 19)),
    ([-1.5, -5, -2, -9, -2, -1], 0, 5, (5, 5, -1))
    ])
def test_max_subarray(arr, low, high, ans):
    """Pass."""
    res = find_max_subarray(arr, low, high)
    assert res == ans,\
        f'Expected {ans}, but got {res}.'
