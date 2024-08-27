from __future__ import annotations

from typing import TYPE_CHECKING, Type

if TYPE_CHECKING:
    from boreholeGUI import tool


def create_main_window(app, main_window: Type[tool.MainWindow]):
    mw = main_window.create(app)
    mw.show()
    main_window.hide_console()
