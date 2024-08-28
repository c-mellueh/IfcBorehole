from __future__ import annotations

from typing import TYPE_CHECKING, Type

if TYPE_CHECKING:
    from boreholeGUI import tool

from boreholeGUI import tool


def add_widget_to_mainwindow(main_window: Type[tool.MainWindow], settings: Type[tool.Settings]):
    main_window.add_step("Settings", settings.get_widget())
