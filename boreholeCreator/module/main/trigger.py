from boreholeCreator import tool
from boreholeCreator.core import main as core


def create_file(path):
    core.create_file(path, tool.Ifc, tool.Location, tool.Borehole, tool.Stratum, tool.Styling)
