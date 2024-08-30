import pandas as pd

ID = "borehole_id"
NAME = "name"
X = "x_pos"
Y = "y_pos"
Z = "z_pos"
HEIGHT = "height"

BOREHOLE_REQUIRED = [(ID, str), (NAME, str), (X, float), (Y, float), (Z, float), (HEIGHT, float)]
IFC_TYPE = "ifc_type"
IFC_GUID = "ifc_guid"
RED = "red"
GREEN = "green"
BLUE = "blue"
TRANSPARENCY = "transparency"

BOREHOLE_OPTIONAL = [
    (RED, float, 0.5),
    (GREEN, float, 0.5),
    (BLUE, float, 0.5),
    (TRANSPARENCY, float, 0.),
    (IFC_GUID, str, ""),
    (IFC_TYPE, str, "IfcBuildingElementProxy"),
]



class BoreholeProperties:
    borehole_dataframe: pd.DataFrame = None
