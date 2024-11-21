import dearpygui.dearpygui as dpg
from dpgenius.default_window import DefaultWindow


class TitleWindow(DefaultWindow):
    def __init__(self, logo_file: str, img_downsize: float):
        super().__init__('Title Window')
        self.logo_file = logo_file
        self.img_downsize = img_downsize
        self.resize_registry = [self.resize_logo]

    def populate(self) -> None:
        width, height, _, data = dpg.load_image(self.logo_file)
        with dpg.texture_registry():
            dpg.add_static_texture(width=width, height=height, default_value=data, tag='logo_texture')
        dpg.add_image('logo_texture',
                      parent=self.tag,
                      tag='logo_img',
                      width=int(self.bounds.width * self.img_downsize),
                      height=int(self.bounds.width * self.get_image_aspect_ratio()))

    def get_image_aspect_ratio(self) -> float:
        width = dpg.get_item_width('logo_texture')
        height = dpg.get_item_height('logo_texture')
        return height / width

    def resize_logo(self):
        dpg.set_item_width('logo_img', int(self.bounds.width * self.img_downsize))
        dpg.set_item_height('logo_img', int(self.bounds.width * self.get_image_aspect_ratio()))
