import boreholeGUI
from . import prop, trigger


def register():
    boreholeGUI.PopupsProperties = prop.PopupsProperties()


def load_ui_triggers():
    trigger.connect()
