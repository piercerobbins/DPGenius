import re
import dearpygui.dearpygui as dpg
from abc import ABC, abstractmethod
from typing import Callable
from dk_label_studio.dpg_template.default_config import DefaultConfig, DPGBounds


class WindowPriority:
    defines_viewport_width = False
    defines_viewport_height = False

    defines_column_width = False
    defines_column_height = False


class DefaultWindow(ABC):
    def __init__(self, label: str) -> None:
        self.label = label
        self.tag = re.sub(r'\s+', '_', label.strip()).lower()
        self.bounds: DPGBounds | None = None
        self.resize_registry: [Callable] = []

    def create(self, bounds: DPGBounds) -> None:
        self.bounds = bounds
        dpg.add_window(label=self.label,
                       tag=self.tag,
                       width=bounds.width,
                       height=bounds.height,
                       pos=bounds.pos,
                       **DefaultConfig.window_settings)

    def resize(self, bounds: DPGBounds) -> None:
        self.bounds = bounds
        dpg.set_item_width(self.tag, bounds.width)
        dpg.set_item_height(self.tag, bounds.height)
        dpg.set_item_pos(self.tag, bounds.pos)
        for resize_func in self.resize_registry:
            resize_func()

    @abstractmethod
    def populate(self) -> None:
        pass
