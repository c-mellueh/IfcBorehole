import logging
from typing import Any

import pandas as pd

import boreholeCreator
import boreholeCreator.core.tool
from boreholeCreator.module.stratum import prop


class Stratum(boreholeCreator.core.tool.Stratum):
    @classmethod
    def get_properties(cls) -> prop.StratumProperties:
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
    def add_stratum(cls, borehole_id: str, name: str, height: float, stratum_id: str, z_pos: float,
                    attributes: dict[str, Any], ifc_type: str = "IfcBuildingElementProxy", shape: int = 0):
        df = cls.get_dataframe()
        columns = list(df)
        row = len(columns)
        df.loc[row] = pd.Series()
        df.at[row, prop.BOREHOLE_ID] = borehole_id
        df.at[row, prop.NAME] = name
        df.at[row, prop.SHAPE] = shape
        df.at[row, prop.IFC_TYPE] = ifc_type
        df.at[row, prop.HEIGHT] = height
        df.at[row, prop.ID] = stratum_id
        df.at[row, prop.Z] = z_pos
        for name, value in attributes.items():
            if name not in columns:
                logging.warning(f"Column '{name}' not found, will be added")
                cls.add_column(name)
                columns = list(df)
            df.at[len(df), columns.index(name)] = value

    @classmethod
    def get_stratums_by_borehole_id(cls, borehole_id: str) -> pd.DataFrame:
        stratum_df = cls.get_dataframe()
        return stratum_df[stratum_df[prop.BOREHOLE_ID] == borehole_id]

    @classmethod
    def get_required_collumns(cls):
        return prop.STRATUM_BASICS

    @classmethod
    def is_dataframe_filled(cls):
        df = list(cls.get_dataframe())
        for col_name in cls.get_required_collumns():
            if col_name not in df:
                logging.error(f"Column '{col_name}' not found in Stratum dataframe'")
                return False
        return True
