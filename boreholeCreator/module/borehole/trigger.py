from boreholeCreator import tool
from boreholeCreator.core import borehole as core


def create_nested_borehole(borehole_row, stratums_rows):
    return core.create_nested_borehole(borehole_row, stratums_rows, tool.Borehole, tool.Geometry, tool.Ifc,
                                       tool.Location)


def create_unnested_borehole(borehole_row):
    return core.create_unnested_borehole(borehole_row, tool.Borehole, tool.Geometry, tool.Ifc, tool.Location)


def create_boreholes():
    return core.create_boreholes(tool.Borehole, tool.Stratum)
