import os

from PySide6.QtGui import QIcon

ICON_PATH = os.path.dirname(__file__)


def get_icon() -> QIcon:
    icon_path = os.path.join(ICON_PATH, "icon.png")
    return QIcon(icon_path)
