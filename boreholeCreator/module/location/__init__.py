import boreholeCreator
from . import prop
def register():
    boreholeCreator.LocationProperties = prop.LocationProperties()
    boreholeCreator.LocationSettings = prop.LocationSettings()