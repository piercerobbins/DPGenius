import dearpygui.dearpygui as dpg
from screeninfo import get_monitors
from dataclasses import dataclass
from dpgenius.default_config import DefaultConfig
from dpgenius.default_layout import DefaultLayout


@dataclass
class DefaultViewport:
    layout: DefaultLayout

    def start(self) -> None:
        dpg.create_context()
        dpg.setup_dearpygui()

        self.create_viewport()
        self.layout.create_windows()

        dpg.configure_app(docking=True, docking_space=True)
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

    def create_viewport(self) -> None:
        primary_monitor = get_monitors()[0]
        height = int(primary_monitor.height * DefaultConfig.viewport_size)
        width = int(height * 1.25)
        pos = [(primary_monitor.width - width) // 2, (primary_monitor.height - height) // 2]

        dpg.create_viewport(title=DefaultConfig.app_name,
                            width=width,
                            height=height)
        dpg.set_viewport_vsync(True)
        dpg.set_viewport_pos(pos)
        dpg.set_viewport_resize_callback(self.on_viewport_resize)

    def on_viewport_resize(self) -> None:
        self.layout.resize_windows()
