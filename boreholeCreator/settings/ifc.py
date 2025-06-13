from __future__ import annotations

from typing import TYPE_CHECKING
import ifcopenshell
import uuid
import boreholeCreator
from boreholeCreator.settings.appdata import AppdataSetting

if TYPE_CHECKING:
    from boreholeCreator.module.ifc.prop import IfcProperties

IFC = "ifc"
AUTHOR = "author"
ORGANIZATION = "organization"


class Ifc:

    application_name = AppdataSetting(IFC, "application_name", str, "IfcBorehole")
    application_version = AppdataSetting(
        IFC, "application_version", str, boreholeCreator.__version__
    )
    project_gobal_id = AppdataSetting(
        IFC, "project_global_id", str, ifcopenshell.guid.compress(uuid.uuid1().hex)
    )
    project_name = AppdataSetting(IFC, "project_name", str, "defaultProjectName")
    file_name = AppdataSetting(IFC, "file_name", str, "defaultFileName.ifc")
    file_schema = AppdataSetting(IFC, "file_schema", str, "IFC4X3_ADD2")
    pset_base_name = AppdataSetting(IFC, "pset_base_name", str, "DefaultPset")
    author_family_name = AppdataSetting(AUTHOR, "FamilyName", str, "Doe")
    author_given_name = AppdataSetting(AUTHOR, "GivenName", str, "John")
    author_identification = AppdataSetting(
        AUTHOR, "Identification", str, "defaultCreator"
    )  # for possible keys see https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcPerson.htm
    organization_name = AppdataSetting(
        ORGANIZATION, "Name", str, "defaultOrg"
    )  # for possible keys see https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcOrganization.htm
    organization_description = AppdataSetting(
        ORGANIZATION, "Description", str, "Description of the organization"
    ) 