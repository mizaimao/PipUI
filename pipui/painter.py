"""Holding plotting functions for drawing UI and stuff."""
from abc import ABC, abstractclassmethod
from typing import Any, Dict, Tuple, List

import numpy as np
import cv2

from pipui.interface import Dot


TOP_PERC: float = 0.05
BOTTOM_PERC: float = 0.01

TOP_MENU_TXT_WIDTH: int = 50


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
        dots: List[Dot] = None,
    ):

        self.dots: List[Dot] = dots
        self.display: Display = self._configure_display_device(
            device_name=display_device
        )(
            width=width,
            height=height,
            main_color=main_color,
            background_color=background_color,
        )
        self.plot_top_menu()
                
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

    def plot_top_menu(self):
        # the first Dot
        dot: Dot = self.dots[0]

        plot_height: int = int(self.display.height * TOP_PERC)
        font_scalar: float = self.get_optimal_font_scale(width=self.display.width)
        print(plot_height)
        print(dot.tabs)

        cv2.putText(
            self.display.background,
            "chicken chicken chicken",
            (0, plot_height),  # position
            cv2.FONT_HERSHEY_SIMPLEX,
            font_scalar,  # font and scale
            self.display.main_color,
            2,
        )


    def get_optimal_font_scale(self, width: int, text: str = None):
        if not text:
            text = " " * TOP_MENU_TXT_WIDTH
        for scale in range(59, -1, -1):
            textSize = cv2.getTextSize(
                text,
                fontFace=cv2.FONT_HERSHEY_DUPLEX,
                fontScale=scale / 10,
                thickness=1,
            )
            if textSize[0][0] <= width:
                return scale / 10
        return 1