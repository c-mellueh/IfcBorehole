import logging
from typing import Type

import ifcopenshell

from boreholeCreator import tool


def create_file(output_path, ifc: Type[tool.Ifc], location: Type[tool.Location], borehole: Type[tool.Borehole],
                stratum: Type[tool.Stratum], styling: Type[tool.Styling],
                util: Type[tool.Util]) -> ifcopenshell.file | None:
    df_borehole = borehole.get_dataframe()
    df_stratum = stratum.get_dataframe()
    if not util.is_dataframe_filled(df_borehole, borehole.get_required_columns(), borehole.get_optional_collumns()):
        return
    if not (util.is_dataframe_filled(df_stratum, stratum.get_required_columns(), stratum.get_optional_collumns())):
        return
    warning_text = "No {0}s defined. Use 'tool.{0}.add_{1}()' to create {0}s or use 'tool.{0}.set_dataframe' to use custom Dataframe"
    if not len(df_borehole):
        logging.warning(warning_text.format("Borehole", "borehole"))
    if not len(df_stratum):
        logging.warning(warning_text.format("Stratum", "stratum"))

    logging.info("Create IFC-Template")
    ifc.reset()
    file = ifc.get_ifcfile()
    if location.get_settings().mapconversion_is_activated():
        location.add_map_conversion(file)

    ifc.fill_person_and_org()
    site_placement = location.get_site_placement()
    logging.info("Create IfcSite")

    ifc.create_ifc_site(site_placement)
    logging.info("Create Boreholes")

    boreholes = borehole.create_boreholes()
    logging.info("Assign Boreholes to Site")

    ifc.assign_entities_to_site(boreholes)
    logging.info("Style Entities Boreholes to Site")

    styling.style_entities()
    logging.info("Write Ifc-File")
    if output_path:
        file.write(output_path)
    logging.info("Done!")
    return file
