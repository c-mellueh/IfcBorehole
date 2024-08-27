import boreholeGUI
from . import prop, trigger


def register():
    boreholeGUI.MainWindowProperties = prop.MainWindowProperties()


def load_ui_triggers():
    trigger.connect()
