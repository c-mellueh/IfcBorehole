from __future__ import annotations

from typing import TYPE_CHECKING

from boreholeGUI.module.borehole import ui

if TYPE_CHECKING:
    from boreholeGUI.module.borehole.prop import BoreholeProperties
import boreholeGUI.core.tool


class Borehole(boreholeGUI.core.tool.Borehole):
    @classmethod
    def get_properties(cls) -> BoreholeProperties:
        return boreholeGUI.BoreholeProperties

    @classmethod
    def get_widget(cls):
        if cls.get_properties().widget is None:
            cls.get_properties().widget = ui.Widget()
        return cls.get_properties().widget
