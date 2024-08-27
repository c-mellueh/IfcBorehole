from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from boreholeGUI.module.stratum.prop import StratumProperties
import boreholeGUI.core.tool


class Stratum(boreholeGUI.core.tool.Stratum):
    @classmethod
    def get_properties(cls) -> StratumProperties:
        return boreholeGUI.StratumProperties

    @classmethod
    def set_widget(cls, widget):
        cls.get_properties().widget = widget

    @classmethod
    def get_widget(cls):
        return cls.get_properties().widget

    @classmethod
    def get_cli(cls):
        from boreholeCreator.tool import Stratum as cli
        return cli
