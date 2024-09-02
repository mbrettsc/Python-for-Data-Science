from load_image import ft_load
import matplotlib.pyplot as plt
from pimp_image import (
    ft_invert,
    ft_red,
    ft_green,
    ft_blue,
    ft_grey,
)


def main():
    array = ft_load("landscape.jpg")

    invert = ft_invert(array)
    red = ft_red(array)
    green = ft_green(array)
    blue = ft_blue(array)
    grey = ft_grey(array)

    fig, axes = plt.subplots(3, 2, figsize=(12, 8))

    axes = axes.flatten()

    images = [array, invert, red, green, blue, grey]
    titles = ['Original', 'Invert', 'Red', 'Green', 'Blue', 'Grey']

    for ax, img, title in zip(axes, images, titles):
        ax.imshow(img)
        ax.set_title(title)
        ax.axis('off') 

    plt.tight_layout()
    plt.show()

    print(ft_invert.__doc__)
    print(ft_red.__doc__)
    print(ft_green.__doc__)
    print(ft_blue.__doc__)
    print(ft_grey.__doc__)


if __name__ == '__main__':
    main()
