from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from boreholeGUI.module.data_frame_table.ui import Widget
import pandas as pd
from boreholeCreator.module.borehole import prop

class BoreholeProperties:
    widget: Widget = None
    dataframe: pd.DataFrame = None
    header_view = None
    warning: str = None
    tooltips = {
        prop.IFC_TYPE: "IFC-Klasse z.B. 'IfcBuildingElementProxy'",
        prop.HEIGHT:   "Z-Ausdehnung der Säule",
        prop.ID:       "Identifier der Säule notwendig um Matching mit Schicht zu erstellen"

    }
