from typing import Dict, List, Union, Tuple

import numpy as np


# Point to framebuffer as it's a numpy array
# N.B. Numpy stores in format HEIGHT then WIDTH, not WIDTH then HEIGHT!
# c is the number of channels, 4 because BGRA
HEIGHT: int = 240
WIDTH: int = 320

# Used for 32bit color, which is not the rpi cheap ass display (RGB565)
# FB = np.memmap('/dev/fb0', dtype='uint8',mode='w+', shape=(h,w,c)) 
#FB: np.ndarray = np.memmap("/dev/fb0", dtype=np.uint16, mode="w+", shape=(HEIGHT, WIDTH))


def convert_RGB(im: np.ndarray) -> np.ndarray:
    """Convert an RGB image to 16bit color space."""
    # Make components of RGB565
    R5 = (im[...,0]>>3).astype(np.uint16) << 11
    G6 = (im[...,1]>>2).astype(np.uint16) << 5
    B5 = (im[...,2]>>3).astype(np.uint16)

    # Assemble components into RGB565 uint16 image
    return R5 | G6 | B5


def convert_BGR(im: np.ndarray) -> np.ndarray:
    """Convert an BGR image to 16bit color space."""
    # Make components of RGB565
    R5 = (im[...,2]>>3).astype(np.uint16) << 11
    G6 = (im[...,1]>>2).astype(np.uint16) << 5
    B5 = (im[...,0]>>3).astype(np.uint16)
    # Assemble components into RGB565 uint16 image
    return R5 | G6 | B5


def display(arr: np.ndarray):
    """Display an image/array to bufferframe."""
    assert len(arr.shape) == 3
    height, width, channel = arr.shape
    assert (height, width) == (HEIGHT, WIDTH), f"Image shape {arr.shape} does not match that of display ({(HEIGHT, WIDTH)})."
    #FB[:] = convert_BGR(arr)


# test_background: np.ndarray = np.full((HEIGHT, WIDTH, 3), (255, 255, 255), dtype=np.uint8)
# display(test_background)



# test_background[0 : 40, 0: 80] = (255, 0, 0)
# test_background[-40 : , -80: ] = (0, 255, 0)
# display(test_background)
