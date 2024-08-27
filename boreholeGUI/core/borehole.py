from __future__ import annotations

from typing import TYPE_CHECKING, Type

from boreholeCreator import tool as cli_tool

if TYPE_CHECKING:
    from boreholeGUI import tool

from boreholeGUI import tool
import pandas as pd


def add_widget_to_mainwindow(main_window: Type[tool.MainWindow], borehole: Type[tool.Borehole], ):
    main_window.add_step("Borehole", borehole.get_widget())
    borehole.set_dataframe(cli_tool.Borehole.get_dataframe())
    borehole.connect_triggers()



def button_clicked(borehole: Type[tool.Borehole], popups: Type[tool.Popups]):
    path, sheet_name = popups.select_excel_worksheet()
    if not path:
        return
    df = pd.read_excel(path, sheet_name=sheet_name)
    borehole.set_dataframe(df)


def paint_table(borehole: Type[tool.Borehole], borehole_cli: Type[cli_tool.Borehole]):
    existing_column_names = set(borehole.get_column_names())
    required_column_names = set(borehole_cli.get_required_collumns())
    missing_column_names = sorted(required_column_names.difference(existing_column_names))
    if missing_column_names:
        missing_column_names = '\n'.join(missing_column_names)
        borehole.set_warning(f"Folgende Spalten müssen ergänzt/umbenannt werden: \n{missing_column_names}")
    else:
        borehole.set_warning(None)


def warning_button_clicked(borehole: Type[tool.Borehole], popups: Type[tool.Popups]):
    warning = borehole.get_warning()
    if not warning:
        return
    pop = popups.create_info_popup(warning, "Achtung!", False)
    pop.exec()
