import dearpygui.dearpygui as dpg
from dataclasses import dataclass
from dpgenius.default_window import DefaultWindow
from dpgenius.default_config import DPGBounds


@dataclass
class DefaultColumn:
    width_percent: float
    windows: list[tuple[DefaultWindow, float]]

    def get_width(self, total_width) -> int:
        return int(self.width_percent * total_width)


@dataclass
class DefaultLayout:
    columns: list[DefaultColumn]

    def create_windows(self) -> None:
        for c, col in enumerate(self.columns):
            for w, (window, height_percent) in enumerate(col.windows):
                window_bounds = self._set_window_bounds(c, w, height_percent)
                window.create(window_bounds)
                window.populate()

    def resize_windows(self) -> None:
        for c, col in enumerate(self.columns):
            for w, (window, height_percent) in enumerate(col.windows):
                window_bounds = self._set_window_bounds(c, w, height_percent)
                window.resize(window_bounds)

    def _set_window_bounds(self, c: int, w: int, height_percent: float) -> DPGBounds:
        width = self.columns[c].get_width(dpg.get_viewport_width())
        height = int(height_percent * dpg.get_viewport_height())
        x_pos = self.columns[c - 1].get_width(dpg.get_viewport_width()) if c > 0 else 0
        y_pos = self.columns[c].windows[w - 1][1] * dpg.get_viewport_height() + self.columns[c].windows[w - 1][0].bounds.pos[1] if w > 0 else 0
        pos = [x_pos, y_pos]
        return DPGBounds(width, height, pos)
