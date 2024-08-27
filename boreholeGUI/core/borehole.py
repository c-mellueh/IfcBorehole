from __future__ import annotations

from typing import TYPE_CHECKING, Type

if TYPE_CHECKING:
    from boreholeGUI import tool

from boreholeGUI import tool
import pandas as pd


def add_widget_to_mainwindow(main_window: Type[tool.MainWindow], borehole: Type[tool.Borehole]):
    main_window.add_step("Borehole", borehole.get_widget())
    borehole.connect_triggers()


def button_clicked(borehole: Type[tool.Borehole], popups: Type[tool.Popups]):
    path, sheet_name = popups.select_excel_worksheet()
    df = pd.read_excel(path, sheet_name=sheet_name)
    borehole.set_dataframe(df)
