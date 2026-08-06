from enum import Enum


class MultiSelectFilterGroupSchemaModifier(str, Enum):
    EXCLUDE_ALL_OF = "exclude_all_of"
    EXCLUDE_ANY_OF = "exclude_any_of"
    INCLUDE_ALL_OF = "include_all_of"
    INCLUDE_ANY_OF = "include_any_of"

    def __str__(self) -> str:
        return str(self.value)
