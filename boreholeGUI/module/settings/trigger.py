from boreholeGUI import tool
from boreholeGUI.core import settings as core


def connect():
    core.add_widget_to_mainwindow(tool.MainWindow, tool.Settings)
