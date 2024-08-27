from typing import Any

import ifcopenshell


class Util:
    @classmethod
    def fill_entity_with_dict(cls, entity: ifcopenshell.entity_instance, data_dict: dict[str, Any]):
        for name, value in data_dict.items():
            if value is None:
                continue
            setattr(entity, name, value)
