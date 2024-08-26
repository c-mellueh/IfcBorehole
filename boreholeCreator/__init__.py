from __future__ import annotations
from typing import TYPE_CHECKING

__version__ = "0.0.1"

import importlib

modules = {
    "borehole": [None, "borehole"],
    "location": [None, "location"],
    "main":     [None, "main"],
    "stratum":  [None, "stratum"],
    "styling":  [None, "styling"]
}

for key, (_, name) in modules.items():
    modules[key][0] = importlib.import_module(f"boreholeCreator.module.{name}")


def register():
    for k, (mod, _) in modules.items():
        mod.register()
