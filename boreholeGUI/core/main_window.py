from __future__ import annotations

import os
from typing import TYPE_CHECKING, Type

if TYPE_CHECKING:
    from boreholeGUI import tool
    from boreholeCreator import tool as cli_tool


def create_main_window(
    app, main_window: Type[tool.MainWindow], settings: Type[tool.Settings]
):
    mw = main_window.create_main_window(app)
    main_window.clear_toolbox()
    for name, widget in main_window.get_steplist():
        main_window.get_toolbox().addItem(widget, name)
        widget.show()
    main_window.create_trigger()
    mw.show()
    main_window.hide_terminal()
    settings.add_setting(
        main_window.get_ui().le_export_path,
        lambda: getattr(settings, "ifc_export_path"),
        lambda x: setattr(settings, "ifc_export_path", x),
        str,
    )
    settings.add_ui_trigger(
        main_window.get_ui().le_export_path,
        lambda x: setattr(settings, "ifc_export_path", x),
    )
    settings.update_widget(
        main_window.get_ui().le_export_path,
        lambda: getattr(settings, "ifc_export_path"),
    )


def select_ifc_clicked(
    main_window: Type[tool.MainWindow],
    popups: Type[tool.Popups],
    settings: Type[tool.Settings],
):
    path = popups.get_save_path("IFC  (*.ifc);;all (*.*)", main_window.get())
    if not path:
        return
    settings.ifc_export_path = path


def run_clicked(
    main_window: Type[tool.MainWindow],
    borehole: Type[tool.Borehole],
    stratum: Type[tool.Stratum],
    settings: Type[tool.Settings],
    popups: Type[tool.Popups],
    ifc: Type[cli_tool.Ifc],
):
    path = settings.ifc_export_path
    if not main_window.is_file_path_valid(path):
        popups.create_warning_popup(
            "Invalid Path", f"Path 'path' is invalid, please check"
        )
        return
    if not settings.settings_are_valid():
        return
    ifc.get_settings().file_name = os.path.basename(path)

    borehole_df = borehole.get_dataframe()
    borehole_df = borehole.get_cli().set_correct_datatypes(borehole_df)
    borehole.get_cli().set_dataframe(borehole_df)
    stratum_df = stratum.get_cli().set_correct_datatypes(stratum.get_dataframe())
    stratum.get_cli().set_dataframe(stratum_df)
    import boreholeCreator

    boreholeCreator.create_file(path)
