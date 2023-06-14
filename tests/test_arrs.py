import pytest

from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([1, 2, 3], -1, "test") == 'test'
    with pytest.raises(IndexError):
        arrs.get([], 0, "test")


@pytest.mark.parametrize('array, start, end, expected', [
    ([1, 2, 3, 4], 1, 3, [2, 3]),
    ([1, 2, 3], 1, 3, [2, 3]),
    ([], 0, 0, []),
    ([1, 2, 3], -4, 2, [1, 2]),
    ([1, 2, 3], -2, None, [2, 3])
])
def test_my_slice(array, start, end, expected):
    assert arrs.my_slice(array, start, end) == expected

# def test_slice():
# assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
# assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
# assert arrs.my_slice([1, 2, 3, 4], - 10) == [1, 2, 3, 4]
