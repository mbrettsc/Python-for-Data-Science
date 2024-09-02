import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def ft_zoom(array: np.ndarray, start_x: int, end_x: int, start_y: int, end_y: int, channels: int):
    """
    Zoom in on a part of an image and display it.

    Parameters:
    - array (np.ndarray): The image array.
    - start_x (int): The starting x-coordinate for the zoom.
    - end_x (int): The ending x-coordinate for the zoom.
    - start_y (int): The starting y-coordinate for the zoom.
    - end_y (int): The ending y-coordinate for the zoom.
    - channels (int): The number of channels (0 for grayscale, 3 for RGB).

    Returns:
    - None
    """
    try:
        if channels == 1:
            zoomed_image = array[start_x:end_x, start_y:end_y, channels]
            cmap = 'gray'
        elif channels == 3:
            zoomed_image = array[start_x:end_x, start_y:end_y, :channels]
            cmap = None
        else:
            raise ValueError("Invalid number of channels. Must be 1 (grayscale) or 3 (RGB).")
        
        print(f"New shape after slicing: {zoomed_image.shape}")
        print(zoomed_image)
        plt.imshow(zoomed_image, cmap=cmap)
        plt.axis('on')
        plt.show()
    
    except Exception as e:
        print(f"Error: {e}")


def main():
    """Test the ft_zoom function with an example image."""
    img = ft_load("animal.jpeg")
    if img is not None:
        ft_zoom(img, 150, 550, 300, 700, 1)

if __name__ == '__main__':
    main()
