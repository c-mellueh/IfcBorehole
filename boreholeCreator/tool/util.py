import logging
from typing import Any

import ifcopenshell
import pandas as pd


class Util:
    @classmethod
    def fill_entity_with_dict(cls, entity: ifcopenshell.entity_instance, data_dict: dict[str, Any]):
        for name, value in data_dict.items():
            if value is None:
                continue
            setattr(entity, name, value)

    @classmethod
    def add_column(cls, dataframe: pd.DataFrame, column_name: str, value=None):
        dataframe.insert(len(dataframe.columns), column_name, value)

    @classmethod
    def add_missing_collumns(cls, df: pd.DataFrame, required_columns: list[str], optional_columns: dict[str, Any]):
        for col_name, default in optional_columns.items():
            if not col_name in df:
                cls.add_column(df, col_name, default)
        for col_name in required_columns:
            if not col_name in df:
                cls.add_column(df, col_name)

    @classmethod
    def is_dataframe_filled(cls, df, required_columns: list[str], optional_columns: dict[str, Any]):
        df_header = list(df)
        is_ok = True
        for col_name, default in optional_columns.items():
            if col_name not in df_header:
                cls.add_column(df, col_name, default)
        for col_name in required_columns:
            if col_name not in df_header:
                logging.error(f"Column '{col_name}' not found in Stratum dataframe")
                is_ok = False
        return is_ok
