import pandas as pd

from ..borehole.prop import ID as BOREHOLE_ID, IFC_TYPE

STRATUM_BASICS = [BOREHOLE_ID, "stratum_name", "stratum_shape", "borehole_index", IFC_TYPE, "stratum_height",
                  "stratum_id"]

BOREHOLE_ID = STRATUM_BASICS[0]
NAME = STRATUM_BASICS[1]
SHAPE = STRATUM_BASICS[2]
BOREHOLE_INDEX = STRATUM_BASICS[3]
HEIGHT = STRATUM_BASICS[4]
ID = STRATUM_BASICS[5]
class StratumProperties:
    stratum_dataframe: pd.DataFrame = pd.DataFrame({k: [] for k in STRATUM_BASICS})
