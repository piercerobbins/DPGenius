import pytest
from dpgenius import DefaultConfig, DefaultViewport, DefaultLayout, DefaultColumn, DefaultWindow


@pytest.fixture
def test_layout(columns: int, windows: int) -> DefaultLayout:
    class TestWindow(DefaultWindow):
        def __init__(self, col_id: int, win_id: int):
            super().__init__(f'Test Window {col_id}-{win_id}')

        def populate(self):
            pass

    return DefaultLayout(columns=[DefaultColumn(width_percent=1/columns,
                                                windows=[(TestWindow(i, j), 1/windows)
                                                         for j in range(windows)])
                                  for i in range(columns)])
