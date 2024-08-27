from __future__ import annotations

from typing import TYPE_CHECKING

import pandas as pd
from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt

from boreholeGUI.module.borehole import trigger, ui

if TYPE_CHECKING:
    from boreholeGUI.module.borehole.prop import BoreholeProperties
import boreholeGUI.core.tool


class PandasModel(QAbstractTableModel):
    """A model to interface a Qt view with pandas dataframe """

    def __init__(self, dataframe: pd.DataFrame, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._dataframe = dataframe

    def rowCount(self, parent=QModelIndex()) -> int:
        """ Override method from QAbstractTableModel

        Return row count of the pandas DataFrame
        """
        if parent == QModelIndex():
            return len(self._dataframe)

        return 0

    def columnCount(self, parent=QModelIndex()) -> int:
        """Override method from QAbstractTableModel

        Return column count of the pandas DataFrame
        """
        if parent == QModelIndex():
            return len(self._dataframe.columns)
        return 0

    def data(self, index: QModelIndex, role=Qt.ItemDataRole):
        """Override method from QAbstractTableModel

        Return data cell from the pandas DataFrame
        """
        if not index.isValid():
            return None

        if role == Qt.DisplayRole:
            return str(self._dataframe.iloc[index.row(), index.column()])

        return None

    def headerData(
            self, section: int, orientation: Qt.Orientation, role: Qt.ItemDataRole
    ):
        """Override method from QAbstractTableModel

        Return dataframe index as vertical header data and columns as horizontal header data.
        """
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self._dataframe.columns[section])

            if orientation == Qt.Orientation.Vertical:
                return str(self._dataframe.index[section])

        return None



class Borehole(boreholeGUI.core.tool.Borehole):
    @classmethod
    def get_properties(cls) -> BoreholeProperties:
        return boreholeGUI.BoreholeProperties

    @classmethod
    def get_widget(cls):
        if cls.get_properties().widget is None:
            cls.get_properties().widget = ui.Widget()
        return cls.get_properties().widget

    @classmethod
    def set_dataframe(cls, dataframe: pd.DataFrame):
        cls.get_properties().dataframe = dataframe
        model = PandasModel(dataframe)
        cls.get_widget().ui.tableView.setModel(model)

    @classmethod
    def get_ui(cls):
        return cls.get_widget().ui

    @classmethod
    def connect_triggers(cls):
        cls.get_ui().pushButton.clicked.connect(trigger.button_clicked)
