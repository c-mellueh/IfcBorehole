import boreholeGUI
from . import prop, trigger


def register():
    boreholeGUI.StratumProperties = prop.StratumProperties()


def load_ui_triggers():
    trigger.connect()
