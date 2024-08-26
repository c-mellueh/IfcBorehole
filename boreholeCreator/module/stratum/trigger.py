from boreholeCreator import tool
from boreholeCreator.core import stratum as core


def create_stratum(row, stratum_index: int, borehole_placement):
    return core.create_stratum(row, stratum_index, borehole_placement, tool.Stratum, tool.Geometry, tool.Ifc)
