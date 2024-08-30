from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from boreholeGUI.module.popups.prop import PopupsProperties
from boreholeGUI import tool
import boreholeGUI.core.tool
import os
from PySide6.QtWidgets import QFileDialog, QMessageBox, QInputDialog, QLineEdit
from boreholeGUI.icons import get_icon

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
        filter_text = f"{file_format}"
        if save:
            path = QFileDialog.getSaveFileName(window, title, path, filter_text)[0]
        else:
            path = QFileDialog.getOpenFileName(window, title, path, filter_text)[0]
        # if path:
        #     tool.Settings.set_export_path(path)
        return path


    @classmethod
    def create_info_popup(cls, text, title="Info", execute: bool = True):
        msg_box = QMessageBox()
        msg_box.setText(text)
        msg_box.setWindowTitle(title)
        icon = get_icon()
        msg_box.setWindowIcon(icon)
        msg_box.setIcon(QMessageBox.Icon.Information)

        if execute:
            msg_box.exec()
        else:
            return msg_box

    @classmethod
    def request_text_input(cls, title: str, request_text, prefill, parent=None):
        if parent is None:
            parent = tool.MainWindow.get()
        answer = QInputDialog.getText(parent, title, request_text,
                                      QLineEdit.EchoMode.Normal,
                                      prefill)
        if answer[1]:
            return answer[0]
        else:
            return None

    @classmethod
    def create_warning_popup(cls, text, title="Warning"):
        msg_box = QMessageBox()
        msg_box.setText(text)
        msg_box.setWindowTitle(title)
        msg_box.setIcon(QMessageBox.Icon.Warning)
        icon = get_icon()
        msg_box.setWindowIcon(icon)
        msg_box.exec()
