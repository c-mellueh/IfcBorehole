import importlib

__version__ = "0.1.1"

modules = {
    "main_window": [None, "main_window"],
    "settings": [None, "settings"],
    "borehole": [None, "borehole"],
    "stratum":  [None, "stratum"],
    "data_frame_table": [None, "data_frame_table"],
}

for key, (_, name) in modules.items():
    modules[key][0] = importlib.import_module(f"boreholeGUI.module.{name}")


def register():
    for k, (mod, _) in modules.items():
        mod.register()


def load_ui_triggers():
    # modules["project"][0].load_ui_triggers()
    modules["main_window"][0].load_ui_triggers()
    for k, (mod, _) in modules.items():
        if k not in ("project", "main_window"):
            mod.load_ui_triggers()
