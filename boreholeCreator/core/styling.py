from __future__ import annotations

from typing import TYPE_CHECKING, Type

if TYPE_CHECKING:
    from boreholeCreator import tool


def style_entities(styling: Type[tool.Styling], borehole: Type[tool.Borehole], stratum: Type[tool.Stratum]):
    for style_dataframe in styling.get_style_list(stratum.get_dataframe()):
        styling.create_styles(style_dataframe)

    for style_dataframe in styling.get_style_list(borehole.get_dataframe()):
        styling.create_styles(style_dataframe)
