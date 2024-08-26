import pandas as pd

from ..borehole.prop import ID as BOREHOLE_ID, IFC_TYPE, Z

STRATUM_BASICS = [BOREHOLE_ID, "stratum_name", "stratum_shape", IFC_TYPE, "stratum_height",
                  "stratum_id", Z]

BOREHOLE_ID = STRATUM_BASICS[0]
NAME = STRATUM_BASICS[1]
SHAPE = STRATUM_BASICS[2]
IFC_TYPE = STRATUM_BASICS[3]
HEIGHT = STRATUM_BASICS[4]
ID = STRATUM_BASICS[5]
Z = STRATUM_BASICS[6]
class StratumProperties:
    stratum_dataframe: pd.DataFrame = pd.DataFrame({k: [] for k in STRATUM_BASICS})
