from __future__ import annotations
from typing import TYPE_CHECKING
import boreholeCreator
import boreholeCreator.core.tool
if TYPE_CHECKING:
    from boreholeCreator.module.location.prop import LocationProperties
class Location(boreholeCreator.core.tool.Location):
    @classmethod
    def get_properties(cls) -> LocationProperties:
        return boreholeCreator.LocationProperties