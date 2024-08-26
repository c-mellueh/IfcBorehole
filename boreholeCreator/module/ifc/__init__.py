import boreholeCreator
from . import prop
def register():
    boreholeCreator.IfcProperties = prop.IfcProperties()