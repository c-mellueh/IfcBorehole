from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from boreholeGUI.module.borehole.prop import BoreholeProperties
import boreholeGUI.core.tool

class Borehole(boreholeGUI.core.tool.Borehole):
    @classmethod
    def get_properties(cls) -> BoreholeProperties:
        return boreholeGUI.BoreholeProperties

    @classmethod
    def set_widget(cls, widget):
        cls.get_properties().widget = widget

    @classmethod
    def get_widget(cls):
        return cls.get_properties().widget

    @classmethod
    def get_cli(cls):
        from boreholeCreator.tool import Borehole as cli
        return cli

    @classmethod
    def get_dataframe(cls):
        return cls.get_properties().dataframe

    @classmethod
    def get_tooltips(cls) -> dict[str, str]:
        return cls.get_properties().tooltips
