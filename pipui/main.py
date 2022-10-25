"""Entrypoint for defining and plot pipboy-like interface."""
import yaml

from interface import UIConfig, preprocess_ui
from painter import PipUI


def main():
    config: UIConfig = UIConfig(**yaml.safe_load(open("default.yaml")))
    ui_object = preprocess_ui(config=config)

    pip_ui: PipUI = PipUI(
        width=1280,
        height=800
    )
    pip_ui.show()


if __name__ == "__main__":
    main()