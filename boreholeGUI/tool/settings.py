from __future__ import annotations

from typing import Any, Callable, TYPE_CHECKING

from PySide6.QtWidgets import QCheckBox, QComboBox, QDoubleSpinBox, QLineEdit

from boreholeGUI import tool

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
                    setter: Callable, datatype):
        cls.get_properties().settings_list.append((widget, getter, setter, datatype))

    @classmethod
    def get_settings_list(cls) -> list[
        tuple[QLineEdit | QComboBox | QDoubleSpinBox | QCheckBox, Callable, Callable, Any]]:
        return cls.get_properties().settings_list

    @classmethod
    def settings_are_valid(cls):
        is_value = True
        for widget, getter, setter, datatype in cls.get_settings_list():
            value = getter()
            try:
                if value is None:
                    continue
                setter(datatype(value))
            except ValueError:
                text = f"Value '{value}' from Setting '{widget.objectName()}' can not be transformed into {datatype}."
                tool.Popups.create_warning_popup(text)
                is_value = False
        return is_value
