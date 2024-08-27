from __future__ import annotations

from typing import TYPE_CHECKING

from boreholeGUI.module.borehole import ui

if TYPE_CHECKING:
    from boreholeGUI.module.color.prop import ColorProperties
import boreholeGUI.core.tool


class Color(boreholeGUI.core.tool.Color):
    @classmethod
    def get_properties(cls) -> ColorProperties:
        return boreholeGUI.ColorProperties

    @classmethod
    def get_widget(cls):
        if cls.get_properties().widget is None:
            cls.get_properties().widget = ui.Widget()
        return cls.get_properties().widget
