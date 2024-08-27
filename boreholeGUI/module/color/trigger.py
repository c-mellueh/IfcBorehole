from boreholeGUI import tool
from boreholeGUI.core import color as core


def connect():
    core.add_widget_to_mainwindow(tool.MainWindow, tool.Color)
