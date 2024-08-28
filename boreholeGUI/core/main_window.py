from __future__ import annotations

from typing import TYPE_CHECKING, Type

if TYPE_CHECKING:
    from boreholeGUI import tool
    from boreholeCreator import tool as cli_tool

def create_main_window(app, main_window: Type[tool.MainWindow]):
    mw = main_window.get_main_window(app)
    main_window.clear_toolbox()
    for name, widget in main_window.get_steplist():
        print(name, widget)
        main_window.get_toolbox().addItem(widget, name)
        widget.show()

    # main_window.get_toolbox().removeItem(0)

    mw.show()
    main_window.hide_console()


def run_clicked(borehole: Type[tool.Borehole], stratum: Type[tool.Stratum], borehole_cli: Type[cli_tool.Borehole],
                stratum_cli: Type[cli_tool.Stratum]):
    borehole_df = borehole.get_dataframe()
    borehole_df = borehole_cli.set_correct_datatypes(borehole_df)
    borehole_cli.set_dataframe(borehole_df)
    stratum_df = stratum_cli.set_correct_datatypes(stratum.get_dataframe())
    stratum_cli.set_dataframe(stratum_df)
    import boreholeCreator
    boreholeCreator.create_file("TestExport.ifc")
