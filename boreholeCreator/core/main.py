from typing import TYPE_CHECKING,Type
from boreholeCreator import tool
def create_file(output_path,ifc:Type[tool.Ifc],location:Type[tool.Location]):
    file = ifc.get_ifcfile()
    site_placement = location.get_site_placement()
    site = ifc.create_ifc_site(site_placement)
    file.write(output_path)
