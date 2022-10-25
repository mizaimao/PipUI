"""Holding plotting functions for drawing UI and stuff."""

from typing import Any, Dict, Tuple, List

import numpy as np


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
        # copy variables
        self.width: int = width
        self.height: int = height
        self.main_color: Tuple[int, int, int] = main_color
        self.background_color: Tuple[int, int, int] = background_color
        self.device: str = p

        # create a blank page
        self.background: np.ndarray = np.full(
            (self.height, self.width, 3), self.background_color
        )
        
    def _configure_display_device(self, device_name: str):
        device: Any = None
        if device_name == "opencv":
            device
        elif device == "rpi":
            device = np.memmap(
                device_name, dtype=np.uint16, mode="w+", shape=(self.height, self.width)
        )
        else:
            raise NotImplementedError(f"Unsupported device: {device_name}")
        return device

    def retrive_image(self):
        return self.background

    def display(self):
