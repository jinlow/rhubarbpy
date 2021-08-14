from typing import List


from typing import List
from numbers import Number


def loopsum(x: List[Number]) -> Number:
    """A foolish implementation of the sum function
    using a loop in python
    """
    total = 0.0
    for i in x:
        total += i
    return total
