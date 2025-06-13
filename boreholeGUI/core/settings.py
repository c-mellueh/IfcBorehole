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


def add_settings_getter_setter(
    settings: Type[tool.Settings],
    geometry: Type[cli_tool.Geometry],
    ifc: Type[cli_tool.Ifc],
    location: Type[cli_settings.Location],
):
    ui = settings.get_widget().ui
    ifc_settings = ifc.get_settings()
    geometry_settings = geometry.get_settings()
    # Geometry
    settings.add_setting(
        ui.sb_radius,
        lambda: getattr(geometry_settings, "radius"),
        lambda x: setattr(geometry_settings, "radius", x),
        float,
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
    map_conversion_attributes = [
        (ui.le_eastings, "Eastings", float),
        (ui.le_northings, "Northings", float),
        (ui.le_orthogonal_height, "OrthogonalHeight", float),
        (ui.le_x_axis_abscissa, "XAxisAbscissa", float),
        (ui.le_x_axis_ordinate, "XAxisOrdinate", float),
        (ui.le_scale, "Scale", float),
    ]

    for widget, name, datatype in map_conversion_attributes:
        settings.add_setting(
            widget,
            lambda n=name: location.get_map_conversion_attribute(n),
            lambda v, n=name: location.set_map_conversion_attribute(n, v),
            datatype,
        )
    # ProjectedCRS
    project_crs_attributes = [
        (ui.le_crs_name, "Name", str),
        (ui.le_crs_description, "Description", str),
        (ui.le_geodetic_datum, "GeodeticDatum", str),
        (ui.le_vertical_datum, "VerticalDatum", str),
        (ui.le_map_projection, "MapProjection", str),
        (ui.le_mapzone, "MapZone", str),
    ]
    for widget, name, datatype in project_crs_attributes:
        settings.add_setting(
            widget,
            lambda n=name: location.get_projected_crs_attribute(n),
            lambda v, n=name: location.set_projected_crs_attribute(n, v),
            datatype,
        )
    # Checkbox Mapconversion
    settings.add_setting(
        ui.cb_mapconversion,
        location.mapconversion_is_activated,
        location.set_mapconversion_activated,
        bool,
    )
    ui.cb_mapconversion.checkStateChanged.connect(
        lambda: activate_mapconversion_toggled(settings)
    )
    activate_mapconversion_toggled(settings)


def activate_mapconversion_toggled(settings: Type[tool.Settings]):
    widget = settings.get_widget().ui.wi_map_conversion
    widget.setEnabled(settings.get_widget().ui.cb_mapconversion.isChecked())


def create_ui_triggers(settings: Type[tool.Settings]):
    for widget, getter, setter, _ in settings.get_settings_list():
        settings.add_ui_trigger(widget, setter)


def paint_event(settings: Type[tool.Settings]):
    for widget, getter, setter, _ in settings.get_settings_list():
        settings.add_paint_event(widget, getter)
