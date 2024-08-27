from __future__ import annotations

from typing import TYPE_CHECKING, Type

if TYPE_CHECKING:
    from boreholeGUI import tool
    from boreholeGUI.module.data_frame_table import ui
from boreholeGUI import tool
import pandas as pd


def button_clicked(widget: ui.Widget, data_frame_table: Type[tool.DataFrameTable], popups: Type[tool.Popups]):
    path, sheet_name = popups.select_excel_worksheet()
    if not path:
        return
    df = pd.read_excel(path, sheet_name=sheet_name)
    data_frame_table.set_dataframe(df, widget)


def paint_table(widget: ui.Widget, data_frame_table: Type[tool.DataFrameTable]):
    widget_tool = data_frame_table.get_tool_from_widget(widget)
    widget_tool_cli = widget_tool.get_cli()
    existing_column_names = set(data_frame_table.get_column_names(widget))
    required_column_names = set(widget_tool_cli.get_required_collumns())
    missing_column_names = sorted(required_column_names.difference(existing_column_names))
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
