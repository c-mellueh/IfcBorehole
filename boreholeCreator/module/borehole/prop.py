import pandas as pd

BOREHOLE_BASICS = ["borehole_id", "borehole_name", "x_pos", "y_pos", "z_pos", "ifc_type", "height"]
ID = BOREHOLE_BASICS[0]
NAME = BOREHOLE_BASICS[1]
X = BOREHOLE_BASICS[2]
Y = BOREHOLE_BASICS[3]
Z = BOREHOLE_BASICS[4]
IFC_TYPE = BOREHOLE_BASICS[5]
HEIGHT = BOREHOLE_BASICS[6]
class BoreholeProperties:
    borehole_dataframe: pd.DataFrame = pd.DataFrame({k: [] for k in BOREHOLE_BASICS})
