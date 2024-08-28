from PySide6 import QtWidgets

from boreholeGUI.module.select_dialog.excel_select_dialog import Ui_Dialog


class ExcelDialog(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
