from __future__ import annotations

from typing import TYPE_CHECKING, Type

import ifcopenshell

import boreholeCreator
import boreholeCreator.core.tool
from boreholeCreator import settings, tool

if TYPE_CHECKING:
    from boreholeCreator.module.location.prop import LocationProperties

O = 0., 0., 0.
X = 1., 0., 0.
Y = 0., 1., 0.
Z = 0., 0., 1.
MZ = 0.0, 0.0, -1.0


class Location(boreholeCreator.core.tool.Location):
    @classmethod
    def get_settings(cls) -> Type[settings.Location]:
        return settings.Location

    @classmethod
    def get_properties(cls) -> LocationProperties:
        return boreholeCreator.LocationProperties

    @classmethod
    def create_ifcaxis2placement(cls,ifcfile, point=O, dir1=Z, dir2=X):
        point = ifcfile.createIfcCartesianPoint(point)
        dir1 = ifcfile.createIfcDirection(dir1)
        dir2 = ifcfile.createIfcDirection(dir2)
        axis2placement = ifcfile.createIfcAxis2Placement3D(point, dir1, dir2)
        return axis2placement

    @classmethod
    def create_ifclocalplacement(cls,ifcfile, point=O, dir1=Z, dir2=X, relative_to=None):
        axis2placement = cls.create_ifcaxis2placement(ifcfile, point, dir1, dir2)
        ifclocalplacement2 = ifcfile.createIfcLocalPlacement(relative_to, axis2placement)
        return ifclocalplacement2

    @classmethod
    def get_site_placement(cls):
        site_pos = cls.get_properties().site_position
        ifcfile = tool.Ifc.get_ifcfile()
        if cls.get_properties().site_placement is None:
            cls.get_properties().site_placement = cls.create_ifclocalplacement(ifcfile, point=site_pos)
        return cls.get_properties().site_placement

    @classmethod
    def add_map_conversion(cls, ifcfile: ifcopenshell.file):
        projected_crs = ifcfile.create_entity("IFCPROJECTEDCRS")
        tool.Util.fill_entity_with_dict(projected_crs, cls.get_properties().projected_crs_data)
        map_conversion = ifcfile.create_entity("IFCMAPCONVERSION")
        map_conversion.SourceCRS = tool.Ifc.get_geometric_representation_context()
        map_conversion.TargetCRS = projected_crs
        tool.Util.fill_entity_with_dict(map_conversion, cls.get_properties().map_conversion_data)

