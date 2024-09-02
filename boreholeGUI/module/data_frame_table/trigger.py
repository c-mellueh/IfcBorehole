from boreholeGUI import tool
from boreholeGUI.core import data_frame_table as core


def connect():
    pass


def button_clicked(data_frame_table_tool):
    core.button_clicked(data_frame_table_tool, tool.Popups)


def warning_clicked(data_frame_table_tool):
    core.warning_button_clicked(data_frame_table_tool, tool.Popups)


def info_clicked(data_frame_table_tool):
    core.info_button_clicked(data_frame_table_tool, tool.Popups)


def paint_table(data_frame_table_tool):
    core.paint_table(data_frame_table_tool)


def header_context_menu_requested(pos, data_frame_table_tool):
    core.header_context_menu_requested(pos, data_frame_table_tool)


def dataframe_select_file_clicked(dialog):
    core.dataframe_select_file_clicked(dialog, tool.Popups)


def request_tooltips(data_frame_table_tool):
    return core.request_tooltips(data_frame_table_tool)
