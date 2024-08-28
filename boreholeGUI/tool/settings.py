from __future__ import annotations

from typing import TYPE_CHECKING

from PySide6.QtWidgets import QWidget

if TYPE_CHECKING:
    from boreholeGUI.module.settings.prop import SettingsProperties
import boreholeGUI.core.tool


class Settings(boreholeGUI.core.tool.Settings):
    @classmethod
    def get_properties(cls) -> SettingsProperties:
        return boreholeGUI.SettingsProperties

    @classmethod
    def get_widget(cls):
        if cls.get_properties().widget is None:
            cls.get_properties().widget = QWidget()
        return cls.get_properties().widget
