from __future__ import annotations

from typing import TYPE_CHECKING

from . import DataFrameTable

if TYPE_CHECKING:
    from boreholeGUI.module.borehole.prop import BoreholeProperties
import boreholeGUI.core.tool


class Borehole(DataFrameTable):
    @classmethod
    def get_properties(cls) -> BoreholeProperties:
        return boreholeGUI.BoreholeProperties

    @classmethod
    def get_cli(cls):
        from boreholeCreator.tool import Borehole as cli
        return cli
