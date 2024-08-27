import boreholeGUI
from . import prop, trigger


def register():
    boreholeGUI.DataFrameTableProperties = prop.DataFrameTableProperties()


def load_ui_triggers():
    trigger.connect()
