import boreholeGUI
from . import prop, trigger


def register():
    boreholeGUI.SettingsProperties = prop.SettingsProperties()
    boreholeGUI.PathSettings = prop.PathSettings()

def load_ui_triggers():
    trigger.connect()
