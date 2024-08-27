from __future__ import annotations

from typing import TYPE_CHECKING

import pandas as pd
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QStyle

from boreholeGUI.module.borehole import trigger, ui
from boreholeGUI.module.pandas.table import DataFrameHeaderView, DataFrameModel

if TYPE_CHECKING:
    from boreholeGUI.module.borehole.prop import BoreholeProperties
import boreholeGUI.core.tool

class Borehole(boreholeGUI.core.tool.Borehole):
    @classmethod
    def get_properties(cls) -> BoreholeProperties:
        return boreholeGUI.BoreholeProperties

    @classmethod
    def get_widget(cls):
        if cls.get_properties().widget is None:
            cls.get_properties().widget = cls._create_widget()
        return cls.get_properties().widget

    @classmethod
    def _create_widget(cls):
        widget = ui.Widget()
        cls.get_properties().widget = widget
        cls.get_warning_button().setIcon(widget.style().standardIcon(QStyle.StandardPixmap.SP_MessageBoxWarning))
        cls.get_warning_button().setText("Achtung!")
        return widget

    @classmethod
    def set_dataframe(cls, dataframe: pd.DataFrame):
        model = DataFrameModel(dataframe)
        cls.get_properties().dataframe = dataframe
        cls.get_properties().header_view = DataFrameHeaderView(Qt.Orientation.Horizontal, dataframe)
        view = cls.get_widget().ui.tableView
        view.setHorizontalHeader(cls.get_properties().header_view)
        view.setModel(model)
        cls.get_properties().header_view.show()
    @classmethod
    def get_ui(cls):
        return cls.get_widget().ui

    @classmethod
    def connect_triggers(cls):
        cls.get_ui().pushButton.clicked.connect(trigger.button_clicked)
        cls.get_warning_button().clicked.connect(trigger.warning_clicked)

    @classmethod
    def get_column_names(cls):
        return list(cls.get_properties().dataframe)

    @classmethod
    def get_warning_button(cls):
        return cls.get_ui().pushButton_2

    @classmethod
    def set_warning(cls, warning: str | None):
        if not warning:
            cls.get_warning_button().hide()
        else:
            cls.get_warning_button().show()
        cls.get_properties().warning = warning
        cls.get_warning_button().setToolTip(warning)

    @classmethod
    def get_warning(cls):
        return cls.get_properties().warning
