import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> np.array:
    """Inverts the color of the image received."""
    inverted = 255 - array

    return inverted


def ft_red(array) -> np.array:
    """Returns the red channel of the image received."""
    red_channel = array.copy()    
    red_channel[:, :, 1] = 0 # green 
    red_channel[:, :, 2] = 0 # blue

    return red_channel


def ft_green(array) -> np.array:
    """Returns the green channel of the image received."""
    green_channel = array.copy()
    green_channel[:, :, 0] = 0 # red
    green_channel[:, :, 2] = 0 # blue

    return green_channel


def ft_blue(array) -> np.array:
    """Returns the blue channel of the image received."""
    blue_channel = array.copy()
    blue_channel[:, :, 0] = 0 # red
    blue_channel[:, :, 1] = 0 # green

    return blue_channel


def ft_grey(array) -> np.array:
    """Returns the grayscale version of the image received."""
    grey_array = array.mean(axis=2, keepdims=True).astype(array.dtype)
    grey_array = np.repeat(grey_array, 3, axis=2) 

    return grey_array
