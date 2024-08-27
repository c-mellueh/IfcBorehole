from __future__ import annotations

import pandas as pd
from PySide6.QtCore import QAbstractTableModel, Qt
from PySide6.QtWidgets import QHeaderView, QLineEdit


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

    def editSection(self, logicalIndex):
        # Create an editor
        editor = QLineEdit(self)
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
