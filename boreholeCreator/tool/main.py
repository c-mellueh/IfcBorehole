import boreholeCreator.core.tool
class Main(boreholeCreator.core.tool.Main):
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
        from boreholeCreator.module.main import trigger
        return trigger.create_boreholes()
