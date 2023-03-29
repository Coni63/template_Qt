import sys
import pickle

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget)
from GUI import Ui_MainWindow, Ui_Form, Ui_Wizard, Ui_Form2
from app import App

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()      # hold the complete UI
        self.ui.setupUi(self)
        self.app = App()               # hold the application data rendered in the UI
        self.saveFile = None

        self.widget = QWidget(self)
        f = Ui_Form2()
        f.setupUi(self.widget)
        a = self.ui.stackedWidget.addWidget(self.widget)

        self.widget2 = QWidget(self)
        f2 = Ui_Form()
        f2.setupUi(self.widget2)
        b = self.ui.stackedWidget.addWidget(self.widget2)

        self.ui.stackedWidget.setCurrentWidget(self.widget)
        # self.ui.stackedWidget.setCurrentIndex(a)
        self.ui.actionOpen.triggered.connect(self.openFile)
        self.ui.actionSave.triggered.connect(self.saveData)
        self.ui.actionSave_As.triggered.connect(self.saveAsData)
        self.ui.actionQuit.triggered.connect(self.quitApp)

    def openFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*)", options=options)
        if fileName:
            self.saveFile = fileName
            with open(self.saveFile, "rb") as f:
                data = pickle.load(f)
                self.app.load(data)

            self.ui.stackedWidget.setCurrentWidget(self.widget2)
            self.ui.statusbar.showMessage(fileName, 3000)
        else:
            self.ui.statusbar.showMessage("Not loaded", 3000)

    def saveData(self):
        if self.saveFile is None:
            self.saveAsData()

        with open(self.saveFile, "wb") as f:
            pickle.dump(self.app.save(), f)

    def saveAsData(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "Save File", "", "All Files(*)", options=options)
        if fileName:
            self.saveFile = fileName
            with open(self.saveFile, "wb") as f:
                pickle.dump(self.app.save(), f)

    def quitApp(self):
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
