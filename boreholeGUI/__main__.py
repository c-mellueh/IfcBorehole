import logging
import sys


def main(log_level=None):
    from PySide6.QtWidgets import QApplication
    import boreholeGUI.core.main_window
    from boreholeGUI import tool
    if log_level == None:
        log_level = logging.INFO
    logging.getLogger().setLevel(log_level)
    print("START")
    boreholeGUI.register()
    app = QApplication(sys.argv)
    boreholeGUI.load_ui_triggers()
    boreholeGUI.core.main_window.create_main_window(app, tool.MainWindow)
    sys.exit(app.exec())

if __name__ == '__main__':
    main()