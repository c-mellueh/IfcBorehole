from __future__ import annotations

from typing import TYPE_CHECKING, Type

if TYPE_CHECKING:
    from boreholeGUI import tool

from boreholeGUI import tool


def add_widget_to_mainwindow(main_window: Type[tool.MainWindow], stratum: Type[tool.Stratum],
                             data_frame_table: Type[tool.DataFrameTable]):
    widget = data_frame_table.create_widget(stratum)
    stratum.set_widget(widget)
    main_window.add_step("Stratum", stratum.get_widget())
    cli_tool = stratum.get_cli()
    data_frame_table.set_dataframe(cli_tool.get_dataframe(), widget)
