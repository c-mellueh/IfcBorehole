import pandas as pd

ID = "borehole_id"
NAME = "borehole_name"
X = "x_pos"
Y = "y_pos"
Z = "z_pos"
IFC_TYPE = "ifc_type"
HEIGHT = "height"
IFC_GUID = "ifc_guid"
BOREHOLE_REQUIRED = [ID, NAME, X, Y, Z, IFC_TYPE, HEIGHT, ]
BOREHOLE_REQUIRED_DATATYPES = [str, str, float, float, float, str, float]
RED = "red"
GREEN = "green"
BLUE = "blue"
TRANSPARENCY = "transparency"

BOREHOLE_OPTIONAL = {RED:          0.5,  # Key & Default Value
                     GREEN:        0.5,
                     BLUE:         0.5,
                     TRANSPARENCY: 0.,
                     IFC_GUID:     ""}




class BoreholeProperties:
    borehole_dataframe: pd.DataFrame = pd.DataFrame({k: [] for k in BOREHOLE_REQUIRED + list(BOREHOLE_OPTIONAL.keys())})
