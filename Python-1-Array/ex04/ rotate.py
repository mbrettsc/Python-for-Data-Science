import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load



def ft_rotate(array: np.ndarray, angle: int, channels: int):
    array = np.rot90(array, k=angle//90)
    plt.imshow(array, cmap='gray')
    plt.axis('on')
    plt.show()


def main():
    load_image = ft_load("animal.jpeg")
    if load_image is not None:
        ft_rotate(load_image, 90, 3)
    

if __name__ == '__main__':
    main()
