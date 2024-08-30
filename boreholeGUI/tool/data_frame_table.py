from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from boreholeGUI.module.data_frame_table.prop import DataFrameTableProperties
from PySide6.QtWidgets import QStyle, QMenu
from PySide6.QtCore import Qt
import pandas as pd
from boreholeGUI.module.data_frame_table import ui, trigger
import boreholeGUI
from boreholeCreator.tool import Util as CliUtil
import geopandas as gpd

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
        v = table_view.horizontalScrollBar().value()
        model = ui.DataFrameModel(dataframe)

        table_view.setModel(model)
        widget_tool = cls.get_tool_from_widget(widget)
        widget_tool.get_properties().dataframe = dataframe

        header_view = ui.DataFrameHeaderView(Qt.Orientation.Horizontal, model)
        table_view.setHorizontalHeader(header_view)
        header_view.show()
        header_view.customContextMenuRequested.connect(lambda pos: trigger.header_context_menu_requested(widget, pos))
        table_view.horizontalScrollBar().setValue(0)  # if not the scrollbar creates a mismatch to view
        table_view.horizontalScrollBar().setValue(v)


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

    @classmethod
    def get_dataframe(cls, widget: ui.Widget) -> pd.DataFrame:
        return cls.get_tool_from_widget(widget).get_properties().dataframe

    @classmethod
    def create_header_context_menu(cls, pos, widget: ui.Widget):
        menu = QMenu(widget)
        table_view = cls.get_table_view(widget).horizontalHeader()
        logical_index = table_view.logicalIndexAt(pos)

        add_column = menu.addAction("Add Column")
        add_column.triggered.connect(lambda: cls.add_column(logical_index + 1, widget))
        fill_column = menu.addAction("Fill Column With Value")
        fill_column.triggered.connect(lambda: cls.fill_column(logical_index, widget))
        clear_column = menu.addAction("Clear Column")
        clear_column.triggered.connect(lambda: cls.clear_column(logical_index, widget))
        remove_column = menu.addAction("Remove Column")
        remove_column.triggered.connect(lambda: cls.remove_column(logical_index, widget))

        missing_titles = cls.get_missing_required_columns(widget)
        if not missing_titles:
            return menu

        sub_menu = menu.addMenu("Umbenennen")
        cls.get_properties().actions = list()
        for title in missing_titles:
            sub_menu.addAction(title).triggered.connect(lambda _, t=title: cls.rename_column(widget, logical_index, t))

        return menu

    @classmethod
    def remove_column(cls, index, widget):
        model = cls.get_table_view(widget).model()
        model.removeColumn(index)

    @classmethod
    def rename_column(cls, widget, index, t):
        df = cls.get_dataframe(widget)
        df.rename(columns={list(df)[index]: t}, inplace=True)

    @classmethod
    def add_column(cls, index, widget: ui.Widget, column_name=None, prefill=None):
        df = cls.get_dataframe(widget)
        if column_name is None:
            column_name = CliUtil.get_new_name("New Column", list(df))
        table_view = cls.get_table_view(widget)
        table_view.model().insertColumn(index, column_name, prefill)

    @classmethod
    def fill_column(cls, logical_index, widget: ui.Widget):
        from boreholeGUI import tool
        answer = tool.Popups.request_text_input("Fill Column with Values", "Value:", "100", widget)
        if answer is None:
            return
        df = cls.get_dataframe(widget)
        df[list(df)[logical_index]] = answer

    @classmethod
    def clear_column(cls, logical_index, widget: ui.Widget):
        df = cls.get_dataframe(widget)
        df[list(df)[logical_index]] = None

    @classmethod
    def get_missing_required_columns(cls, widget: ui.Widget):
        widget_tool = cls.get_tool_from_widget(widget)
        widget_tool_cli = widget_tool.get_cli()
        existing_column_names = set(cls.get_column_names(widget))
        required_column_names = set(widget_tool_cli.get_required_column_names())
        missing_column_names = sorted(required_column_names.difference(existing_column_names))
        return missing_column_names

    @classmethod
    def get_missing_optional_columns(cls, widget: ui.Widget):
        widget_tool = cls.get_tool_from_widget(widget)
        widget_tool_cli = widget_tool.get_cli()
        existing_column_names = set(cls.get_column_names(widget))
        required_column_names = set(widget_tool_cli.get_optional_collumns())
        missing_column_names = sorted(required_column_names.difference(existing_column_names))
        return missing_column_names

    @classmethod
    def create_select_dialog(cls):
        dialog = ui.SelectDialog()
        dialog.ui.pushButton.clicked.connect(lambda: trigger.dataframe_select_file_clicked(dialog))
        return dialog

    @classmethod
    def transform_geopandas(cls, path) -> pd.DataFrame:
        df = gpd.read_file(path)
        from boreholeCreator.module.borehole.prop import X, Y, Z
        df[[X, Y, Z]] = df["geometry"].get_coordinates(include_z=True)
        return pd.DataFrame(df).drop("geometry", axis=1)
