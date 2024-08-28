from __future__ import annotations

from typing import Any, TYPE_CHECKING

import boreholeCreator

if TYPE_CHECKING:
    from boreholeCreator.module.location.prop import LocationProperties


class Location:
    @classmethod
    def get_properties(cls) -> LocationProperties:
        return boreholeCreator.LocationProperties

    @classmethod
    def mapconversion_is_activated(cls) -> bool:
        return cls.get_properties().use_map_conversion

    @classmethod
    def set_mapconversion_activated(cls, state: bool):
        cls.get_properties().use_map_conversion = state

    @classmethod
    def set_map_conversion_attribute(cls, attribute_name: str, value: Any):
        """

        :param attribute_name: For possible Attributes see  https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcMapConversion.htm
                    SourceCRS and TargetCRS will be filled automatically. Please don't set manually
        :param value:
        :return:
        """
        cls.get_properties().map_conversion_data[attribute_name] = value

    @classmethod
    def get_map_conversion_attribute(cls, attribute_name: str) -> Any:
        return cls.get_properties().map_conversion_data.get(attribute_name)

    @classmethod
    def set_projected_crs_attribute(cls, attribute_name, value: Any):
        """

        :param attribute_name: For possible Attributes see  https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcProjectedCRS.htm
        :param value:
        :return:
        """
        cls.get_properties().projected_crs_data[attribute_name] = value

    @classmethod
    def get_projected_crs_attribute(cls, attribute_name: str) -> Any:
        return cls.get_properties().projected_crs_data.get(attribute_name)

    @classmethod
    def get_site_position(cls):
        return cls.get_properties().site_position

    @classmethod
    def set_site_position(cls, value):
        cls.get_properties().site_position = value
