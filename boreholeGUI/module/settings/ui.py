from PySide6 import QtWidgets

from . import trigger
from .widget import Ui_Form


class Widget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def paintEvent(self, event):
        super().paintEvent(event)
        trigger.paint_event()
