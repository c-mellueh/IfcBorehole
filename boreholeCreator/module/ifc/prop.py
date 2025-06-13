import uuid

import ifcopenshell.guid

from boreholeCreator import __version__ as application_version


class IfcProperties:
    owner_history: ifcopenshell.entity_instance = None
    ifcfile: ifcopenshell.file = None
    project: ifcopenshell.entity_instance = None
    geometric_representation_context: ifcopenshell.entity_instance = None
    site: ifcopenshell.entity_instance = None
    ifc_person: ifcopenshell.entity_instance = None
    ifc_organization: ifcopenshell.entity_instance = None
