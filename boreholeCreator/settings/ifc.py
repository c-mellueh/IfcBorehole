from __future__ import annotations

from typing import TYPE_CHECKING

import boreholeCreator
from boreholeCreator.settings.appdata import Appdata as appdata

if TYPE_CHECKING:
    from boreholeCreator.module.ifc.prop import IfcProperties

IFC = "ifc"
APPICATION_NAME = "application_name"
APPICATION_VERSION = "application_version"
AUTHOR_FAMILY_NAME = "author_family_name"
AUTHOR_GIVEN_NAME = "author_given_name"


class Ifc:
    @classmethod
    def get_properties(cls) -> IfcProperties:
        return boreholeCreator.IfcProperties

    @classmethod
    def set_application_name(cls, name: str):
        appdata.set_setting(APPICATION_NAME, IFC, name)

    @classmethod
    def get_application_name(cls):
        return appdata.get_string_setting(APPICATION_NAME, IFC, "IfcBorehole")

    @classmethod
    def set_application_version(cls, version: str):
        appdata.set_setting(APPICATION_VERSION, IFC, version)

    @classmethod
    def get_application_version(cls):
        appdata.get_string_setting(APPICATION_VERSION, IFC, boreholeCreator.__version__)

    @classmethod
    def set_author_attribute(cls, name, value):
        cls.get_properties().creator[name] = value

    @classmethod
    def get_author_attribute(cls, name):
        return cls.get_properties().creator.get(name)

    @classmethod
    def set_organization_attribute(cls, name, value):
        cls.get_properties().organization[name] = value

    @classmethod
    def get_organization_attribute(cls, name):
        return cls.get_properties().organization.get(name)

    @classmethod
    def set_project_name(cls, name: str):
        cls.get_properties().project_name = name

    @classmethod
    def get_project_name(cls):
        return cls.get_properties().project_name

    @classmethod
    def set_file_name(cls, name: str):
        cls.get_properties().file_name = name

    @classmethod
    def get_file_name(cls):
        return cls.get_properties().file_name

    @classmethod
    def set_file_schema(cls, schema: str):
        cls.get_properties().file_schema = schema

    @classmethod
    def get_file_schema(cls):
        return cls.get_properties().file_schema

    @classmethod
    def set_default_pset_name(cls, name: str):
        cls.get_properties().pset_base_name = name

    @classmethod
    def get_default_pset_name(cls):
        return cls.get_properties().pset_base_name
