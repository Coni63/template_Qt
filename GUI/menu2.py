from typing import Any
from GUI.qt_py.ui_widget2 import Ui_Form
from app.app import App


class Menu2(Ui_Form):
    def __init__(self, parent: Any, app: App, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(parent)

        self.app = app

        self.dial.valueChanged.connect(self.on_dial_value_changed)
        self.horizontalSlider.valueChanged.connect(self.on_slider_value_changed)

    def update(self, app: App):
        self.app = app
        self.on_dial_value_changed(self.app.value)  # set initial value

    def on_dial_value_changed(self, value: int):
        self.app.value = value
        self.lcdNumber.display(self.app.value)
        self.progressBar.setValue(self.app.value)
        self.horizontalSlider.setValue(self.app.value)

    def on_slider_value_changed(self, value: int):
        self.app.value = value
        self.lcdNumber.display(self.app.value)
        self.progressBar.setValue(self.app.value)
        self.dial.setValue(self.app.value)
