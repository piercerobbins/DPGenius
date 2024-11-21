from dpgenius import DefaultViewport, DefaultLayout, DefaultColumn, DefaultWindow

if __name__ == '__main__':
    class TestWindow1(DefaultWindow):
        def __init__(self):
            super().__init__('Test Window 1')

        def populate(self):
            pass

    test_column_1 = DefaultColumn(width_percent=1,
                                  windows=[(TestWindow1(), 1)])
    test_layout = DefaultLayout(columns=[test_column_1])
    viewport = DefaultViewport(test_layout)
    viewport.start()
