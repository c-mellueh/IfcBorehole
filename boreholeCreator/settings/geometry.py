from __future__ import annotations

from typing import TYPE_CHECKING

import boreholeCreator
from boreholeCreator.settings.appdata import Appdata as appdata

if TYPE_CHECKING:
    from boreholeCreator.module.geometry.prop import GeometryProperties

GEOMETRY = "geometry"
RADIUS = "radius"

class Geometry:
    @classmethod
    def get_properties(cls) -> GeometryProperties:
        return boreholeCreator.GeometryProperties

    @classmethod
    def get_radius(cls):
        return appdata.get_float_setting(RADIUS,GEOMETRY,1.0)

    @classmethod
    def set_radius(cls, radius):
        appdata.set_setting(RADIUS, GEOMETRY, radius)
