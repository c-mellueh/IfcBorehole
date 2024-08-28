import pandas as pd

from ..borehole.prop import BLUE, GREEN, IFC_GUID, IFC_TYPE, RED, TRANSPARENCY, Z
from ..borehole.prop import ID as BOREHOLE_ID

NAME = "stratum_name"
SHAPE = "stratum_shape"
HEIGHT = "stratum_height"
ID = "stratum_id"

STRATUM_REQUIRED = [BOREHOLE_ID, NAME, SHAPE, IFC_TYPE, HEIGHT,
                    ID, Z, IFC_GUID]
STRATUM_REQUIRED_DATATYPE = [str, str, int, str, float, str, float, str]

STRATUM_OPTIONAL = {RED:          0.5,  # Key & Default Value
                    GREEN:        0.5,
                    BLUE:         0.5,
                    TRANSPARENCY: 0.}


class StratumProperties:
    stratum_dataframe: pd.DataFrame = pd.DataFrame({k: [] for k in STRATUM_REQUIRED + list(STRATUM_OPTIONAL.keys())})
