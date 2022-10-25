"""Holding plotting functions for drawing UI and stuff."""
from abc import ABC, abstractclassmethod
from typing import Any, Dict, Tuple, List

import numpy as np
import cv2


class Display(ABC):
    @abstractclassmethod
    def __init__(
        self,
        width: int = 640,
        height: int = 480,
        main_color: Tuple[int, int, int] = (0, 255, 0),  # BGR
        background_color: Tuple[int, int, int] = (0, 0, 0),  # BGR
    ):
        pass

    @abstractclassmethod
    def show(self):
        pass


class OpenCVDisplay(Display):

    def __init__(
        self,
        width: int = 640,
        height: int = 480,
        main_color: Tuple[int, int, int] = (0, 255, 0),  # BGR
        background_color: Tuple[int, int, int] = (0, 0, 0),  # BGR
    ):
        self.width: int = width
        self.height: int = height
        self.main_color: Tuple[int, int, int] = main_color
        self.background_color: Tuple[int, int, int] = background_color

        # create a blank page
        self.background: np.ndarray = np.full(
            (self.height, self.width, 3), self.background_color, dtype=np.uint8
        )

    def show(self):
        k = ord('n')
        while k==ord('n'):    
            cv2.imshow('chicken', self.background)
            k = cv2.waitKey(0)
        cv2.destroyAllWindows()


class PipUI:
    """Controller of UI and its components."""
    def __init__(
        self,
        width: int = 640,
        height: int = 480,
        main_color: Tuple[int, int, int] = (0, 255, 0),  # BGR
        background_color: Tuple[int, int, int] = (0, 0, 0),  # BGR
        display_device: str = "opencv",
    ):

        self.display: Display = self._configure_display_device(
            device_name=display_device
        )(
            width=width,
            height=height,
            main_color=main_color,
            background_color=background_color,
        )
                
    def _configure_display_device(self, device_name: str):
        device: Display = None
        if device_name == "opencv":
            device = OpenCVDisplay
        elif device == "rpi":
            pass
            # device = np.memmap(
            #     device_name, dtype=np.uint16, mode="w+", shape=(self.height, self.width)
            # )
        else:
            raise NotImplementedError(f"Unsupported device: {device_name}")
        return device

    def retrive_image(self):
        return self.display.background

    def show(self):
        self.display.show()
