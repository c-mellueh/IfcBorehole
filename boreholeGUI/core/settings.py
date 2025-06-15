from __future__ import annotations

from typing import TYPE_CHECKING, Type

from PySide6.QtWidgets import QCheckBox, QComboBox, QDoubleSpinBox, QLineEdit

if TYPE_CHECKING:
    from boreholeGUI import tool
    from boreholeCreator import tool as cli_tool
    from boreholeCreator import settings as cli_settings
from boreholeGUI import tool


def add_widget_to_mainwindow(
    main_window: Type[tool.MainWindow], settings: Type[tool.Settings]
):
    widget = settings.get_widget()
    main_window.add_step("Settings", widget)
    settings.signaller.update_requested.connect(
        lambda: update_all_fields(settings)
    )

def add_settings_getter_setter(
    settings: Type[tool.Settings],
    geometry: Type[cli_tool.Geometry],
    ifc: Type[cli_tool.Ifc],
    location: Type[cli_tool.Location],
):
    ui = settings.get_widget().ui
    ifc_settings = ifc.get_settings()
    geometry_settings = geometry.get_settings()
    location_settings = location.get_settings()
    
    # Geometry
    settings.add_setting(
        ui.sb_radius,
        lambda: getattr(geometry_settings, "radius"),
        lambda x: setattr(geometry_settings, "radius", x),
        float,
    )
    settings.add_setting(
        ui.cb_primitive,
        lambda: getattr(geometry_settings, "use_primitive"),
        lambda x: setattr(geometry_settings, "use_primitive", x),
        bool,
    )
    # Application
    settings.add_setting(
        ui.le_application_name,
        lambda: getattr(ifc_settings, "application_name"),
        lambda x: setattr(ifc_settings, "application_name", x),
        str,
    )
    settings.add_setting(
        ui.le_application_version,
        lambda: getattr(ifc_settings, "application_version"),
        lambda x: setattr(ifc_settings, "application_version", x),
        str,
    )

    # Author
    settings.add_setting(
        ui.le_author_family_name,
        lambda: getattr(ifc_settings, "author_family_name"),
        lambda x: setattr(ifc_settings, "author_family_name", x),
        str,
    )
    settings.add_setting(
        ui.le_author_given_name,
        lambda: getattr(ifc_settings, "author_given_name"),
        lambda x: setattr(ifc_settings, "author_given_name", x),
        str,
    )

    # Organization
    settings.add_setting(
        ui.le_company_name,
        lambda: getattr(ifc_settings, "organization_name"),
        lambda x: setattr(ifc_settings, "organization_name", x),
        str,
    )
    settings.add_setting(
        ui.le_company_description,
        lambda: getattr(ifc_settings, "organization_description"),
        lambda x: setattr(ifc_settings, "organization_description", x),
        str,
    )

    # Misc.
    settings.add_setting(
        ui.cb_file_schema,
        lambda: getattr(ifc_settings, "file_schema"),
        lambda x: setattr(ifc_settings, "file_schema", x),
        str,
    )
    settings.add_setting(
        ui.le_default_pset_name,
        lambda: getattr(ifc_settings, "pset_base_name"),
        lambda x: setattr(ifc_settings, "pset_base_name", x),
        str,
    )

    # MapConversion
    location_attributes = [
        (ui.le_eastings, "eastings", float),
        (ui.le_northings, "northings", float),
        (ui.le_orthogonal_height, "orthogonal_height", float),
        (ui.le_x_axis_abscissa, "x_axis_abscissa", float),
        (ui.le_x_axis_ordinate, "x_axis_ordinate", float),
        (ui.le_scale, "scale", float),
        (ui.cb_mapconversion, "mapconversion_is_activated", bool),
        (ui.le_crs_name, "crs_name", str),
        (ui.le_crs_description, "crs_description", str),
        (ui.le_geodetic_datum, "geodetic_datum", str),
        (ui.le_vertical_datum, "vertical_datum", str),
        (ui.le_map_projection, "map_projection", str),
        (ui.le_mapzone, "map_zone", str),
    ]

    for widget, name, data_type in location_attributes:
        settings.add_setting(
            widget,
            lambda n=name: getattr(location_settings, n),
            lambda x, n=name: setattr(location_settings, n, x),
            data_type,
        )

    ui.cb_mapconversion.checkStateChanged.connect(
        lambda: activate_mapconversion_toggled(settings)
    )
    activate_mapconversion_toggled(settings)
    update_all_fields(settings)


def activate_mapconversion_toggled(settings: Type[tool.Settings]):
    widget = settings.get_widget().ui.wi_map_conversion
    widget.setEnabled(settings.get_widget().ui.cb_mapconversion.isChecked())


def create_ui_triggers(settings: Type[tool.Settings]):
    for widget, getter, setter, _ in settings.get_settings_list():
        print(widget, setter)
        settings.add_ui_trigger(widget, setter)


def update_all_fields(settings: Type[tool.Settings]):
    for widget, getter, setter, _ in settings.get_settings_list():
        settings.update_widget(widget, getter)
