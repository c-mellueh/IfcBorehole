import boreholeGUI
from . import prop, trigger


def register():
    boreholeGUI.SettingsProperties = prop.SettingsProperties()


def load_ui_triggers():
    trigger.connect()
