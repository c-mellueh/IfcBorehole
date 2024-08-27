import boreholeGUI
from . import prop, trigger


def register():
    boreholeGUI.ColorProperties = prop.ColorProperties()


def load_ui_triggers():
    trigger.connect()
