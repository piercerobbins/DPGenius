from dataclasses import dataclass


@dataclass
class DPGBounds:
    width: int
    height: int
    pos: list[int]


@dataclass
class DefaultConfig:
    app_name: str = 'DPG Template'
    viewport_size = 0.75
    default_button_size = DPGBounds(width=200, height=50, pos=[0, 0])
    window_settings = {'no_focus_on_appearing': True,
                       'no_close': True,
                       'no_title_bar': True,
                       'no_move': True,
                       'no_resize': True}
