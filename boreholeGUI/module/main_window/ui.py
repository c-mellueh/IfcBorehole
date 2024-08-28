from PySide6 import QtWidgets

from boreholeGUI import __version__ as version
from boreholeGUI.icons import get_icon
from .window import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(get_icon())
        self.setWindowTitle(f"IfcBorehole v{version}")
