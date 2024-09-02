from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from boreholeGUI.module.data_frame_table.prop import DataFrameTableProperties
    from boreholeCreator.tool import Stratum as CliStratum
    from boreholeCreator.tool import Borehole as CliBorehole
from PySide6.QtWidgets import QStyle, QMenu
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
import pandas as pd
from boreholeGUI.module.data_frame_table import ui, trigger
import boreholeGUI
from boreholeCreator.tool import Util as CliUtil
import geopandas as gpd

class DataFrameTable:
    """
    This is Class needs to be subclassed to work correctly!
    """
    @classmethod
    def get_properties(cls) -> DataFrameTableProperties:
        return boreholeGUI.DataFrameTableProperties

    @classmethod
    def create_widget(cls):
        widget = ui.Widget()
        cls.get_properties().widget = widget

        warning_button = cls.get_warning_button()
        warning_button.setIcon(widget.style().standardIcon(QStyle.StandardPixmap.SP_MessageBoxWarning))
        warning_button.setText("Achtung!")

        widget.ui.pushButton.clicked.connect(lambda: trigger.button_clicked(cls))
        warning_button.clicked.connect(lambda: trigger.warning_clicked(cls))

        info_button = cls.get_info_button()
        info_button.setIcon(widget.style().standardIcon(QStyle.StandardPixmap.SP_MessageBoxInformation))
        info_button.setText("Info!")
        info_button.clicked.connect(lambda: trigger.info_clicked(cls))
        cls.get_table_view()._tool = cls
        return widget

    @classmethod
    def get_ui(cls, ):
        return cls.get_widget().ui

    @classmethod
    def get_table_view(cls) -> ui.TableView:
        return cls.get_ui().tableView

    @classmethod
    def get_model(cls) -> ui.DataFrameModel:
        return cls.get_table_view().model()

    @classmethod
    def get_widget(cls):
        return cls.get_properties().widget

    @classmethod
    def set_widget(cls, widget):
        cls.get_properties().widget = widget

    @classmethod
    def set_dataframe(cls, dataframe: pd.DataFrame):
        table_view = cls.get_table_view()
        v = table_view.horizontalScrollBar().value()
        model = ui.DataFrameModel(dataframe, tool=cls)

        table_view.setModel(model)
        cls.get_properties().dataframe = dataframe
        header_view = ui.DataFrameHeaderView(Qt.Orientation.Horizontal, model)
        table_view.setHorizontalHeader(header_view)
        header_view.show()
        header_view.customContextMenuRequested.connect(lambda pos: trigger.header_context_menu_requested(pos, cls))
        table_view.horizontalScrollBar().setValue(0)  # if not the scrollbar creates a mismatch to view
        table_view.horizontalScrollBar().setValue(v)


    @classmethod
    def set_warning(cls, warning: str | None):
        button = cls.get_warning_button()
        if not warning:
            button.hide()
        else:
            button.show()
        button.setToolTip(warning)

    @classmethod
    def set_info(cls, info: str | None):
        button = cls.get_info_button()
        if not info:
            button.hide()
        else:
            button.show()
        button.setToolTip(info)

    @classmethod
    def get_warning_button(cls):
        return cls.get_widget().ui.button_warn

    @classmethod
    def get_info_button(cls):
        return cls.get_widget().ui.button_info

    @classmethod
    def get_warning(cls):
        return cls.get_warning_button().toolTip()

    @classmethod
    def get_info(cls):
        return cls.get_info_button().toolTip()

    @classmethod
    def get_column_names(cls, ):
        return list(cls.get_dataframe())

    @classmethod
    def get_dataframe(cls) -> pd.DataFrame:
        return cls.get_properties().dataframe

    @classmethod
    def create_header_context_menu(cls, pos):
        widget = cls.get_widget()
        menu = QMenu(widget)
        table_view = cls.get_table_view().horizontalHeader()
        logical_index = table_view.logicalIndexAt(pos)

        add_column = menu.addAction("Add Column")
        add_column.triggered.connect(lambda: cls.add_column(logical_index + 1))
        fill_column = menu.addAction("Fill Column With Value")
        fill_column.triggered.connect(lambda: cls.fill_column(logical_index))
        clear_column = menu.addAction("Clear Column")
        clear_column.triggered.connect(lambda: cls.clear_column(logical_index))
        remove_column = menu.addAction("Remove Column")
        remove_column.triggered.connect(lambda: cls.remove_column(logical_index))

        missing_titles = cls.get_missing_required_columns()
        missing_titles += cls.get_missing_optional_columns()
        if not missing_titles:
            return menu

        sub_menu = menu.addMenu("Umbenennen")
        cls.get_properties().actions = list()
        for title in missing_titles:
            action: QAction = sub_menu.addAction(title)
            action.triggered.connect(lambda _, t=title: cls.rename_column(logical_index, t))

        return menu

    @classmethod
    def remove_column(cls, index):
        model = cls.get_model()
        model.removeColumn(index)

    @classmethod
    def rename_column(cls, index, t):
        df = cls.get_dataframe()
        df.rename(columns={list(df)[index]: t}, inplace=True)

    @classmethod
    def add_column(cls, index, column_name=None, prefill=None):
        df = cls.get_dataframe()
        if column_name is None:
            column_name = CliUtil.get_new_name("New Column", list(df))
        cls.get_model().insertColumn(index, column_name, prefill)

    @classmethod
    def fill_column(cls, logical_index):
        widget = cls.get_widget()
        from boreholeGUI import tool
        answer = tool.Popups.request_text_input("Fill Column with Values", "Value:", "100", widget)
        if answer is None:
            return
        df = cls.get_dataframe()
        df[list(df)[logical_index]] = answer

    @classmethod
    def clear_column(cls, logical_index):
        df = cls.get_dataframe()
        df[list(df)[logical_index]] = None

    @classmethod
    def get_cli(cls) -> CliBorehole | CliStratum | None:
        return

    @classmethod
    def get_missing_required_columns(cls):
        widget_tool_cli = cls.get_cli()
        existing_column_names = set(cls.get_column_names())
        required_column_names = set(widget_tool_cli.get_required_column_names())
        missing_column_names = sorted(required_column_names.difference(existing_column_names))
        return missing_column_names

    @classmethod
    def get_missing_optional_columns(cls):
        widget_tool_cli = cls.get_cli()
        existing_column_names = set(cls.get_column_names())
        required_column_names = set(widget_tool_cli.get_optional_column_names())
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

    @classmethod
    def get_tooltips(cls):
        return cls.get_properties().tooltips
