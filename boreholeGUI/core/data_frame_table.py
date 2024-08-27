from __future__ import annotations

from typing import TYPE_CHECKING, Type

if TYPE_CHECKING:
    from boreholeGUI import tool
    from boreholeGUI.module.data_frame_table import ui
    from PySide6.QtCore import QPoint
from boreholeGUI import tool
import pandas as pd


def button_clicked(widget: ui.Widget, data_frame_table: Type[tool.DataFrameTable], popups: Type[tool.Popups]):
    path, sheet_name = popups.select_excel_worksheet()
    if not path:
        return
    df = pd.read_excel(path, sheet_name=sheet_name)
    data_frame_table.set_dataframe(df, widget)


def paint_table(widget: ui.Widget, data_frame_table: Type[tool.DataFrameTable]):
    missing_column_names = data_frame_table.get_missing_required_columns(widget)
    if missing_column_names:
        missing_column_names = '\n'.join(missing_column_names)
        data_frame_table.set_warning(f"Folgende Spalten müssen ergänzt/umbenannt werden: \n{missing_column_names}",
                                     widget)
    else:
        data_frame_table.set_warning(None, widget)


def warning_button_clicked(widget: ui.Widget, data_frame_table: Type[tool.DataFrameTable], popups: Type[tool.Popups]):
    warning = data_frame_table.get_warning(widget)
    if not warning:
        return
    pop = popups.create_info_popup(warning, "Achtung!", False)
    pop.exec()


def header_context_menu_requested(widget: ui.Widget, pos: QPoint, data_frame_table: Type[tool.DataFrameTable]):
    header = data_frame_table.get_table_view(widget).horizontalHeader()
    menu = data_frame_table.create_header_context_menu(pos, widget)
    menu.exec(header.mapToGlobal(pos))
