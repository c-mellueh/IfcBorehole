import pandas as pd

from ..borehole.prop import ID as BOREHOLE_ID

ID = "stratum_id"
NAME = "stratum_name"
BOREHOLE_INDEX = "borehole_index"
class StratumProperties:
    stratum_dataframe: pd.DataFrame = pd.DataFrame({BOREHOLE_ID: [], NAME: []})
