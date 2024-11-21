import pytest
import dearpygui.dearpygui as dpg
from dpgenius import DefaultConfig, DefaultViewport
from test.test_fixtures import test_layout


@pytest.mark.parametrize(('columns', 'windows'), [(i, i) for i in range(1, 5)])
def test_app_setup(test_layout, columns, windows):
    DefaultConfig.app_name = 'Test App Setup'
    viewport = DefaultViewport(test_layout)
    viewport.setup()
    for column in test_layout.columns:
        for test_window in column.windows:
            assert dpg.get_item_label(test_window[0].tag) == test_window[0].label
    dpg.destroy_context()
