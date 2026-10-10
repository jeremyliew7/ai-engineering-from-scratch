import sys

import numpy as np

print("Python:", sys.executable)
print("Numpy:", np.__version__)


def double(value: int) -> int:
    return value * 2


print(double(3))
