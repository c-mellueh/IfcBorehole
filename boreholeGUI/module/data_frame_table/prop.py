from __future__ import annotations

from typing import TYPE_CHECKING

import pandas as pd

if TYPE_CHECKING:
    from .ui import Widget


class DataFrameTableProperties:
    widget: Widget = None
    dataframe: pd.DataFrame = None
    header_view = None
    warning = None
    tooltips: dict = None
