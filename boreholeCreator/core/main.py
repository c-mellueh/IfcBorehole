from typing import Type

from boreholeCreator import tool


def create_file(output_path, ifc: Type[tool.Ifc], location: Type[tool.Location], borehole: Type[tool.Borehole],
                stratum: Type[tool.Stratum]):
    if not (borehole.is_dataframe_filled() and stratum.is_dataframe_filled()):
        return
    file = ifc.get_ifcfile()
    site_placement = location.get_site_placement()
    ifc.create_ifc_site(site_placement)
    boreholes = borehole.create_boreholes()
    ifc.assign_entities_to_site(boreholes)
    file.write(output_path)
