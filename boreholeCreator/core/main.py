from typing import Type

from boreholeCreator import tool
from boreholeCreator.module.borehole.prop import ID


def create_file(output_path, main: Type[tool.Main], ifc: Type[tool.Ifc], location: Type[tool.Location]):
    file = ifc.get_ifcfile()
    site_placement = location.get_site_placement()
    ifc.create_ifc_site(site_placement)
    boreholes = main.create_boreholes()
    ifc.assign_entities_to_site(boreholes)
    file.write(output_path)


def create_boreholes(main: Type[tool.Main], borehole: Type[tool.Borehole], stratum: Type[tool.Stratum]):
    borehole_dataframe = borehole.get_dataframe()
    ifc_boreholes = list()
    for index, row in borehole_dataframe.iterrows():
        stratums = stratum.get_stratums_by_borehole_id(row[ID])
        if stratums:
            ifc_boreholes.append(main.create_nested_borehole(row, stratums))
        else:
            ifc_boreholes.append(main.create_unnested_boreholes(row))
    return ifc_boreholes
