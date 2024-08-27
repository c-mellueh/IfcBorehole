from __future__ import annotations

__version__ = "0.0.1"

import importlib

modules = {
    "borehole": [None, "borehole"],
    "location": [None, "location"],
    "main":     [None, "main"],
    "stratum":  [None, "stratum"],
    "styling":  [None, "styling"],
    "geometry": [None,"geometry"],
    "ifc": [None, "ifc"],
}

for key, (_, name) in modules.items():
    modules[key][0] = importlib.import_module(f"boreholeCreator.module.{name}")


def _register():
    for k, (mod, _) in modules.items():
        mod.register()


_register()


def create_file(export_path: str | None):
    from boreholeCreator.module.main import trigger
    return trigger.create_file(export_path)
