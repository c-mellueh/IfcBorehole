from typing import Type

import pandas as pd

from boreholeCreator import tool
from boreholeCreator.module.borehole.prop import HEIGHT, NAME


def create_nested_borehole(borehole_row: pd.Series, stratum_df: pd.DataFrame, borehole: Type[tool.Borehole],
                           geometry: Type[tool.Geometry], ifc: Type[tool.Ifc], location: Type[tool.Location]):
    pos = borehole.get_position(borehole_row)
    ifcfile = ifc.get_ifcfile()
    site_placement = location.get_site_placement()
    borehole_placement = location.create_ifclocalplacement(ifcfile, pos, relative_to=site_placement)
    pyramid_shape = geometry.create_pyramid()
    ifc_borehole = ifc.create_borehole(borehole_row, borehole_placement, pyramid_shape)
    ifc_stratums = list()
    for stratum_index, stratum_row in stratum_df.iterrows():
        ifc_stratums.append(borehole.create_stratum(stratum_row, borehole_placement))
    ifc.assign_stratums_to_borehole(ifc_borehole, ifc_stratums)

    return ifc_borehole


def create_unnested_borehole(borehole_row: pd.Series, borehole: Type[tool.Borehole], geometry: Type[tool.Geometry],
                             ifc: Type[tool.Ifc], location: Type[tool.Location]):
    pos = borehole.get_position(borehole_row)
    placement = location.create_ifclocalplacement(ifc.get_ifcfile(), pos, relative_to=location.get_site_placement())
    shape = geometry.create_cylinder(borehole_row[NAME], borehole[HEIGHT])
    ifc_borehole = ifc.create_borehole(borehole_row, placement, shape)
    return ifc_borehole
