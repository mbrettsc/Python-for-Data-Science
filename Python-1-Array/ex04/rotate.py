import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def manual_transpose(array: np.ndarray):
    """Transpose a 2D array."""
    rows, cols = array.shape
    transposed = np.zeros((cols, rows), dtype=array.dtype)

    for i in range(rows):
        for j in range(cols):
            transposed[j, i] = array[i, j]
    
    return transposed


def ft_rotate(array: np.ndarray):
    """Rotate an image by 90 degrees."""
    cutted_array = array[150:550, 300:700, :1]
    cutted_array = np.squeeze(cutted_array)
    print("The shape of image is: ", cutted_array.shape)
    print(cutted_array)
    transposed_array = manual_transpose(cutted_array)
    print(f"New shape after Transpose: {transposed_array.shape}")
    print(transposed_array)
    plt.imshow(transposed_array, cmap='gray')
    plt.axis('on')
    plt.show()

def main():
    load_image = ft_load("animal.jpeg")
    if load_image is not None:
        ft_rotate(load_image)
    

if __name__ == '__main__':
    main()
