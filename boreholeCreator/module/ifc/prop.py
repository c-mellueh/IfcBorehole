from boreholeCreator import __version__ as application_version
import ifcopenshell.guid
import uuid
class IfcProperties:
    creator = dict()    # for possible keys see https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcPerson.htm
    organization = {"Name":"defaultOrg"}  # for possible keys see https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcOrganization.htm
    application = "boreholeCreator"
    application_version = application_version
    project_gobal_id = ifcopenshell.guid.compress(uuid.uuid1().hex)
    project_name = "defaultProjectName"
