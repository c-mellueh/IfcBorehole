PATH_SETTINGS = "paths"
from boreholeCreator.settings.appdata import AppdataSetting
class SettingsProperties:
    widget = None
    settings_list = list()
class PathSettings:
    ifc_export_path = AppdataSetting(
        PATH_SETTINGS, "ifc_export_path", str, "$USER/export.ifc"
    )
    import_path = AppdataSetting(
        PATH_SETTINGS, "import_path", str, "$USER/Desktop/import.xlsx"
    )