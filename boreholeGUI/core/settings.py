from __future__ import annotations

from typing import TYPE_CHECKING, Type

from PySide6.QtWidgets import QCheckBox, QComboBox, QDoubleSpinBox, QLineEdit

if TYPE_CHECKING:
    from boreholeGUI import tool
    from boreholeCreator import settings as cli_settings
from boreholeGUI import tool


def add_widget_to_mainwindow(main_window: Type[tool.MainWindow], settings: Type[tool.Settings]):
    widget = settings.get_widget()
    main_window.add_step("Settings", widget)


def add_settings_getter_setter(settings: Type[tool.Settings],
                               geometry: Type[cli_settings.Geometry],
                               ifc: Type[cli_settings.Ifc],
                               location: Type[cli_settings.Location], ):
    ui = settings.get_widget().ui

    # Geometry
    settings.add_setting(ui.sb_radius, geometry.get_radius, geometry.set_radius, float)

    # Application
    settings.add_setting(ui.le_application_name, ifc.get_application_name, ifc.set_application_name, str)
    settings.add_setting(ui.le_application_version, ifc.get_application_version, ifc.set_application_version, str)

    # Author
    settings.add_setting(ui.le_author_family_name, lambda: ifc.get_author_attribute("FamilyName"),
                         lambda v: ifc.set_author_attribute("FamilyName", v), str)
    settings.add_setting(ui.le_author_given_name, lambda: ifc.get_author_attribute("GivenName"),
                         lambda v: ifc.set_author_attribute("GivenName", v), str)

    # Organization
    settings.add_setting(ui.le_company_name, lambda: ifc.get_organization_attribute("Name"),
                         lambda v: ifc.set_organization_attribute("Name", v), str)
    settings.add_setting(ui.le_company_description, lambda: ifc.get_organization_attribute("Description"),
                         lambda v: ifc.set_organization_attribute("Description", v), str)

    # Misc.
    settings.add_setting(ui.cb_file_schema, ifc.get_file_schema, ifc.set_file_schema, str)
    settings.add_setting(ui.le_default_pset_name, ifc.get_default_pset_name, ifc.set_default_pset_name, str)

    # MapConversion
    map_conversion_attributes = [(ui.le_eastings, "Eastings", float),
                                 (ui.le_northings, "Northings", float),
                                 (ui.le_orthogonal_height, "OrthogonalHeight", float),
                                 (ui.le_x_axis_abscissa, "XAxisAbscissa", float),
                                 (ui.le_x_axis_ordinate, "XAxisOrdinate", float),
                                 (ui.le_scale, "Scale", float)]

    for widget, name, datatype in map_conversion_attributes:
        settings.add_setting(widget, lambda n=name: location.get_map_conversion_attribute(n),
                             lambda v, n=name: location.set_map_conversion_attribute(n, v), datatype)
    # ProjectedCRS
    project_crs_attributes = [(ui.le_crs_name, "Name", str),
                              (ui.le_crs_description, "Description", str),
                              (ui.le_geodetic_datum, "GeodeticDatum", str),
                              (ui.le_vertical_datum, "VerticalDatum", str),
                              (ui.le_map_projection, "MapProjection", str),
                              (ui.le_mapzone, "MapZone", str)]
    for widget, name, datatype in project_crs_attributes:
        settings.add_setting(widget, lambda n=name: location.get_projected_crs_attribute(n),
                             lambda v, n=name: location.set_projected_crs_attribute(n, v), datatype)
    # Checkbox Mapconversion
    settings.add_setting(ui.cb_mapconversion, location.mapconversion_is_activated, location.set_mapconversion_activated,
                         bool)
    ui.cb_mapconversion.checkStateChanged.connect(lambda: activate_mapconversion_toggled(settings))
    activate_mapconversion_toggled(settings)


def activate_mapconversion_toggled(settings: Type[tool.Settings]):
    widget = settings.get_widget().ui.wi_map_conversion
    widget.setEnabled(settings.get_widget().ui.cb_mapconversion.isChecked())


def create_ui_triggers(settings: Type[tool.Settings]):
    def none_handler(v):
        return None if v == "None" else v

    for widget, getter, setter, _ in settings.get_settings_list():
        if isinstance(widget, QLineEdit):
            widget.textEdited.connect(lambda v, s=setter: s(none_handler(v)))

        elif isinstance(widget, QComboBox):
            widget.currentTextChanged.connect(setter)

        elif isinstance(widget, QDoubleSpinBox):
            widget.valueChanged.connect(setter)

        elif isinstance(widget, QCheckBox):
            widget.checkStateChanged.connect(lambda checked, w=widget: setter(w.isChecked()))



def paint_event(settings: Type[tool.Settings]):
    for widget, getter, setter, _ in settings.get_settings_list():
        value = getter()
        if isinstance(widget, QLineEdit) and widget.text() != value:
            widget.setText(str(value))

        elif isinstance(widget, QComboBox) and widget.currentText() != value:
            widget.setCurrentText(value)

        elif isinstance(widget, QDoubleSpinBox) and widget.value() != value:
            widget.setValue(value)

        elif isinstance(widget, QCheckBox) and widget.isChecked() != value:
            print(widget, value, getter)
            widget.setChecked(value)

        widget.setToolTip(str(type(value)))
