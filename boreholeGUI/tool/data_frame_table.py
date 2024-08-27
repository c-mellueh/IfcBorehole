from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from boreholeGUI.module.data_frame_table.prop import DataFrameTableProperties
from PySide6.QtWidgets import QStyle
from PySide6.QtCore import Qt
import pandas as pd
from boreholeGUI.module.data_frame_table import ui, trigger
import boreholeGUI


class DataFrameTable:
    @classmethod
    def get_properties(cls) -> DataFrameTableProperties:
        return boreholeGUI.DataFrameTableProperties

    @classmethod
    def create_widget(cls, widget_tool):
        widget = ui.Widget()
        cls.get_properties().tool_dict[widget] = widget_tool
        warning_button = cls.get_warning_button(widget)
        warning_button.setIcon(widget.style().standardIcon(QStyle.StandardPixmap.SP_MessageBoxWarning))
        warning_button.setText("Achtung!")

        widget.ui.pushButton.clicked.connect(lambda: trigger.button_clicked(widget))
        warning_button.clicked.connect(lambda: trigger.warning_clicked(widget))
        return widget

    @classmethod
    def get_ui(cls, widget: ui.Widget):
        return widget.ui

    @classmethod
    def get_table_view(cls, widget: ui.Widget):
        return cls.get_ui(widget).tableView

    @classmethod
    def set_dataframe(cls, dataframe: pd.DataFrame, widget: ui.Widget):
        table_view = cls.get_table_view(widget)
        model = ui.DataFrameModel(dataframe)
        header_view = ui.DataFrameHeaderView(Qt.Orientation.Horizontal, dataframe)
        table_view.setHorizontalHeader(header_view)
        table_view.setModel(model)
        widget_tool = cls.get_tool_from_widget(widget)
        widget_tool.get_properties().dataframe = dataframe
        header_view.show()

    @classmethod
    def get_tool_from_widget(cls, widget: ui.Widget):
        return cls.get_properties().tool_dict.get(widget)

    @classmethod
    def set_warning(cls, warning: str | None, widget: ui.Widget):
        if not warning:
            cls.get_warning_button(widget).hide()
        else:
            cls.get_warning_button(widget).show()
        cls.get_warning_button(widget).setToolTip(warning)

    @classmethod
    def get_warning_button(cls, widget: ui.Widget):
        return widget.ui.pushButton_2

    @classmethod
    def get_warning(cls, widget: ui.Widget):
        return cls.get_warning_button(widget).toolTip()

    @classmethod
    def get_column_names(cls, widget: ui.Widget):
        widget_tool = cls.get_tool_from_widget(widget)
        return list(widget_tool.get_properties().dataframe)
