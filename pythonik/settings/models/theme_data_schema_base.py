from enum import Enum


class ThemeDataSchemaBase(str, Enum):
    DARK = "dark"
    LIGHT = "light"

    def __str__(self) -> str:
        return str(self.value)
