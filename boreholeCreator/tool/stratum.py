import logging
from typing import Any

import pandas as pd

import boreholeCreator
import boreholeCreator.core.tool
from boreholeCreator import tool
from boreholeCreator.module.stratum import prop


class Stratum(boreholeCreator.core.tool.Stratum):
    @classmethod
    def get_properties(cls) -> prop.StratumProperties:
        return boreholeCreator.StratumProperties

    @classmethod
    def get_dataframe(cls) -> pd.DataFrame:
        if cls.get_properties().stratum_dataframe is None:
            cls.reset_dataframe()
        return cls.get_properties().stratum_dataframe

    @classmethod
    def set_dataframe(cls, df: pd.DataFrame):
        cls.get_properties().stratum_dataframe = df

    @classmethod
    def add_stratum(cls, borehole_id: str, name: str, height: float, stratum_id: str, z_pos: float,
                    attributes: dict[str, Any], ifc_type: str = "IfcBuildingElementProxy", shape: int = 0):
        df = cls.get_dataframe()
        columns = list(df)
        row = len(df)
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
                tool.Util.add_column(df, name)
                columns = list(df)
            df.at[len(df), columns.index(name)] = value

    @classmethod
    def get_stratums_by_borehole_id(cls, borehole_id: str) -> pd.DataFrame:
        stratum_df = cls.get_dataframe()
        return stratum_df[stratum_df[prop.BOREHOLE_ID] == borehole_id]

    @classmethod
    def get_required_columns(cls):
        return prop.STRATUM_REQUIRED

    @classmethod
    def get_required_column_names(cls):
        return [x[0] for x in cls.get_required_columns()]

    @classmethod
    def get_required_column_datatypes(cls):
        return [x[1] for x in cls.get_required_columns()]

    @classmethod
    def get_optional_collumns(cls) -> list[tuple[str, type, Any]]:
        return prop.STRATUM_OPTIONAL

    @classmethod
    def get_optional_column_names(cls):
        return [x[0] for x in cls.get_optional_collumns()]

    @classmethod
    def get_optional_column_datatypes(cls):
        return [x[1] for x in cls.get_optional_collumns()]

    @classmethod
    def get_optional_column_defaults(cls):
        return [x[2] for x in cls.get_optional_collumns()]

    @classmethod
    def is_dataframe_filled(cls):
        df = cls.get_dataframe()
        df_header = list(df)
        for col_name, datatype, default in cls.get_optional_collumns():
            if col_name not in df_header:
                tool.Util.add_column(df, col_name, default)
        for col_name in cls.get_required_column_names():
            if col_name not in df_header:
                logging.error(f"Column '{col_name}' not found in Stratum dataframe")
                return False
        return True

    @classmethod
    def reset_dataframe(cls):
        required = cls.get_required_columns()
        optional = cls.get_optional_collumns()
        df = pd.DataFrame({
            k: pd.Series(dtype=dt) for k, dt in required + [x[:2] for x in optional]
        })
        cls.get_properties().stratum_dataframe = df

    @classmethod
    def set_correct_datatypes(cls, dataframe: pd.DataFrame):
        for name, datatype in zip(cls.get_required_column_names(), cls.get_required_column_datatypes()):
            dataframe[name] = dataframe[name].astype(datatype)
        return dataframe
