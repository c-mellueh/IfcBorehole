import logging
import sys


def main(initial_file: str | None = None, log_level=None):
    from PySide6.QtWidgets import QApplication
    import boreholeGUI.core.main_window
    from boreholeGUI import tool
    if log_level == None:
        log_level = logging.WARNING

    print("START")
    boreholeGUI.register()
    # tool.Logging.set_log_level(log_level)
    app = QApplication(sys.argv)
    boreholeGUI.core.main_window.create_main_window(app, tool.MainWindow)
    boreholeGUI.load_ui_triggers()
    # core.project.create_project(tool.Project)
    # core.main_window.create_menus(tool.MainWindow, tool.Util)
    # if initial_file is not None:
    #     core.project.open_project(initial_file, tool.Project)
    sys.exit(app.exec())
