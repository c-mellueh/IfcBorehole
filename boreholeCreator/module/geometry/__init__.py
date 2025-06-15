import boreholeCreator
from . import prop


def register():
    boreholeCreator.GeometryProperties = prop.GeometryProperties()
    boreholeCreator.GeometrySettings = prop.GeometrySettings()
