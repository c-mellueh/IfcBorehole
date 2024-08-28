from boreholeCreator import settings as cli_settings
from boreholeGUI import tool
from boreholeGUI.core import settings as core


def connect():
    core.add_widget_to_mainwindow(tool.MainWindow, tool.Settings)
    core.add_settings_getter_setter(tool.Settings, cli_settings.Geometry, cli_settings.Ifc, cli_settings.Location)
    core.create_ui_triggers(tool.Settings)


def paint_event():
    core.paint_event(tool.Settings)
