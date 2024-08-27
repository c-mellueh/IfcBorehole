from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .ui import Widget
import pandas as pd

class BoreholeProperties:
    widget: Widget = None
    dataframe: pd.DataFrame = None
    header_view = None
    warning: str = None
