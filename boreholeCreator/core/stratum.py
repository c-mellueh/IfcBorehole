from __future__ import annotations

from typing import Type

import pandas as pd

from boreholeCreator import tool
from boreholeCreator.module.stratum.prop import HEIGHT, NAME, SHAPE


def create_stratum(row: pd.Series, borehole_placement, geometry: Type[tool.Geometry], ifc: Type[tool.Ifc]):
    shape_index = row[SHAPE] or 0
    name = row[NAME]
    height = row[HEIGHT]
    if shape_index == 0:
        shape = geometry.create_cylinder(name, height)
    elif shape_index == 1:
        shape = geometry.create_cuboid(name, height)
    else:
        shape = geometry.create_prism(name, height)
    stratum = ifc.create_stratum(shape, row, borehole_placement)
    return stratum
