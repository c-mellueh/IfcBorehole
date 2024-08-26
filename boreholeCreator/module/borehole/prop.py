import pandas as pd
ID = "borehole_id"
NAME = "borehole_name"

class BoreholeProperties:
    borehole_dataframe: pd.DataFrame = pd.DataFrame({ID: [], NAME: []})