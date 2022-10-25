"""Entrypoint for defining and plot pipboy-like interface."""
import yaml

from interface import UIConfig, preprocess_ui
from painter import PipUI
from fb_helper import display

def main():
    config: UIConfig = UIConfig(**yaml.safe_load(open("default.yaml")))
    ui_object = preprocess_ui(config=config)

    pip_ui: PipUI = PipUI(
        width=320,
        height=240
    )
    display(pip_ui.retrive_image())
    return

if __name__ == "__main__":
    main()