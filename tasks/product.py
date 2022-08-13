from typing import Any
from itertools import zip_longest

__all__ = (
    'cartesian_product',
)


def cartesian_product(arr1: list[Any], arr2: list[Any]) -> list:
    """
    Должна возвращать все пары элементы двух массивов:
    cartesian_product([1, 2], [3, 4]) == [(1, 3), (1, 4), (2, 3), (2, 4)]
    """
    ans = list()
    for i in arr1:
        for j in arr2:
            ans.append((i, j))
    return ans


print(cartesian_product([1, 2], [3, 4]))

