import numpy as np
import matplotlib.pyplot as plt


def ft_load(path: str) -> np.ndarray:
    """Load an image from a file."""
    try:
        img = plt.imread(path)
        if img.ndim != 3 or img.shape[2] != 3:
            raise ValueError("Image is not a color image")
    except Exception as e:
        print(e)
        return None

    return img
