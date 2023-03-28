import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget)
from GUI import Ui_MainWindow, Ui_Form, Ui_Wizard, Ui_Form2


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.widget = QWidget(self)
        f = Ui_Form2()
        f.setupUi(self.widget)
        a = self.ui.stackedWidget.addWidget(self.widget)
        print(a)

        self.widget2 = QWidget(self)
        f2 = Ui_Form()
        f2.setupUi(self.widget2)
        b = self.ui.stackedWidget.addWidget(self.widget2)
        print(b)

        self.ui.stackedWidget.setCurrentWidget(self.widget)
        # self.ui.stackedWidget.setCurrentIndex(a)
        self.ui.actionOpen.triggered.connect(self.foo)

    def foo(self):
        # self.ui.stackedWidget.setCurrentIndex(3)
        self.ui.stackedWidget.setCurrentWidget(self.widget2)
        self.ui.statusbar.showMessage("Ready", 3000)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
