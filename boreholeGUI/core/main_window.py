from __future__ import annotations

from typing import TYPE_CHECKING, Type

if TYPE_CHECKING:
    from boreholeGUI import tool


def create_main_window(app, main_window: Type[tool.MainWindow]):
    mw = main_window.get_main_window(app)
    main_window.clear_toolbox()
    for name, widget in main_window.get_steplist():
        main_window.get_toolbox().addItem(widget, name)
        widget.show()

    # main_window.get_toolbox().removeItem(0)

    mw.show()
    main_window.hide_console()
