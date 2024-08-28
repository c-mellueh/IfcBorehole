from boreholeCreator import settings as cli_settings
from boreholeGUI import tool
from boreholeGUI.core import main_window as core


def connect():
    pass

def run_clicked():
    core.run_clicked(tool.MainWindow, tool.Borehole, tool.Stratum, tool.Settings, tool.Popups, cli_settings.Ifc)


def select_ifc_clicked():
    core.select_ifc_clicked(tool.MainWindow, tool.Popups)
