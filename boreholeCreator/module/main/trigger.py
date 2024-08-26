from boreholeCreator import tool
from boreholeCreator.core import main as core


def create_boreholes():
    return core.create_boreholes(tool.Main, tool.Borehole, tool.Stratum)
