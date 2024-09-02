from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from boreholeGUI.module.stratum.prop import StratumProperties
import boreholeGUI.core.tool
from . import DataFrameTable


class Stratum(DataFrameTable):
    @classmethod
    def get_properties(cls) -> StratumProperties:
        return boreholeGUI.StratumProperties

    @classmethod
    def get_cli(cls):
        from boreholeCreator.tool import Stratum as cli
        return cli
