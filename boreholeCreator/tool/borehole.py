import logging
from typing import Any

import pandas as pd

import boreholeCreator.core.tool
from boreholeCreator.module.borehole.prop import BoreholeProperties, ID, NAME, X, Y, Z


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
    def add_borehole(cls, borehole_id: str, name: str, attributes: dict[str, Any],
                     coordinates: tuple[float, float, float | None]):
        df = cls.get_dataframe()
        columns = list(df)
        row = len(df)
        df.loc[row] = [None for _ in columns]
        df.at[row, ID] = borehole_id
        df.at[row, NAME] = name
        for name, value in attributes.items():
            if name not in columns:
                logging.warning(f"Column '{name}' not found, will be added")
                cls.add_column(name)
                columns = list(df)
            column = columns.index(name)
            df.at[row, column] = value

        df.at[row][X] = coordinates[0]
        df.at[row][Y] = coordinates[1]
        df.at[row][Z] = coordinates[2]

    @classmethod
    def get_position(cls, row: pd.Series):
        return row[X], row[Y], row[Z]

    @classmethod
    def create_stratum(cls, row: pd.Series, borehole_placement):
        from boreholeCreator.module.stratum import trigger
        return trigger.create_stratum(row, borehole_placement)
