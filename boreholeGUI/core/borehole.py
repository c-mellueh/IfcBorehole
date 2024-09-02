from __future__ import annotations

from typing import TYPE_CHECKING, Type

from boreholeCreator import tool as cli_tool

if TYPE_CHECKING:
    from boreholeGUI import tool

from boreholeGUI import tool


def add_widget_to_mainwindow(main_window: Type[tool.MainWindow], borehole: Type[tool.Borehole]):
    widget = borehole.create_widget()
    borehole.set_widget(widget)
    main_window.add_step("Borehole", borehole.get_widget())
    borehole.set_dataframe(cli_tool.Borehole.get_dataframe())
