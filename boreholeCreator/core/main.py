import logging
from typing import Type

from boreholeCreator import tool


def create_file(output_path, ifc: Type[tool.Ifc], location: Type[tool.Location], borehole: Type[tool.Borehole],
                stratum: Type[tool.Stratum], styling: Type[tool.Styling]) -> None:
    if not (borehole.is_dataframe_filled() and stratum.is_dataframe_filled()):
        return
    logging.info("Create IFC-Template")
    file = ifc.get_ifcfile()
    site_placement = location.get_site_placement()
    logging.info("Create IfcSite")

    ifc.create_ifc_site(site_placement)
    logging.info("Create Boreholes")

    boreholes = borehole.create_boreholes()
    logging.info("Create Boreholes to Site")

    ifc.assign_entities_to_site(boreholes)
    logging.info("Style Entities Boreholes to Site")

    styling.style_entities()
    logging.info("Write Ifc-File")

    file.write(output_path)
    logging.info("Done!")
