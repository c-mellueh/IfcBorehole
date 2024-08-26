import logging
from typing import Any

import pandas as pd

import boreholeCreator.core.tool
from boreholeCreator.module.borehole.prop import BoreholeProperties, ID, NAME


class Borehole(boreholeCreator.core.tool.Borehole):
    @classmethod
    def get_properties(cls) -> BoreholeProperties:
        return boreholeCreator.BoreholeProperties

    @classmethod
    def get_dataframe(cls) -> pd.DataFrame:
        return cls.get_properties().borehole_dataframe

    @classmethod
    def set_dataframe(cls, df: pd.DataFrame):
        cls.get_properties().borehole_dataframe = df

    @classmethod
    def add_column(cls, column_name: str, value=None):
        df = cls.get_dataframe()
        df.insert(len(df.columns), column_name, value)

    @classmethod
    def add_borehole(cls, borehole_id: str, name: str, attributes: dict[str, Any]):
        df = cls.get_dataframe()
        columns = list(df)
        df.loc[len(df)] = [None for _ in columns]
        df.at[len(df), ID] = borehole_id
        df.at[len(df), NAME] = name
        for name, value in attributes.items():
            if name not in columns:
                logging.warning(f"Column '{name}' not found, will be added")
                cls.add_column(name)
                columns = list(df)
            index = columns.index(name)
            df.at[len(df), index] = value
