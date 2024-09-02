from __future__ import annotations

from typing import TYPE_CHECKING, Type

if TYPE_CHECKING:
    from boreholeGUI import tool
    from boreholeGUI.module.data_frame_table import ui
    from PySide6.QtCore import QPoint
from boreholeGUI import tool
import pandas as pd

FILE_TYPES = [
    ("Excel", "xlsx", 0),
    ("CSV", "csv", 2),
    ("GeoJSON", "geoJSON", 1),
    ("Shapefile", "shp", 1),
    ("Geopackage", "gpkg", 1),
]


def button_clicked(widget: ui.Widget, data_frame_table: Type[tool.DataFrameTable], popups: Type[tool.Popups]):
    dialog = data_frame_table.create_select_dialog()
    if not dialog.exec():
        return
    path, sheet_name = dialog.ui.lineEdit.text(), dialog.ui.comboBox.currentText()
    index = None
    for name, file_type, n in FILE_TYPES:
        if path.endswith(file_type):
            index = n

    if index == 0:
        df = pd.read_excel(path, sheet_name=sheet_name)
    elif index == 1:
        df = data_frame_table.transform_geopandas(path)
    elif index == 2:
        df = pd.read_csv(path)
    else:
        popups.create_warning_popup(f"Fileformat '{path.split('.')[-1]}' not supported'")
        return
    data_frame_table.set_dataframe(df, widget)


def paint_table(widget: ui.Widget, data_frame_table: Type[tool.DataFrameTable]):
    missing_required_column_names = data_frame_table.get_missing_required_columns(widget)
    if missing_required_column_names:
        missing_required_column_names = '\n'.join([f"'{x}'" for x in missing_required_column_names])
        data_frame_table.set_warning(
            f"Folgende Spalten müssen ergänzt/umbenannt werden: \n{missing_required_column_names}",
                                     widget)
    else:
        data_frame_table.set_warning(None, widget)

    missing_optional_column_names = data_frame_table.get_missing_optional_columns(widget)
    if missing_optional_column_names:
        missing_optional_column_names = '\n'.join([f"'{x}'" for x in missing_optional_column_names])
        data_frame_table.set_info(
            f"Folgende Spalten können ergänzt/umbenannt werden: \n{missing_optional_column_names}",
            widget)
    else:
        data_frame_table.set_info(None, widget)


def warning_button_clicked(widget: ui.Widget, data_frame_table: Type[tool.DataFrameTable], popups: Type[tool.Popups]):
    warning = data_frame_table.get_warning(widget)
    if not warning:
        return
    pop = popups.create_info_popup(warning, "Achtung!", False)
    pop.exec()


def info_button_clicked(widget: ui.Widget, data_frame_table: Type[tool.DataFrameTable], popups: Type[tool.Popups]):
    info = data_frame_table.get_info(widget)
    if not info:
        return
    pop = popups.create_info_popup(info, "Info!", False)
    pop.exec()


def header_context_menu_requested(widget: ui.Widget, pos: QPoint, data_frame_table: Type[tool.DataFrameTable]):
    header = data_frame_table.get_table_view(widget).horizontalHeader()
    menu = data_frame_table.create_header_context_menu(pos, widget)
    menu.exec(header.mapToGlobal(pos))


def dataframe_select_file_clicked(dialog: ui.SelectDialog, popups: Type[tool.Popups]):
    file_type = ";;".join([f"{name} (*.{file})" for name, file, _ in FILE_TYPES + [("all", "*", 0)]])
    path = popups.get_open_path(file_type, dialog)
    if not path:
        return
    dialog.ui.lineEdit.setText(path)
    if path.endswith("xlsx"):
        dialog.ui.comboBox.show()
        sheet_names = pd.ExcelFile(path).sheet_names
        dialog.ui.comboBox.clear()
        dialog.ui.comboBox.addItems(sheet_names)
    else:
        dialog.ui.comboBox.hide()


def request_tooltips(stratum: Type[tool.Stratum]):
    return stratum.get_tooltips()  # TODO: Improve Tooltip handling
