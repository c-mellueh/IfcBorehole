from PySide6 import QtWidgets

from . import trigger


class Widget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from .widget import Ui_Form
        self.ui = Ui_Form()
        self.ui.setupUi(self)


class TableView(QtWidgets.QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paintEvent(self, e):
        super().paintEvent(e)
        trigger.paint_table()
