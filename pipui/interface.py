"""Functions to plot UI."""

from typing import Any, Dict, List, Tuple
from dataclasses import dataclass, field


class Page:  # third level
    """
    Individual pages. Can be divided into left and right part,
    or used as a single large page.
    """
    def __init__(self):
        self.components: Dict[str, List[str]] = {}


class Tab:  # second level
    """"""
    def __init__(self):
        self.pages: Dict[str, Page] = {}


class Dot:  # top level
    """"""
    def __init__(self):
        self.tabs: Dict[str, Tab] = {}



@dataclass
class UIConfig:
    """UI element configuration."""
    # WTF
    ATAB1: Dict[str, List[Dict[str, Dict[str, List[str]]]]] = field(default_factory = {})



def process_page(sub_config: Dict[str, Any]):
    """
    Process third level of UI elements. At this "Page" level, each page can be comprised of
    left and right parts, or a single part.

    This function create single pages.
    """
    page_object: Page = Page()
    components: List[str] = sub_config["components"]
    for c in components:
        page_object.components[c] = None

    return page_object


def process_tabs(sub_config: Dict[str, Any]):
    """Process second level of UI elements."""
    tab_object: Tab = Tab()

    # each tab is made from multiple pages
    for page_name, page_definition in sub_config.items():
        tab_object.pages[page_name] = process_page(page_definition)
    return tab_object


def preprocess_ui(config: UIConfig):
    """Spawn each level of objects of UI elements."""
    dot_object: Dot = Dot()

    # process the first dot function
    for tab, sub_config in config.ATAB1.items():  # TODO: rename
        dot_object.tabs[tab] = process_tabs(sub_config)

    return dot_object
