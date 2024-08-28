from PySide6 import QtWidgets
from pyqtconsole.console import PythonConsole

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


class Console(PythonConsole):
    def __init__(self, *args, **kwds):
        super(Console, self).__init__(*args, **kwds)
        self.setWindowIcon(get_icon())
        self.setWindowTitle("Console")

    def closeEvent(self, event):
        super().closeEvent(event)
