import boreholeGUI
from . import prop, trigger


def register():
    boreholeGUI.BoreholeProperties = prop.BoreholeProperties()


def load_ui_triggers():
    trigger.connect()
