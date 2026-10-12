from enum import Enum


class ExternalShareOptionsTypeSchemaShowForGroups(str, Enum):
    ALL = "all"
    EXCEPT = "except"
    SELECTED_ONLY = "selected_only"

    def __str__(self) -> str:
        return str(self.value)
