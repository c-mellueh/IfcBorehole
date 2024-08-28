from boreholeCreator import tool as cli_tool
from boreholeGUI import tool
from boreholeGUI.core import main_window as core


def connect():
    pass


def run_clicked():
    core.run_clicked(tool.Borehole, tool.Stratum, cli_tool.Borehole, cli_tool.Stratum)
