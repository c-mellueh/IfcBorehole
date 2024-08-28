from __future__ import annotations

import pandas as pd
from PySide6.QtCore import QAbstractTableModel, Qt
from PySide6.QtWidgets import QCompleter, QDialog, QHeaderView, QLineEdit, QTableView, QWidget

from .select_dialog import Ui_Dialog


class DataFrameModel(QAbstractTableModel):
    def __init__(self, df=pd.DataFrame(), parent=None):
        super().__init__(parent)
        self._dataframe = df

    def rowCount(self, parent=None):
        return self._dataframe.shape[0]

    def columnCount(self, parent=None):
        return self._dataframe.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        if role == Qt.DisplayRole or role == Qt.EditRole:
            return str(self._dataframe.iloc[index.row(), index.column()])

        return None

    def setData(self, index, value, role=Qt.EditRole):
        if index.isValid() and role == Qt.EditRole:
            # Update the dataframe with the new value
            self._dataframe.iloc[index.row(), index.column()] = value
            # Emit dataChanged signal to notify the view
            self.dataChanged.emit(index, index, [Qt.DisplayRole, Qt.EditRole])
            return True
        return False

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole or role == Qt.EditRole:
            if orientation == Qt.Horizontal:
                return str(self._dataframe.columns[section])
            elif orientation == Qt.Vertical:
                return str(self._dataframe.index[section])
        return None

    def setHeaderData(self, section, orientation, value, role=Qt.EditRole):
        if role == Qt.EditRole:
            if orientation == Qt.Horizontal:
                self._dataframe.columns = (
                        list(self._dataframe.columns[:section])
                        + [value]
                        + list(self._dataframe.columns[section + 1:])
                )
            elif orientation == Qt.Vertical:
                self._dataframe.index = (
                        list(self._dataframe.index[:section])
                        + [value]
                        + list(self._dataframe.index[section + 1:])
                )
            self.headerDataChanged.emit(orientation, section, section)
            return True
        return False

    def headerFlags(self, orientation, section):
        # Enable editing on the header
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

    def updateDataFrame(self, df):
        """Function to update the entire DataFrame"""
        self.beginResetModel()
        self._dataframe = df
        self.endResetModel()


class DataFrameHeaderView(QHeaderView):
    def __init__(self, orientation, dataframe, parent=None):
        super().__init__(orientation, parent)
        self.dataframe = dataframe
        self.setSectionsClickable(True)
        self.setEditTriggers(QHeaderView.DoubleClicked)
        self.sectionDoubleClicked.connect(self.editSection)
        self.setModel(DataFrameModel(dataframe))
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

    def editSection(self, logicalIndex):
        widget = self.parentWidget().parentWidget()
        from boreholeGUI import tool
        missing_columns = tool.DataFrameTable.get_missing_required_columns(widget)
        missing_columns += tool.DataFrameTable.get_missing_optional_columns(widget)
        # Create an editor
        editor = QLineEdit(self)
        editor.setCompleter(QCompleter(missing_columns))
        editor.setFrame(False)
        editor.setText(self.model().headerData(logicalIndex, self.orientation(), Qt.DisplayRole))

        # Position the editor in the correct header section
        rect = self.sectionViewportPosition(logicalIndex)
        editor.setGeometry(rect, 0, self.sectionSize(logicalIndex), self.height())

        # Connect the editor's editingFinished signal
        editor.editingFinished.connect(lambda: self.commitAndCloseEditor(editor, logicalIndex))
        editor.setFocus()
        editor.show()

    def commitAndCloseEditor(self, editor, logicalIndex):
        # Commit the new header data to the model
        self.model().setHeaderData(logicalIndex, self.orientation(), editor.text(), Qt.EditRole)
        # Close the editor
        editor.deleteLater()


class Widget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from .widget import Ui_Form
        self.ui = Ui_Form()
        self.ui.setupUi(self)


class TableView(QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paintEvent(self, e):
        super().paintEvent(e)
        from . import trigger
        trigger.paint_table(self.parentWidget())


class SelectDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
