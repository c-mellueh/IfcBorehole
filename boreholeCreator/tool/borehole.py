import logging

import pandas as pd

import boreholeCreator.core.tool
from boreholeCreator.module.borehole.prop import BoreholeProperties
from typing import Any



class Borehole(boreholeCreator.core.tool.Borehole):
    @classmethod
    def get_properties(cls) -> BoreholeProperties:
        return boreholeCreator.BoreholeProperties

    @classmethod
    def get_borehold_df(cls) -> pd.DataFrame:
        return cls.get_properties().borehole_dataframe

    @classmethod
    def add_column(cls,column_name:str,value = None):
        df = cls.get_borehold_df()
        df.insert(len(df.columns),column_name,value)

    @classmethod
    def add_borehole(cls,id:str,name:str,attributes:dict[str,Any]):
        df = cls.get_borehold_df()
        columns = list(df)
        row = [None for _ in columns]
        row[0],row[1]  = id,name
        for name,value in attributes.items():
            if name not in columns:
                logging.warning(f"Column '{name}' not found, will be added")
                cls.add_column(name)
                row.append(None)
                columns = list(df)
            index = columns.index(name)
            row[index] = value
        df.loc[len(df)] = row
