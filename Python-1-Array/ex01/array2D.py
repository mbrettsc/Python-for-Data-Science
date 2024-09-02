import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Slice a 2D list."""
    x = np.array(family)
    print("My shape is :", x.shape)
    x = x[start:end]
    print("My new shape is :", x.shape)
    return x.tolist()
