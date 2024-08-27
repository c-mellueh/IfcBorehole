from __future__ import annotations

from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .ui import Widget


class DataFrameTableProperties:
    tool_dict: dict[Widget, Any] = dict()
