from boreholeGUI import tool
from boreholeGUI.core import data_frame_table as core


def connect():
    pass


def button_clicked(widget):
    core.button_clicked(widget, tool.DataFrameTable, tool.Popups)


def warning_clicked(widget):
    core.warning_button_clicked(widget, tool.DataFrameTable, tool.Popups)


def paint_table(widget):
    core.paint_table(widget, tool.DataFrameTable)


def header_context_menu_requested(widget, pos):
    core.header_context_menu_requested(widget, pos, tool.DataFrameTable)


def dataframe_select_file_clicked(dialog):
    core.dataframe_select_file_clicked(dialog, tool.Popups)


def request_tooltips():
    return core.request_tooltips(tool.Stratum)
