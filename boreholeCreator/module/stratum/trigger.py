from boreholeCreator import tool
from boreholeCreator.core import stratum as core


def create_stratum(row, borehole_placement):
    return core.create_stratum(row, borehole_placement, tool.Geometry, tool.Ifc)
