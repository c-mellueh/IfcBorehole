import logging
from typing import Any, Type

import pandas as pd

import boreholeCreator.core.tool
from boreholeCreator import tool
from boreholeCreator.module.borehole import prop


class Borehole(boreholeCreator.core.tool.Borehole):
    @classmethod
    def get_properties(cls) -> prop.BoreholeProperties:
        return boreholeCreator.BoreholeProperties

    @classmethod
    def get_dataframe(cls) -> pd.DataFrame:
        if cls.get_properties().borehole_dataframe is None:
            cls.reset_dataframe()
        return cls.get_properties().borehole_dataframe

    @classmethod
    def set_dataframe(cls, df: pd.DataFrame):
        cls.get_properties().borehole_dataframe = df

    @classmethod
    def add_borehole(cls, borehole_id: str, name: str, coordinates: tuple[float, float, float | None],
                     attributes: dict[str, Any], height: float, ifc_type: str = "IfcBuildingElementProxy"):
        df = cls.get_dataframe()
        columns = list(df)
        row = len(df)
        df.loc[row] = [None for _ in columns]
        df.at[row, prop.ID] = borehole_id
        df.at[row, prop.NAME] = name
        df.at[row, prop.HEIGHT] = height
        df.at[row, prop.IFC_TYPE] = ifc_type
        df.at[row, prop.X] = coordinates[0]
        df.at[row, prop.Y] = coordinates[1]
        df.at[row, prop.Z] = coordinates[2]

        for name, value in attributes.items():
            if name not in columns:
                logging.warning(f"Column '{name}' not found, will be added")
                tool.Util.add_column(df, name)
                columns = list(df)
            df.at[row, name] = value

    @classmethod
    def get_position(cls, row: pd.Series):
        return row[prop.X], row[prop.Y], row[prop.Z]

    @classmethod
    def create_stratum(cls, row: pd.Series, stratum_index: int, borehole_placement):
        from boreholeCreator.module.stratum import trigger
        return trigger.create_stratum(row, stratum_index, borehole_placement)

    @classmethod
    def get_required_columns(cls) -> list[tuple[str, type]]:
        return prop.BOREHOLE_REQUIRED

    @classmethod
    def get_required_column_names(cls) -> list[str]:
        return [x[0] for x in cls.get_required_columns()]

    @classmethod
    def get_required_column_datatypes(cls) -> list[type]:
        return [x[1] for x in cls.get_required_columns()]

    @classmethod
    def set_correct_datatypes(cls, dataframe: pd.DataFrame) -> pd.DataFrame:
        col_names = cls.get_optional_column_names() + cls.get_required_column_names()
        col_datatypes = cls.get_optional_column_datatypes() + cls.get_required_column_datatypes()
        for name, datatype in zip(col_names, col_datatypes):
            if name in list(dataframe):
                dataframe[name] = dataframe[name].astype(datatype)
        return dataframe

    @classmethod
    def get_optional_collumns(cls) -> list[tuple[str, Type, Any]]:
        """

        :return: list[tuple[name,Datatype,default_value]]
        """
        return prop.BOREHOLE_OPTIONAL

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
        df_header = list(cls.get_dataframe())
        for col_name, datatypes, default in cls.get_optional_collumns():
            if col_name not in df_header:
                tool.Util.add_column(cls.get_dataframe(), col_name, default)

        for col_name in cls.get_required_column_names():
            if col_name not in df_header:
                logging.error(f"Column '{col_name}' not found in Borehole dataframe")
                return False
        return True

    @classmethod
    def create_nested_borehole(cls, borehole_row, stratums_df):
        from boreholeCreator.module.borehole import trigger

        return trigger.create_nested_borehole(borehole_row, stratums_df)

    @classmethod
    def create_unnested_boreholes(cls, borehole_row):
        from boreholeCreator.module.borehole import trigger

        return trigger.create_unnested_borehole(borehole_row)

    @classmethod
    def create_boreholes(cls):
        from boreholeCreator.module.borehole import trigger
        return trigger.create_boreholes()

    @classmethod
    def reset_dataframe(cls):
        required = cls.get_required_columns()
        optional = [x[:2] for x in cls.get_optional_collumns()]
        dataframe = pd.DataFrame({k: pd.Series(dtype=dt) for k, dt in required + optional})
        cls.get_properties().borehole_dataframe = dataframe
