import logging
from typing import Any

import pandas as pd

import boreholeCreator.core.tool
from boreholeCreator.module.borehole import prop
from boreholeCreator.module.borehole import trigger


class Borehole(boreholeCreator.core.tool.Borehole):
    @classmethod
    def get_properties(cls) -> prop.BoreholeProperties:
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
        df.at[row, prop.ID] = borehole_id
        df.at[row, prop.NAME] = name
        for name, value in attributes.items():
            if name not in columns:
                logging.warning(f"Column '{name}' not found, will be added")
                cls.add_column(name)
                columns = list(df)
            column = columns.index(name)
            df.at[row, column] = value

        df.at[row][prop.X] = coordinates[0]
        df.at[row][prop.Y] = coordinates[1]
        df.at[row][prop.Z] = coordinates[2]

    @classmethod
    def get_position(cls, row: pd.Series):
        return row[prop.X], row[prop.Y], row[prop.Z]

    @classmethod
    def create_stratum(cls, row: pd.Series, borehole_placement):
        from boreholeCreator.module.stratum import trigger
        return trigger.create_stratum(row, borehole_placement)

    @classmethod
    def get_required_collumns(cls) -> list[str]:
        return prop.BOREHOLE_BASICS

    @classmethod
    def is_dataframe_filled(cls):
        df = list(cls.get_dataframe())
        for col_name in cls.get_required_collumns():
            if col_name not in df:
                logging.error(f"Column '{col_name}' not found in Borehole dataframe'")
                return False
        return True

    @classmethod
    def create_nested_borehole(cls, borehole_row, stratums_df):
        return trigger.create_nested_borehole(borehole_row, stratums_df)

    @classmethod
    def create_unnested_boreholes(cls, borehole_row):
        return trigger.create_unnested_borehole(borehole_row)

    @classmethod
    def create_boreholes(cls):
        return trigger.create_boreholes()
