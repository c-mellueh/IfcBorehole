import logging
from typing import Any

import pandas as pd

import boreholeCreator
import boreholeCreator.core.tool
from boreholeCreator.module.stratum.prop import BOREHOLE_ID, NAME, StratumProperties


class Stratum(boreholeCreator.core.tool.Stratum):
    @classmethod
    def get_properties(cls) -> StratumProperties:
        return boreholeCreator.StratumProperties

    @classmethod
    def get_dataframe(cls) -> pd.DataFrame:
        return cls.get_properties().stratum_dataframe

    @classmethod
    def set_dataframe(cls, df: pd.DataFrame):
        cls.get_properties().stratum_dataframe = df

    @classmethod
    def add_column(cls, column_name: str, value=None):
        df = cls.get_dataframe()
        df.insert(len(df.columns), column_name, value)

    @classmethod
    def add_stratum(cls, borehole_id: str, name: str, attributes: dict[str, Any], shape: int = 0):
        df = cls.get_dataframe()
        columns = list(df)
        df.loc[len(df)] = pd.Series()
        df.at[len(df), BOREHOLE_ID] = borehole_id
        df.at[len(df), NAME] = name
        for name, value in attributes.items():
            if name not in columns:
                logging.warning(f"Column '{name}' not found, will be added")
                cls.add_column(name)
                columns = list(df)
            index = columns.index(name)
            df.at[len(df), index] = value

    @classmethod
    def get_stratums_by_borehole_id(cls, borehole_id: str) -> pd.DataFrame:
        stratum_df = cls.get_dataframe()
        return stratum_df[stratum_df[BOREHOLE_ID] == borehole_id]
