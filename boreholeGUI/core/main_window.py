from __future__ import annotations

import os
from typing import TYPE_CHECKING, Type

if TYPE_CHECKING:
    from boreholeGUI import tool
    from boreholeCreator import settings as cli_settings

def create_main_window(app, main_window: Type[tool.MainWindow]):
    mw = main_window.create_main_window(app)
    main_window.clear_toolbox()
    for name, widget in main_window.get_steplist():
        main_window.get_toolbox().addItem(widget, name)
        widget.show()
    main_window.create_trigger()
    mw.show()
    main_window.hide_console()


def select_ifc_clicked(main_window: Type[tool.MainWindow], popups: Type[tool.Popups]):
    path = popups.get_save_path("IFC  (*.ifc);;all (*.*)", main_window.get())
    if not path:
        return
    main_window.set_export_path(path)


def run_clicked(main_window: Type[tool.MainWindow], borehole: Type[tool.Borehole], stratum: Type[tool.Stratum],
                settings: Type[tool.Settings], popups: Type[tool.Popups], cli_settings_ifc: Type[cli_settings.Ifc]):
    path = main_window.get_export_path()
    if not main_window.is_file_path_valid(path):
        popups.create_warning_popup("Invalid Path", f"Path 'path' is invalid, please check")
        return
    if not settings.settings_are_valid():
        return
    cli_settings_ifc.set_file_name(os.path.basename(path))

    borehole_df = borehole.get_dataframe()
    borehole_df = borehole.get_cli().set_correct_datatypes(borehole_df)
    borehole.get_cli().set_dataframe(borehole_df)
    stratum_df = stratum.get_cli().set_correct_datatypes(stratum.get_dataframe())
    stratum.get_cli().set_dataframe(stratum_df)
    import boreholeCreator
    boreholeCreator.create_file("TestExport.ifc")
