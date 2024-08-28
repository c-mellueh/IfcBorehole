import uuid

import ifcopenshell.guid

from boreholeCreator import __version__ as application_version


class IfcProperties:
    creator = {
        # for possible keys see https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcPerson.htm
        "Identification": None,
        "FamilyName":     None,
        "GivenName":      "defaultCreator", }
    organization = {
        "Name": "defaultOrg"}  # for possible keys see https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcOrganization.htm
    application_name = "boreholeCreator"
    application_version = application_version
    project_gobal_id = ifcopenshell.guid.compress(uuid.uuid1().hex)
    project_name = "defaultProjectName"
    file_name = "defaultFileName.ifc"
    file_schema = "IFC4X3_ADD2"
    pset_base_name = "DefaultPset"

    owner_history: ifcopenshell.entity_instance = None
    ifcfile: ifcopenshell.file = None
    project: ifcopenshell.entity_instance = None
    geometric_representation_context: ifcopenshell.entity_instance = None
    site: ifcopenshell.entity_instance = None
    ifc_person: ifcopenshell.entity_instance = None
    ifc_organization: ifcopenshell.entity_instance = None
