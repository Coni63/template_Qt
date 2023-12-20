from typing import Any
from PySide6.QtCore import QAbstractTableModel, Qt

from GUI.qt_py.ui_widget import Ui_Form
from app.app import App


class MyTableModel(QAbstractTableModel):

    def __init__(self, datain, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self.arraydata = datain

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        return len(self.arraydata[0])

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role == Qt.EditRole:
            print("edit mode")
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.arraydata[index.row()][index.column()]


class Menu1(Ui_Form):
    def __init__(self, parent: Any, app: App, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(parent)
        self.app = app

        self.model = MyTableModel(self.app.data, None)
        self.tableView.setModel(self.model)
