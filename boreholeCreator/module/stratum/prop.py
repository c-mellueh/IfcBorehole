import pandas as pd

from ..borehole.prop import BLUE, GREEN, HEIGHT, IFC_GUID, IFC_TYPE, NAME, RED, TRANSPARENCY, Z
from ..borehole.prop import ID as BOREHOLE_ID

ID = "stratum_id"
STRATUM_REQUIRED = [(BOREHOLE_ID, str), (ID, str), (NAME, str), (HEIGHT, float), (Z, float)]
SHAPE = "stratum_shape"

STRATUM_OPTIONAL = [
    (RED, float, 0.5),
    (GREEN, float, 0.5),
    (BLUE, float, 0.5),
    (TRANSPARENCY, float, 0.),
    (IFC_GUID, str, ""),
    (IFC_TYPE, str, "IfcBuildingElementProxy"),
    (SHAPE, int, 0),
]


class StratumProperties:
    stratum_dataframe: pd.DataFrame = None
