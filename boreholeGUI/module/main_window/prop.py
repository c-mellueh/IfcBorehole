from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .window import Ui_MainWindow
    from PySide6.QtWidgets import QApplication, QWidget
    from .ui import MainWindow
class MainWindowProperties:
    main_window: MainWindow = None
    step_list: list[tuple[str, QWidget]] = list()
    ui: Ui_MainWindow = None
    application: QApplication = None
