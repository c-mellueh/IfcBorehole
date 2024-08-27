from __future__ import annotations

from typing import TYPE_CHECKING

from boreholeGUI.module.borehole import ui

if TYPE_CHECKING:
    from boreholeGUI.module.stratum.prop import StratumProperties
import boreholeGUI.core.tool


class Stratum(boreholeGUI.core.tool.Stratum):
    @classmethod
    def get_properties(cls) -> StratumProperties:
        return boreholeGUI.StratumProperties

    @classmethod
    def get_widget(cls):
        if cls.get_properties().widget is None:
            cls.get_properties().widget = ui.Widget()
        return cls.get_properties().widget
