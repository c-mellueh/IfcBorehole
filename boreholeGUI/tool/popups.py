from __future__ import annotations

from typing import TYPE_CHECKING

import pandas as pd

if TYPE_CHECKING:
    from boreholeGUI.module.popups.prop import PopupsProperties
from boreholeGUI import tool
import boreholeGUI.core.tool
import os
from PySide6.QtWidgets import QFileDialog, QMessageBox
from boreholeGUI.module.popups import ui


class Popups(boreholeGUI.core.tool.Popups):
    @classmethod
    def get_properties(cls) -> PopupsProperties:
        return boreholeGUI.PopupsProperties

    @classmethod
    def get_open_path(cls, file_format: str, window, path=None, title=None) -> str:
        return cls._get_path(file_format, window, path, False, title)

    @classmethod
    def get_save_path(cls, file_format: str, window, path=None, title=None) -> str:
        window = tool.MainWindow.get()
        return cls._get_path(file_format, window, path, True, title)

    @classmethod
    def _get_path(cls, file_format: str, window, path=None, save: bool = False, title=None) -> str:
        """ File Open Dialog with modifiable file_format"""
        if path:
            basename = os.path.basename(path)
            split = os.path.splitext(basename)[0]
            filename_without_extension = os.path.splitext(split)[0]
            dirname = os.path.dirname(path)
            path = os.path.join(dirname, filename_without_extension)
        if title is None:
            title = f"Save {file_format}" if save else f"Open {file_format}"

        if save:
            path = QFileDialog.getSaveFileName(window, title, path, f"{file_format} Files (*.{file_format})")[0]
        else:
            path = QFileDialog.getOpenFileName(window, title, path, f"{file_format} Files (*.{file_format})")[0]
        # if path:
        #     tool.Settings.set_export_path(path)
        return path

    @classmethod
    def select_excel_worksheet(cls):
        dialog = ui.ExcelDialog()
        dialog.ui.pushButton.clicked.connect(lambda: cls.select_excel_file(dialog))
        if not dialog.exec():
            return None, None
        return dialog.ui.lineEdit.text(), dialog.ui.comboBox.currentText()

    @classmethod
    def select_excel_file(cls, dialog: ui.ExcelDialog):
        file_type = "Excel  (*.xlsx);;all (*.*)"
        path = cls.get_open_path(file_type, dialog)
        if not path:
            return
        dialog.ui.lineEdit.setText(path)
        sheet_names = pd.ExcelFile(path).sheet_names
        dialog.ui.comboBox.clear()
        dialog.ui.comboBox.addItems(sheet_names)

    @classmethod
    def create_info_popup(cls, text, title="Info", execute: bool = True):
        msg_box = QMessageBox()
        # icon = get_icon()
        # msg_box.setWindowIcon(icon)
        msg_box.setText(text)
        msg_box.setWindowTitle(title)
        msg_box.setIcon(QMessageBox.Icon.Information)

        if execute:
            msg_box.exec()
        else:
            return msg_box
