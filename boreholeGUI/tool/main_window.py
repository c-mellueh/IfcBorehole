from __future__ import annotations

import ctypes
from typing import TYPE_CHECKING

from PySide6.QtWidgets import QApplication

import boreholeGUI
import boreholeGUI.core.tool
from boreholeGUI.module.main_window import ui

if TYPE_CHECKING:
    from boreholeGUI.module.main_window.prop import MainWindowProperties


class MainWindow(boreholeGUI.core.tool.MainWindow):
    @classmethod
    def get_properties(cls) -> MainWindowProperties:
        return boreholeGUI.MainWindowProperties

    @classmethod
    def get_main_window(cls, application: QApplication):
        if cls.get_properties().main_window is None:
            cls.get_properties().main_window = ui.MainWindow()
            cls.get_properties().ui = cls.get_properties().main_window.ui
            cls.get_properties().application = application
        return cls.get_properties().main_window

    @classmethod
    def hide_console(cls):
        hWnd = ctypes.windll.kernel32.GetConsoleWindow()
        if hWnd != 0:
            ctypes.windll.user32.ShowWindow(hWnd, 0)

    @classmethod
    def add_step(cls, name, widget):
        cls.get_properties().step_list.append((name, widget))

    @classmethod
    def get_ui(cls):
        return cls.get_properties().ui

    @classmethod
    def get_toolbox(cls):
        return cls.get_ui().toolBox

    @classmethod
    def clear_toolbox(cls):
        tb = cls.get_toolbox()
        for index in reversed(range(tb.count())):
            widget = tb.widget(index)
            tb.removeItem(index)
            widget.deleteLater()

    @classmethod
    def get_steplist(cls):
        return cls.get_properties().step_list
