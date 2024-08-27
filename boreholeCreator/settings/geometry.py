from __future__ import annotations

from typing import TYPE_CHECKING

import boreholeCreator

if TYPE_CHECKING:
    from boreholeCreator.module.geometry.prop import GeometryProperties


class Geometry:
    @classmethod
    def get_properties(cls) -> GeometryProperties:
        return boreholeCreator.GeometryProperties

    def get_radius(cls):
        return cls.get_properties().radius

    def set_radius(cls, radius):
        cls.get_properties().radius = radius
