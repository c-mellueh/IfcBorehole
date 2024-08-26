from boreholeCreator import tool
from boreholeCreator.core import styling as core


def style_entities():
    core.style_entities(tool.Styling, tool.Borehole, tool.Stratum)
