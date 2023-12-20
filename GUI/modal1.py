from GUI.qt_py.ui_dialog1 import Ui_Dialog


class Modal1(Ui_Dialog):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(parent)