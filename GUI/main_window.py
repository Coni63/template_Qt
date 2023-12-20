from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QDialog
from GUI.qt_py.ui_main_window import Ui_MainWindow
from GUI.menu1 import Menu1
from GUI.menu2 import Menu2
from GUI.modal1 import Modal1
from app.app import App


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.app = App()
        self.save_file = None

        self.ui = Ui_MainWindow()      # hold the complete UI
        self.ui.setupUi(self)

        self.form_widget = Menu1(parent=self.ui.page, app=self.app)
        self.form2_widget = Menu2(parent=self.ui.page_2, app=self.app)

        self.ui.pb_menu1.clicked.connect(lambda: self.show_ui_form(0))
        self.ui.pb_menu2.clicked.connect(lambda: self.show_ui_form(1))
        self.ui.pb_menu3.clicked.connect(lambda: self.open_modal())
        self.ui.pb_menu4.clicked.connect(self.show_message)

        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionSave.triggered.connect(self.save_data)
        self.ui.actionSave_As.triggered.connect(self.save_as_data)
        self.ui.actionQuit.triggered.connect(self.quit_app)

    def show_ui_form(self, index=0):
        self.ui.stackedWidget.setCurrentIndex(index)

    def open_modal(self):
        dialog = QDialog(self)
        Modal1(dialog)
        dialog.exec()

    def show_message(self):
        self.ui.statusbar.showMessage("Menu 4 clicked", 3000)

    def open_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*)", options=options)
        if file_name:
            self.save_file = file_name
            self.app = App.load(self.save_file)
            self.form2_widget.update(self.app)
            self.ui.statusbar.showMessage(f"{self.save_file} loaded", 3000)
        else:
            self.ui.statusbar.showMessage("Not loaded", 3000)

    def save_data(self):
        if self.save_file is None:
            self.save_as_data()
            return

        self.app.save(self.save_file)

    def save_as_data(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "All Files(*)", options=options)
        if file_name:
            self.save_file = file_name
            self.app.save(self.save_file)

    def quit_app(self):
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.close()
