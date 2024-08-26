import ifcopenshell
import ifcopenshell.api
import pandas as pd

import boreholeCreator.core.tool
from boreholeCreator import tool


class Styling(boreholeCreator.core.tool.Styling):
    @classmethod
    def style_entities(cls):
        from boreholeCreator.module.styling import trigger
        trigger.style_entities()
        pass

    @classmethod
    def get_style_list(cls, dataframe: pd.DataFrame):
        from boreholeCreator.module.stratum import prop as stratum_prop
        df_list = list()
        for i, sub_df in dataframe[[stratum_prop.RED, stratum_prop.GREEN, stratum_prop.BLUE,
                                    stratum_prop.TRANSPARENCY]].drop_duplicates().iterrows():
            idx = dataframe.columns.intersection(sub_df.index)
            df_list.append(dataframe.loc[dataframe[idx].eq(sub_df.loc[idx]).all(1)])
        return df_list

    @classmethod
    def create_style(cls, red, green, blue, transparency):
        ifcfile = tool.Ifc.get_ifcfile()
        style = ifcopenshell.api.run("style.add_style", ifcfile)
        attributes = {
            "SurfaceColour": {"Name": None, "Red": red, "Green": green, "Blue": blue},
            "Transparency":  transparency,  # 0 is opaque, 1 is transparent
        }
        ifcopenshell.api.run("style.add_surface_style", ifcfile,
                             style=style, ifc_class="IfcSurfaceStyleShading", attributes=attributes)
        return style

    @classmethod
    def get_rgbt(cls, dataframe: pd.DataFrame) -> tuple[float, float, float, float]:
        from boreholeCreator.module.borehole.prop import RED, GREEN, BLUE, TRANSPARENCY
        return tuple(dataframe[[RED, GREEN, BLUE, TRANSPARENCY]].drop_duplicates().itertuples(index=False, name=None))[
            0]

    @classmethod
    def create_styles(cls, dataframe: pd.DataFrame):
        from boreholeCreator.module.borehole.prop import IFC_GUID
        r, g, b, t = cls.get_rgbt(dataframe)
        style = cls.create_style(r, g, b, t)
        ifcfile = tool.Ifc.get_ifcfile()
        for ifc_guid in dataframe[IFC_GUID]:
            ifcopenshell.api.run("style.assign_representation_styles", ifcfile,
                                 shape_representation=ifcfile.by_guid(ifc_guid).Representation, styles=[style])
