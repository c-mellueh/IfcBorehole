from __future__ import annotations

from typing import TYPE_CHECKING

import boreholeCreator

if TYPE_CHECKING:
    from boreholeCreator.module.ifc.prop import IfcProperties


class Ifc:
    @classmethod
    def get_properties(cls) -> IfcProperties:
        return boreholeCreator.IfcProperties

    @classmethod
    def set_application_name(cls, name: str):
        cls.get_properties().application_name = name

    @classmethod
    def get_application_name(cls):
        return cls.get_properties().application_name

    @classmethod
    def set_application_version(cls, version: str):
        cls.get_properties().application_version = version

    @classmethod
    def get_application_version(cls):
        return cls.get_properties().application_version

    @classmethod
    def set_creator_attribute(cls, name, value):
        cls.get_properties().creator[name] = value

    @classmethod
    def get_creator_attribute(cls, name):
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
