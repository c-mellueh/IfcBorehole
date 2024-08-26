from __future__ import annotations

from typing import Type

import pandas as pd

from boreholeCreator import tool
from boreholeCreator.module.stratum import prop


def create_stratum(row: pd.Series, stratum_index: int, borehole_placement, stratum: Type[tool.Stratum],
                   geometry: Type[tool.Geometry], ifc: Type[tool.Ifc]):
    shape_index = row[prop.SHAPE] or 0
    name = row[prop.NAME]
    height = row[prop.HEIGHT]
    if shape_index == 0:
        shape = geometry.create_cylinder(name, height)
    elif shape_index == 1:
        shape = geometry.create_cuboid(name, height)
    else:
        shape = geometry.create_prism(name, height)
    ifc_stratum = ifc.create_stratum(shape, row, borehole_placement)
    stratum.get_dataframe().at[stratum_index, prop.IFC_GUID] = ifc_stratum.GlobalId
    return ifc_stratum
