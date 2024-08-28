from __future__ import annotations

from typing import Callable, TYPE_CHECKING

from PySide6.QtWidgets import QCheckBox, QComboBox, QDoubleSpinBox, QLineEdit

if TYPE_CHECKING:
    from boreholeGUI.module.settings.prop import SettingsProperties
import boreholeGUI.core.tool
from boreholeGUI.module.settings import ui

class Settings(boreholeGUI.core.tool.Settings):
    @classmethod
    def get_properties(cls) -> SettingsProperties:
        return boreholeGUI.SettingsProperties

    @classmethod
    def get_widget(cls) -> ui.Widget:
        if cls.get_properties().widget is None:
            cls.get_properties().widget = ui.Widget()
        return cls.get_properties().widget

    @classmethod
    def add_setting(cls, widget: QLineEdit | QComboBox | QDoubleSpinBox | QCheckBox, getter: Callable,
                    setter: Callable):
        cls.get_properties().settings_list.append((widget, getter, setter))

    @classmethod
    def get_settings_list(cls) -> list[tuple[QLineEdit | QComboBox | QDoubleSpinBox | QCheckBox, Callable, Callable]]:
        return cls.get_properties().settings_list
